from tkinter import*
import pyttsx3

def convert():
	text_speech=input.get("1.0", "end-1c")
	res=pyttsx3.init()
	res.say(text_speech)
	res.runAndWait()
def clear():
	input.delete("1.0", "end")
def exit():
	root.quit()

root=Tk()
root.title("Speech")
root.geometry("800x400+300+150")  
root.resizable(False,False)

photo = PhotoImage(file="C:/Users/hp/OneDrive/Desktop/speech_converter/bk.png")
p=Label(image=photo)
p.pack()

n1=Label(root,text="Text To Voice Converter",fg="gray",font=("Times 25 bold"),bg="black")
n1.place(x=80,y=20)

lbl_input1=Label(root,text="Enter your text here",fg="white",font=("Times 19 bold"),bg="black")
lbl_input1.place(x=250,y=100)
input=Text(root, height = 5, width = 40 , font=("Arial 16 bold"))
input.place(x=130,y=140)

button1 = Button( root, text = "Convert",bd = '9',bg="black",fg="white",command=convert)
button1.place(x=200,y=300)
button2 = Button( root, text = "Clear",bd = '9',bg="black",fg="white",command=clear)
button2.place(x=360,y=300)
button3 = Button( root, text = "Exit",bd = '9',bg="black",fg="white",command=exit)
button3.place(x=500,y=300)

root.mainloop()