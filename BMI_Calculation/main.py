from  tkinter import *

window =Tk()
window.title("BMI Calculator")
window.minsize(width=250,height=250)

label_1 = Label()
label_2 = Label()
label_3 = Label(text="BMI Calculation")

def calculate_bmi():
    height = boy.get()
    weight = kilo.get()

    if weight == '' or height == '':
        label_3.config(text="Enter both weight and height")
    else:
        try:
            bmi = float(weight) / (float(height) / 100)**2
            print_result(bmi)

        except:
            label_3.config(text="Please enter valid number!!")

label_1.config(text="Enter Your Weight(kg)")
label_1.pack(padx=5,pady=5)


kilo = Entry()
kilo.config(width=20)
kilo.pack(padx=5,pady=5)


label_2.config(text="Enter Your Heights(cm)")
label_2.pack(padx=5,pady=5)

boy = Entry()
boy.config(width=20)
boy.pack(padx=5,pady=5)

button = Button(text="Calculate",command=calculate_bmi)
button.pack(padx=5,pady=5)
label_3.pack(padx=5,pady=5)

def print_result(bmi):
    if bmi <= 18.4:
        label_3.config(text=f"Your bmi is {round(bmi,2)}.You are Underweight")
    elif 18.4 < bmi <= 24.9:
        label_3.config(text=f"Your bmi is {round(bmi, 2)}.You are Normal weight")
    elif 24.9 < bmi <=39.9:
        label_3.config(text=f"Your bmi is {round(bmi, 2)}.You are Overweight")
    else:
        label_3.config(text=f"Your bmi is {round(bmi, 2)}.You are Obese")


window.mainloop()