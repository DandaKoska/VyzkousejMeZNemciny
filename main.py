import random

vocabulary_sets = {
    "1": {
        "label":"Super! 2 Lekce 18 Část 1",
        "vocabulary":{
            "das Gepäck": "zavazadlo",
            "meinen, h. gemeint": "myslet si, mínit",
            "der Reporter": "reportér",
            "der Strand":"pláž",
            "der Berg":"hora",
            "der See":"jezero",
            "das Wetter":"počasí",
            "regnen, h. geregnet":"pršet",
            "es regnet":"prší",
            "scheinen, h. geschienen":"zde: svítit",
            "die Sonne":"slunce",
            "es ist warm/kalt":"je teplo/chladno",
            "der Regen":"déšť",
            "Spanien":"Španělsko",
            "die ganze Zeit":"(po) celou dobu",
            "weiterfahren, i. weitergefahren":"jet dál",
            "zurück sein":"být zpátky",
            "bald":"brzy (v budoucnosti)",
            "Bis bald!":"Tak zatím!",
            "vor allem":"především",
            "daheim":"doma",
            "das ganze Jahr über":"po celý rok",
            "übernachten, h. übernachtet":"přenocovat",
            "die Karte":"zde: mapa",
            "die Taschenlampe":"kapesní svítilna, baterka",
            "der Wald":"les",
            "die Wiese":"louka",
            "der Grillplatz":"místo pro grilování",
            "der Bikini":"bikiny (dvoudílné plavky)",
            "die Badehose":"(pánské) plavky",
            "die Sonnenbrille":"sluneční brýle",
            "der Ball":"míč",
            "die Spielkarte":"hrací karta"
        }
    },
    
    "2": {
        "label":"Super! 2 Lekce 18 Část 2",
        "vocabulary":{
            "die Massage": "masáž",
            "schaffen": "vytvořit",
            "die Kerze": "svíčka",
            "wandern": "jít na túru",
            "die Sonnenblume": "slunečnice",
            "laufen": "chodit, běhat",
            "das Feld": "pole",
            "der Gummistiefel": "holínka",
            "der Wanderschuh": "turistická bota",
            "ruhig": "klidně",
            "lassen": "nechat",
            "mitbringen": "přinést",
            "der Laptop": "laptop",
            "das Dach": "střecha",
            "oben": "nahoře",
            "von oben": "shora",
            "doppelt": "dvakrát",
            "wollen": "chtít",
            "(un)möglich": "(ne)možný",
            "üben": "cvičit, procvičovat",
            "reiten, i. geritten": "jet/jezdit na koni",
            "das Ergebnis": "výsledek",
            "mitmachen": "(z)účastnit se",
            "Du hast recht": "Máš pravdu",
            "Das stimmt (nicht)": "To je (není) pravda",
            "beide": "oba",
            "international": "mezinárodní",
            "die Burg": "hrad",
            "mithelfen": "vypomáhat",
            "die Unterkunft": "ubytování",
            "freiwillig": "dobrovolný",
            "interessieren": "zajímat",
            "der Ort": "zde: místo"
        }
    },
}

def learn_vocabulary(vocabulary):
    words = list(vocabulary.keys())
    random.shuffle(words)
    for word in words:
        translation = vocabulary[word]
        guess = input(f"Jak se překládá slovo '{word}'? ")
        if guess == translation:
            print("Správně!")
        else:
            print(f"Nesprávně. Správný překlad je '{translation}'.")

def test_vocabulary(vocabulary):
    words = list(vocabulary.keys())
    random.shuffle(words)
    correct = 0
    incorrect = []
    for word in words:
        translation = vocabulary[word]
        guess = input(f"Jak se překládá slovo '{word}'? ")
        if guess == translation:
            print("správně")
            correct += 1
        else:
            print("špatně")
            incorrect.append((word, translation, guess))
    percentage = (correct / len(words)) * 100
    print(f"Uhodli jste {correct} z {len(words)} slov správně ({percentage:.2f}%).")
    if incorrect:
        print("Slova, která jste uhodli špatně:")
        for word, translation, guess in incorrect:
            print(f"{word} - správný překlad: {translation}, váš překlad: {guess}")

# Zeptejte se uživatele, kterou sadu slovíček chce naučit
vocabulary_set = input("Kterou sadu slovíček chcete naučit? (1 nebo 2) ")
if vocabulary_set in vocabulary_sets:
    vocabulary = vocabulary_sets[vocabulary_set]["vocabulary"]
    action = input("Chcete se učit nebo testovat? (u/t) ")
    if action == "u":
        learn_vocabulary(vocabulary)
    elif action == "t":
        test_vocabulary(vocabulary)
    else:
        print("Neplatná akce. Prosím, zadejte 'u' pro učení nebo 't' pro testování.")
else:
    print("Neplatná sada slovíček. Prosím, zadejte '1' nebo '2'.")
