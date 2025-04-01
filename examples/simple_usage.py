#!/usr/bin/env python3
"""
Simple example demonstrating the use of device_detector.
"""

from device_detector import DeviceDetector

# Example user agent strings
user_agents = [
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
]

def print_detection_result(result):
    print("\nDetection Result:")
    print("----------------")
    
    if "device" in result:
        device = result["device"]
        print(f"Device Type: {device.get('type', 'Unknown')}")
        print(f"Device Brand: {device.get('brand', 'Unknown')}")
        print(f"Device Model: {device.get('model', 'Unknown')}")
    
    if "os" in result:
        os = result["os"]
        print(f"OS Name: {os.get('name', 'Unknown')}")
        print(f"OS Version: {os.get('version', 'Unknown')}")
        print(f"OS Platform: {os.get('platform', 'Unknown')}")
    
    if "client" in result:
        client = result["client"]
        print(f"Client Name: {client.get('name', 'Unknown')}")
        print(f"Client Version: {client.get('version', 'Unknown')}")
        print(f"Client Type: {client.get('type', 'Unknown')}")
    
    print("\n==================================================\n")

def main():
    # Create a detector with a cache size of 1000
    detector = DeviceDetector.with_cache(1000)
    
    # Parse each user agent string
    for user_agent in user_agents:
        print(f"Parsing user agent: {user_agent}")
        result = detector.parse(user_agent)
        print_detection_result(result)

if __name__ == "__main__":
    main() 