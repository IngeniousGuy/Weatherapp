from turtle import width
import matplotlib.pyplot as plt
from time import strftime
from urllib import response
import requests
import tkinter as tk
import socket
import datetime
from PIL import Image, ImageTk
from requests import*
def stnews():
    id=loc['countryCode']
    getnews(id)
def getnews(cntry):
        newsc=tk.Tk()
        newsc.title("NEWS")
        newsc.geometry("1000x600")
        api_key="fd98a6aea71a41c79fd4a98d35278514"
        url="https://newsapi.org/v2/top-headlines?country="+cntry+"&apiKey="+api_key
        news=requests.get(url).json()
        articles=news["articles"]
        myarticle=[]
        mydesc=[]
        mynews=''
        yaxis=0
        i=0
        for article in articles:
                title=str(article['title']+":")
                description=str(article['description'])
                a=len(description)
                if(a<160):
                        lbl=tk.Label(newsc,text=title,font=('calibri', 10, 'bold'),).place(relx=0.05,rely=yaxis)
                        lbl=tk.Label(newsc,text=description,font=('calibri', 10, 'bold')).place(relx=0.05,rely=yaxis+0.03)
                        yaxis=yaxis+0.1
                else:
                        i=i-1
                i+=1
                if i==10:
                        break
def gmtadjust(hrs,mins,gmtsec):
    hrs=int(hrs)
    mins=int(mins)
    gmtsec=(float(gmtsec))
    frtime=hrs+(mins/60)
    gmtsec=0.00027777778*gmtsec
    frtime=frtime+gmtsec
    mins=int(60*(frtime%1))
    hrs=int(frtime)
    if hrs>=24:
        hrs=hrs%24
    if(hrs<10):
        if (mins<10):
            return '0'+str(hrs)+":"+0+str(mins)
        else:
            return '0'+str(hrs)+":"+str(mins)
    else:
        if (mins<10):
            return str(hrs)+":"+0+str(mins)
        else:
            return str(hrs)+":"+str(mins)
def plot():
    add=getloc('fcst')
    tdict=requests.get(add).json()
    mintemp=[]
    maxtemp=[]
    j=0
    day=0
    time=[]
    for i in tdict["list"]:
            tim=gmtadjust(i['dt_txt'][11:13],i['dt_txt'][14:16],str(tdict['city']['timezone']))
            if day!=0:
                    time.append(tim+'\nday:'+str(day))
            else:
                    time.append(tim+'\ntoday')
            maxtemp.append(i['main']['temp_max']-273.15)
            mintemp.append(i['main']['temp_min']-273.15)
            if int(tim[0:2])>=21:
                    day=day+1
            if j>=10:
                    break
            j+=1
    y=mintemp
    x=time
    plt.plot(x,y)
    y=maxtemp
    x=time
    plt.plot(x,y,color='red')
    plt.show()
def getadd():
    b="http://ip-api.com/json/"+str(getip())
    response=requests.get(b).json()
    addr=str('City: '+response['city'])+"\n"+str("Country: "+response['country'])
    canvas.create_text(0.9*w,0.14*h,text=addr,font = ('calibri', 10, 'bold'))
    return response
def getloc(type):
    a="http://ip-api.com/json/"+str(getip())
    response=requests.get(a).json()
    # address="City: "+response['city']+",country: "+response['country']+"\nzip:"+response[zip]
    addr=str('City: '+response['city'])+str("Country: "+response['country'])
    canvas.create_text(0.9*w,0.12*h,text=addr,font = ('calibri', 10, 'bold'))
    if type=="fcst":
        latlong="https://api.openweathermap.org/data/2.5/forecast?lat="+str(response['lat'])+"&lon="+str(response['lon'])+"&appid=de803cb1b03372d91615c0a284d8fbfe"
    elif type=='curr':
        latlong="https://api.openweathermap.org/data/2.5/weather?lat="+str(response['lat'])+"&lon="+str(response['lon'])+"&appid=de803cb1b03372d91615c0a284d8fbfe"
    return latlong
def time():
    ctime=strftime("%H:%M:%S %p")
    tmlbl.config(text=ctime)
    tmlbl.after(1000,time)
def getip():
    ip=get("https://api.ipify.org").text
    ip=str(ip)
    canvas.create_text(0.9*w,0.1*h,text=ip,font = ('calibri', 10, 'bold'))
    return ip
class hehe:
    def background(weather):
        try:
            string=str(weather+'.png')
            background_image=tk.PhotoImage(file=string)
            return background_image
        except:
            background_image=tk.PhotoImage(file="sunny.png")
            return background_image

def curnweather():
    weather=(weatherdata["weather"][0]['description'])
    temperature=weatherdata['main']["temp"]-273.15
    temp=str("{:.2f}".format(temperature))
    cweather=str(weather.capitalize()+"\n"+temp+"°C")
    wlbl.config(text=cweather)
    wlbl.after(10000000,curnweather)
    return weather
def moreinfo():
    visibility=str(weatherd['visibility'])
    pressure=str(weatherd['main']["pressure"])
    humidity=str(weatherd['main']["humidity"])
    message="Pressure :"+pressure+"pa\nVisibility :"+visibility+"m\nHumidity :"+humidity
    messagewindow=tk.Tk()
    messagewindow.title("Weather")
    messagewindow.geometry('200x200')
    messagewindow.configure(bg='#000033')
    messageb=tk.Label(messagewindow,text=message,font=('calibri', 20, 'bold'),fg='white',bg='#000033')
    messageb.pack()
    clbt=tk.Button(messagewindow,text='close',command=messagewindow.destroy)
    clbt.pack()
def date():
        cdate=strftime("%D %A")
        dtlbl.config(text=cdate)
        dtlbl.after(10000,date)

def dimtopercent(p,net):
    return (p*net)
h=600
w=1000
root=tk.Tk()
root.title("Weather")
canvas=tk.Canvas(root,height=h,width=w)
canvas.pack()
root.maxsize(w,h)
root.minsize(w,h)

#weather
wlbl=tk.Button(canvas,font = ('calibri', 40, 'bold'),command=moreinfo)
wlbl.place(relx=0.4,rely=0.1)
add=getloc('curr')
weatherdata=requests.get(add).json()
weatherd=weatherdata
curweather=curnweather()

#background image
background_image=hehe.background(curweather)
canvas.create_image(0,0,anchor=tk.NW,image=background_image)

#time
tmlbl=tk.Label(canvas,font = ('calibri', 40, 'bold'))
tmlbl.place(relx=0.1,rely=0.7)
time()

#date
dtlbl=tk.Label(canvas,font = ('calibri', 20, 'bold'))
dtlbl.place(relx=0.1,rely=0.83)
date()
#IP address
ip=getip()
loc=getadd()

#button
icimage=tk.PhotoImage(file='sun.png')
button=tk.Button(canvas,image=icimage,height=100,width=100,command=plot)
button.place(relx=0.7,rely=0.8)
canvas.create_text(0.75*w,0.75*h,text="10-hour forecast",font = ('calibri', 20, 'bold'))
nwbtn=tk.Button(canvas,text="news",font = ('calibri', 20, 'bold'),height=2,width=5,command=stnews)
nwbtn.place(relx=0.85,rely=0.8)

root.mainloop()