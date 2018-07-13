class Investment:
    def __init__(self):
        self.monthlyInvestment = 0
        self.yearInterestRate = 0
        self.years = 0

    def CalculateFutureValue(self):
        monthyInterestRate = self.yearInterestRate /12 /100
        months = self.years * 12
        futureValue = 0
        for i in range(months):
            futureValue += self.monthlyInvestment
            monthlyInterestAmount = futureValue * monthyInterestRate
            futureValue +=  monthlyInterestAmount

        return futureValue


