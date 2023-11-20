import random

vocabulary_sets = {
    "1": {
        "label": "Super! 2 Lekce 18 Část 1",
        "vocabulary": {
                    "oznámkovat": "h. markiert",
                    "mít": "h. gehabt",
                    "jíst": "h. gegessen",
                    "pít": "h. getrunken",
                    "být": "b. gewessen",
                    "číst": "h. gelesen",
                    "jít": "b. gegangen",
                    "vidět": "h. gesehen",
                    "přijít": "b. gekommen",
                    "vědět": "h. gekannt",
                    "jmenovat se": "h. geheißen",
                    "cestovat": "b. gereist",
                    "napsat": "h. geschrieben",
                    "zpívat": "h. gesungen",
                    "návštěva": "h. besucht",
                    "najít": "h. gefunden",
                    "studovat": "h. studiert",
                    "mluvit": "h. gesprochen",
                    "plavat": "b. geschwommen",
                    "řídit": "b. gefahren",
                    "programovat": "h. programmiert",
                    "setkat": "h. getroffen",
                    "dostávat": "h. bekommen",
                    "pomoc": "h. geholfen",
                    "s sebou": "h. mitgebracht",
                    "vstát": "b. aufgestanden",
                    "pozvat": "h. eingeladen",
                    "vzít": "h. genommen",
                    "přinést": "h. gebracht",
                    "opravit": "h. repariert",
                }
    },
    "2": {
        "label": "Super! 2 Lekce 18 Část 2",
        "vocabulary": {
            # Your existing vocabulary set 2 here...
        }
    },
    # Add more vocabulary sets if needed
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
