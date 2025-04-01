"""
Fast Device Detector - A high-performance device detection library written in Rust.

This module provides Python bindings for the Rust device detector library,
offering fast and accurate device detection from user agent strings.
"""

from .fast_device_detector import DeviceDetector

__version__ = "0.1.0"
__all__ = ["DeviceDetector"] 