
from .full import *
from .base import *
from .full_response import *
from .base_response import *
from urllib.request import urlopen as urlopen
from json import loads

class Animal:
        def __init__(self, url, apiKey):
            self.url = url
            self.apiKey = apiKey
        def get(self, uid):
            url_to_open = self.url + "/api/v1/rest/animal?uid=" + uid
            fetched_data = urlopen(url_to_open)
            decoded_data = fetched_data.readlines()[0].decode("utf-8")
            parsed_data = loads(decoded_data)
            print(parsed_data)
            args_mapping = parsed_data["animal"]
            return AnimalFull(**args_mapping)
            
        def search(self, searchCriteria):
            pass
            
class AstronomicalObject:
        def __init__(self, url, apiKey):
            self.url = url
            self.apiKey = apiKey
        def get(self, uid):
            url_to_open = self.url + "/api/v1/rest/astronomicalObject?uid=" + uid
            fetched_data = urlopen(url_to_open)
            decoded_data = fetched_data.readlines()[0].decode("utf-8")
            parsed_data = loads(decoded_data)
            print(parsed_data)
            args_mapping = parsed_data["astronomicalObject"]
            return AstronomicalObjectFull(**args_mapping)
            
        def search(self, searchCriteria):
            pass
            
class Book:
        def __init__(self, url, apiKey):
            self.url = url
            self.apiKey = apiKey
        def get(self, uid):
            url_to_open = self.url + "/api/v1/rest/book?uid=" + uid
            fetched_data = urlopen(url_to_open)
            decoded_data = fetched_data.readlines()[0].decode("utf-8")
            parsed_data = loads(decoded_data)
            print(parsed_data)
            args_mapping = parsed_data["book"]
            return BookFull(**args_mapping)
            
        def search(self, searchCriteria):
            pass
            
class BookCollection:
        def __init__(self, url, apiKey):
            self.url = url
            self.apiKey = apiKey
        def get(self, uid):
            url_to_open = self.url + "/api/v1/rest/bookCollection?uid=" + uid
            fetched_data = urlopen(url_to_open)
            decoded_data = fetched_data.readlines()[0].decode("utf-8")
            parsed_data = loads(decoded_data)
            print(parsed_data)
            args_mapping = parsed_data["bookCollection"]
            return BookCollectionFull(**args_mapping)
            
        def search(self, searchCriteria):
            pass
            
class BookSeries:
        def __init__(self, url, apiKey):
            self.url = url
            self.apiKey = apiKey
        def get(self, uid):
            url_to_open = self.url + "/api/v1/rest/bookSeries?uid=" + uid
            fetched_data = urlopen(url_to_open)
            decoded_data = fetched_data.readlines()[0].decode("utf-8")
            parsed_data = loads(decoded_data)
            print(parsed_data)
            args_mapping = parsed_data["bookSeries"]
            return BookSeriesFull(**args_mapping)
            
        def search(self, searchCriteria):
            pass
            
class Character:
        def __init__(self, url, apiKey):
            self.url = url
            self.apiKey = apiKey
        def get(self, uid):
            url_to_open = self.url + "/api/v1/rest/character?uid=" + uid
            fetched_data = urlopen(url_to_open)
            decoded_data = fetched_data.readlines()[0].decode("utf-8")
            parsed_data = loads(decoded_data)
            print(parsed_data)
            args_mapping = parsed_data["character"]
            return CharacterFull(**args_mapping)
            
        def search(self, searchCriteria):
            pass
            
class ComicCollection:
        def __init__(self, url, apiKey):
            self.url = url
            self.apiKey = apiKey
        def get(self, uid):
            url_to_open = self.url + "/api/v1/rest/comicCollection?uid=" + uid
            fetched_data = urlopen(url_to_open)
            decoded_data = fetched_data.readlines()[0].decode("utf-8")
            parsed_data = loads(decoded_data)
            print(parsed_data)
            args_mapping = parsed_data["comicCollection"]
            return ComicCollectionFull(**args_mapping)
            
        def search(self, searchCriteria):
            pass
            
class ComicSeries:
        def __init__(self, url, apiKey):
            self.url = url
            self.apiKey = apiKey
        def get(self, uid):
            url_to_open = self.url + "/api/v1/rest/comicSeries?uid=" + uid
            fetched_data = urlopen(url_to_open)
            decoded_data = fetched_data.readlines()[0].decode("utf-8")
            parsed_data = loads(decoded_data)
            print(parsed_data)
            args_mapping = parsed_data["comicSeries"]
            return ComicSeriesFull(**args_mapping)
            
        def search(self, searchCriteria):
            pass
            
