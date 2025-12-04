# AI Agent for User Data Management

An AI-powered agent that helps users upload Excel files with user data and automatically updates a user service via PATCH requests.

## Features

- 🤖 **AI Chat Interface**: Interactive chat using Google AI SDK (Gemini)
- 📊 **Excel Processing**: Automatically reads and validates Excel files with user data
- 🔄 **User Service Integration**: Makes PATCH requests to update users in the service
- ✅ **Data Validation**: Validates Excel files for required fields and data integrity
- 💬 **Streamlit UI**: Beautiful web interface for easy interaction

## Prerequisites

- Python 3.8+
- Google AI API Key (from [Google AI Studio](https://makersuite.google.com/app/apikey))
- Access to the User Service API

## Setup

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure environment variables**:
   - Copy `.env.example` to `.env`
   - Fill in your Google AI API key
   - Set the User Service URL and API key (if required)

   ```bash
   cp .env.example .env
   # Edit .env with your credentials
   ```

3. **Run the application**:
   ```bash
   streamlit run app.py
   ```

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

1. **Start the app**: Run `streamlit run app.py`
2. **Upload Excel file**: Use the sidebar to upload your Excel file
3. **Chat with AI**: Ask the AI agent questions or request help
4. **Update users**: Click the "Update Users in Service" button to send PATCH requests

## Configuration

Edit `config.py` or set environment variables:
- `GOOGLE_AI_API_KEY`: Your Google AI API key
- `USER_SERVICE_URL`: Base URL for the user service API (e.g., `http://localhost:8000/api/users`)
- `USER_SERVICE_API_KEY`: Optional API key for authentication
- `MODEL_NAME`: Google AI model to use (default: `gemini-pro`)

## Project Structure

```
ai_agent/
├── src/
│   ├── app.py                 # Streamlit application
│   ├── ai_agent.py            # AI agent logic
│   ├── excel_processor.py     # Excel file processing
│   ├── user_service_client.py # User service API client
│   ├── config.py              # Configuration
│   ├── requirements.txt       # Dependencies
│   ├── .env.example           # Environment variables template
│   └── README.md              # This file
```

## API Integration

The agent makes PATCH requests to update users:
- Endpoint: `{USER_SERVICE_URL}/{user_id}`
- Method: PATCH
- Body: JSON with user data fields
- Headers: Includes Authorization if API key is configured

## Error Handling

The agent handles:
- Invalid Excel file formats
- Missing required columns
- Duplicate user IDs
- API connection errors
- Data validation errors

## License

MIT

