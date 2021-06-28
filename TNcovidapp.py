from math import dist
import requests, json, time
import tkinter as tk
root=tk.Tk()
root.geometry("425x300")
root.title('Tamil Nadu COVID-19 Tracker App')
root['bg']='yellow'
day = str(time.localtime().tm_mday) + '.' + str(time.localtime().tm_mon) +  '.' + str(time.localtime().tm_year)
district = tk.StringVar()

display_result = tk.Label(root,text='Enter TN District', font=('calibre',20, 'bold'), bg='yellow')
display_result.pack()
district_entry = tk.Entry(root,textvariable = district, font=('calibre',10,'normal'), width=50,borderwidth=5)
district_entry.pack()
time_label = tk.Label(root, text = f"Date:{day}", font=('calibre',20, 'bold'), bg='yellow')
time_label.pack()
api_source = tk.Label(root,text = 'https://api.covid19india.org/state_district_wise.json', font=('calibre',10, 'bold'), bg='yellow')
api_source.pack()

def submit():
    try:
        #display_result.grid(row = 2,column =0)
        api = 'https://api.covid19india.org/state_district_wise.json'
        data = requests.get(api).json()
        district1=district.get().strip().capitalize()
        x=data.get('Tamil Nadu').get('districtData').get(district1)
        print(district1, x)
        display_result.config(text=f"Entered Place: {district1}"+'\n'+f"Confirmed Cases: {x.get('confirmed')}"+'\n'+f"Active Cases: {x.get('active')}"+'\n'+f"Deaths: {x.get('deceased')}"+'\n'+f"Recovered: {x.get('recovered')}")
        display_result.pack()
    except:
        display_result.config(text="Try Again, Enter TN district")
        display_result.pack()    

def key_handler(event):
    if event.keysym in ("Return", "equal"):
        global x
        x = submit()
root.bind("<Key>", key_handler)
root.mainloop()
