from tkinter import *
import tkinter as tk
import boto3

def getText():
    aws_mag_con=boto3.session.Session(aws_access_key_id='',
    aws_secret_access_key='')
    
    translate_client=aws_mag_con.client(service_name='translate',region_name='us-east-1')
    result=textExample.get("1.0","end")
    response=translate_client.translate_text(Text=result,SourceLanguageCode='tr',TargetLanguageCode='en')
    
    text1.insert('1.0',response.get('TranslatedText'))
    text2.insert('1.0','Source Language Code :' +response.get('SourceLanguageCode'))
    text2.insert('end','\nTarget Language Code :' +response.get('TargetLanguageCode'))

def main_screen():
    global screen
    global code
    global text1,text2,textExample

    root=tk.Tk()
    root.geometry("600x400")
    root.configure(background="DarkOrange1")
    root.title("AWS Translate")
    
    def reset():
        textExample.delete(1.0,END)
        text1.delete(1.0,END)
        text2.delete(1.0,END)

    Label(text = "Text").place(x=10,y=10)
    textExample=tk.Text(width=50,height=5)
    textExample.pack()
    Label( text = "Translated Text").place(x=10,y=100)
    text1=tk.Text(width=50,height=5)
    text1.pack()
    text2=tk.Text(width=50,height=3)
    text2.pack()
   
    Button(text="Translate",height="3",width=18,bg="#ed3833",fg="white",bd=0,command=getText).place(x=100,y=300)
    Button(text="Clear",height="3",width=18,bg="#1089ff",fg="white",bd=0,command=reset).place(x=250,y=300)

    root.mainloop()

main_screen()

   


    