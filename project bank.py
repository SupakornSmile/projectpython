import tkinter as tk

page = 1

def button_change(num):
    global page
    page = num

root = tk.Tk()
root.geometry("300x275")

while page == 1:
    btn_deposit = tk.Button(root, text ="deposit", command=button_change(2), width=11, font=("Arial", 14))
    btn_deposit.grid(row=3, column=2)
    btn_loan = tk.Button(root, text ="loan", command=button_change(4), width=11, font=("Arial", 14))
    btn_loan.grid(row=4, column=2)
while page == 2:
    btn_money = tk.Button(root, text ="deposit", command=button_change(2), width=5, font=("Arial", 14))
    btn_deposit.grid(row=1, column=2)
    btn_year = tk.Button(root, text ="loan", command=button_change(2), width=5, font=("Arial", 14))
    btn_year.grid(row=2, column=2)

btn_home = tk.Button(root, text ="Home", command=button_change(1), width=5, font=("Arial", 14))
btn_home.grid(row=1, column=1)

root.mainloop()
