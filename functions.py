import json
from uuid import uuid4
import tabulate as tbl
import tkinter.messagebox as mb


def add_to_basket(store_articles: 'list[list]', basket: 'list[list]', article_to_add: str):
    price = 0
    article_name = ''
    # Removing the article from the the store
    for article in store_articles:
        if article[0] == article_to_add:
            price = article[3]
            article_name = article[1]
            article[2] -= 1
            if article[2] == 0:
                store_articles.remove(article)

    # adding the article to the basket
    is_already_there = False
    for article in basket:
        if article[0] == article_to_add:
            article[2] += 1
            is_already_there = True
    if not is_already_there:
        basket.append([article_to_add, article_name, 1, price, price*1])


def remove_from_basket(store_articles: 'list[list]', basket: 'list[list]', article_to_remove: str):

    price = 0
    article_name = ''
    # removing article to the basket
    for article in basket:
        if article[0] == article_to_remove:
            price = article[3]
            article_name = article[1]
            article[2] -= 1
            if (article[2] == 0):
                basket.remove(article)

    # HERE: restoring the article to the store
    is_already_there = False
    for article in store_articles:
        if article[0] == article_to_remove:
            article[2] += 1
            is_already_there = True
    if not is_already_there:
        store_articles.append(
            [article_to_remove, article_name, 1, price])


def validate_purchase(basket: 'list[list]', name_of_the_client: str) -> str:
    clients: list[dict] = json.load(open('./data/clients.json', 'r'))
    # TODO: check if the client is already in the database
    # if true, check the number of visists and the articles puchases
    # if the number of purchases is >2 for an article, we do a reduction

    client: dict = {}
    # find the rig client:
    is_already_exist = False
    for cl in clients:
        if cl["name"] == name_of_the_client:
            is_already_exist = True
            cl['visits'] += 1
            client = cl
            cl['purchases'].append(basket)

    if not is_already_exist:
        client = {
            'name': name_of_the_client,
            'visits': 1,
            'purchases': [basket]
        }
        clients.append(client)

    "saving the client in the clients file"
    with open('./data/clients.json', 'w') as client_file:
        json.dump(clients, client_file)

    # Now we can process the bill by modifiying the basket content

    for new_purchase in basket:

        # calculate the total price
        new_purchase[4] = new_purchase[2] * \
            new_purchase[3]
        hasReduction = False
        if client['visits'] > 2:
            for old_purchases in list(client['purchases'][:-1]):

                for old_purchase in old_purchases:
                    print(new_purchase)
                    if old_purchase[0] == new_purchase[0] and old_purchase[2] >= 2:
                        # we have to accord the reduction
                        hasReduction = True
                        new_purchase[4] *= 0.98
        if hasReduction:
            mb.showinfo(
                "Reductions😍", f"Felicitations vous beneficiez d'une reduction de 2% sur l'article {new_purchase['name']}")

    # Data that will be contained in a bill
    bill = {
        'client_name': name_of_the_client,
        'file_name': str(uuid4())+'.txt',
        'purchases': basket
    }
    # savaing the new bill in the invoices file, and
    invoices = json.load(open('./data/invoices.json', 'r'))
    invoices.append(bill)
    with open('./data/invoices.json', 'w') as invoices_file:
        json.dump(invoices, invoices_file)

    # generate the bill_file
    bill_writter(bill)
    basket = []
    return bill['file_name']


def bill_writter(bill: dict) -> None:
    basket: list = bill['purchases']
    count, total = 0, 0
    for article in basket:
        count += article[2]
        total += article[4]
    basket.append(['TOTAL','', count, '', total])
    headers = ['Code', 'Article',  'Quantité',
               'Prix Unitaire', 'Prix total']
    with open(f'./data/bills/{bill["file_name"]}', 'w', encoding="utf-8") as bill_file:
        table = tbl.tabulate(basket, headers=headers,
                             tablefmt='fancy_grid', showindex=True)
        print(bill['client_name'])
        name = str(bill['client_name']).title()
        bill_file.write(f"Nom du client: {name}\n{table}")
