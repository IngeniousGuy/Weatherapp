import requests
import tkinter as tk
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
        f2=tk.Frame(newsc,height=600,width=1000).place(x=0,y=0)
        for article in articles:
                title=str(article['title']+":")
                description=str(article['description'])
                print(description)
                a=len(description)
                if(a<160):
                        lbl=tk.Label(f2,text=title,font=('calibri', 10, 'bold'),).place(relx=0.05,rely=yaxis)
                        lbl=tk.Label(f2,text=description,font=('calibri', 10, 'bold')).place(relx=0.05,rely=yaxis+0.03)
                        yaxis=yaxis+0.1
                else:
                        i=i-1
                i+=1
                if i==10:
                        break
        newsc.mainloop()
a=getnews('IN')