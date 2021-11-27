import serial
from time import sleep
import json

class sim900:
    def __init__(self,baudrate=9600,port='/dev/tty0',timeout=1,log=False):
        self.port=serial.Serial(port,baudrate=baudrate,timeout=timeout)
        self.log=log
    
    def get_serial_msg(self):
        sleep(2)
        result=self.port.readall()
        self.port.reset_input_buffer()
        self.port.reset_output_buffer()
        if self.log:
            print(result)
        return result

    def gsm_start(self, apn='www'):
        self.port.write(str.encode('AT\r\n'))
        responce=self.get_serial_msg()
        if responce == None or 'OK' not in responce:
            raise Exception('No Responce!')
        self.port.write(str.encode("AT+SAPBR=3,1,\"Contype\",\"GPRS\"\r\n"))
        self.get_serial_msg()
        self.port.write(str.encode("AT+SAPBR=3,1,\"APN\",\"{}\"\r\n".format(apn)))
        self.get_serial_msg()
        self.port.write(str.encode("AT+SAPBR=1,1\r\n"))
        self.get_serial_msg()
        self.port.write(str.encode("AT+SAPBR=2,1\r\n"))
        self.get_serial_msg()
        
    def http_init(self, url):
        self.port.write(str.encode("AT+HTTPINIT\r\n"))
        self.get_serial_msg()
        self.port.write(str.encode("AT+HTTPPARA=\"CID\",1\r\n"))
        self.get_serial_msg()
        self.port.write(str.encode("AT+HTTPPARA=\"URL\",\"{}\"\r\n".format(url)))
        
        
    def http_get(self, url):
        pass
    
    def http_post(self, url, data):
        self.http_init(url)
        self.port.write(b"AT+HTTPPARA=\"CONTENT\",\"application/json\"\r\n")
        self.get_serial_msg()
        self.port.write(str.encode("AT+HTTPDATA={},100000\r\n".format(len(data))))
        self.get_serial_msg()
        self.port.write(str.encode(data))
        self.get_serial_msg()
        self.port.write(b"AT+HTTPACTION=1\r\n")
        self.get_serial_msg()
        self.port.write(b"AT+HTTPTERM\r\n")
    