class ComicStrip:
        def __init__(self, url, apiKey):
            self.url = url
            self.apiKey = apiKey
        def get(self, uid):
            url_to_open = self.url + "/api/v1/rest/comicStrip?uid=" + uid
            fetched_data = urlopen(url_to_open)
            decoded_data = fetched_data.readlines()[0].decode("utf-8")
            parsed_data = loads(decoded_data)
            print(parsed_data)
            args_mapping = parsed_data["comicStrip"]
            return ComicStripFull(**args_mapping)
            
        def search(self, searchCriteria):
            pass
            
class Comics:
        def __init__(self, url, apiKey):
            self.url = url
            self.apiKey = apiKey
        def get(self, uid):
            url_to_open = self.url + "/api/v1/rest/comics?uid=" + uid
            fetched_data = urlopen(url_to_open)
            decoded_data = fetched_data.readlines()[0].decode("utf-8")
            parsed_data = loads(decoded_data)
            print(parsed_data)
            args_mapping = parsed_data["comics"]
            return ComicsFull(**args_mapping)
            
        def search(self, searchCriteria):
            pass
            
class Company:
        def __init__(self, url, apiKey):
            self.url = url
            self.apiKey = apiKey
        def get(self, uid):
            url_to_open = self.url + "/api/v1/rest/company?uid=" + uid
            fetched_data = urlopen(url_to_open)
            decoded_data = fetched_data.readlines()[0].decode("utf-8")
            parsed_data = loads(decoded_data)
            print(parsed_data)
            args_mapping = parsed_data["company"]
            return CompanyFull(**args_mapping)
            
        def search(self, searchCriteria):
            pass
            
class Conflict:
        def __init__(self, url, apiKey):
            self.url = url
            self.apiKey = apiKey
        def get(self, uid):
            url_to_open = self.url + "/api/v1/rest/conflict?uid=" + uid
            fetched_data = urlopen(url_to_open)
            decoded_data = fetched_data.readlines()[0].decode("utf-8")
            parsed_data = loads(decoded_data)
            print(parsed_data)
            args_mapping = parsed_data["conflict"]
            return ConflictFull(**args_mapping)
            
        def search(self, searchCriteria):
            pass
            
class Element:
        def __init__(self, url, apiKey):
            self.url = url
            self.apiKey = apiKey
        def get(self, uid):
            url_to_open = self.url + "/api/v1/rest/element?uid=" + uid
            fetched_data = urlopen(url_to_open)
            decoded_data = fetched_data.readlines()[0].decode("utf-8")
            parsed_data = loads(decoded_data)
            print(parsed_data)
            args_mapping = parsed_data["element"]
            return ElementFull(**args_mapping)
            
        def search(self, searchCriteria):
            pass
            
class Episode:
        def __init__(self, url, apiKey):
            self.url = url
            self.apiKey = apiKey
        def get(self, uid):
            url_to_open = self.url + "/api/v1/rest/episode?uid=" + uid
            fetched_data = urlopen(url_to_open)
            decoded_data = fetched_data.readlines()[0].decode("utf-8")
            parsed_data = loads(decoded_data)
            print(parsed_data)
            args_mapping = parsed_data["episode"]
            return EpisodeFull(**args_mapping)
            
        def search(self, searchCriteria):
            pass
            
class Food:
        def __init__(self, url, apiKey):
            self.url = url
            self.apiKey = apiKey
        def get(self, uid):
            url_to_open = self.url + "/api/v1/rest/food?uid=" + uid
            fetched_data = urlopen(url_to_open)
            decoded_data = fetched_data.readlines()[0].decode("utf-8")
            parsed_data = loads(decoded_data)
            print(parsed_data)
            args_mapping = parsed_data["food"]
            return FoodFull(**args_mapping)
            
        def search(self, searchCriteria):
            pass
            
class Literature:
        def __init__(self, url, apiKey):
            self.url = url
            self.apiKey = apiKey
        def get(self, uid):
            url_to_open = self.url + "/api/v1/rest/literature?uid=" + uid
            fetched_data = urlopen(url_to_open)
            decoded_data = fetched_data.readlines()[0].decode("utf-8")
            parsed_data = loads(decoded_data)
            print(parsed_data)
            args_mapping = parsed_data["literature"]
            return LiteratureFull(**args_mapping)
            
        def search(self, searchCriteria):
            pass
            
