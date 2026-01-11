"""
GPIO 0: Pin(0)
GPIO 1: Pin(1)
GPIO 2: Pin(2)
GPIO 3: Pin(3)
GPIO 4: Pin(4)
GPIO 5: Pin(5)
GPIO 6: Pin(6)
GPIO 7: Pin(7)
GPIO 8: Pin(8)
GPIO 9: Pin(9)
GPIO 10: Pin(10)
GPIO 11: Pin(11)
GPIO 12: Pin(12)
GPIO 13: Pin(13)
GPIO 14: Pin(14)
GPIO 15: Pin(15)
GPIO 16: Pin(16)
GPIO 17: Pin(17)
GPIO 18: Pin(18)
GPIO 21: Pin(21)
GPIO 26: Pin(26)
GPIO 33: Pin(33)
GPIO 34: Pin(34)
GPIO 35: Pin(35)
GPIO 36: Pin(36)
GPIO 37: Pin(37)
GPIO 38: Pin(38)
GPIO 39: Pin(39)
GPIO 40: Pin(40)
GPIO 41: Pin(41)
GPIO 42: Pin(42)
GPIO 43: Pin(43)
GPIO 44: Pin(44)
GPIO 45: Pin(45)
GPIO 46: Pin(46)
GPIO 47: Pin(47)
"""

# Print available GPIO pins
from machine import Pin
 
 # ESP32-S3 has up to 48 GPIOs
for i in range(48):
  try:
    p = Pin(i)
    print(f"GPIO {i}: {p}")
  except:
    pass

