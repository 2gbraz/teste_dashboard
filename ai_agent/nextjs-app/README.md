# User Data AI Agent - Next.js Application

A modern Next.js application for uploading Excel files with user data and updating a user service with AI assistance.

## Features

- 🤖 **AI Chat Interface**: Interactive chat using Google AI SDK (Gemini)
- 📊 **Excel Processing**: Automatically reads and validates Excel files with user data
- 🔄 **User Service Integration**: Makes PATCH requests to update users in the service
- ✅ **Data Validation**: Validates Excel files for required fields and data integrity
- 🎨 **Modern UI**: Beautiful, responsive interface built with Next.js, React, and Tailwind CSS

## Prerequisites

- Node.js 18+ and npm/yarn
- Python 3.8+ (for backend API)
- Google AI API Key (from [Google AI Studio](https://makersuite.google.com/app/apikey))
- Access to the User Service API

## Setup

**Note:** All commands below assume you're starting from the project root directory (`/Users/gilbraz/teste_python`).

### 1. Install Frontend Dependencies

```bash
cd ai_agent/nextjs-app
npm install
```

### 2. Install Backend Dependencies

```bash
cd ai_agent/nextjs-app/backend
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env.local` file in the `nextjs-app` directory:

```bash
NEXT_PUBLIC_API_URL=http://localhost:8000
```

Create a `.env` file in the `backend` directory (or use the existing one from `ai_agent/src`):

```bash
GOOGLE_AI_API_KEY=your_google_ai_api_key_here
USER_SERVICE_URL=http://localhost:8000/api/users
USER_SERVICE_API_KEY=your_api_key_if_required
MODEL_NAME=gemini-2.5-flash
```

### 4. Run the Application

**Terminal 1 - Start the Backend API:**
```bash
cd ai_agent/nextjs-app/backend
python main.py
# Or use uvicorn directly:
# uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

**Terminal 2 - Start the Next.js Frontend:**
```bash
cd ai_agent/nextjs-app
npm run dev
```

The application will be available at:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000

## Excel File Format

Your Excel file must include:
- **Required**: `id` column (unique user identifiers)
- **Optional**: Any other user fields you want to update (e.g., `name`, `email`, `phone`, `role`, `status`)

Example Excel structure:
| id | name | email | phone | role |
|---|---|---|---|---|
| 1 | John Doe | john@example.com | 123-456-7890 | admin |
| 2 | Jane Smith | jane@example.com | 098-765-4321 | user |

## Usage

1. **Start both servers**: Backend API and Next.js frontend
2. **Upload Excel file**: Use the file upload component in the sidebar
3. **Chat with AI**: Ask the AI agent questions or request help
4. **Update users**: Click the "Update Users in Service" button to send PATCH requests

## Project Structure

```
nextjs-app/
├── app/                    # Next.js app directory
│   ├── layout.tsx         # Root layout
│   ├── page.tsx           # Main page
│   └── globals.css        # Global styles
├── components/            # React components
│   ├── FileUpload.tsx     # File upload component
│   ├── ChatInterface.tsx  # Chat UI component
│   ├── UserPreview.tsx    # User preview component
│   └── ActionButtons.tsx  # Action buttons component
├── lib/                   # Utility functions
│   └── api.ts            # API client functions
├── types/                 # TypeScript types
│   └── index.ts          # Type definitions
├── backend/              # Python FastAPI backend
│   ├── main.py          # FastAPI application
│   └── requirements.txt # Python dependencies
└── package.json          # Node.js dependencies
```

## API Endpoints

The backend provides the following endpoints:

- `GET /` - API status
- `GET /health` - Health check
- `POST /api/process-excel` - Process uploaded Excel file
- `POST /api/chat` - Send chat message to AI agent
- `POST /api/update-users` - Update users in the user service

## Development

### Frontend Development

```bash
npm run dev      # Start development server
npm run build    # Build for production
npm run start    # Start production server
npm run lint     # Run ESLint
```

### Backend Development

The backend uses FastAPI with auto-reload. Make sure the Python path includes the `ai_agent/src` directory so it can import the existing modules.

## Error Handling

The application handles:
- Invalid Excel file formats
- Missing required columns
- Duplicate user IDs
- API connection errors
- Data validation errors

## License

MIT