class Location:
        def __init__(self, url, apiKey):
            self.url = url
            self.apiKey = apiKey
        def get(self, uid):
            url_to_open = self.url + "/api/v1/rest/location?uid=" + uid
            fetched_data = urlopen(url_to_open)
            decoded_data = fetched_data.readlines()[0].decode("utf-8")
            parsed_data = loads(decoded_data)
            print(parsed_data)
            args_mapping = parsed_data["location"]
            return LocationFull(**args_mapping)
            
        def search(self, searchCriteria):
            pass
            
class Magazine:
        def __init__(self, url, apiKey):
            self.url = url
            self.apiKey = apiKey
        def get(self, uid):
            url_to_open = self.url + "/api/v1/rest/magazine?uid=" + uid
            fetched_data = urlopen(url_to_open)
            decoded_data = fetched_data.readlines()[0].decode("utf-8")
            parsed_data = loads(decoded_data)
            print(parsed_data)
            args_mapping = parsed_data["magazine"]
            return MagazineFull(**args_mapping)
            
        def search(self, searchCriteria):
            pass
            
class MagazineSeries:
        def __init__(self, url, apiKey):
            self.url = url
            self.apiKey = apiKey
        def get(self, uid):
            url_to_open = self.url + "/api/v1/rest/magazineSeries?uid=" + uid
            fetched_data = urlopen(url_to_open)
            decoded_data = fetched_data.readlines()[0].decode("utf-8")
            parsed_data = loads(decoded_data)
            print(parsed_data)
            args_mapping = parsed_data["magazineSeries"]
            return MagazineSeriesFull(**args_mapping)
            
        def search(self, searchCriteria):
            pass
            
class Material:
        def __init__(self, url, apiKey):
            self.url = url
            self.apiKey = apiKey
        def get(self, uid):
            url_to_open = self.url + "/api/v1/rest/material?uid=" + uid
            fetched_data = urlopen(url_to_open)
            decoded_data = fetched_data.readlines()[0].decode("utf-8")
            parsed_data = loads(decoded_data)
            print(parsed_data)
            args_mapping = parsed_data["material"]
            return MaterialFull(**args_mapping)
            
        def search(self, searchCriteria):
            pass
            
class MedicalCondition:
        def __init__(self, url, apiKey):
            self.url = url
            self.apiKey = apiKey
        def get(self, uid):
            url_to_open = self.url + "/api/v1/rest/medicalCondition?uid=" + uid
            fetched_data = urlopen(url_to_open)
            decoded_data = fetched_data.readlines()[0].decode("utf-8")
            parsed_data = loads(decoded_data)
            print(parsed_data)
            args_mapping = parsed_data["medicalCondition"]
            return MedicalConditionFull(**args_mapping)
            
        def search(self, searchCriteria):
            pass
            
class Movie:
        def __init__(self, url, apiKey):
            self.url = url
            self.apiKey = apiKey
        def get(self, uid):
            url_to_open = self.url + "/api/v1/rest/movie?uid=" + uid
            fetched_data = urlopen(url_to_open)
            decoded_data = fetched_data.readlines()[0].decode("utf-8")
            parsed_data = loads(decoded_data)
            print(parsed_data)
            args_mapping = parsed_data["movie"]
            return MovieFull(**args_mapping)
            
        def search(self, searchCriteria):
            pass
            
class Occupation:
        def __init__(self, url, apiKey):
            self.url = url
            self.apiKey = apiKey
        def get(self, uid):
            url_to_open = self.url + "/api/v1/rest/occupation?uid=" + uid
            fetched_data = urlopen(url_to_open)
            decoded_data = fetched_data.readlines()[0].decode("utf-8")
            parsed_data = loads(decoded_data)
            print(parsed_data)
            args_mapping = parsed_data["occupation"]
            return OccupationFull(**args_mapping)
            
        def search(self, searchCriteria):
            pass
            
class Organization:
        def __init__(self, url, apiKey):
            self.url = url
            self.apiKey = apiKey
        def get(self, uid):
            url_to_open = self.url + "/api/v1/rest/organization?uid=" + uid
            fetched_data = urlopen(url_to_open)
            decoded_data = fetched_data.readlines()[0].decode("utf-8")
            parsed_data = loads(decoded_data)
            print(parsed_data)
            args_mapping = parsed_data["organization"]
            return OrganizationFull(**args_mapping)
            
        def search(self, searchCriteria):
            pass
            
