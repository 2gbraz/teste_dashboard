# Image Agent with Pause/Approval Flow

An image generation agent using Google ADK with approval workflow for bulk requests.

## Setup

### 1. Install Dependencies

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure Google API Key

You have **three options** to set your Google API key:

#### Option 1: Local Config File (Recommended for development)

1. Open `config.py`
2. Replace `your_google_api_key_here` with your actual API key
3. Get your API key from: https://aistudio.google.com/app/apikey

```python
# config.py
GOOGLE_API_KEY = "AIza..."  # Your actual key here
```

#### Option 2: Environment Variable

```bash
export GOOGLE_API_KEY="AIza..."  # On Windows: set GOOGLE_API_KEY=AIza...
python image_agent_pause_approval.py
```

#### Option 3: Kaggle Secrets (For Kaggle Notebooks)

1. Go to Kaggle Notebook Settings
2. Add a new secret with name: `GOOGLE_API_KEY`
3. No additional configuration needed - the script will auto-detect

## Usage

### Run the Built-in Demo

```bash
python image_agent_pause_approval.py
```

This will test:
- Single image generation (auto-approved)
- Bulk image generation (pending → approval flow)

### Run Comprehensive Tests

```bash
python test_image_agent.py
```

## How It Works

### Approval Workflow

1. **Single Image Request** → Auto-approved and generated immediately
2. **Multiple Images Request** → Creates pending order with approval token
3. **Approval/Rejection** → User decides whether to proceed
4. **Generation** → Images generated after approval

### Agent Features

- ✅ Auto-approval for single images
- ✅ Manual approval required for bulk requests (>1 image)
- ✅ Resumability support (saves state to `agent_state.json`)
- ✅ MCP integration for image generation
- ✅ Works in Kaggle and local environments

## Project Structure

```
.
├── image_agent_pause_approval.py  # Main agent implementation
├── test_image_agent.py            # Test scripts
├── config.py                      # Local API key configuration
├── requirements.txt               # Python dependencies
├── agent_state.json              # Agent state (auto-generated)
└── README.md                     # This file
```

## Requirements

- Python 3.10+ (required for MCP support)
- Node.js/npm (for MCP Everything Server)
- Google API Key (Gemini access)

## Troubleshooting

### ModuleNotFoundError

Make sure you're in the virtual environment:
```bash
source venv/bin/activate
pip install -r requirements.txt
```

### Authentication Errors

Check that your API key is correctly set in one of the three options above.

### MCP Server Issues

Ensure Node.js is installed:
```bash
node --version
npm --version
```

The script uses `npx` to run the MCP Everything Server automatically.

## License

Google ADK License - See package documentation

