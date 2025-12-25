"""
Dify Tool Plugin - Get User Profile
This plugin provides a tool to get user profile information from an external API.
"""

from typing import Any, Dict, Optional
import requests
import os


def get_user_profile(token: Optional[str] = None, **kwargs) -> Dict[str, Any]:
    """
    Get user profile information from the external API.
    
    Args:
        token: Authorization token. If not provided, will try to get from context or environment.
        **kwargs: Additional context variables that may contain auth_token.
    
    Returns:
        Dictionary containing user profile information.
    """
    # Get token from parameter, context, environment variable, or request context
    # Dify may pass token through kwargs or context
    auth_token = (
        token 
        or kwargs.get("auth_token") 
        or kwargs.get("token")
        or os.getenv("AUTH_TOKEN") 
        or ""
    )
    
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
        result = response.json()
        
        # 格式化返回数据，提取用户信息
        # 如果 API 返回格式为 {"result": 0, "data": {"user": {...}}}
        # 则提取 user 信息并返回
        if isinstance(result, dict):
            if result.get("result") == 0 and "data" in result:
                user_data = result.get("data", {}).get("user", {})
                if user_data:
                    return {
                        "result": 0,
                        "user_id": user_data.get("user_id"),
                        "email": user_data.get("email"),
                        "user_name": user_data.get("user_name"),
                        "timezone": user_data.get("timezone"),
                        "language": user_data.get("language"),
                        "created_time": user_data.get("created_time")
                    }
            # 如果已经是扁平化的格式，直接返回
            return result
        
        return result
    except requests.exceptions.RequestException as e:
        return {
            "error": str(e),
            "result": -1,
            "result_info": f"Failed to get user profile: {str(e)}"
        }


# Export the function for Dify to use
__all__ = ["get_user_profile"]

