"""Module for processing Excel files with user data."""
import pandas as pd
import logging
from typing import List, Dict, Optional, Tuple
from io import BytesIO

logger = logging.getLogger(__name__)


class ExcelProcessor:
    """Processes Excel files and converts them to the required format."""
    
    def __init__(self):
        self.required_fields = ['id']  # Minimum required field
        self.optional_fields = ['name', 'email', 'phone', 'role', 'status']
    
    def read_excel(self, file_content: bytes, sheet_name: Optional[str] = None) -> pd.DataFrame:
        """
        Read Excel file from bytes.
        
        Args:
            file_content: Bytes content of the Excel file
            sheet_name: Optional sheet name to read (reads first sheet if not specified)
            
        Returns:
            DataFrame with the Excel data
        """
        try:
            df = pd.read_excel(BytesIO(file_content), sheet_name=sheet_name)
            
            # Ensure we have a DataFrame, not a dict (which can happen with sheet_name=None)
            if isinstance(df, dict):
                # If multiple sheets, take the first one
                if df:
                    df = list(df.values())[0]
                else:
                    raise ValueError("No sheets found in Excel file")
            
            if not isinstance(df, pd.DataFrame):
                raise ValueError(f"Expected DataFrame, got {type(df)}")
            
            logger.info(f"Successfully read Excel file with {len(df)} rows")
            return df
        except Exception as e:
            logger.error(f"Error reading Excel file: {str(e)}")
            raise
    
    def validate_data(self, df: pd.DataFrame) -> Tuple[bool, List[str]]:
        """
        Validate that the DataFrame has required fields.
        
        Args:
            df: DataFrame to validate
            
        Returns:
            Tuple of (is_valid, list_of_errors)
        """
        errors = []
        
        # Check if DataFrame is empty
        if df.empty:
            errors.append("Excel file is empty")
            return False, errors
        
        # Check for required fields
        if 'id' not in df.columns:
            errors.append("Excel file must contain an 'id' column")
        
        # Check for duplicate IDs
        if 'id' in df.columns:
            duplicates = df['id'].duplicated().sum()
            if duplicates > 0:
                errors.append(f"Found {duplicates} duplicate IDs in the Excel file")
        
        return len(errors) == 0, errors
    
    def convert_to_user_format(self, df: pd.DataFrame) -> List[Dict]:
        """
        Convert DataFrame to the format expected by the user service.
        
        Args:
            df: DataFrame with user data
            
        Returns:
            List of dictionaries in the format: [{'id': 'user_id', 'data': {...}}]
        """
        users = []
        
        # Replace NaN values with None for JSON serialization
        df = df.where(pd.notna(df), None)
        
        for _, row in df.iterrows():
            user_id = str(row.get('id', ''))
            if not user_id:
                logger.warning(f"Skipping row without ID: {row.to_dict()}")
                continue
            
            # Extract all fields except 'id' as the data to update
            user_data = {col: row[col] for col in df.columns if col != 'id' and row[col] is not None}
            
            users.append({
                'id': user_id,
                'data': user_data
            })
        
        logger.info(f"Converted {len(users)} users to the required format")
        return users
    
    def process_excel_file(self, file_content: bytes, sheet_name: Optional[str] = None) -> List[Dict]:
        """
        Complete processing pipeline: read, validate, and convert Excel file.
        
        Args:
            file_content: Bytes content of the Excel file
            sheet_name: Optional sheet name to read
            
        Returns:
            List of user dictionaries ready for API calls
        """
        # Read Excel file
        df = self.read_excel(file_content, sheet_name)
        
        # Validate data
        is_valid, errors = self.validate_data(df)
        if not is_valid:
            error_msg = "; ".join(errors)
            raise ValueError(f"Validation failed: {error_msg}")
        
        # Convert to user format
        users = self.convert_to_user_format(df)
        
        return users