class Performer:
        def __init__(self, url, apiKey):
            self.url = url
            self.apiKey = apiKey
        def get(self, uid):
            url_to_open = self.url + "/api/v1/rest/performer?uid=" + uid
            fetched_data = urlopen(url_to_open)
            decoded_data = fetched_data.readlines()[0].decode("utf-8")
            parsed_data = loads(decoded_data)
            print(parsed_data)
            args_mapping = parsed_data["performer"]
            return PerformerFull(**args_mapping)
            
        def search(self, searchCriteria):
            pass
            
class Season:
        def __init__(self, url, apiKey):
            self.url = url
            self.apiKey = apiKey
        def get(self, uid):
            url_to_open = self.url + "/api/v1/rest/season?uid=" + uid
            fetched_data = urlopen(url_to_open)
            decoded_data = fetched_data.readlines()[0].decode("utf-8")
            parsed_data = loads(decoded_data)
            print(parsed_data)
            args_mapping = parsed_data["season"]
            return SeasonFull(**args_mapping)
            
        def search(self, searchCriteria):
            pass
            
class Series:
        def __init__(self, url, apiKey):
            self.url = url
            self.apiKey = apiKey
        def get(self, uid):
            url_to_open = self.url + "/api/v1/rest/series?uid=" + uid
            fetched_data = urlopen(url_to_open)
            decoded_data = fetched_data.readlines()[0].decode("utf-8")
            parsed_data = loads(decoded_data)
            print(parsed_data)
            args_mapping = parsed_data["series"]
            return SeriesFull(**args_mapping)
            
        def search(self, searchCriteria):
            pass
            
class Soundtrack:
        def __init__(self, url, apiKey):
            self.url = url
            self.apiKey = apiKey
        def get(self, uid):
            url_to_open = self.url + "/api/v1/rest/soundtrack?uid=" + uid
            fetched_data = urlopen(url_to_open)
            decoded_data = fetched_data.readlines()[0].decode("utf-8")
            parsed_data = loads(decoded_data)
            print(parsed_data)
            args_mapping = parsed_data["soundtrack"]
            return SoundtrackFull(**args_mapping)
            
        def search(self, searchCriteria):
            pass
            
class Spacecraft:
        def __init__(self, url, apiKey):
            self.url = url
            self.apiKey = apiKey
        def get(self, uid):
            url_to_open = self.url + "/api/v1/rest/spacecraft?uid=" + uid
            fetched_data = urlopen(url_to_open)
            decoded_data = fetched_data.readlines()[0].decode("utf-8")
            parsed_data = loads(decoded_data)
            print(parsed_data)
            args_mapping = parsed_data["spacecraft"]
            return SpacecraftFull(**args_mapping)
            
        def search(self, searchCriteria):
            pass
            
class SpacecraftClass:
        def __init__(self, url, apiKey):
            self.url = url
            self.apiKey = apiKey
        def get(self, uid):
            url_to_open = self.url + "/api/v1/rest/spacecraftClass?uid=" + uid
            fetched_data = urlopen(url_to_open)
            decoded_data = fetched_data.readlines()[0].decode("utf-8")
            parsed_data = loads(decoded_data)
            print(parsed_data)
            args_mapping = parsed_data["spacecraftClass"]
            return SpacecraftClassFull(**args_mapping)
            
        def search(self, searchCriteria):
            pass
            
class Species:
        def __init__(self, url, apiKey):
            self.url = url
            self.apiKey = apiKey
        def get(self, uid):
            url_to_open = self.url + "/api/v1/rest/species?uid=" + uid
            fetched_data = urlopen(url_to_open)
            decoded_data = fetched_data.readlines()[0].decode("utf-8")
            parsed_data = loads(decoded_data)
            print(parsed_data)
            args_mapping = parsed_data["species"]
            return SpeciesFull(**args_mapping)
            
        def search(self, searchCriteria):
            pass
            
class Staff:
        def __init__(self, url, apiKey):
            self.url = url
            self.apiKey = apiKey
        def get(self, uid):
            url_to_open = self.url + "/api/v1/rest/staff?uid=" + uid
            fetched_data = urlopen(url_to_open)
            decoded_data = fetched_data.readlines()[0].decode("utf-8")
            parsed_data = loads(decoded_data)
            print(parsed_data)
            args_mapping = parsed_data["staff"]
            return StaffFull(**args_mapping)
            
        def search(self, searchCriteria):
            pass
            
