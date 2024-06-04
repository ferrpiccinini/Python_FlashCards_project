from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

#functions
def funcao_change():
    global timer_fun, current_card
    window.after_cancel(timer_fun)
    current_card = random.choice(dict_final)
    canvas.itemconfig(actually_image, image=img)
    canvas.itemconfig(language, text="French:")
    canvas.itemconfig(word, text=current_card["French"])
    timer_fun = window.after(3000, funcao_flip)

def funcao_flip():
    state = canvas.itemcget(language, 'text')
    state2 = canvas.itemcget(word, 'text')
    canvas.itemconfig(word, text=current_card["English"])
    canvas.itemconfig(actually_image, image=img2)
    canvas.itemconfig(language, text="English:")

def correct_button():
    dict_final.remove(current_card)
    print(len(dict_final))
    data = pandas.DataFrame(dict_final)
    data.to_csv("data/words_to_learn.csv", index=False)
    funcao_change()


#working with the words
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    panda = pandas.read_csv("data/french_words.csv")
    dict_final = panda.to_dict(orient="records")
else:
    dict_final = data.to_dict(orient="records")



#GUI SETUP
window = Tk()
window.title("FlashY")
window.config(padx=50, pady=50,background=BACKGROUND_COLOR)

timer_fun = window.after(3000, funcao_flip)

canvas = Canvas(width=800, height=526)
img = PhotoImage(file="images/card_front.png")
img2 = PhotoImage(file="images/card_back.png")
actually_image = canvas.create_image(400,263,image=img)
language = canvas.create_text(400, 150,text="French:", font=("Ariel",30,"italic"))
word = canvas.create_text(400, 263,text="", font=("Ariel",45,"bold"))
canvas.config(background=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

img_right_button = PhotoImage(file="images/right.png")
butao_certo = Button(image=img_right_button,highlightthickness=0,command=correct_button)
butao_certo.grid(row=1,column=0)

img_wrong_button = PhotoImage(file="images/wrong.png")
butao_errado = Button(image=img_wrong_button,highlightthickness=0, command=funcao_change)
butao_errado.grid(row=1,column=1)






funcao_change()
window.mainloop()