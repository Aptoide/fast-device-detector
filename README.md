# Fast Device Detector

A fast device detection library written in Rust with Python bindings.

## Installation

The package is available as a private package on GitHub. To install it:

```bash
pip install --index-url https://github.com/simplecastapps/rust-device-detector.git fast-device-detector
```

This will automatically download and install the appropriate wheel for your platform and Python version.

## Usage

```python
from fast_device_detector import DeviceDetector

# Create a detector with a cache size of 1000
detector = DeviceDetector.with_cache(1000)

# Parse a user agent string
user_agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1"
result = detector.parse(user_agent)

# Access the results
if "device" in result:
    device = result["device"]
    print(f"Device Type: {device.get('type')}")
    print(f"Device Brand: {device.get('brand')}")
    print(f"Device Model: {device.get('model')}")

if "os" in result:
    os = result["os"]
    print(f"OS Name: {os.get('name')}")
    print(f"OS Version: {os.get('version')}")
    print(f"OS Platform: {os.get('platform')}")

if "client" in result:
    client = result["client"]
    print(f"Client Name: {client.get('name')}")
    print(f"Client Version: {client.get('version')}")
    print(f"Client Type: {client.get('type')}")
```

## Development

To build from source (for development):

```bash
pip install maturin
maturin develop
```

## License

This project is licensed under the MIT License - see the LICENSE file for details. 