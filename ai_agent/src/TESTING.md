# Testing Guide for AI Agent

## Prerequisites

1. **Python 3.8+** installed
2. **Google AI API Key** - Get one from [Google AI Studio](https://makersuite.google.com/app/apikey)
3. **User Service** running (or mock it for testing)

## Step 1: Install Dependencies

```bash
cd ai_agent/src
pip install -r requirements.txt
```

Or if using a virtual environment:

```bash
# Activate your virtual environment first
source ../../venv/bin/activate  # On macOS/Linux
# or
../../venv\Scripts\activate  # On Windows

pip install -r requirements.txt
```

## Step 2: Configure Environment Variables

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` and add your credentials:
   ```bash
   # Required: Google AI API Key
   GOOGLE_AI_API_KEY=your_actual_api_key_here
   
   # Optional: User Service Configuration
   USER_SERVICE_URL=http://localhost:8000/api/users
   USER_SERVICE_API_KEY=your_api_key_if_needed
   
   # Optional: Model name
   MODEL_NAME=gemini-pro
   ```

## Step 3: Create Sample Excel File

Run the script to create a test Excel file:

```bash
python create_sample_excel.py
```

This creates `sample_users.xlsx` with 3 sample users.

## Step 4: Test the Application

### Option A: Full Streamlit App (Recommended)

```bash
streamlit run app.py
```

Or:

```bash
python run.py
```

The app will open in your browser (usually at `http://localhost:8501`).

**Testing Steps:**
1. ✅ Check that the app loads without errors
2. ✅ Upload `sample_users.xlsx` using the sidebar
3. ✅ Verify the file is processed and shows preview
4. ✅ Chat with the AI agent
5. ✅ Click "Update Users in Service" button (if user service is running)

### Option B: Test Individual Components

#### Test Excel Processor

```python
from excel_processor import ExcelProcessor

processor = ExcelProcessor()
with open('sample_users.xlsx', 'rb') as f:
    users = processor.process_excel_file(f.read())
    print(f"Processed {len(users)} users")
    print(users)
```

#### Test User Service Client

```python
from user_service_client import UserServiceClient

client = UserServiceClient()
# Test with a single user
result = client.patch_user('1', {'name': 'Updated Name'})
print(result)
```

#### Test AI Agent

```python
from ai_agent import AIAgent

agent = AIAgent()
response = agent.chat("Hello! Can you help me upload a user file?")
print(response)
```

## Step 5: Test with Mock User Service (Optional)

If you don't have the user service running, you can use a mock server:

```bash
# Install httpie or use curl
pip install httpie

# Start a simple mock server (requires additional setup)
# Or use a tool like Postman Mock Server
```

Or test the Excel processing without making actual API calls:

```python
from excel_processor import ExcelProcessor

processor = ExcelProcessor()
with open('sample_users.xlsx', 'rb') as f:
    users = processor.process_excel_file(f.read())
    # Just print the users without calling the API
    for user in users:
        print(f"Would update user {user['id']} with data: {user['data']}")
```

## Common Issues & Solutions

### Issue: "GOOGLE_AI_API_KEY must be set"
- **Solution**: Make sure you created `.env` file and added your API key

### Issue: "ModuleNotFoundError: No module named 'pandas'"
- **Solution**: Install dependencies: `pip install -r requirements.txt`

### Issue: "Error processing Excel file"
- **Solution**: Check that your Excel file has an 'id' column and no duplicate IDs

### Issue: "Connection refused" when updating users
- **Solution**: Make sure your user service is running, or update `USER_SERVICE_URL` in `.env`

## Expected Behavior

1. **File Upload**: Should validate and process Excel files
2. **AI Chat**: Should respond to user messages using Google AI
3. **User Updates**: Should make PATCH requests to `{USER_SERVICE_URL}/{user_id}`

## Testing Checklist

- [ ] Dependencies installed
- [ ] `.env` file configured with API key
- [ ] Sample Excel file created
- [ ] Streamlit app runs without errors
- [ ] Excel file uploads and processes correctly
- [ ] AI chat responds appropriately
- [ ] User service updates work (if service is available)

