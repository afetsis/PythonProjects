sendComm = []


def setCommand(yNumber):
    overHead()
    controlDiscrete = '42'
    for i in controlDiscrete:
        sendComm.append(hex(ord(i)))           # append command number

    sendComm.append(hex(ord('3')))             # append set command
    for i in yNumber:
        sendComm.append(hex(ord(i)))           # append output number
    calcLrc()


def resetCommand(yNumber):
    overHead()
    controlDiscrete = '42'
    for i in controlDiscrete:
        sendComm.append(hex(ord(i)))  # append command number
    sendComm.append(hex(ord('4')))  # append reset command
    for i in yNumber:
        sendComm.append(hex(ord(i)))  # append output number
    calcLrc()


def readRegStatus(yNumber):
    overHead()
    readDisctete = '44'
    for i in readDisctete:
        sendComm.append(hex(ord(i)))
    sendComm.append(hex(ord('0')))
    sendComm.append(hex(ord('1')))
    for i in yNumber:
        sendComm.append(hex(ord(i)))  # append output number
    calcLrc()


def overHead():
    sendComm.append('0x02')                     # STX
    stationNo = '01'                            # Station Number 01
    for i in stationNo:
        sendComm.append(hex(ord(i)))           # append station number


def calcLrc():
    lrcSum = 0
    for i in range(0, len(sendComm)):
        lrcSum += int(sendComm[i], 16)

    lrcSum = str(hex(lrcSum))
    lrcSumUppercase = lrcSum.upper()
    lrcHight = hex(ord(lrcSumUppercase[3]))
    lrcLow = hex(ord(lrcSumUppercase[4]))

    sendComm.append(lrcHight)  # append high byte of LRC
    sendComm.append(lrcLow)  # append low byte of LRC
    sendComm.append('0x03')  # append ETX ($03)

# create set commands list
setRegisterHex = []
for x in range(0, 56):
    setCommand('Y00' + str(x).zfill(2))
    setRegisterHex.insert(x, sendComm)
    sendComm = []
setRegister = []
templist = []

for i in range(0, len(setRegisterHex)):         # calc integer set commands
    for j in range(0, len(setRegisterHex[i])):
        templist.append(int(setRegisterHex[i][j], 16))
    setRegister.append(templist)
    templist = []

# create reset command list
resetRegisterHex = []
for x in range(0, 56):
    resetCommand('Y00' + str(x).zfill(2))
    resetRegisterHex.insert(x, sendComm)
    sendComm = []
resetRegister = []


for i in range(0, len(resetRegisterHex)):           # calc integer reset commands
    for j in range(0, len(resetRegisterHex[i])):
        templist.append(int(resetRegisterHex[i][j], 16))
    resetRegister.append(templist)
    templist = []

# create status integer command list
statusRegisterHex = []
for x in range(0, 56):
    readRegStatus('Y00' + str(x).zfill(2))
    statusRegisterHex.insert(x, sendComm)
    sendComm = []
statusRegister = []


for i in range(0, len(statusRegisterHex)):           # calc integer reset commands
    for j in range(0, len(statusRegisterHex[i])):
        templist.append(int(statusRegisterHex[i][j], 16))
    statusRegister.append(templist)
    templist = []