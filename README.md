# MicroPython Scripts

Welcome to my collection of basic MicroPython scripts! This repository is a personal project aimed at learning and experimenting with MicroPython. As a beginner in this field, I appreciate any advice or feedback you can offer.


## Introduction

This repository contains a variety of simple scripts written in MicroPython. These scripts are designed to help beginners (like myself) get familiar with the basics of MicroPython and its capabilities. As I am still learning, I welcome and greatly appreciate any advice or feedback.

## Getting Started

### Prerequisites

To run these scripts, you will need:

- A MicroPython-compatible board (e.g., ESP8266, ESP32, RPi Pico)
- USB cable for connecting the board to your computer
- MicroPython firmware installed on your board
- A code editor (e.g., Thonny, VSCode) and a way to upload scripts to your board (e.g., ampy, rshell, or the built-in tools in Thonny)

### Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/gibbato/micropython-scripts.git
    ```
2. Connect your MicroPython-compatible board to your computer.
3. Upload the desired script to your board using your preferred method.

## Scripts

### 1. `blink.py`

This script blinks the onboard LED for a Raspberry Pi Pico.

### 2. `socket_webserver.py`

This script sets up a simple web server on a MicroPython-compatible board (such as the Raspberry Pi Pico) that turns on an LED and notifies the user via text on a web page.

### 3. `onbrd_led_w_web_server.py`

This script sets up a simple web server on a MicroPython-compatible board (such as the Raspberry Pi Pico) that allows you to control an LED through a web interface.

### 4. `external_led.py`

This script blinks an external led using pin 15

### 5. `external_led_webserver.py`

This script to control an external LED via a web server using pin 15.

### `secrets.py` File

Before running the script, ensure you have a `secrets.py` file with your Wi-Fi credentials. It should look like this:

```python
SSID = 'your-ssid'
PASSWORD = 'your-password'


