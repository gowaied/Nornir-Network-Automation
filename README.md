# Nornir Network Automation

## Overview
This project automates the configuration of network devices using [Nornir](https://nornir.readthedocs.io/en/latest/), a powerful Python automation framework. The script configures loopback interfaces on routers and VLANs on switches.

## Features
- Automates loopback configuration on routers.
- Configures VLANs on switches.
- Uses **Netmiko** for device communication.
- Uses **Nornir** for inventory management and task execution.
- Collects real-time command output for verification.
- Supports user authentication at runtime.

## Prerequisites
Ensure the following are installed on your system:

- Python 3.8+
- Nornir (`pip install nornir`)
- Netmiko (`pip install netmiko`)
- Nornir Netmiko plugin (`pip install nornir-netmiko`)
- Nornir Utilities (`pip install nornir-utils`)
- A valid `config.yml` file for Nornir inventory.

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/nornir-network-automation.git
   cd nornir-network-automation
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
1. Ensure your `config.yml` file is properly set up for your network inventory.
2. Run the script:
   ```sh
   python nornir_script.py
   ```
3. Enter your credentials when prompted.
4. The script will configure routers and switches as per the predefined settings.
5. After router configuration, press **Enter** to proceed with VLAN setup on switches.

## Configuration Details
### Loopback Interface Configuration
- Adds a loopback interface (`Lo0`) on routers.
- Assigns unique IP addresses with a `/32` subnet mask.

### VLAN Configuration
- Creates VLANs 10, 20, 30, and 40.
- Assigns them names: Engineering, Sales, HR, and Accounting.

## Example Output
```
Enter the username: admin
Enter the password:
Enter the secret:

+----------------------+-----------------+
| Device              | Output          |
+----------------------+-----------------+
| R1                  | Loopback Config |
| SW1                 | VLANs Created   |
+----------------------+-----------------+
```

## Contributing
Feel free to contribute by submitting issues or pull requests.


## Author
[Mohamed Gowaied](https://github.com/gowaied)