class Technology:
        def __init__(self, url, apiKey):
            self.url = url
            self.apiKey = apiKey
        def get(self, uid):
            url_to_open = self.url + "/api/v1/rest/technology?uid=" + uid
            fetched_data = urlopen(url_to_open)
            decoded_data = fetched_data.readlines()[0].decode("utf-8")
            parsed_data = loads(decoded_data)
            print(parsed_data)
            args_mapping = parsed_data["technology"]
            return TechnologyFull(**args_mapping)
            
        def search(self, searchCriteria):
            pass
            
class Title:
        def __init__(self, url, apiKey):
            self.url = url
            self.apiKey = apiKey
        def get(self, uid):
            url_to_open = self.url + "/api/v1/rest/title?uid=" + uid
            fetched_data = urlopen(url_to_open)
            decoded_data = fetched_data.readlines()[0].decode("utf-8")
            parsed_data = loads(decoded_data)
            print(parsed_data)
            args_mapping = parsed_data["title"]
            return TitleFull(**args_mapping)
            
        def search(self, searchCriteria):
            pass
            
class TradingCard:
        def __init__(self, url, apiKey):
            self.url = url
            self.apiKey = apiKey
        def get(self, uid):
            url_to_open = self.url + "/api/v1/rest/tradingCard?uid=" + uid
            fetched_data = urlopen(url_to_open)
            decoded_data = fetched_data.readlines()[0].decode("utf-8")
            parsed_data = loads(decoded_data)
            print(parsed_data)
            args_mapping = parsed_data["tradingCard"]
            return TradingCardFull(**args_mapping)
            
        def search(self, searchCriteria):
            pass
            
class TradingCardDeck:
        def __init__(self, url, apiKey):
            self.url = url
            self.apiKey = apiKey
        def get(self, uid):
            url_to_open = self.url + "/api/v1/rest/tradingCardDeck?uid=" + uid
            fetched_data = urlopen(url_to_open)
            decoded_data = fetched_data.readlines()[0].decode("utf-8")
            parsed_data = loads(decoded_data)
            print(parsed_data)
            args_mapping = parsed_data["tradingCardDeck"]
            return TradingCardDeckFull(**args_mapping)
            
        def search(self, searchCriteria):
            pass
            
class TradingCardSet:
        def __init__(self, url, apiKey):
            self.url = url
            self.apiKey = apiKey
        def get(self, uid):
            url_to_open = self.url + "/api/v1/rest/tradingCardSet?uid=" + uid
            fetched_data = urlopen(url_to_open)
            decoded_data = fetched_data.readlines()[0].decode("utf-8")
            parsed_data = loads(decoded_data)
            print(parsed_data)
            args_mapping = parsed_data["tradingCardSet"]
            return TradingCardSetFull(**args_mapping)
            
        def search(self, searchCriteria):
            pass
            
class VideoGame:
        def __init__(self, url, apiKey):
            self.url = url
            self.apiKey = apiKey
        def get(self, uid):
            url_to_open = self.url + "/api/v1/rest/videoGame?uid=" + uid
            fetched_data = urlopen(url_to_open)
            decoded_data = fetched_data.readlines()[0].decode("utf-8")
            parsed_data = loads(decoded_data)
            print(parsed_data)
            args_mapping = parsed_data["videoGame"]
            return VideoGameFull(**args_mapping)
            
        def search(self, searchCriteria):
            pass
            
class VideoRelease:
        def __init__(self, url, apiKey):
            self.url = url
            self.apiKey = apiKey
        def get(self, uid):
            url_to_open = self.url + "/api/v1/rest/videoRelease?uid=" + uid
            fetched_data = urlopen(url_to_open)
            decoded_data = fetched_data.readlines()[0].decode("utf-8")
            parsed_data = loads(decoded_data)
            print(parsed_data)
            args_mapping = parsed_data["videoRelease"]
            return VideoReleaseFull(**args_mapping)
            
        def search(self, searchCriteria):
            pass
            
class Weapon:
        def __init__(self, url, apiKey):
            self.url = url
            self.apiKey = apiKey
        def get(self, uid):
            url_to_open = self.url + "/api/v1/rest/weapon?uid=" + uid
            fetched_data = urlopen(url_to_open)
            decoded_data = fetched_data.readlines()[0].decode("utf-8")
            parsed_data = loads(decoded_data)
            print(parsed_data)
            args_mapping = parsed_data["weapon"]
            return WeaponFull(**args_mapping)
            
        def search(self, searchCriteria):
            pass
            
