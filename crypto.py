import json
from locale import currency
from turtle import left
import requests
from tkinter import *


window = Tk()
window.title("Crypto Price Tracker")
window.geometry("300x100")



def tracker():
    value.delete(0, END)
    value.insert(END, "Choose A Coin to Start")

#Currency Changer

def coineth():
    def selecteth():
        global btc
        lbl.config(text = "1 Ethereum to USD =")
    selecteth()
    global currency
    value.delete(0, END)
    key = "https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT"
   
    # requesting data from url
    data = requests.get(key)  
    data = data.json()

    value.insert(END, data['price'])

def coinbtc():
    def selectbtc():
        global btc   
        lbl.config(text = "1 Bitcoin to USD =")
    selectbtc()
    global currency
    value.delete(0, END)
    key = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
   
    # requesting data from url
    data = requests.get(key)  
    data = data.json()

    value.insert(END, data['price'])


lbl = Label(window, text="Choose A Coin to Start")
value = Entry(window, text="Crypto", bd=4)
cryptotype = ()


slct = Label(window, text="Currency = ")
btc = Button(window, text="BTC", command=coinbtc)
eth = Button(window, text="ETH", command=coineth)

tracker()


lbl.pack()
lbl.place(x=5,y=5)
value.pack()
value.place(x=5,y=30)

#Selector

slct.pack()
slct.place(x=180,y=30)

eth.pack()
eth.place(x=250,y=10)
btc.pack()
btc.place(x=250,y=40)


window.mainloop()