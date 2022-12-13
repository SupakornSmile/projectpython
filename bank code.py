from tkinter import *

class depositacc:
    def __init__(self):
        window = Tk()
        window.title("deposit")

        Label(window, text = "Interest Rate").grid(row = 1,column = 1, sticky = W)
        Label(window, text = "Months").grid(row = 2,column = 1, sticky = W)
        Label(window, text = "Balance").grid(row = 3,column = 1, sticky = W)
        Label(window, text = "Change (for change)").grid(row = 4,column = 1, sticky = W)
        Label(window, text = "When (for change)").grid(row = 5,column = 1, sticky = W)
        Label(window, text = "Total Receive").grid(row = 6,column = 1, sticky = W)
        Label(window, text = "After Change").grid(row = 7,column = 1, sticky = W)
 
        self.intrate = StringVar()   
        Entry(window, textvariable = self.intrate,justify = RIGHT).grid(row = 1, column = 2)
 
        self.months = StringVar()
        Entry(window, textvariable = self.months,justify = RIGHT).grid(row = 2, column = 2)

        self.balanc = StringVar()
        Entry(window, textvariable = self.balanc,justify = RIGHT).grid(row = 3, column = 2)

        self.change = StringVar()
        Entry(window, textvariable = self.change,justify = RIGHT).grid(row = 4, column = 2)

        self.when = StringVar()
        Entry(window, textvariable = self.when,justify = RIGHT).grid(row = 5, column = 2)
        
        self.totalpay = StringVar()
        lblTotalre = Label(window, textvariable =self.totalpay).grid(row = 6,column = 2, sticky = E)
     
        btTotalre = Button(window, text = "Result",command = self.result).grid(row = 8, column = 2, sticky = E)

        self.changepay = StringVar()
        Iblchange = Label(window, textvariable =self.changepay).grid(row = 7,column = 2, sticky = E)

        btchange = Button(window, text = "change",command = self.resultc).grid(row = 8, column = 1, sticky = E)

        window.mainloop()

    def result(self):
        balance = self.balancet(float(self.balanc.get()), float(self.intrate.get())/1200, int(self.months.get()))
        self.totalpay.set(format(balance, '10.2f'))

    def resultc(self):
        balancec = self.changet(float(self.balanc.get()), float(self.intrate.get())/1200, int(self.months.get()), float(self.change.get()), int(self.when.get()))
        if balancec == ("months out of range"):
            self.changepay.set(format(balancec))
        else:
            self.changepay.set(format(balancec, '10.2f'))

    def balancet(self, balance, intrate, months):
        balance = balance*(1+intrate)**months
        return balance

    def changet(self, balance, intrate, months, change, when):
        if when >= months:
            balancec = ("months out of range")
        else:
            balancec = balance*(1+intrate)**when
            balancec = balancec + change
            balancec = balancec*(1+intrate)**(months - when)
        return balancec

class loanacc:
    def __init__(self):
        window = Tk()
        window.title("loan")

        Label(window, text = "Interest Rate").grid(row = 1,column = 1, sticky = W)
        Label(window, text = "Months").grid(row = 2,column = 1, sticky = W)
        Label(window, text = "Loan").grid(row = 3,column = 1, sticky = W)
        Label(window, text = "Monthly Payment").grid(row = 4,column = 1, sticky = W)
        Label(window, text = "Total Payment").grid(row = 5,column = 1, sticky = W)
 
        self.intrate = StringVar()   
        Entry(window, textvariable = self.intrate,justify = RIGHT).grid(row = 1, column = 2)
 
        self.months = StringVar()
        Entry(window, textvariable = self.months,justify = RIGHT).grid(row = 2, column = 2)

        self.loan = StringVar()
        Entry(window, textvariable = self.loan,justify = RIGHT).grid(row = 3, column = 2)

        self.monthlypay = StringVar()
        lblMonthlyPayment = Label(window, textvariable =self.monthlypay).grid(row = 4,column = 2, sticky = E)

        self.totalpay = StringVar()
        lblTotalpay= Label(window, textvariable =self.totalpay).grid(row = 5,column = 2, sticky = E)
     
        btTotalpay = Button(window, text = "Result",command = self.result).grid(row = 6, column = 2, sticky = E)

        window.mainloop()

    def result(self):
        monthlyPayment = self.getMonthlypay(float(self.loan.get()), float(self.intrate.get())/1200, int(self.months.get()))
        self.monthlypay.set(format(monthlyPayment, '10.2f'))
        totalPayment = float(self.monthlypay.get()) * int(self.months.get())
        self.totalpay.set(format(totalPayment, '10.2f'))
        
    def getMonthlypay(self, loan, intrate, months):
        monthlyPayment = loan * intrate / (1 - 1 / (1 + intrate) ** (months))
        return monthlyPayment

while True:
    n = input('1 : deposit\n2 : loan\nq : quit\nEnter command : ')
    if n == 'q':
        break
    elif n == ("1"):
        depositacc()
    elif n == ("2"):
        loanacc()
    else:
        print("error")