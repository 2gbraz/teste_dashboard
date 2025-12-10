"""FastAPI backend for the Next.js AI Agent application."""
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Optional
import sys
import os

# Add parent directory to path to import ai_agent modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../src'))

from ai_agent import AIAgent
from excel_processor import ExcelProcessor
from user_service_client import UserServiceClient

app = FastAPI(title="User Data AI Agent API")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize services
try:
    agent = AIAgent()
    excel_processor = ExcelProcessor()
    user_service_client = UserServiceClient()
except ValueError as e:
    print(f"Warning: Failed to initialize services: {e}")
    agent = None
    excel_processor = None
    user_service_client = None


class ChatRequest(BaseModel):
    message: str
    processed_users: Optional[List[Dict]] = None


class UpdateUsersRequest(BaseModel):
    users: List[Dict]


@app.get("/")
async def root():
    return {"message": "User Data AI Agent API", "status": "running"}


@app.get("/health")
async def health():
    return {"status": "healthy"}


@app.post("/api/process-excel")
async def process_excel(file: UploadFile = File(...)):
    """Process an uploaded Excel file and return user data."""
    if not excel_processor:
        raise HTTPException(status_code=500, detail="Excel processor not initialized")
    
    try:
        # Read file content
        file_content = await file.read()
        
        if not file_content:
            raise HTTPException(status_code=400, detail="Empty file uploaded")
        
        # Process Excel file
        users = excel_processor.process_excel_file(file_content)
        
        return {
            "success": True,
            "users": users,
            "count": len(users)
        }
    except ValueError as e:
        import traceback
        print(f"ValueError in process_excel: {str(e)}")
        print(traceback.format_exc())
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        import traceback
        print(f"Exception in process_excel: {str(e)}")
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")


@app.post("/api/chat")
async def chat(request: ChatRequest):
    """Handle chat messages with the AI agent."""
    if not agent:
        raise HTTPException(status_code=500, detail="AI agent not initialized")
    
    try:
        # Add context about processed users if available
        user_message = request.message
        if request.processed_users:
            num_users = len(request.processed_users)
            user_context = f"\n[System: User has uploaded an Excel file with {num_users} users. "
            user_context += f"Users are ready to be updated in the service. Sample users: {request.processed_users[:3]}]"
            user_message += user_context
        
        response = agent.chat(user_message, None)
        
        return {
            "message": response,
            "success": True
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating response: {str(e)}")


@app.post("/api/update-users")
async def update_users(request: UpdateUsersRequest):
    """Update users in the user service."""
    if not user_service_client:
        raise HTTPException(status_code=500, detail="User service client not initialized")
    
    try:
        # Convert users to the format expected by the client
        users = []
        for user in request.users:
            user_id = user.get('id')
            user_data = user.get('data', {})
            if user_id:
                users.append({
                    'id': user_id,
                    'data': user_data
                })
        
        if not users:
            raise HTTPException(status_code=400, detail="No valid users provided")
        
        # Update users
        results = user_service_client.patch_users_batch(users)
        
        # Calculate statistics
        total = len(results)
        successful = sum(1 for success in results.values() if success)
        failed = total - successful
        
        return {
            "total": total,
            "successful": successful,
            "failed": failed,
            "results": results
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error updating users: {str(e)}")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

