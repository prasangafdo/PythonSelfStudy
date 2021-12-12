"""
Created on Dec 8, 2021

@author: Prasanga Fernando
"""


class ElectricityBillCalculator:
    billAmount = None

    def __init__(self, unitsCount):
        if unitsCount < 20:
            self.billAmount = unitsCount * 2
        elif 19 < unitsCount < 50:
            higherAmount = unitsCount - 20
            calculatedAmount = higherAmount * 3 + (unitsCount - higherAmount) * 2
            self.billAmount = calculatedAmount
            # higherAmount = pointsCount - 50
            # calculatedAmount = higherAmount*5
            # lowerAmount = pointsCount - higherAmount
        elif unitsCount > 49:
            highestAmount = unitsCount - 50
            higherAmount = unitsCount - highestAmount - 20
            calculatedAmount = higherAmount * 3 + highestAmount * 5 + (unitsCount - (higherAmount + highestAmount)) * 2
            self.billAmount = calculatedAmount

        # if 50 < pointsCount:
        #     self.billAmount = pointsCount * 5
        # elif 50 > pointsCount > 20:
        #     self.billAmount = pointsCount * 3
        # else:
        #     self.billAmount = pointsCount * 2


unitsCount = int(input("Enter number of units to calculate the electricity bill"))

bill1 = ElectricityBillCalculator(unitsCount)
print("Calculated bill amount for the entered unit count is ", bill1.billAmount)
