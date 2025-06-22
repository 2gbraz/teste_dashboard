"""
Google Sheets Configuration and Authentication Setup

This file contains the configuration for connecting to Google Sheets.
Follow the setup instructions below to connect your dashboard to your Google Sheets.
"""

import gspread
from google.oauth2.service_account import Credentials
import pandas as pd
import streamlit as st

def setup_google_sheets_connection():
    """
    Setup Google Sheets connection using service account credentials
    """
    try:
        # Define the scope
        scope = [
            'https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive'
        ]
        
        # Load credentials from service account file
        # You need to create a service account and download the JSON key file
        credentials = Credentials.from_service_account_file(
            'service_account_key.json',  # Replace with your key file path
            scopes=scope
        )
        
        # Authorize the clientsheet
        client = gspread.authorize(credentials)
        
        return client
    
    except FileNotFoundError:
        st.error("❌ Service account key file not found. Please follow the setup instructions.")
        return None
    except Exception as e:
        st.error(f"❌ Error setting up Google Sheets connection: {str(e)}")
        return None

def load_sheet_data(client, sheet_url, worksheet_name="Sheet1"):
    """
    Load data from Google Sheets
    """
    try:
        # Extract sheet ID from URL
        sheet_id = sheet_url.split('/d/')[1].split('/')[0]
        
        # Open the spreadsheet
        spreadsheet = client.open_by_key(sheet_id)
        
        # Select the worksheet
        worksheet = spreadsheet.worksheet(worksheet_name)
        
        # Get all values
        data = worksheet.get_all_records()
        
        # Convert to DataFrame
        df = pd.DataFrame(data)
        
        return df
    
    except Exception as e:
        st.error(f"❌ Error loading data from Google Sheets: {str(e)}")
        return None

# Setup Instructions
SETUP_INSTRUCTIONS = """
## 🔧 Google Sheets Setup Instructions

### 1. Create a Google Cloud Project
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable the Google Sheets API and Google Drive API

### 2. Create a Service Account
1. In your Google Cloud project, go to "IAM & Admin" > "Service Accounts"
2. Click "Create Service Account"
3. Give it a name (e.g., "financial-dashboard")
4. Grant it the "Editor" role
5. Create and download the JSON key file

### 3. Share Your Google Sheet
1. Open your Google Sheet
2. Click "Share" in the top right
3. Add your service account email (found in the JSON key file) as an Editor
4. Make sure the sheet is accessible

### 4. Configure the Dashboard
1. Place the downloaded JSON key file in your project directory
2. Update the file path in `google_sheets_config.py`
3. Run the dashboard with: `streamlit run financial_dashboard.py`

### 5. Expected Data Format
Your Google Sheet should have columns like:
- Date
- Revenue
- Expenses
- Profit
- Cash_Flow
- Assets
- Liabilities
- Equity

The first row should contain column headers.
"""

if __name__ == "__main__":
    print(SETUP_INSTRUCTIONS) 