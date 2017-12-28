import urllib.request
import json
import os
import yaml

# class AstronomicalObject:
#     def __init__(self, uid):
#         self.fetchedPage = urllib.request.urlopen("http://stapi.co/api/v1/rest/astronomicalObject?uid=" + str(uid))
#         self.jsonData = json.loads(str(self.fetchedPage.readlines()[0].decode("UTF-8")))
#         for key, value in self.jsonData["astronomicalObject"].items():
#             if type(value) is not dict:
#                 setattr(self, key, value)


class RestClient:
    entity_types = ['food', 'material', 'conflict', 'weapon', 'video_release',
    'performer', 'book', 'comics', 'occupation', 'episode', 'organization', 'magazine',
    'astronomical_object', 'platform', 'element', 'trading_card', 'trading_card_deck', 'company',
    'soundtrack', 'animal', 'trading_card_set', 'comic_series', 'spacecraft_type', 'genre',
    'medical_condition', 'video_game', 'technology', 'reference', 'spacecraft_class',
    'magazine_series', 'season', 'movie', 'spacecraft', 'book_collection', 'comic_strip',
    'staff', 'series', 'comic_collection', 'content_rating', 'title', 'content_language',
    'common', 'species', 'location', 'country', 'book_series', 'character', 'literature']


    def __init__(self, url, apiKey):
        self.url = url
        self.apiKey = apiKey
    def getAstronomicalObject(self):
        return GetAstronomicalObject(self, url, apiKey)
