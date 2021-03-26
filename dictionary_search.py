import json

import requests


class SearchDictionary:
    def __init__(self, word):
        self.word = word

    def check_word(self):
        url = "https://api.dictionaryapi.dev/api/v2/entries/en_US/" + str(self.word)

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        print(json.loads(response.text))


if __name__ == '__main__':
    word = input("Enter Word:- ")
    obj = SearchDictionary(word)
    obj.check_word()
