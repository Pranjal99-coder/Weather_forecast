import tkinter as tk
import requests
from tkinter import font
from PIL import Image,ImageTk


root = tk.Tk()
root.title("Weather Forecast")
root.geometry("500x500")

# Api key: 10a47f920e53f2fc1b093e8ee04f9b3e
# Api URl: api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

def format_response(weather):
    try:
        city = weather['name']
        condition = weather['weather'][0]['description']
        temp = weather['main']['temp']
        temp_min = weather['main']['temp_min']
        temp_max = weather['main']['temp_max']
        final_str = 'City:%s\nCondition:%s\nTemperature:%s\nMin Temperature:%s\nMax Temperature:%s'%(city,condition,temp,temp_min,temp_max)
    except:
        final_str = "The data can not be retrived"
    
    return final_str
 
def get_weather(city):
    weather_key = '10a47f920e53f2fc1b093e8ee04f9b3e'
    url = 'https://api.openweathermap.org/data/2.5/weather' 
    parameter = {'APPID':weather_key,'q':city,'units':'imperial'}
    response = requests.get(url,parameter)
    #print(response.json())
    weather = response.json()

    print(weather['name'])
    print(weather['weather'][0]['description'])
    print(weather['main']['temp'])
    print(weather['main']['temp_min'])
    print(weather['main']['temp_max'])

    result['text'] = format_response(weather)

    icon_name = weather['weather'][0]['icon']
    open_image(icon_name)

def open_image(icon):
    size = int(frame_two.winfo_height()*0.25)
    img = ImageTk.PhotoImage(Image.open('./img/' + icon +'.png').resize((size,size)))
    weather_icon.delete('all')
    weather_icon.create_image(0,0,anchor='nw',image=img)
    weather_icon.image = img
    

img = Image.open('./Light_blue.png')
img = img.resize((500,500),Image.ANTIALIAS)
img_photo = ImageTk.PhotoImage(img)

bg_label = tk.Label(root,image=img_photo)
bg_label.place(x=0,y=0,width=500,height=500)

title = tk.Label(bg_label,text='Weather of more than 100,000 cities!',fg='black',bg='light blue',font=('Aldhabi',17))
title.place(x=51,y=32)

frame_one = tk.Frame(bg_label,bg="blue",bd=5)
frame_one.place(x=50,y=70,width=400,height=50)

text_box = tk.Entry(frame_one,font=('Aldhabi',25),width=15)
text_box.grid(row=0,column=0,sticky='w')

btn = tk.Button(frame_one,text='Weather',fg='red',font=('Aldhabi',14,'bold'),command=lambda: get_weather(text_box.get()))
btn.grid(row=0,column=1,padx=15)

frame_two = tk.Frame(bg_label,bg="blue",bd=5)
frame_two.place(x=50,y=140,width=400,height=300)

result = tk.Label(frame_two,font=40,bg='white',justify='left',anchor='nw')
result.place(relwidth=1,relheight=1)

weather_icon = tk.Canvas(result,bg='white',bd=0,highlightthickness=1)
weather_icon.place(relx=0.75,rely=0,relwidth=1,relheight=0.5)


root.mainloop()
