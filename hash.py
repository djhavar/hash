from tkinter import *
from firebase import firebase
from simplecrypt import encrypt,decrypt

login_window = Tk()
login_window.geometry("400x400")
login_window.config(bg='#AB92BF')

user=''
code=''
fcode=''
messt=''
messe=''

def sendData():
    global user
    global messe
    global code
    
    message = user+":"+messe.get()
    cighercode=encrypt('AIM',message)
    hex_string = ciphercode.hex()
    put_date = firebase.put("/",your_code,hex_string)
    print(put_date)