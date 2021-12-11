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
        elif pointsCount > 49:
            highestAmount = pointsCount - 50
            higherAmount = pointsCount - highestAmount - 20
            calculatedAmount = higherAmount * 3 + highestAmount * 5 + (pointsCount - (higherAmount + highestAmount)) * 2
            self.billAmount = calculatedAmount

        # if 50 < pointsCount:
        #     self.billAmount = pointsCount * 5
        # elif 50 > pointsCount > 20:
        #     self.billAmount = pointsCount * 3
        # else:
        #     self.billAmount = pointsCount * 2


bill1 = ElectricityBillCalculator(49)
print(bill1.billAmount)

bill2 = ElectricityBillCalculator(52)
print(bill2.billAmount)
# bill1 = ElectricityBillCalculator(20)
# print(bill1.billAmount)
# bill1 = ElectricityBillCalculator(19)
# print(bill1.billAmount)
# bill1 = ElectricityBillCalculator(40)
# print(bill1.billAmount)
# bill1 = ElectricityBillCalculator(70)
# print(bill1.billAmount)
