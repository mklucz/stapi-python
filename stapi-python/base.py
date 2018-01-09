class Animal:
    def __init__(self, uid, name, avian=None, canine=None, earthAnimal=None, earthInsect=None, feline=None)
        """Base animal, returned in search results
        Args:
            uid (string): Animal unique ID
            name (string): Animal name
            avian (boolean): Whether it's an avian
            canine (boolean): Whether it's a canine
            earthAnimal (boolean): Whether it's an earth animal
            earthInsect (boolean): Whether it's an earth insect
            feline (boolean): Whether it's a feline
        """
        self.uid = uid
        self.name = name
        self.avian = avian
        self.canine = canine
        self.earthAnimal = earthAnimal
        self.earthInsect = earthInsect
        self.feline = feline
class AstronomicalObject:
    def __init__(self, uid, astronomicalObjectType, name, location=None)
        """Base astronomical object, returned in search results
        Args:
            uid (string): Astronomical object's unique ID
            name (string): Astronomical object name
            location (#/definitions/AstronomicalObjectHeader): Location of astronomical object (optional)
        """
        self.uid = uid
        self.name = name
        self.location = location
class Book:
    def __init__(self, uid, anthology, audiobook, audiobookAbridged, biographyBook, eBook, novel, novelization, referenceBook, rolePlayingBook, title, audiobookPublishedDay=None, audiobookPublishedMonth=None, audiobookPublishedYear=None, audiobookRunTime=None, numberOfPages=None, productionNumber=None, publishedDay=None, publishedMonth=None, publishedYear=None, stardateFrom=None, stardateTo=None, yearFrom=None, yearTo=None)
        """Base book, returned in search results
        Args:
            uid (string): Book unique ID
            title (string): Book title
            audiobookPublishedDay (integer): Day the audiobook was published
            audiobookPublishedMonth (integer): Month the audiobook was published
            audiobookPublishedYear (integer): Year the audiobook was published
            audiobookRunTime (integer): Audiobook run time, in minutes
            numberOfPages (integer): Number of pages
            productionNumber (string): Book's production number
            publishedDay (integer): Day the book was published
            publishedMonth (integer): Month the book was published
            publishedYear (integer): Year the book was published
            stardateFrom (number): Starting stardate of book story
            stardateTo (number): Ending stardate of book story
            yearFrom (integer): Starting year of book story
            yearTo (integer): Ending year of book story
        """
        self.uid = uid
        self.title = title
        self.audiobookPublishedDay = audiobookPublishedDay
        self.audiobookPublishedMonth = audiobookPublishedMonth
        self.audiobookPublishedYear = audiobookPublishedYear
        self.audiobookRunTime = audiobookRunTime
        self.numberOfPages = numberOfPages
        self.productionNumber = productionNumber
        self.publishedDay = publishedDay
        self.publishedMonth = publishedMonth
        self.publishedYear = publishedYear
        self.stardateFrom = stardateFrom
        self.stardateTo = stardateTo
        self.yearFrom = yearFrom
        self.yearTo = yearTo
