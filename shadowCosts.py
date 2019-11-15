
def getCostArray():
	pricetable = open("supplycostdemand.txt",'r')

	costlines = pricetable.readlines()[:-1]

	pricetable.close()

	costLoS = []
	for i in costlines:
		costLoS = costLoS + i.split()#[ "no,no,no","no,no,no","no,no,no"] is the format of values currently

	costLoSS = []
	for s in costLoS:
		costLoSS = costLoSS + s.split(',')#["no","no","no","no",....] 
	del costLoSS[3::4]#removes every 4th value, in this case the supply values

	costLoLI = []

	for i in range(len(costLoSS)):
		costLoLI = costLoLI + [int(costLoSS[i])]#[no, no, no, no, ...]

	costLoLG = [costLoLI[n:n+3]for n in range(0, len(costLoLI), 3)] #[[no, no, no][no, no, no][no, no, no]]

	return(costLoLG)

def getSupplyArray():

	pricetable2 = open("supplycostdemand.txt",'r')

	supplylines = pricetable2.readlines()[:-1]

	pricetable2.close()

	supplyLoS = []
	for i in supplylines:
		supplyLoS = supplyLoS + i.split()#["no,no,no,no","no,no,no,no","no,no,no,no"]

	supplyLoSS = []
	for s in supplyLoS:
		supplyLoSS = supplyLoSS + s.split(',')

	supplyLoSSS = supplyLoSS[3::4]#every 4th element(the supply value of each line) is saved into a new list 

	supplyLoI = []
	for i in range(len(supplyLoSSS)):
		supplyLoI = supplyLoI + [int(supplyLoSSS[i])]

	return supplyLoI

def getDemandArray():

	pricetable3 = open("supplycostdemand.txt",'r')

	demandline = pricetable3.readlines()[-1]

	pricetable3.close()

	demandLoS = [demandline]

	demandLoSS = []
	for i in demandLoS:
		demandLoSS = demandLoSS + i.split(',')

	demandLoI = []
	for i in range(len(demandLoSS)):
		demandLoI = demandLoI + [int(demandLoSS[i])]

	return demandLoI

SupplyArray = getSupplyArray()

CostArray = getCostArray()

DemandArray = getDemandArray()

print ("Cost Array:" , CostArray)

print ("Supply Array:" , SupplyArray)

print ("Demand Array:" , DemandArray)

allocation = [[None,None,None], #create a blank 2D array to be filled with initial allocation values
              [None,None,None],
              [None,None,None]]

supplyInd = 0 #set index values to 0 to begin in the north-west corner of the array
demandInd = 0
sumSupply = SupplyArray[0] + SupplyArray[1] + SupplyArray[2] #find the sum of the supply

while sumSupply > 0: #conditional which terminates the allocation once all supply has been distributed
	if SupplyArray[supplyInd] <= DemandArray[demandInd]:
		allocation[supplyInd][demandInd] = SupplyArray[supplyInd]
		sumSupply = sumSupply - SupplyArray[supplyInd]
		DemandArray[demandInd] = DemandArray[demandInd] - SupplyArray[supplyInd]
		supplyInd = supplyInd + 1

	elif SupplyArray[supplyInd] > DemandArray[demandInd]:
		allocation[supplyInd][demandInd] = DemandArray[demandInd]
		sumSupply = sumSupply - DemandArray[demandInd]
		SupplyArray[supplyInd] = SupplyArray[supplyInd] - DemandArray[demandInd]
		demandInd = demandInd + 1
	

print ("Initial allocation:" , allocation)
