import re


def check_new_signaux(event):
    # Check avec des regex voir si le message Telegram du channel est bien un signaux.
    zone_entree = re.search("Zone d’entrée : [0-9]+ [0-9]+", event.raw_text)
    tp1 = re.search("TP1 : [0-9]+ [0-9]+", event.raw_text)
    tp2 = re.search("TP2 : [0-9]+ [0-9]+", event.raw_text)
    tp3 = re.search("TP3 : [0-9]+ [0-9]+", event.raw_text)
    sl = re.search("SL : [0-9]+ [0-9]+", event.raw_text)

    # Check avec une condition si c'est un signaux de trading, si c'est OK ALORS :
    # On enleve les espaces, le texte, parse le text en integer.
    if zone_entree is None or tp1 is None or tp2 is None or sl is None:
        print("MESSAGE NORMAL PAS DE SIGNAUX DE TRADING AND QUIT !")
        return False
    else:
        print("SIGNAUX DE TRADING !")
        zone_entree = int(re.sub(" ", "", zone_entree[0][15:]))
        tp1 = int(re.sub(" ", "", tp1[0][6:]))
        tp2 = int(re.sub(" ", "", tp2[0][6:]))
        if tp3 is not None:
            tp3 = int(re.sub(" ", "", tp3[0][6:]))
        else:
            tp3 = "OUVERT"
        sl = int(re.sub(" ", "", sl[0][5:]))
        return True


def check_modify_sl(event):
    print("test")


def check_stop(event):
    print("test")
