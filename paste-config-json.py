"""
https://github.com/cnadler86/micropython-camera-API/blob/0fd1f6cf561b0e26833acad741e4e6b16b5cdd02/src/camera_pins.h#L232

#define MICROPY_CAMERA_PIN_PWDN     MICROPY_CAMERA_PIN_NONE
#define MICROPY_CAMERA_PIN_RESET    MICROPY_CAMERA_PIN_NONE
#define MICROPY_CAMERA_PIN_XCLK     15
#define MICROPY_CAMERA_PIN_SIOD     4
#define MICROPY_CAMERA_PIN_SIOC     5

#define MICROPY_CAMERA_PIN_D0       11
#define MICROPY_CAMERA_PIN_D1       9
#define MICROPY_CAMERA_PIN_D2       8
#define MICROPY_CAMERA_PIN_D3       10
#define MICROPY_CAMERA_PIN_D4       12
#define MICROPY_CAMERA_PIN_D5       18
#define MICROPY_CAMERA_PIN_D6       17
#define MICROPY_CAMERA_PIN_D7       16
#define MICROPY_CAMERA_PIN_VSYNC    6
#define MICROPY_CAMERA_PIN_HREF     7
#define MICROPY_CAMERA_PIN_PCLK     13


https://github.com/cnadler86/micropython-camera-API/tree/0fd1f6cf561b0e26833acad741e4e6b16b5cdd02

Default values:
- xclk_freq: 20MHz // Default for OV2640 (normally either 10 MHz or 20 MHz). Plase adapt it to your camera sensor.
- frame_size: QQVGA
- pixel_format: RGB565
- jpeg_quality: 85 // Quality of JPEG output in percent. Higher means higher quality.
- powerdown_pin and reset_pin: -1 ( = not used/available/needed)
- fb_count:
  - 2 for ESP32S3 boards
  - 1 for all other
- grab_mode:
  - LATEST for ESP32S3 boards
  - WHEN_EMPTY for all other

"""

with open("config.json", "w") as f:
    f.write(r'''
{
  "data_pins": [11,9,8,10,12,18,17,16],
  "pclk_pin": 13,
  "vsync_pin": 6,
  "href_pin": 7,
  "sda_pin": 4,
  "scl_pin": 5,
  "xclk_pin": 15,
  "xclk_freq": 20000000,
  "powerdown_pin": -1,
  "reset_pin": -1
}
    ''')

