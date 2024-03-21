class Dictionary:
    def __init__(self, language):
        self.language = language
        self._dict = []

    def loadDictionary(self,language):
        # Trasformare le  parole in lower
        with open("resources/" + language + ".txt", 'r', encoding="utf-8") as file:
            for line in file:
                valori = line.strip("\n")
                self._dict.append(valori)
        return self._dict

    def printAll(self):
        for parola in self._dict:
            print(parola)

    @property
    def dict(self):
        return self._dict

    def __contains__(self, item):
        for i in self._dict:
            if i == item:
                return True
        return False
