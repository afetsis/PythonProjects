from disRegister import *

Y = []
setCommandListHex = []
setCommandListInt = []
resetCommandList = []
testlist = []


for i in range(0, 56):
	Y.append(disRegister('Y00'+str(i).zfill(2)))

print('Set Command List')

for i in range(0, 56):
	Y[i].set('Y00'+str(i).zfill(2))
	setCommandListHex.insert(i, Y[i].sendComm)
	#print(setCommandListHex[i])

print(setCommandListHex[0])



#for i in range(0, 56):
	#for j in range(0, 14):
		#print(setCommandListHex[i][j])






# print('Reset Command List')
# for i in range(0, 55):
# 	Y[i].reset('Y000'+str(i).zfill(2))
# 	resetCommandList.append(Y[i].sendComm)
# 	print(resetCommandList[i])

# Y42.readDisStatus('Y0042')

# M100 = disRegister('M0100')
# M100.set('M0100')
