use pyo3::exceptions::PyRuntimeError;
use pyo3::prelude::*;
use pyo3::types::{PyDict, PyType};
use rust_device_detector::device_detector::DeviceDetector;

#[pyclass]
struct DeviceDetectorWrapper {
    detector: DeviceDetector,
}

#[pymethods]
impl DeviceDetectorWrapper {
    /// Create a new DeviceDetector
    #[new]
    #[pyo3(text_signature = "()")]
    fn new() -> Self {
        Self {
            detector: DeviceDetector::new(),
        }
    }

    /// Create a new DeviceDetector with cache
    #[classmethod]
    #[pyo3(text_signature = "(cls, cache_size)")]
    fn with_cache(_cls: &Bound<'_, PyType>, cache_size: u64) -> Self {
        Self {
            detector: DeviceDetector::new_with_cache(cache_size),
        }
    }

    /// Parse a user agent string and return device information.
    #[pyo3(text_signature = "(user_agent)")]
    fn parse(&self, py: Python<'_>, user_agent: &str) -> PyResult<PyObject> {
        // Parse the user agent
        let detection_result = self.detector.parse(user_agent, None)
            .map_err(|e| PyErr::new::<PyRuntimeError, _>(
                format!("Failed to parse user agent: {}", e)))?;
        
        // Create the main dictionary for our return value
        let dict = PyDict::new(py);
        
        // Add device information if available
        if let Some(known_device) = detection_result.get_known_device() {
            // Device information
            if let Some(device) = &known_device.device {
                let device_dict = PyDict::new(py);
                
                // Convert device_type to a string representation
                if let Some(device_type) = &device.device_type {
                    // Convert the enum to a string the safest way possible
                    let type_str = format!("{:?}", device_type);
                    device_dict.set_item("type", type_str)?;
                }
                
                device_dict.set_item("brand", &device.brand)?;
                device_dict.set_item("model", &device.model)?;
                dict.set_item("device", device_dict)?;
            }
            
            // OS information
            if let Some(os) = &known_device.os {
                let os_dict = PyDict::new(py);
                os_dict.set_item("name", &os.name)?;
                
                // Add version if available
                if let Some(version) = &os.version {
                    os_dict.set_item("version", version)?;
                }
                
                // Add platform if available
                if let Some(platform) = &os.platform {
                    os_dict.set_item("platform", platform)?;
                }
                
                dict.set_item("os", os_dict)?;
            }
            
            // Client information
            if let Some(client) = &known_device.client {
                let client_dict = PyDict::new(py);
                client_dict.set_item("name", &client.name)?;
                
                // Safely add version if available
                if let Some(version) = &client.version {
                    client_dict.set_item("version", version)?;
                }
                
                // Use the raw identifier syntax r#type to access the 'type' field
                client_dict.set_item("type", format!("{:?}", client.r#type))?;
                
                dict.set_item("client", client_dict)?;
            }
        }
        
        Ok(dict.into())
    }
}

/// A Python module implemented in Rust.
#[pymodule]
fn device_detector(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<DeviceDetectorWrapper>()?;
    Ok(())
}
