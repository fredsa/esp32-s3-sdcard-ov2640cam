
# ESP32-S3 SDCard OV2640 CAM devboard

ESP32-S3 WROOM N16R8 CAM Development Board WiFi+ Bluetooth-compatible Module OV2640/5640 Camera

<img src="devboard/front-back.png" height="40%" width="40%">


# SDCard fix

SDCard `CS` (pin 2) must be pulled low.

- You can tie `CS` permanently to ground (middle example)
- Or, you can connect `CS` to a GPIO pin (left/right shows connection to `IO41`)

<img src="devboard/sdcard-fix.jpg" height="80%" width="80%">
