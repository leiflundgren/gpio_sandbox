#!/usr/bin/python
import RPi.GPIO as GPIO

#Detect and display board information
#If additional changes are made beyond Rev2,
#this code will need to be updated.
print("Meltwater's Pi Hardware - GPIO Info")
print("Board Revision: " + str(GPIO.RPI_REVISION))
if (GPIO.RPI_REVISION > 2):
  print("Warning: New Revision detected check for new pinouts.")
print("P1:")
print(" 3V3     1 2      5V")

#Select board revision here to allow for pins 3 & 5 update
if (GPIO.RPI_REVISION == 1):
 print(" SDA0    3 4      5V")
 print(" SCL0    5 6     Gnd")
else:
 print(" SDA1    3 4      5V")
 print(" SCL1    5 6     Gnd")

print(" GPIO04  7 8      Tx")
print(" Gnd     9 10     Rx")
print(" GPIO17 11 12 GPIO18")

#Select board revision here to allow for pin 13 update
if (GPIO.RPI_REVISION == 1):
 print(" GPIO21 13 14    Gnd")
else:
 print(" GPIO27 13 14    Gnd")

print(" GPIO22 15 16 GPIO23")
print(" 3V3    17 18 GPIO24")
print(" MOSI   19 20    Gnd")
print(" MISO   21 22 GPIO25")
print(" SCLK   23 24    CE0")
print(" Gnd    25 26    CE1")

#Select board revision here for Rev2's new P5 header
# (as viewed from topside)
if (GPIO.RPI_REVISION != 1):
 print("")
 print("P5:")
 print(" 3V3     2 1      5V")
 print(" SCL0    4 3    SDA0")
 print(" GPIO31  6 5  GPIO30")
 print(" Gnd     8 7     Gnd")

#End