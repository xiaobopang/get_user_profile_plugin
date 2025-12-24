"""
Dify Tool Plugin - Get User Profile
This plugin provides a tool to get user profile information from an external API.
"""

from typing import Any, Dict, Optional
import requests
import os


def get_user_profile(token: Optional[str] = None) -> Dict[str, Any]:
    """
    Get user profile information from the external API.
    
    Args:
        token: Authorization token. If not provided, will try to get from environment or request context.
    
    Returns:
        Dictionary containing user profile information.
    """
    # Get token from parameter, environment variable, or request context
    auth_token = token or os.getenv("AUTH_TOKEN") or ""
    
    url = "http://43.130.39.119/user/get_profile"
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {auth_token}"
    }
    body = {}
    
    try:
        response = requests.post(url, headers=headers, json=body, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {
            "error": str(e),
            "result": -1,
            "result_info": f"Failed to get user profile: {str(e)}"
        }


# Export the function for Dify to use
__all__ = ["get_user_profile"]

