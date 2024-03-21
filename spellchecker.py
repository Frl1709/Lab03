import time

import dictionary
import multiDictionary as md

class SpellChecker:

    def __init__(self):
        self._multidictionary = md.MultiDictionary()
        pass

    def handleSentence(self, txtIn, language):
        # Prendere la frase, eliminare la punteggiatura, dividerla in parole, ritornare le parole sbagliate, trovare il tempo di processo.
        # Elimino la punteggiatura e divido in parole
        start_time = time.time()
        clear_sentence = replaceChars(txtIn).lower().split()
        self._multidictionary.add_language(language)
        revisionato = self._multidictionary.searchWord(clear_sentence, language)
        print("Usando __contains__()")
        for word in revisionato:
            if not word.corretta:
                print(word)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Time elapse: {execution_time}")
        print("-----------------------------------------------------------------------")
        start_time1 = time.time()
        clear_sentence1 = replaceChars(txtIn).lower().split()
        self._multidictionary.add_language(language)
        revisionato1 = self._multidictionary.searchWordLinear(clear_sentence1, language)
        print("Usando la ricerca lineare")
        for word in revisionato1:
            if not word.corretta:
                print(word)
        end_time1 = time.time()
        execution_time1 = end_time1 - start_time1
        print(f"Time elapse: {execution_time1}")
        print("-----------------------------------------------------------------------")
        print("Usando la ricerca dicotomica")
        start_time2 = time.time()
        clear_sentence2 = replaceChars(txtIn).lower().split()
        self._multidictionary.add_language(language)
        revisionato2 = self._multidictionary.searchWordDichotomic(clear_sentence2, language)
        for word in revisionato2:
            if not word.corretta:
                print(word)
        end_time2 = time.time()
        execution_time2 = end_time2 - start_time2
        print(f"Time elapse: {execution_time2}")




    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\!£$%&/()=?^'[]{}@ç°#§*+-/;,:.-_<>"
    for c in chars:
        text = text.replace(c,"")
    return text