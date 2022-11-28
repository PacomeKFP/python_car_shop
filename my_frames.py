from tkinter import *
import tkinter.ttk as ttk
from vars import *
from functions import *



def articles_frame_list(win: Frame, articles: 'list[dict]', basket: 'list[dict]', callback) -> Frame:
    screen = Frame(win, bg=bg)
    screen.grid(row=len(articles)+2, column=6)

    Label(screen, text='Faites vos choix et validez votre commande ',
          font=font14, bg=bg, fg=fg).grid(row=0, columnspan=6)

    # Adding headers to our table
    columns_names = ('Code', 'Nom', 'Prix Unitaire', 'Quantité en Stock')
    columns_id = ('code', 'name', 'price', 'stock')
    tree = ttk.Treeview(screen, columns=columns_id, show='headings', selectmode='browse')
    for i in range(len(columns_id)):
        tree.heading(columns_id[i], text=columns_names[i])

    # adding data in the treeview
    # formating articles for displaying
    data = []
    for i in range(len(articles)):
        data.append((articles[i][1], articles[i][0],
                    articles[i][2], articles[i][2]))
    # adding them to the tree to be displayed
    for line in data:
        tree.insert('', END, values=line)

    # the event triggered when an item of the treeView is selected
    def item_selected(event):
        # TODO: modify this function to handle the selected item
        for selected_item in tree.selection():
            item = tree.item(selected_item)
            record = item['values']
            add_to_basket(articles, basket, record)
            callback()
    # biding the item selection event to a function
    tree.bind('<<TreeviewSelect>>', item_selected)
    tree.grid(row=0, column=0, sticky=NSEW)
    return screen


def basket_list_frame(win: Frame, articles: 'list[dict]', basket: 'list[dict]', callback) -> Frame:
    screen2 = Frame(win, bg=bg)
    screen2.grid(row=len(articles)+2, column=6)

    # Adding headers to our table
    columns_names = ('Code', 'Nom', 'Prix Unitaire', 'Qté', 'Prix Total')
    columns_id = ('code', 'name', 'price', 'quantity', 'total_price')
    tree2 = ttk.Treeview(screen2, columns=columns_id, show='headings')
    for i in range(len(columns_id)):
        tree2.heading(columns_id[i], text=columns_names[i])
    data = []
    for i in range(len(basket)):
        data.append((i+1, basket[i]['name'],
                    basket[i]['price'], basket[i]['count'], basket[i]['price']*basket[i]['count']))
    # adding them to the tree to be displayed
    for line in data:
        tree2.insert('', END, values=line)

    # the event triggered when an item of the treeView is selected

    def item_selected(event):
        # TODO: modify this function to handle the selected item
        for selected_item in tree2.selection():
            item = tree2.item(selected_item)
            record = item['values']
            remove_from_basket(articles, basket, record[1])
            callback()
    # biding the item selection event to a function
    tree2.bind('<<TreeviewSelect>>', item_selected)
    tree2.grid(row=0, column=0, sticky=NSEW)
    return screen2
