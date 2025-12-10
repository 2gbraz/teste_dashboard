# Quick Start Guide

## Prerequisites

- Node.js 18+ installed
- Python 3.8+ installed
- Google AI API Key

## Setup Steps

### 1. Install Dependencies

**Frontend:**
```bash
cd nextjs-app
npm install
```

**Backend:**
```bash
cd nextjs-app/backend
pip install -r requirements.txt
```

### 2. Configure Environment

**Backend (.env file in `ai_agent/src/` or `nextjs-app/backend/`):**
```bash
GOOGLE_AI_API_KEY=your_key_here
USER_SERVICE_URL=http://localhost:8000/api/users
USER_SERVICE_API_KEY=optional_api_key
MODEL_NAME=gemini-2.5-flash
```

**Frontend (.env.local in `nextjs-app/`):**
```bash
NEXT_PUBLIC_API_URL=http://localhost:8000
```

### 3. Start the Application

**Terminal 1 - Backend:**
```bash
cd ai_agent/nextjs-app/backend
python main.py
```

**Terminal 2 - Frontend:**
```bash
cd ai_agent/nextjs-app
npm run dev
```

### 4. Access the Application

Open your browser and navigate to: http://localhost:3000

## Usage

1. Upload an Excel file using the sidebar (must include an 'id' column)
2. Preview the processed users
3. Chat with the AI agent
4. Click "Update Users in Service" to send PATCH requests

## Troubleshooting

- **Backend won't start**: Check that Python dependencies are installed and environment variables are set
- **Frontend can't connect**: Ensure backend is running on port 8000
- **CORS errors**: Check that backend CORS settings include your frontend URL
- **Excel processing fails**: Verify your Excel file has an 'id' column and no duplicate IDs

