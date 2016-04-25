from registerCommands import setRegister
from registerCommands import resetRegister
from registerCommands import statusRegister
from serialTxRx import sendSerial


while True:
    try:
        cmdString = str(input('Give command: '))
        regNum = int(input('Give output number: '))
        if cmdString == 'set':
            sendSerial(setRegister[regNum])
        elif cmdString == 'reset':
            sendSerial(resetRegister[regNum])
        elif cmdString == 'status':
            sendSerial(statusRegister[regNum])

    except ValueError:
        print('Wrong values')
        break


