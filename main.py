from tkinter import *
import requests
import json
from tkinter import messagebox,Menu
pycrypto=Tk()
pycrypto.title("My Crypto Portfolio")
pycrypto.iconbitmap("bit.ico")
def font_colour(amount):
    if amount>=0:
        return "green"
    else:
        return "red" 
        
def app_nav():
    def close_app():
        
    
        pycrypto.quit()
        messagebox.showwarning("Notification","Do You Want To Close app")  
            
    menu=Menu(pycrypto)
    file_item=Menu(menu)
    file_item.add_command(label="Clear Portfolio") 
    file_item.add_command(label="Close App",command=close_app)   
    menu.add_cascade(label="FILE",menu=file_item)
    pycrypto.config(menu=menu)
   




             
def Portfolio():
    api_request=requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=5&convert=USD&CMC_PRO_API_KEY=9ff15b29-7401-4a02-8ee1-e79f0ddb42d5")
    api=json.loads(api_request.content)
    coins=[
        {
            "symbol":"BTC",
            "amount_owned":2,
            "price_per_coin":3200
        },

        {
            "symbol":"EOB",
            "amount_owned":100,
        "price_per_coin":3.75
        },
        
        {
            "symbol":"ETH",
            "amount_owned":20,
            "price_per_coin":199.37
        },

        {
            "symbol":"XRP",
            "amount_owned":1000,
            "price_per_coin":0.15
    }

        
        
        
    ]
    total_pL_portfolio=0
    total_current=0
    total_amount_paid=0
    coin_row=1
    for i in range(0,5):
        for coin in coins:
            if api["data"][i]["symbol"]==coin['symbol']:
                total_paid=coin["amount_owned"]*coin["price_per_coin"]
                current_value=coin["amount_owned"]*api["data"][i]["quote"]["USD"]["price"]
                pL_percoin=api["data"][i]["quote"]["USD"]["price"]-coin["price_per_coin"]
                total_pL=pL_percoin*coin["amount_owned"]
                total_pL_portfolio=total_pL_portfolio+total_pL
                total_current=total_current+current_value
                total_amount_paid=total_amount_paid+total_paid

                name=Label(pycrypto,text=(api["data"][i]["name"]),bg="grey",fg="white",font="Lato 12 bold",padx="5",pady="5",borderwidth="2",relief="groove")
                name.grid(row=coin_row,column=0,sticky=N+S+E+W)

                price=Label(pycrypto,text=api["data"][i]["quote"]["USD"]["price"],bg="black",fg="white",font="Lato 12 bold",padx="5",pady="5",borderwidth="2",relief="groove")
                price.grid(row=coin_row,column=1,sticky=N+S+E+W)

                no_of_coins=Label(pycrypto,text=coin["amount_owned"],bg="grey",fg="white",font="Lato 12 bold",padx="5",pady="5",borderwidth="2",relief="groove")
                no_of_coins.grid(row=coin_row,column=2,sticky=N+S+E+W)

                amt_paid=Label(pycrypto,text=coin["amount_owned"]*coin["price_per_coin"],bg="black",fg="white",font="Lato 12 bold",padx="5",pady="5",borderwidth="2",relief="groove")
                amt_paid.grid(row=coin_row,column=3,sticky=N+S+E+W)

                current_val=Label(pycrypto,text=coin["amount_owned"]*api["data"][i]["quote"]["USD"]["price"],bg="grey",fg=font_colour(coin["amount_owned"]*api["data"][i]["quote"]["USD"]["price"]),font="Lato 12 bold",padx="5",pady="5",borderwidth="2",relief="groove")
                current_val.grid(row=coin_row,column=4,sticky=N+S+E+W)

                pl_pcoin=Label(pycrypto,text=api["data"][i]["quote"]["USD"]["price"]-coin["price_per_coin"],bg="black",fg="white",font="Lato 12 bold",padx="5",pady="5",borderwidth="2",relief="groove")
                pl_pcoin.grid(row=coin_row,column=5,sticky=N+S+E+W)

                total_pl=Label(pycrypto,text=pL_percoin*coin["amount_owned"],bg="grey",fg=font_colour(pL_percoin*coin["amount_owned"]),font="Lato 12 bold",padx="5",pady="5",borderwidth="2",relief="groove")
                total_pl.grid(row=coin_row,column=6,sticky=N+S+E+W)

                coin_row=coin_row+1
    total_amountpaid=Label(pycrypto,text=total_amount_paid,bg="grey",fg="white",font="Lato 12 bold",padx="5",pady="5",borderwidth="2",relief="groove")
    total_amountpaid.grid(row=coin_row,column=3,sticky=N+S+E+W) 

    totalcurr=Label(pycrypto,text=total_current,bg="grey",fg="white",font="Lato 12 bold",padx="5",pady="5",borderwidth="2",relief="groove")
    totalcurr.grid(row=coin_row,column=4,sticky=N+S+E+W) 

    total_pl=Label(pycrypto,text=total_pL_portfolio+total_pL,bg="grey",fg="white",font="Lato 12 bold",padx="5",pady="5",borderwidth="2",relief="groove")
    total_pl.grid(row=coin_row,column=6,sticky=N+S+E+W) 

    api=""
    refresh=Button(pycrypto,text="REFRESH",bg="#142E54",fg="white",command=Portfolio,font="Lato 12 bold",padx="5",pady="5",borderwidth="2",relief="groove")
    refresh.grid(row=coin_row,column=6,sticky=N+S+E+W)
    messagebox.showinfo("Notification","Refreshed Successfully")


           

name=Label(pycrypto,text="Coin Name",bg="#142E54",fg="white",font="Lato 12 bold",padx="5",pady="5",borderwidth="2",relief="groove")
name.grid(row=0,column=0,sticky=N+S+E+W)
name=Label(pycrypto,text="Price",bg="#142E54",fg="white",font="Lato 12 bold",padx="5",pady="5",borderwidth="2",relief="groove")
name.grid(row=0,column=1,sticky=N+S+E+W)
name=Label(pycrypto,text="Coin Owned",bg="#142E54",fg="white",font="Lato 12 bold",padx="5",pady="5",borderwidth="2",relief="groove")
name.grid(row=0,column=2,sticky=N+S+E+W)
name=Label(pycrypto,text="AmountPaid",bg="#142E54",fg="white",font="Lato 12 bold",padx="5",pady="5",borderwidth="2",relief="groove")
name.grid(row=0,column=3,sticky=N+S+E+W)
name=Label(pycrypto,text="Current value",bg="#142E54",fg="white",font="Lato 12 bold",padx="5",pady="5",borderwidth="2",relief="groove")
name.grid(row=0,column=4,sticky=N+S+E+W)
name=Label(pycrypto,text="P/L Per coin",bg="#142E54",fg="white",font="Lato 12 bold",padx="5",pady="5",borderwidth="2",relief="groove")
name.grid(row=0,column=5,sticky=N+S+E+W)
name=Label(pycrypto,text="Total P/L with Coin",bg="#142E54",fg="white",font="Lato 12 bold",padx="5",pady="5",borderwidth="2",relief="groove")
name.grid(row=0,column=6,sticky=N+S+E+W)

Portfolio()

app_nav()

pycrypto.mainloop()
print("Executed")

                

                
        