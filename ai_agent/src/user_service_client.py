"""Client for interacting with the User Service API."""
import requests
import logging
from typing import Dict, List, Optional
from config import USER_SERVICE_URL, USER_SERVICE_API_KEY

logger = logging.getLogger(__name__)


class UserServiceClient:
    """Client for making requests to the User Service."""
    
    def __init__(self):
        self.base_url = USER_SERVICE_URL
        self.api_key = USER_SERVICE_API_KEY
        self.headers = {
            "Content-Type": "application/json",
        }
        if self.api_key:
            self.headers["Authorization"] = f"Bearer {self.api_key}"
    
    def patch_user(self, user_id: str, user_data: Dict) -> Optional[Dict]:
        """
        Make a PATCH request to update a user.
        
        Args:
            user_id: The ID of the user to update
            user_data: Dictionary containing the user data to update
            
        Returns:
            Response data if successful, None otherwise
        """
        url = f"{self.base_url}/{user_id}"
        
        try:
            response = requests.patch(url, json=user_data, headers=self.headers, timeout=30)
            response.raise_for_status()
            logger.info(f"Successfully updated user {user_id}")
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Error updating user {user_id}: {str(e)}")
            if hasattr(e, 'response') and e.response is not None:
                logger.error(f"Response: {e.response.text}")
            return None
    
    def patch_users_batch(self, users: List[Dict]) -> Dict[str, bool]:
        """
        Update multiple users in batch.
        
        Args:
            users: List of dictionaries, each containing 'id' and 'data' keys
            
        Returns:
            Dictionary mapping user IDs to success status
        """
        results = {}
        for user in users:
            user_id = user.get('id')
            user_data = user.get('data', {})
            if user_id:
                success = self.patch_user(user_id, user_data) is not None
                results[user_id] = success
            else:
                logger.warning(f"Skipping user without ID: {user}")
                results[user.get('id', 'unknown')] = False
        return results

