import dictionary
import spellchecker

sc = spellchecker.SpellChecker()

while(True):
    sc.printMenu()

    txtIn = input()
    if not txtIn.isdigit():
        print("Inserire un valore compreso tra 1 e 4")
        txtIn = input()
    if not 1 <= int(txtIn) <= 4:
        print("Inserire un valore compreso tra 1 e 4")
        txtIn = input()

    # Add input control here!

    if int(txtIn) == 1:
        print("Inserisci la tua frase in Italiano\n")
        txtIn = input()
        sc.handleSentence(txtIn,"Italian")
        continue

    if int(txtIn) == 2:
        print("Inserisci la tua frase in Inglese\n")
        txtIn = input()
        sc.handleSentence(txtIn,"English")
        continue

    if int(txtIn) == 3:
        print("Inserisci la tua frase in Spagnolo\n")
        txtIn = input()
        sc.handleSentence(txtIn,"Spanish")
        continue

    if int(txtIn) == 4:
        break


