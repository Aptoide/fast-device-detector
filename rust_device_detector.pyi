from typing import Dict, Optional, Any, ClassVar, Type

class DeviceDetectorWrapper:
    """Python wrapper for the Rust DeviceDetector."""
    
    def __init__(self) -> None:
        """Create a new DeviceDetector."""
        ...
    
    @classmethod
    def with_cache(cls: Type['DeviceDetectorWrapper'], cache_size: int) -> 'DeviceDetectorWrapper':
        """Create a new DeviceDetector with cache.
        
        Args:
            cache_size: Size of the cache in number of entries
            
        Returns:
            A new DeviceDetector instance with caching enabled
        """
        ...
    
    def parse(self, user_agent: str) -> Dict[str, Any]:
        """Parse a user agent string and return device information.
        
        Args:
            user_agent: The user agent string to parse
            
        Returns:
            A dictionary containing parsed information with the following possible keys:
            - device: Information about the device (type, brand, model)
            - os: Information about the operating system (name, version, platform)
            - client: Information about the client (name, version, type)
            - bot: Information about the bot if the user agent belongs to a bot (name)
            
        Raises:
            RuntimeError: If parsing fails
        """
        ... 