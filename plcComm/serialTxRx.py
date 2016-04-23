import serial
import time

ser = serial.Serial()


def setSerialSettings():
	ser.port = 'set port COM10'
	ser.baudrate = 9600
	ser.bytesize = serial.SEVENBITS             # number of bits per bytes
	ser.parity = serial.PARITY_EVEN             # set parity check: no parity
	ser.stopbits = serial.STOPBITS_ONE          # number of stop bits
	ser.timeout = 1                             # non-block read
	# ser.timeout = 2                           # timeout block read
	ser.xonxoff = False                         # disable software flow control
	ser.rtscts = False                          # disable hardware (RTS/CTS) flow control
	ser.dsrdtr = False                          # disable hardware (DSR/DTR) flow control
	ser.writeTimeout = 2                        # timeout for write

setSerialSettings()


def serialTxRx(command):
	print('send command is:', command)
	try:
		ser.open()
	except Exception as e:
		print('error open serial port: ' + str(e))
		exit()
	if ser.isOpen():
		try:
			ser.flushInput()                        # flush input buffer, discarding all its contents
			ser.flushOutput()                       # flush output buffer, aborting current output
			ser.write(serial.to_bytes(command))
			print('write data: {}', command)
			time.sleep(0.01)                        # give the serial port sometime to receive the data
			linesNum = 0
			while True:
				response = ser.readline()           # read data from serial
				print('read data: ', response)
				linesNum += 1
				if linesNum >= 1:
					break
			ser.close()

			parseResponse(response)                 # check received data

		except Exception as e1:
			print('error communicating...: ' + str(e1))
	else:
		print('cannot open serial port ')


def parseResponse(response):
	pass


def setReg(setCommand):
	serialTxRx(setCommand)

def resetReg(resetCommand):
	serialTxRx(resetCommand)