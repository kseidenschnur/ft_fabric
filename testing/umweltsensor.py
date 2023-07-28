import ftrobopy

txt = ftrobopy.ftrobopy(host="192.168.0.14")
res = txt.i2c_read(0x76, 0x22) #0x00 - 0xFF
print(res)