from .main import *

class RestClient:
    
    def __init__(self, url="http://stapi.co", apiKey=""):
        self.DEFAULT_URL = "http://stapi.co"
        self.DEFAULT_API_KEY = ""

        self.url = url
        self.apiKey = apiKey
        
        self.animal = Animal(url, apiKey)
        self.astronomicalObject = AstronomicalObject(url, apiKey)
        self.book = Book(url, apiKey)
        self.bookCollection = BookCollection(url, apiKey)
        self.bookSeries = BookSeries(url, apiKey)
        self.character = Character(url, apiKey)
        self.comicCollection = ComicCollection(url, apiKey)
        self.comicSeries = ComicSeries(url, apiKey)
        self.comicStrip = ComicStrip(url, apiKey)
        self.comics = Comics(url, apiKey)
        self.company = Company(url, apiKey)
        self.conflict = Conflict(url, apiKey)
        self.element = Element(url, apiKey)
        self.episode = Episode(url, apiKey)
        self.food = Food(url, apiKey)
        self.literature = Literature(url, apiKey)
        self.location = Location(url, apiKey)
        self.magazine = Magazine(url, apiKey)
        self.magazineSeries = MagazineSeries(url, apiKey)
        self.material = Material(url, apiKey)
        self.medicalCondition = MedicalCondition(url, apiKey)
        self.movie = Movie(url, apiKey)
        self.occupation = Occupation(url, apiKey)
        self.organization = Organization(url, apiKey)
        self.performer = Performer(url, apiKey)
        self.season = Season(url, apiKey)
        self.series = Series(url, apiKey)
        self.soundtrack = Soundtrack(url, apiKey)
        self.spacecraft = Spacecraft(url, apiKey)
        self.spacecraftClass = SpacecraftClass(url, apiKey)
        self.species = Species(url, apiKey)
        self.staff = Staff(url, apiKey)
        self.technology = Technology(url, apiKey)
        self.title = Title(url, apiKey)
        self.tradingCard = TradingCard(url, apiKey)
        self.tradingCardDeck = TradingCardDeck(url, apiKey)
        self.tradingCardSet = TradingCardSet(url, apiKey)
        self.videoGame = VideoGame(url, apiKey)
        self.videoRelease = VideoRelease(url, apiKey)
        self.weapon = Weapon(url, apiKey)











# entity_types = ['food', 'material', 'conflict', 'weapon', 'video_release',
#     'performer', 'book', 'comics', 'occupation', 'episode', 'organization', 'magazine',
#     'astronomical_object', 'platform', 'element', 'trading_card', 'trading_card_deck', 'company',
#     'soundtrack', 'animal', 'trading_card_set', 'comic_series', 'spacecraft_type', 'genre',
#     'medical_condition', 'video_game', 'technology', 'reference', 'spacecraft_class',
#     'magazine_series', 'season', 'movie', 'spacecraft', 'book_collection', 'comic_strip',
#     'staff', 'series', 'comic_collection', 'content_rating', 'title', 'content_language',
#     'common', 'species', 'location', 'country', 'book_series', 'character', 'literature']