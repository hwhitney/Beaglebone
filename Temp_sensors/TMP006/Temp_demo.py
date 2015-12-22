#!/usr/bin/env python
import time
import Adafruit_TMP.TMP006 as TMP006

#code from example in Adafruit_Python_TMP
# For the Beaglebone Black the library will assume bus 1 by default, which is
# exposed with SCL = P9_19 and SDA = P9_20.
sensor = TMP006.TMP006()
sensor.begin()
'''
Optionally initialize with a faster but less precise sample rate.
You can use any value from TMP006_CFG_1SAMPLE, TMP006_CFG_2SAMPLE,
TMP006_CFG_4SAMPLE,TMP006_CFG_8SAMPLE, or TMP006_CFG_16SAMPLE for the
sample rate.
sensor.begin(samplerate=TMP006.CFG_1SAMPLE)
'''
# Loop printing measurements every second.
print 'Press Ctrl-C to quit.'
while True:
    obj_temp = sensor.readObjTempC()
    die_temp = sensor.readDieTempC()
    print 'Object temperature: {0:0.3F}C'.format(obj_temp)
    print '   Die temperature: {0:0.3F}C'.format(die_temp)
    time.sleep(1.0)
#!/usr/bin/env python
