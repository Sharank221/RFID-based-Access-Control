from mfrc522 import MFRC522 
import utime
from machine import Pin
buzzer = Pin(27, Pin.OUT)
RLed =Pin(18,Pin.OUT)
GLed =Pin(19,Pin.OUT)
buzzer.value(0)
RLed.value(0)
GLed.value(0)



def uidToString(uid):
    mystring = ""
    for i in uid:
        mystring = "%02X" % i + mystring
    return mystring
                  
rc522 = MFRC522(spi_id=0,sck=6,miso=4,mosi=7,cs=5,rst=22)

print("")
print("Place the RFID Card")
print("")


while True:

    (stat, tag_type) = rc522.request(rc522.REQALL)

    if stat == rc522.OK:
        (status, raw_uid) = rc522.SelectTagSN()
        if stat == rc522.OK:
            rfid_data = "{:02x}{:02x}{:02x}{:02x}".format(raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3])
            print("Card detected! UID: {}".format(rfid_data))
            if rfid_data == "21b87f1d":
                print("USER 1")
                GLed.value(0.5)
                utime.sleep(0.5)
            elif rfid_data == "4381e195":
                print("USER 2")
                GLed.value(0.5)
                utime.sleep(0.5)
            elif rfid_data == "11ca7c23":
                print("USER 3")
                GLed.value(0.5)
                utime.sleep(0.5)
            else:
                print("unauthorized User")
                buzzer.value(1)
                RLed.value(1)
                utime.sleep(1)
                buzzer.value(0)
                RLed.value(0)
                