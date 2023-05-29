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
    # Zde dando kdyžtak přidávej další slovíčka a dáme to na parts ve stylu super2 lektion 18 part 1 a to stejný ale part 2 v jiným listu chápeš
}

def select_vocabulary_set():
    print("Dostupné sady slovíček:")
    for vocab_set, vocab_data in vocabulary_sets.items():
        label = vocab_data["label"]
        print(f"Type '{vocab_set}' for {label}")

    vocabulary_set = input("Zadejte název sady slovíček: ")
    return vocabulary_set

def german_vocabulary_quiz(vocabulary_set):
    vocabulary = vocabulary_sets.get(vocabulary_set)
    if not vocabulary:
        print(f"Sada slovíček '{vocabulary_set}' neexistuje.")
        return

    incorrect_words = list(vocabulary["vocabulary"].keys())
    incorrect_count = 0

    for czech_word in incorrect_words:
        correct_translation = vocabulary["vocabulary"][czech_word]
        user_translation = input(f"Jak se řekne '{correct_translation}' po německy? ")

        if user_translation.lower() == czech_word.lower():
            print("Správně!")
        else:
            print(f"Nesprávně. Správný překlad je: '{czech_word}'.")
            incorrect_count += 1

    print(f"\nPočet špatných odpovědí: {incorrect_count}/{len(vocabulary['vocabulary'])}")

def german_vocabulary_prep(vocabulary_set):
    vocabulary = vocabulary_sets.get(vocabulary_set)
    if not vocabulary:
        print(f"Vocabulary set '{vocabulary_set}' does not exist.")
        return

    incorrect_words = list(vocabulary["vocabulary"].keys())
    correct_count = 0

    while incorrect_words:
        czech_word = random.choice(incorrect_words)
        correct_translation = vocabulary["vocabulary"][czech_word]
        user_translation = input(f"Jak se řekne '{correct_translation}' po německy? ")

        if user_translation.lower() == czech_word.lower():
            print("Správně!")
            incorrect_words.remove(czech_word)
            correct_count += 1
        else:
            print(f"Nesprávně. Správný překlad je: '{czech_word}'.")

    print(f"\nVšechna slova byla správně zopakována! Celkový počet správných odpovědí: {correct_count}/{len(vocabulary['vocabulary'])}")

def main():
    vocabulary_set = select_vocabulary_set()

    while True:
        print("Vyber si možnost:")
        print("1. Učící se fáze")
        print("2. Test")
        print("3. Odejít")
        print("4. Vybrat jinou sadu slovíček")

        choice = input("Zadejte svoji volbu: ")

        if choice == "1":
            german_vocabulary_prep(vocabulary_set)
        elif choice == "2":
            german_vocabulary_quiz(vocabulary_set)
        elif choice == "3":
            print("Ukončuji!")
            break
        elif choice == "4":
            vocabulary_set = select_vocabulary_set()
        else:
            print("Neplatná volba.\n")

if __name__ == "__main__":
    main()
