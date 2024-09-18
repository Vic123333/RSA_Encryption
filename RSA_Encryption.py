import random
from Primzahlen import *


#Es werden nur kleine Primzahlen verwendet, da dies demonstrativ für eine Implementierung des RSA-Verfahrens dienen soll und auf jedem Computer laufen kann.
#Deshalb ist die Datei "Primzahlem.py" bereits angehängt, da das Zufällige suchen bei schlechter Leistung viel Zeit in Anspruch nehmen würde.
#Normalerweise werden p und q mit jeweils mehr als 512 bis 2048 Bit zufällig gewählt.


def ggT(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def erggT(a, b):
    u, v, s, t = 1, 0, 0, 1
    while b!=0:
        q=a//b
        a, b = b, a-q*b
        u, s = s, u-q*s
        v, t = t, v-q*t
    return u


def Eingabe(Text):
    return input(Text)


def Chiffrierung(e, N, m):
    c = (m**e)%N
    return c


def Dechiffrierung(d, N, c):
    m = (c**d)%N
    return m


def RSA(p, q, e):
    if p == 0 and q == 0:
        p = random.choice(Primzahlen)
        q = random.choice(Primzahlen)

    while p == q:
        p = random.choice(Primzahlen)

    # RSA-Modul
    N = p * q

    # Eulersche Phi-Funktion (Anzahl der Teilerfremdenzahlen zu N)
    phi_n = (p - 1) * (q - 1)

    # Zufällige  Zahl e, die teilerfremde zu Phi(N) ist, also 1<e<phi(n) ggT(e, phi(n)) = 1
    if e != 0:
        pass
    else:
        while True:
            e = random.randint(2, phi_n)
            if ggT(e, phi_n) == 1 and erggT(e, phi_n) > 0 and e < phi_n:
                break

    d = erggT(e, phi_n)

    Schlüssel = {
    "öffentlicher_Schlüssel": [e, N],
    "privater_Schlüssel": [d, N],
    }

    return Schlüssel


def RSA_Programm():
    Verschlüseln_oder_Entschlüsseln = Eingabe("Wollen Sie eine Nachricht verschlüsseln oder entschlüsseln: ").lower()

    if Verschlüseln_oder_Entschlüsseln == "verschlüsseln":
        Schlüssel_vorhanden = Eingabe("Wollen Sie die Parameter selbst wählen? Ja oder Nein: ").lower()
        if Schlüssel_vorhanden == "ja":
            p = int(Eingabe("p = "))
            q = int(Eingabe("q = "))
            e = int(Eingabe("e = "))
        else:
            p, q, e = 0, 0, 0
            Schlüssel = RSA(p=p, q=q, e=e)
        m = int(Eingabe("Geben Sie die Zahl ein, die verschlüsselt werden soll: "))
        c = Chiffrierung(Schlüssel["öffentlicher_Schlüssel"][0], Schlüssel["öffentlicher_Schlüssel"][1], m)
        print(f"Die Zahl {m} wurde mit dem öffentlichen Schlüssel {Schlüssel['öffentlicher_Schlüssel']} verschlüsselt {c}.")
        Weiter_Frage = Eingabe("Soll die Nachicht entschlüsselt werden? Ja oder Nein: ").lower()
        if Weiter_Frage == "ja":
            m = Dechiffrierung(Schlüssel["privater_Schlüssel"][0], Schlüssel["privater_Schlüssel"][1], c)
            print(f"Die verschlüsselte Nachricht {c} wurde mit dem privaten Schlüssel {Schlüssel['privater_Schlüssel']} entschlüsselt {m}.")



    elif Verschlüseln_oder_Entschlüsseln == "entschlüsseln":
        p = int(Eingabe("p = "))
        q = int(Eingabe("q = "))
        e = int(Eingabe("e = "))
        Schlüssel = RSA(p=p, q=q, e=e)

        c = int(Eingabe("Geben Sie die Zahl ein, die entschlüsselt werden soll: "))
        m = Dechiffrierung(Schlüssel["privater_Schlüssel"][0], Schlüssel["privater_Schlüssel"][1], c)
        print(f"Die verschlüsselte Nachricht {c} wurde mit dem privaten Schlüssel {Schlüssel['privater_Schlüssel']} entschlüsselt {m}.")


RSA_Programm()



#Falls Sie den Text selbst durchführen wollen.
# def primfaktoren(n):
#     faktoren = []
#     z = n
#     while z > 1:
#         i = 2
#         gefunden = False
#         while i*i <= n and not gefunden:
#             if z % i == 0:
#                 gefunden = True
#                 p = i
#             else:
#                 i = i + 1
#         if not gefunden:
#             p = z
#         faktoren = faktoren + [p]
#         z = z // p
#     return faktoren
#
# print(primfaktoren(11294836000185182004739327135074338023702743595508996535605386137113131858114980414026078704581834950720656413858356255382624156762980350532381713398837163861611859948267002274751902168003361982606637222789451874254706737691926233602755882284767805048177431669999348695001282651919942628207954606932388523479536698162813451401325024495403963922164708782956968430045531395073500497754785387424288093478807322067058225072147935874466098950035430872942796804823084739584209638467358415003169562310267557413576657183603821111003734788446602360232219976989950209662089031748172271019328780189526733667835089294067029108661))



