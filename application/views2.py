# RObię taki jakby mały newsletter, który wysyła maila po podaniu adresu.
# Wymyśliłam że jeśli ktoś poda kolejny raz tego samego maila to będzie krzyczał że mail jest już używany.

# Zrobiłam jakby taką małą bazę w jsonie (ogólnie to będzie zapisywało maila po dodaniu od użytkownika,
# ale do tego etapu jeszcze nei doszlam) no i tu zaczyna się problem, bo chcę żeby przeszukało całą bazęi
# jeśli znajdzie maila to powie mail jest w bazie, a jesli nei znajdzie no to wysle maila, no i jedyny sposób
# jaki mi wpadł do głowy to pętla, ale to ovzywiście iteruje po wszystkim, i wtedy wysyłą maila do każdego adresu
# zawartego w pliku ;( tu potrzebuje pomocy.

# A to mój kod:

import csv

from application import app
from flask import render_template, request, jsonify, url_for, json, Flask, current_app
# import pandas as pd
import smtplib
import os
import json


# app = Flask(__name__)


@app.route('/')
def subscribe():
    return render_template('subscribe.html')


def is_exist(subscribers, chosen_one):
    for i in subscribers:
        if chosen_one == i["mail"]:
            return True
    return False


def send_mail(email, name):
    sent_from = 'backtocode314@gmail.com'
    sent_to = f'{email}'
    subject = f'Hi {name}!'
    text = "Thank you for your subscribe!"

    msg = f"Subject: {subject}\n\n{text}"
    serwer = smtplib.SMTP('smtp.gmail.com', 587)
    serwer.starttls()
    serwer.login('backtocode314@gmail.com', 'qzwimnjltoinihyf')
    serwer.sendmail(sent_from, sent_to, msg)
    serwer.close()

    print("Wyslano wiadomosc")


@app.route('/', methods=["POST"])
def form():
    name = request.form.get("name")
    email = request.form.get("email")

    if not name or not email:
        error = "All fields are required."
        return render_template("subscribe.html", error=error, name=name, email=email)

    elif name or email:
        with current_app.open_resource('subs.json', 'r') as data_file:
            subscribers = json.load(data_file)

        # subscribers = [{"id": 0, "name": "Ala", "mail": "ala@ala.ala"},
        # {"id": 1, "name": "Ian", "mail": "ian@ian.ian"}]

        if is_exist(subscribers, email):
            print('istnieje')


        else:
            print('nie istnieje')
            # send_mail(email, name)
            print(type(subscribers))
            print(subscribers)
            print(type(data_file))
            print(data_file)
            data = {
                "name": name,
                "mail": email
            }
         
            # with open(subscribers, 'a'):
            #     json.dump(data, subscribers)
            # subscribers.close()
            print(data)
            print(subscribers)

    return render_template('subscribe.html', name=name, email=email)

# if __name__ == "__main__":
#     app.run(debug=True)
