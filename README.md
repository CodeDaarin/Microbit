# Set H — BMI-1: micro:bit LEGO–Colab Interface

## Requirements

### Minimum System Requirements
- **Python**: 3.8 or higher (tested on 3.10–3.13)
- **OS**: Windows 10/11 (primary), Linux, macOS
- **Hardware**: BBC micro:bit (v1 or v2) connected via USB
- **Jupyter**: Local runtime (VS Code recommended, Conda can be used as well)

### Python Packages
- pyserial
- ipywidgets
- jupyter_http_over_ws
- paho-mqtt

### Usage instructions
- Plug in your microbit to your computer via USB
- Flash the 'microbit.py' file to the microbit using microbit's official website: https://python.microbit.org/v/3
    - Copy and paste the program into the website and click on 'Send to micro:bit'
- Run "Colab_server_microbit.ipynb" in Google Colab
- Run "Local_server_microbit.ipynb" in your VS Code or Conda Jupyter environment
