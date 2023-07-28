#!/usr/bin/env python3
import ftrobopy

txt=ftrobopy.ftrobopy('auto', use_TransferAreaMode=True)

temperatur = txt.getTemperature()
print(temperatur)
spannung = txt.getPower()
print(spannung)