import time
from serialTxRx import *

class disRegister():
    def __init__(self, yNumber):
        self.yNumber = yNumber  # Y output number
        

    ser = setSerialSettings()
    sendComm = []
    
    def overHead(self, sendComm):
        sendComm.append('0x02')                     # STX
        stationNo = '01'                            # Station Number 01

        for i in stationNo:
            sendComm.append(hex(ord(i)))           # append station number

    def set(self, yNumber):
        del self.sendComm[:]
        self.overHead(self.sendComm)
        controlDiscrete = '42'
        for i in controlDiscrete:
            self.sendComm.append(hex(ord(i)))           # append command number

        self.sendComm.append(hex(ord('3')))             # append set command

        for i in yNumber:
            self.sendComm.append(hex(ord(i)))           # append output number

        #print('Set Command:')
        self.calcLrc()

    def reset(self, yNumber):
        del self.sendComm[:]
        self.overHead(self.sendComm)
        controlDiscrete = '42'
        for i in controlDiscrete:
            self.sendComm.append(hex(ord(i)))  # append command number
        self.sendComm.append(hex(ord('4')))  # append reset command
        for i in yNumber:
            self.sendComm.append(hex(ord(i)))  # append output number

        #print('Reset Command:')
        self.calcLrc()

    def readDisStatus(self, yNumber):
        del self.sendComm[:]
        self.overHead(self.sendComm)
        readDisctete = '44'
        for i in readDisctete:
            self.sendComm.append(hex(ord(i)))
        self.sendComm.append(hex(ord('0')))
        self.sendComm.append(hex(ord('1')))
        for i in yNumber:
            self.sendComm.append(hex(ord(i)))  # append output number

        #print('Status command')
        self.calcLrc()

    def calcLrc(self):
        lrcSum = 0
        for i in range(0, len(self.sendComm)):
            lrcSum += int(self.sendComm[i], 16)

        lrcSum = str(hex(lrcSum))
        lrcSumUppercase = lrcSum.upper()
        lrcHight = hex(ord(lrcSumUppercase[3]))
        lrcLow = hex(ord(lrcSumUppercase[4]))

        self.sendComm.append(lrcHight)  # append high byte of LRC
        self.sendComm.append(lrcLow)  # append low byte of LRC
        self.sendComm.append('0x03')  # append ETX ($03)
        #print(self.sendComm)
        
        #self.serialRxTx(self.sendComm, self.ser)  # send to serial RX
        #return(self.sendComm)
        return(self.sendComm)
        del self.sendComm[:]
   

    # def serialRxTx(self, sendComm, ser):
    #     sendCommInt = []
    #     for i in range(0, len(self.sendComm)):
    #         sendCommInt.append(int(self.sendComm[i],16))

    #     print(sendCommInt)

    #     try: 
    #         ser.open()
    #     except Exception as e:
    #         print ('error open serial port: ' + str(e))
    #         exit()
    #     if ser.isOpen():
    #         try:
    #             ser.flushInput() #flush input buffer, discarding all its contents
    #             ser.flushOutput()#flush output buffer, aborting current output 
    #             ser.write(serial.to_bytes(sendCommInt))
    #             print('write data: {}', sendCommInt)
    #             time.sleep(0.01)  #give the serial port sometime to receive the data
    #             linesNum = 0
    #             while True:
    #                 response = ser.readline()
    #                 print('read data: ', response)
    #                 linesNum +=1
    #                 if (linesNum>=1):
    #                     break
    #             ser.close()
    #             del sendCommInt[:]
    #         except Exception as e1:
    #             print('error communicating...: ' + str(e1))
    #     else:
    #         print('cannot open serial port ')

    # self.parseResponse(self.sendComm, serialResponse)
    
    # def parseResponse(self, sendComm, serialResponse):
        
    #     if (len(serialResponse)==9):    # response from set/reset
    #         if(serialResponse[5]=='0x30' and self.sendComm[5]=='0x33'):  # no error
    #             print('Set response')
    #             print(serialResponse)
    #             print('{} is set!'.format(self.yNumber))

    #         elif(serialResponse[5]=='0x30' and self.sendComm[5]=='0x34'):
    #             print('Reset response')
    #             print(serialResponse)
    #             print('{} is reset!'.format(self.yNumber))

    #         elif(serialResponse[5]!='0x30'):
    #             print('error {} in set/reset serial read',serialResponse[5]) # response error
        
    #     elif(len(serialResponse)==10): # response from status reading

    #         if(serialResponse[6]=='0x30'): # no error
    #             if(serialResponse[7]=='0x30'):
    #                 print('{} status is OFF!'.format(self.yNumber))
    #             elif(serialResponse[7]=='0x31'):
    #                 print('{} status is ON!'.format(self.yNumber))
            
    #         else:
    #             print('error {} in serial status read',serialResponse[6])

    #     del self.sendComm[:] # delete sendComm buffer for next command'''