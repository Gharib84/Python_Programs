from logic import Investment
import tkinter as tk
from tkinter import ttk
import locale

class FutureValueFrame(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10 ")
        self.parent = parent
        self.investment = Investment()
        result = locale.setlocale(locale.LC_ALL, "")
        if result == "c":
            locale.setlocale(locale.LC_ALL, "en_US")
        self.monthlyInvestment = tk.StringVar()
        self.yearlyInterestRate = tk.StringVar()
        self.years = tk.StringVar()
        self.futureValue = tk.StringVar()

        self.initcomponent()


    def initcomponent(self):
        self.pack()
        ttk.Label(self, text="Monthly Investment: ").grid(column=0, row=0, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.monthlyInvestment).grid(column=1, row=0)
        ttk.Label(self, text="Yearly Interest Rate: ").grid(column=0, row=1, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.yearlyInterestRate).grid(column=1, row=1)
        ttk.Label(self, text="Years: ").grid(column=0, row=2, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.years).grid(column=1, row=2)
        ttk.Label(self, text="Future Value: ").grid(column=0, row=3, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.futureValue, state="readonly").grid(column=1, row=3)

        self.makeButtons()

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=3)

    def makeButtons(self):
        buttonFrame = ttk.Frame(self)
        buttonFrame.grid(column=0, row=4, columnspan=2, sticky=tk.E)
        ttk.Button(buttonFrame, text="calculate", command=self.calculate).grid(column=0, row=0, padx=5)
        ttk.Button(buttonFrame, text="Exit", command=self.parent.destroy).grid(column=1, row=0)


    def calculate(self):
        self.investment.monthlyInvestment = float(self.monthlyInvestment.get())
        self.investment.yearInterestRate = float(self.yearlyInterestRate.get())
        self.investment.years = int(self.years.get())
        self.futureValue.set(locale.currency(self.investment.CalculateFutureValue(), grouping=True))

  
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Future Calculate Value")
    FutureValueFrame(root)
    root.mainloop()