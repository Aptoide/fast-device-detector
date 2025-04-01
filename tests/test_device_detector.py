#!/usr/bin/env python3
"""
Tests for the device_detector module.
"""

import unittest
from fast_device_detector import DeviceDetector


class DeviceDetectorTests(unittest.TestCase):
    """Test cases for the DeviceDetector class."""

    def setUp(self):
        """Set up the test environment."""
        self.detector = DeviceDetector()
        self.detector_with_cache = DeviceDetector.with_cache(1000)

    def test_basic_initialization(self):
        """Test that the detector can be initialized."""
        self.assertIsNotNone(self.detector)
        self.assertIsNotNone(self.detector_with_cache)

    def test_parse_mobile_device(self):
        """Test parsing a mobile device user agent."""
        iphone_ua = "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1"
        result = self.detector.parse(iphone_ua)
        
        # Check that device information is present
        self.assertIn("device", result)
        self.assertIn("os", result)
        self.assertIn("client", result)
        
        # Check specific device details
        device = result["device"]
        self.assertEqual(device.get("brand"), "Apple")
        self.assertIn("iPhone", device.get("model", ""))
        
        # Check OS details
        os = result["os"]
        self.assertEqual(os.get("name"), "iOS")
        
        # Check client details
        client = result["client"]
        self.assertEqual(client.get("name"), "Mobile Safari")

    def test_parse_desktop_device(self):
        """Test parsing a desktop device user agent."""
        chrome_ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        result = self.detector.parse(chrome_ua)
        
        # Check that device information is present
        self.assertIn("device", result)
        self.assertIn("os", result)
        self.assertIn("client", result)
        
        # Check OS details
        os = result["os"]
        self.assertEqual(os.get("name"), "Windows")
        self.assertIn("10", os.get("version", ""))
        
        # Check client details
        client = result["client"]
        self.assertEqual(client.get("name"), "Chrome")
        self.assertIn("91", client.get("version", ""))

    def test_cache_functionality(self):
        """Test that caching works by parsing the same user agent twice."""
        # This is a simple test to ensure the with_cache method doesn't error
        # We can't directly test cache hits, but we can verify it works
        ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        
        # Parse the same UA twice with the cached detector
        result1 = self.detector_with_cache.parse(ua)
        result2 = self.detector_with_cache.parse(ua)
        
        # The results should be identical
        self.assertEqual(result1, result2)


if __name__ == "__main__":
    unittest.main() 