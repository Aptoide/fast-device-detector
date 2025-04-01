"""
Type hints for the Fast Device Detector library.
"""

from typing import Dict, Optional, Union, Any

class DeviceDetector:
    """
    A high-performance device detector that uses Rust under the hood.
    
    This class provides methods to detect device information from user agent strings,
    including device type, brand, model, operating system, and client details.
    """
    
    def __init__(self) -> None:
        """Create a new DeviceDetector instance."""
        ...
    
    @classmethod
    def with_cache(cls, cache_size: int) -> "DeviceDetector":
        """
        Create a new DeviceDetector instance with a specified cache size.
        
        Args:
            cache_size: The number of user agent strings to cache for faster subsequent lookups.
            
        Returns:
            A new DeviceDetector instance with caching enabled.
        """
        ...
    
    def parse(self, user_agent: str) -> Dict[str, Dict[str, str]]:
        """
        Parse a user agent string and return device information.
        
        Args:
            user_agent: The user agent string to parse.
            
        Returns:
            A dictionary containing device information with the following structure:
            {
                "device": {
                    "type": str,  # e.g., "SmartPhone", "Desktop"
                    "brand": str,  # e.g., "Apple", "Samsung"
                    "model": str   # e.g., "iPhone", "Galaxy S10"
                },
                "os": {
                    "name": str,      # e.g., "iOS", "Android"
                    "version": str,   # e.g., "14.4.2", "10"
                    "platform": str   # e.g., "x64"
                },
                "client": {
                    "name": str,      # e.g., "Chrome", "Safari"
                    "version": str,   # e.g., "91.0.4472.124"
                    "type": str       # e.g., "Browser"
                }
            }
            
            All fields are optional and will only be present if detected.
        """
        ... 