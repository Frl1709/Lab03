from dictionary import Dictionary
import richWord as rw


class MultiDictionary:

    def __init__(self):
       self.multiDict = {}

    def add_language(self, language):
        if language not in self.multiDict:
            dizionario = Dictionary(language)
            dizionario.loadDictionary(language)
            self.multiDict[language] = dizionario
        return self.multiDict[language]


    def searchWord(self, words, language):
        revisione = []
        for word in words:
            stato = rw.RichWord(word)
            if self.multiDict[language].__contains__(word):
                stato.corretta = True
            elif not self.multiDict[language].__contains__(word):
                stato.corretta = False
            revisione.append(stato)
        return revisione


    def searchWordLinear(self, words, language):
        revisione = []
        for word in words:
            stato = rw.RichWord(word)
            for i in self.multiDict[language].dict:
                if word == i:
                    stato.corretta = True
            if stato.corretta is None:
                stato.corretta = False
            revisione.append(stato)
        return revisione


    def searchWordDichotomic(self, words, language):
        revisione = []
        for word in words:
            start = 0
            lista_per_ricerca = self.multiDict[language].dict
            end = len(lista_per_ricerca)-1
            stato = rw.RichWord(word)
            while start <= end:
                mid = (start + end) // 2
                if lista_per_ricerca[mid] == word:
                    stato.corretta = True
                    break
                elif lista_per_ricerca[mid] < word:
                    start = mid + 1
                elif lista_per_ricerca[mid] > word:
                    end = mid - 1
                else:
                    stato.corretta = False
                    break
            revisione.append(stato)
        return revisione

