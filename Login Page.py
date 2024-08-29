from tkinter import *
window = Tk()
window.title("Login Page Simulator")
window.geometry('500x500')
window.tk.call('tk', 'scaling', 6.0)

lbl = Label(window, text="What do you want to do?", font="arial")
lbl.grid(column=50, row=0)

option1 = Button(window, text="Add list")
option1.grid(column=3, row=3)

option2 = Button(window, text="Remove list")
option2.grid(column=3, row=6)

acc = ['Dhimas']
Condition = True
#While buat loop main menu
while Condition:
    option = (input('What do you wanna do? 1. Add list; 2. Remove List; 3. Login Test; 4. Check List; 5. Quit ' ))
    if option == '1':
        add = input('Who do you want to add to the list? ')
        #Append buat nambah string dalam sebuah list
        acc.append(add)
    elif option == '2':
        remove = input('Whom do you want to remove? ' + str(acc) + ' ')
        #Line dibawah ini buat break kalau semisal input "remove" ngga ada di list "acc"
        if remove not in acc:
            print('konzy')
            continue
        #Remove buat ngilangin string dalam sebuah list
        acc.remove(remove)
    elif option == '3':
        Login = input("What's your name? ")
        if Login in acc:
            print('Login Succesfull!')
        else:
            print('Invalid')
    elif option == '4':
        print(acc)
    elif option == '5':
        break
    else:
        print("Invalid")
