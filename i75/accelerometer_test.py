from machine import Pin, I2C
from devices import lis3dh
import time
i2c = I2C(0, sda=Pin(20), scl=Pin(21))
print(i2c.scan())
imu = lis3dh.LIS3DH_I2C(i2c)

# If we have found the LIS3DH
if imu.device_check():
    # Set range of accelerometer (can be RANGE_2_G, RANGE_4_G, RANGE_8_G or RANGE_16_G).
    imu.range = lis3dh.RANGE_2_G

    # Loop forever printing accelerometer values
    while True:
        # Read accelerometer values (in m / s ^ 2).  Returns a 3-tuple of x, y,
        # z axis values.  Divide them by 9.806 to convert to Gs.
        x, y, z = [value / lis3dh.STANDARD_GRAVITY for value in imu.acceleration]
        print("x = %0.3f G, y = %0.3f G, z = %0.3f G" % (x, y, z))
        # Small delay to keep things responsive but give time for interrupt processing.
        time.sleep(1)