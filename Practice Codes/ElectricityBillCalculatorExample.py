"""
Created on Dec 8, 2021

@author: Prasanga Fernando
"""


class ElectricityBillCalculator:
    billAmount = None

    def __init__(self, pointsCount):
        if pointsCount < 20:
            self.billAmount = pointsCount * 2
        elif 19 < pointsCount < 50:
            higherAmount = pointsCount - 20
            calculatedAmount = higherAmount * 3 + (pointsCount - higherAmount) * 2
            self.billAmount = calculatedAmount
            # higherAmount = pointsCount - 50
            # calculatedAmount = higherAmount*5
            # lowerAmount = pointsCount - higherAmount
        else:
            print("Highh")

        # if 50 < pointsCount:
        #     self.billAmount = pointsCount * 5
        # elif 50 > pointsCount > 20:
        #     self.billAmount = pointsCount * 3
        # else:
        #     self.billAmount = pointsCount * 2

bill1 = ElectricityBillCalculator(21)
print(bill1.billAmount)

# bill1 = ElectricityBillCalculator(20)
# print(bill1.billAmount)
# bill1 = ElectricityBillCalculator(19)
# print(bill1.billAmount)
# bill1 = ElectricityBillCalculator(40)
# print(bill1.billAmount)
# bill1 = ElectricityBillCalculator(70)
# print(bill1.billAmount)
