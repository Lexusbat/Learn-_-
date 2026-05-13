from tkinter import *
window = Tk()
window.title("Treasure Island")
window.geometry("700x500")
label1 = Label(window, text = "Welcome to Treasure Island.\nYour mission is to find the treasure.")
label1.pack()

label2 = Label(window, text = "You're at a cross road. Where do you want to go? Type 'left' or 'right'")
label2.pack()

png = PhotoImage(file="100 Day Python\GIF\Adventure.png") 
label3 = Label(window, image=png)
label3.configure(image=png)
label3.pack() 


input1 = Entry(window)
input1.pack()

placeholder = "Type your answer here"
input1.insert(0, placeholder)


def clear_placeholder(event):
    if input1.get() == placeholder:
        input1.delete(0, END)

input1.bind("<FocusIn>", clear_placeholder)

stage = 1 # Tracking stages of game
retry_button = None


def restart_game():
    global stage, retry_button

    stage = 1
    input1.delete(0, END)
    label2.config(text = "You're at a cross road. Where do you want to go? Type 'left' or 'right'")

    if retry_button is not None:
        retry_button.destroy()
        retry_button = None


def game_over(message):
    global stage, retry_button

    stage = 0
    input1.delete(0, END)
    label2.config(text = message)

    if retry_button is None:
        retry_button = Button(window, text="Retry", command=restart_game)
        retry_button.pack()

def submit_answer():
    global stage

    answer = input1.get().strip().lower()
    input1.delete(0, END)


    if stage == 1:
        if answer == 'left':
            stage = 2
            input1.delete(0, 'end')
            label2.config(text = "You come to a lake. There is an island in the middle of the lake. \nType 'wait' to wait for a boat. Type 'swim' to swim across.")
        elif answer == 'right':
            game_over("You fall into a hole. Game Over.")
        elif answer not in ['left', 'right']:
            stage = 1
            input1.delete(0, 'end')
            label2.config(text = "Invalid answer. Please type 'left' or 'right'.")
    
    elif stage == 2:
        if answer == 'wait':
            stage = 3
            input1.delete(0, 'end')
            label2.config(text = "Whilst waiting, you see a broken leafy cottage and walk towards it. \n Do you enter the house? Type 'yes' or 'no'")
        elif answer == 'swim':
            game_over("You get attacked by an angry trout. Game Over.")

        elif answer not in ['wait', 'swim']:
            stage = 2
            input1.delete(0, 'end')
            label2.config(text = "Invalid answer. Please type 'wait' or 'swim'.")

    elif stage == 3:
            if answer == 'yes':
                stage = 1
                input1.delete(0, 'end')
                label2.config(text = "You enter the house and find the treasure. You Win!")
            elif answer == 'no':
                game_over("You are captured by pirates that arrived at the bank of the lake. \n Game Over.")

            elif answer not in ['yes', 'no']:
                stage = 3
                input1.delete(0, 'end')
                label2.config(text = "Invalid answer. Please type 'yes' or 'no'.")



button = Button(window, text="Submit", command=submit_answer)
button.pack()

window.mainloop()
