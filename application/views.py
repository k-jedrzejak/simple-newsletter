from application import app
from flask import render_template, request,json, current_app
import smtplib
import json


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
    subject = 'Newsletter'
    text = f'Hi {name}! <br> Thank you for your subscribe!"'

    msg = f"Subject: {subject}\n\n{text}"
    serwer = smtplib.SMTP('smtp.gmail.com', 587)
    serwer.starttls()
    serwer.login('backtocode314@gmail.com', 'qzwimnjltoinihyf')
    serwer.sendmail(sent_from, sent_to, msg)
    serwer.close()

    print('email sent')


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

        if is_exist(subscribers, email):
            error = "This email has been used. Please enter another e-mail address."
            return render_template("subscribe.html", error=error, name=name, email=email)

        else:
            send_mail(email, name)
            success = "Thanks for your subscribe!"
            return render_template("subscribe.html", success=success, name=name, email=email)

    return render_template('subscribe.html', name=name, email=email)

