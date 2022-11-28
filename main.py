import json
import os
import tkinter as tk
import tkinter.messagebox as mb
from my_frames import *
from vars import *
from functions import validate_purchase



a: Frame
b: Frame


window = tk.Tk(className="Shopping Application")
window.geometry("1080x720")
window.config(bg=bg, padx=padx, pady=pady)

app = Frame(window, bg=bg)

# where we will store current user orders
basket = []
client_name = StringVar()

articles, clients = [], []
with open('./data/articles.json', 'r') as f1, open('./data/clients.json', 'r') as f2:
    articles, clients = json.load(f1), json.load(f2)
packed = False


def refresh_window():
    global a
    global b
    global packed
    global articles
    with open('./data/articles.json', 'w') as articles_file:
        # print(articles)
        json.dump(articles, articles_file)
    a.destroy()
    b.destroy()
    display_frames()

    if not packed:
        btn.pack(fill=X)
        packed = True


def valid_purchase():
    global app
    file_name = validate_purchase(
        basket=basket, name_of_the_client=client_name.get().strip())
    info_box = mb.showinfo(title='Well done', message=f'Votre facture a bien ete genere\n Merci pour vos achats, à la prochaine\n\n')    
    dest =f"data\\bills\\{file_name}"
    if info_box == 'ok':
        # os.startfile(dest, 'open')
        window.quit()
        

btn = Button(window, text='Valider ma commande', font=font14b,
             padx=padx, pady=pady, fg=fg, bg=bg, command=valid_purchase)


def display_frames():
    global a
    global b
    a = articles_frame_list(app, articles, basket, refresh_window)
    b = basket_list_frame(app, articles, basket, refresh_window)
    a.grid(row=3, pady=pady)
    b.grid(row=15, pady=pady)


def start():
    global client_name
    if client_name.get().strip() == "":
        client_name.set('')
        return mb.showinfo('Pas si vite ...', 'Veuiller entrer votre nom avant de continuer')
    client_name.set(client_name.get().title().strip())
    welcome_frame.destroy()
    app.pack()
    display_frames()


# Show a welcome frame and ask the user name
welcome_frame = tk.Frame(window, background=bg)
tk.Label(welcome_frame, text="Bienvenu\n veuillez entrer votre nom",
         font=font18, bg=bg, fg=fg).pack(expand=YES, padx=padx, pady=pady)
tk.Entry(welcome_frame, text="Votre nom: ", font=font16,
         textvariable=client_name).pack(fill=X, padx=2*padx)
tk.Button(welcome_frame, text='Je commence mes amplets', command=start,
          bg=bg, fg=fg, font=font16).pack(fill=X, padx=padx, pady=pady)
welcome_frame.pack(expand=YES, fill=BOTH,)


mainloop()
