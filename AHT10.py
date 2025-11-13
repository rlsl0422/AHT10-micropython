import utime


class AHT10:
    def __init__(self, i2c, address=0x38):
        utime.sleep_ms(20)
        self.i2c = i2c
        self.address = address
        self.raw_data = bytearray(6)
        self.temp = None
        self.humidity = None

    def get_temp(self):
        self._measurement()
        return round(self.temp, 2)

    def get_humidity(self):
        self._measurement()
        return round(self.humidity, 2)

    def _measurement(self):
        d = bytearray(4)
        d[0] = 0xAC
        d[1] = 0x33
        d[2] = 0x00
        self.i2c.writeto(self.address, d[0:3])
        utime.sleep_ms(80)
        self.raw_data = self.i2c.readfrom(0x38, 6)
        h = ((self.raw_data[1] << 12) 
             | (self.raw_data[2] << 4) 
             | (self.raw_data[3] >> 4))
        t = (
            ((self.raw_data[3] & 0b00001111) << 16)
            | (self.raw_data[4] << 8)
            | (self.raw_data[5])
        )
        self.temp = t / 1048576 * 200 - 50
        self.humidity = h / 1048576 * 100
