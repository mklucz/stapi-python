import urllib.request
import json
import os
# import yaml

# class AstronomicalObject:
#     def __init__(self, uid):
#         self.fetchedPage = urllib.request.urlopen("http://stapi.co/api/v1/rest/astronomicalObject?uid=" + str(uid))
#         self.jsonData = json.loads(str(self.fetchedPage.readlines()[0].decode("UTF-8")))
#         for key, value in self.jsonData["astronomicalObject"].items():
#             if type(value) is not dict:
#                 setattr(self, key, value)

    # def getAstronomicalObject(self):
    #     return GetAstronomicalObject(self, url, apiKey)



entity_types = ['food', 'material', 'conflict', 'weapon', 'video_release',
'performer', 'book', 'comics', 'occupation', 'episode', 'organization', 'magazine',
'astronomical_object', 'platform', 'element', 'trading_card', 'trading_card_deck', 'company',
'soundtrack', 'animal', 'trading_card_set', 'comic_series', 'spacecraft_type', 'genre',
'medical_condition', 'video_game', 'technology', 'reference', 'spacecraft_class',
'magazine_series', 'season', 'movie', 'spacecraft', 'book_collection', 'comic_strip',
'staff', 'series', 'comic_collection', 'content_rating', 'title', 'content_language',
'common', 'species', 'location', 'country', 'book_series', 'character', 'literature']

klasy = []
for entity in entity_types:
    klasy.append(entity[:1].upper() + entity[1:])
# print(klasy)
lepsze_klasy = []
for klasa in klasy:
    for i in range(len(klasa)-2):
        if klasa[i] == "_":
            # print(klasa)
            klasa = klasa[:i] + klasa[i+1].upper() + klasa[i+2:]
            # print(klasa)
            # print("\n")
    lepsze_klasy.append(klasa)
    # print(klasa)
lepsze_klasy.sort()

def lower_first_char(s):
    return s[0].lower() + s[1:]
# for lasa in lepsze_klasy:
#     print("self." + lasa[0].lower() + lasa[1:] + " = " + lasa + "(url, apiKey)")

def helper_klasy_full_response():
    full_response_file = open("full_response.py", "w")
    for klasa in lepsze_klasy:
        full_response_file.write("class " + klasa + "FullResponse" + ":")
        full_response_file.write("""
        def __init__(self, uid):
            self.uid = uid
            self.""" + lower_first_char(klasa) + " = " + klasa + "Full(uid)")

        full_response_file.write("\n\n")
helper_klasy_full_response()

def helper_klasy_main():
    main_file = open("main.py", "w")
    for klasa in lepsze_klasy:
        main_file.write("class " + klasa + ":")
        main_file.write("""
        def __init__(self, url, apiKey):
            self.url = url
            self.apiKey = apiKey""")
        main_file.write("""
        def get(self, uid):
            pass
        def search(self, searchCriteria):
            pass
            """)
        main_file.write("\n")

    main_file.close()


# for klasa in lepsze_klasy:
#     print("class " + klasa + ":")
#     print("""
#     def __init__(self, url, apiKey):
#         self.url = url
#         self.apiKey = apiKey""")
#     print("""
#     def get(uid):
#         pass

#     def search(searchCriteria):
#         pass""")
#     print("\n")