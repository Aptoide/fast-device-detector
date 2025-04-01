"""Python bindings for rust-device-detector.

A high-performance device detection library built on top of the 
rust-device-detector Rust crate.
"""

from .fast_device_detector import DeviceDetectorWrapper

# Re-export the wrapper as DeviceDetector for a more Pythonic API
DeviceDetector = DeviceDetectorWrapper

__all__ = ["DeviceDetector", "DeviceDetectorWrapper"] 