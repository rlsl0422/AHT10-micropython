## Example
```python
#Using with esp32 c3 super

import AHT10
from machine import I2C, Pin

i2c = I2C(0, scl=Pin(9), sda= Pin(8), freq=400000)

aht10 = AHT10.AHT10(i2c)

print(aht10.get_temp(),aht10.get_humidity())
```
