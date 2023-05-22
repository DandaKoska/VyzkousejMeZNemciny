import random

vocabulary = {
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
    "(un]möglich": "(ne)možný",
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

def german_vocabulary_quiz():
    correct_count = 0
    for czech_word, correct_translation in vocabulary.items():
        user_translation = input(f"Jak se řekne '{czech_word}' po německy? ")

        if user_translation.lower() == correct_translation.lower():
            print("Správně!")
            correct_count += 1
        else:
            print(f"Nesprávně. Správný překlad je: '{correct_translation}'.")

    print(f"\nCelkový počet správných odpovědí: {correct_count}/{len(vocabulary)}")

def german_vocabulary_prep():
    incorrect_words = list(vocabulary.keys())
    correct_count = 0

    while incorrect_words:
        czech_word = random.choice(incorrect_words)
        correct_translation = vocabulary[czech_word]
        user_translation = input(f"Jak se řekne '{correct_translation}' po německy? ")

        if user_translation.lower() == czech_word.lower():
            print("Správně!")
            incorrect_words.remove(czech_word)
            correct_count += 1
        else:
            print(f"Nesprávně. Správný překlad je: '{czech_word}'.")

    print(f"\nVšechna slova byla správně zopakována! Celkový počet správných odpovědí: {correct_count}/{len(vocabulary)}")

def main():
    while True:
        print("Vítej v programu pro učení se Německých slovíček!")
        print("Vyber si možnost:")
        print("1. Učící se fáze")
        print("2. Test")
        print("3. Odejít")

        choice = input("Zadejte svoji volbu: ")

        if choice == "1":
            german_vocabulary_prep()
        elif choice == "2":
            german_vocabulary_quiz()
        elif choice == "3":
            print("Ukončuji!")
            break
        else:
            print("Neplatná volba.\n")

if __name__ == "__main__":
    main()
