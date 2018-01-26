class AnimalFull:
    def __init__(self, uid, name, earthAnimal=None, earthInsect=None, avian=None, canine=None, feline=None):
        """Full animal, returned when queried using UID
        Args:
            uid (string): Animal unique ID
            name (string): Animal name
            earthAnimal (boolean): Whether it's an earth animal
            earthInsect (boolean): Whether it's an earth insect
            avian (boolean): Whether it's an avian
            canine (boolean): Whether it's a canine
            feline (boolean): Whether it's a feline
        """
        self.uid = uid
        self.name = name
        self.earthAnimal = earthAnimal
        self.earthInsect = earthInsect
        self.avian = avian
        self.canine = canine
        self.feline = feline
class AstronomicalObjectFull:
    def __init__(self, uid, name, astronomicalObjectType, location=None, astronomicalObjects=None):
        """Full astronomical object, returned when queried using UID
        Args:
            uid (string): Astronomical object's unique ID
            name (string): Astronomical object name
            astronomicalObjectType (#/definitions/AstronomicalObjectType): Type of astronomical object
            location (#/definitions/AstronomicalObjectBase): Location of astronomical object (optional)
            astronomicalObjects (array): Astronomical objects located in this astronomical object, like planets in a star system
        """
        self.uid = uid
        self.name = name
        self.astronomicalObjectType = astronomicalObjectType
        self.location = location
        self.astronomicalObjects = astronomicalObjects
class BookFull:
    def __init__(self, uid, title, novel, referenceBook, biographyBook, rolePlayingBook, eBook, anthology, novelization, audiobook, audiobookAbridged, publishedYear=None, publishedMonth=None, publishedDay=None, numberOfPages=None, stardateFrom=None, stardateTo=None, yearFrom=None, yearTo=None, audiobookPublishedYear=None, audiobookPublishedMonth=None, audiobookPublishedDay=None, audiobookRunTime=None, productionNumber=None, bookSeries=None, authors=None, artists=None, editors=None, audiobookNarrators=None, publishers=None, audiobookPublishers=None, characters=None, references=None, audiobookReferences=None, bookCollections=None):
        """Full book, returned when queried using UID
        Args:
            uid (string): Book unique ID
            title (string): Book title
            publishedYear (integer): Year the book was published
            publishedMonth (integer): Month the book was published
            publishedDay (integer): Day the book was published
            numberOfPages (integer): Number of pages
            stardateFrom (number): Starting stardate of book story
            stardateTo (number): Ending stardate of book story
            yearFrom (integer): Starting year of book story
            yearTo (integer): Ending year of book story
            novel (boolean): Whether it's a novel
            referenceBook (boolean): Whether it's a reference book
            biographyBook (boolean): Whether it's a biography book
            rolePlayingBook (boolean): Whether it's a role playing book
            eBook (boolean): Whether it's an e-book
            anthology (boolean): Whether it's an anthology
            novelization (boolean): Whether it's a novelization
            audiobook (boolean): Whether it's an audiobook, or has been release as an audiobook in addition to other form
            audiobookAbridged (boolean): If it's an audiobook, whether it's been abridged
            audiobookPublishedYear (integer): Year the audiobook was published
            audiobookPublishedMonth (integer): Month the audiobook was published
            audiobookPublishedDay (integer): Day the audiobook was published
            audiobookRunTime (integer): Audiobook run time, in minutes
            productionNumber (string): Book production number
            bookSeries (array): Book series this book is included in
            authors (array): Authors of the book
            artists (array): Artists involved in the book
            editors (array): Editors involved in the book
            audiobookNarrators (array): Audiobook narrators
            publishers (array): Book publishers
            audiobookPublishers (array): Audiobook publishers
            characters (array): Characters appearing the book
            references (array): References
            audiobookReferences (array): Audiobook references
            bookCollections (array): Book collections this book is included in
        """
        self.uid = uid
        self.title = title
        self.publishedYear = publishedYear
        self.publishedMonth = publishedMonth
        self.publishedDay = publishedDay
        self.numberOfPages = numberOfPages
        self.stardateFrom = stardateFrom
        self.stardateTo = stardateTo
        self.yearFrom = yearFrom
        self.yearTo = yearTo
        self.novel = novel
        self.referenceBook = referenceBook
        self.biographyBook = biographyBook
        self.rolePlayingBook = rolePlayingBook
        self.eBook = eBook
        self.anthology = anthology
        self.novelization = novelization
        self.audiobook = audiobook
        self.audiobookAbridged = audiobookAbridged
        self.audiobookPublishedYear = audiobookPublishedYear
        self.audiobookPublishedMonth = audiobookPublishedMonth
        self.audiobookPublishedDay = audiobookPublishedDay
        self.audiobookRunTime = audiobookRunTime
        self.productionNumber = productionNumber
        self.bookSeries = bookSeries
        self.authors = authors
        self.artists = artists
        self.editors = editors
        self.audiobookNarrators = audiobookNarrators
        self.publishers = publishers
        self.audiobookPublishers = audiobookPublishers
        self.characters = characters
        self.references = references
        self.audiobookReferences = audiobookReferences
        self.bookCollections = bookCollections
class BookCollectionFull:
    def __init__(self, uid=None, title=None, publishedYear=None, publishedMonth=None, publishedDay=None, numberOfPages=None, stardateFrom=None, stardateTo=None, yearFrom=None, yearTo=None, bookSeries=None, authors=None, artists=None, editors=None, publishers=None, characters=None, references=None, books=None):
        """Full book collection, returned when queried using UID
        Args:
            uid (string): Book collection unique ID
            title (string): Book collection title
            publishedYear (integer): Year the book collection was published
            publishedMonth (integer): Month the book collection was published
            publishedDay (integer): Day the book collection was published
            numberOfPages (integer): Number of pages
            stardateFrom (number): Starting stardate of book collection stories
            stardateTo (number): Ending stardate of book collection stories
            yearFrom (integer): Starting year of book collection stories
            yearTo (integer): Ending year of book collection stories
            bookSeries (array): Book series this book collection is included in
            authors (array): Authors of the book collection
            artists (array): Artists involved in the book collection
            editors (array): Editors involved in the book collection
            publishers (array): Book collection publishers
            characters (array): Characters appearing in the book collection
            references (array): References
            books (array): Books included in this book collection
        """
        self.uid = uid
        self.title = title
        self.publishedYear = publishedYear
        self.publishedMonth = publishedMonth
        self.publishedDay = publishedDay
        self.numberOfPages = numberOfPages
        self.stardateFrom = stardateFrom
        self.stardateTo = stardateTo
        self.yearFrom = yearFrom
        self.yearTo = yearTo
        self.bookSeries = bookSeries
        self.authors = authors
        self.artists = artists
        self.editors = editors
        self.publishers = publishers
        self.characters = characters
        self.references = references
        self.books = books
class BookSeriesFull:
    def __init__(self, uid, title, publishedYearFrom=None, publishedMonthFrom=None, publishedYearTo=None, publishedMonthTo=None, numberOfBooks=None, yearFrom=None, yearTo=None, miniseries=None, eBookSeries=None, parentSeries=None, childSeries=None, publishers=None, books=None):
        """Full book series, returned when queried using UID
        Args:
            uid (string): Book series unique ID
            title (string): Book series title
            publishedYearFrom (integer): Year from which the book series was published
            publishedMonthFrom (integer): Month from which the book series was published
            publishedYearTo (integer): Year to which the book series was published
            publishedMonthTo (integer): Month to which the book series was published
            numberOfBooks (integer): Number of books in book series
            yearFrom (integer): Starting year of book series stories
            yearTo (integer): Ending year of book series stories
            miniseries (boolean): Whether it's a miniseries
            eBookSeries (boolean): Whether it's a e-book series
            parentSeries (array): Book series this book series is included in
            childSeries (array): Child book series included in this book series
            publishers (array): Companies that published this book series
            books (array): Books included in this book series
        """
        self.uid = uid
        self.title = title
        self.publishedYearFrom = publishedYearFrom
        self.publishedMonthFrom = publishedMonthFrom
        self.publishedYearTo = publishedYearTo
        self.publishedMonthTo = publishedMonthTo
        self.numberOfBooks = numberOfBooks
        self.yearFrom = yearFrom
        self.yearTo = yearTo
        self.miniseries = miniseries
        self.eBookSeries = eBookSeries
        self.parentSeries = parentSeries
        self.childSeries = childSeries
        self.publishers = publishers
        self.books = books
class CharacterFull:
    def __init__(self, uid, name, gender=None, yearOfBirth=None, monthOfBirth=None, dayOfBirth=None, placeOfBirth=None, yearOfDeath=None, monthOfDeath=None, dayOfDeath=None, placeOfDeath=None, height=None, weight=None, deceased=None, bloodType=None, maritalStatus=None, serialNumber=None, hologramActivationDate=None, hologramStatus=None, hologramDateStatus=None, hologram=None, fictionalCharacter=None, mirror=None, alternateReality=None, performers=None, episodes=None, movies=None, characterSpecies=None, characterRelations=None, titles=None, occupations=None, organizations=None):
        """Full character, returned when queried using UID
        Args:
            uid (string): Character unique ID
            name (string): Character name
            gender (#/definitions/Gender): Character gender
            yearOfBirth (integer): Year the character was born
            monthOfBirth (integer): Month the character was born
            dayOfBirth (integer): Day the character was born
            placeOfBirth (string): Place of birth
            yearOfDeath (integer): Year the character died
            monthOfDeath (integer): Month the character died
            dayOfDeath (integer): Day the character died
            placeOfDeath (string): Place of death
            height (integer): Height in centimeters
            weight (integer): Weight in kilograms
            deceased (boolean): Whether this character is deceased
            bloodType (#/definitions/BloodType): Blood type
            maritalStatus (#/definitions/MaritalStatus): Marital status
            serialNumber (string): Serial number
            hologramActivationDate (string): Hologram activation date
            hologramStatus (string): Hologram status
            hologramDateStatus (string): Hologram date status
            hologram (boolean): Whether this character is a hologram
            fictionalCharacter (boolean): Whether this character is a fictional character (from universe point of view)
            mirror (boolean): Whether this character is from mirror universe
            alternateReality (boolean): Whether this character is from alternate reality
            performers (array): Performers who played this character
            episodes (array): Episodes in which this character appeared
            movies (array): Movies in which this character appeared
            characterSpecies (array): Species this character belongs to
            characterRelations (array): Relations with other characters
            titles (array): Titles this character holds
            occupations (array): Occupations of this character
            organizations (array): Organizations this character has affiliation with
        """
        self.uid = uid
        self.name = name
        self.gender = gender
        self.yearOfBirth = yearOfBirth
        self.monthOfBirth = monthOfBirth
        self.dayOfBirth = dayOfBirth
        self.placeOfBirth = placeOfBirth
        self.yearOfDeath = yearOfDeath
        self.monthOfDeath = monthOfDeath
        self.dayOfDeath = dayOfDeath
        self.placeOfDeath = placeOfDeath
        self.height = height
        self.weight = weight
        self.deceased = deceased
        self.bloodType = bloodType
        self.maritalStatus = maritalStatus
        self.serialNumber = serialNumber
        self.hologramActivationDate = hologramActivationDate
        self.hologramStatus = hologramStatus
        self.hologramDateStatus = hologramDateStatus
        self.hologram = hologram
        self.fictionalCharacter = fictionalCharacter
        self.mirror = mirror
        self.alternateReality = alternateReality
        self.performers = performers
        self.episodes = episodes
        self.movies = movies
        self.characterSpecies = characterSpecies
        self.characterRelations = characterRelations
        self.titles = titles
        self.occupations = occupations
        self.organizations = organizations
class ComicCollectionFull:
    def __init__(self, uid, title, publishedYear=None, publishedMonth=None, publishedDay=None, coverYear=None, coverMonth=None, coverDay=None, numberOfPages=None, stardateFrom=None, stardateTo=None, yearFrom=None, yearTo=None, photonovel=None, comicSeries=None, writers=None, artists=None, editors=None, staff=None, publishers=None, characters=None, references=None, comics=None):
        """Full comic collection, returned when queried using UID
        Args:
            uid (string): Comic collection unique ID
            title (string): Comic collection title
            publishedYear (integer): Year the comic collection was published
            publishedMonth (integer): Month the comic collection was published
            publishedDay (integer): Day the comic collection was published
            coverYear (integer): Cover publication year
            coverMonth (integer): Cover publication month
            coverDay (integer): Cover publication day
            numberOfPages (integer): Number of pages
            stardateFrom (number): Starting stardate of comic collection stories
            stardateTo (number): Ending stardate of comic collection stories
            yearFrom (integer): Starting year of comic collection stories
            yearTo (integer): Ending year of comic collection stories
            photonovel (boolean): Whether it's a photonovel collection
            comicSeries (array): Comic series this comic collection is included in
            writers (array): Writers involved in the comic collection
            artists (array): Artists involved in the comic collection
            editors (array): Editors involved in the comic collection
            staff (array): Other staff involved in the comic collection
            publishers (array): Comic collection publishers
            characters (array): Characters appearing in the comic collection
            references (array): References
            comics (array): Comics included in this comic collection
        """
        self.uid = uid
        self.title = title
        self.publishedYear = publishedYear
        self.publishedMonth = publishedMonth
        self.publishedDay = publishedDay
        self.coverYear = coverYear
        self.coverMonth = coverMonth
        self.coverDay = coverDay
        self.numberOfPages = numberOfPages
        self.stardateFrom = stardateFrom
        self.stardateTo = stardateTo
        self.yearFrom = yearFrom
        self.yearTo = yearTo
        self.photonovel = photonovel
        self.comicSeries = comicSeries
        self.writers = writers
        self.artists = artists
        self.editors = editors
        self.staff = staff
        self.publishers = publishers
        self.characters = characters
        self.references = references
        self.comics = comics
class ComicSeriesFull:
    def __init__(self, uid, title, publishedYearFrom=None, publishedMonthFrom=None, publishedDayFrom=None, publishedYearTo=None, publishedMonthTo=None, publishedDayTo=None, numberOfIssues=None, stardateFrom=None, stardateTo=None, yearFrom=None, yearTo=None, miniseries=None, photonovelSeries=None, parentSeries=None, childSeries=None, publishers=None, comics=None):
        """Full comic series, returned when queried using UID
        Args:
            uid (string): Comic series unique ID
            title (string): Comic series title
            publishedYearFrom (integer): Year from which the comic series was published
            publishedMonthFrom (integer): Month from which the comic series was published
            publishedDayFrom (integer): Day from which the comic series was published
            publishedYearTo (integer): Year to which the comic series was published
            publishedMonthTo (integer): Month to which the comic series was published
            publishedDayTo (integer): Day to which the comic series was published
            numberOfIssues (integer): Number of issues
            stardateFrom (number): Starting stardate of comic series stories
            stardateTo (number): Ending stardate of comic series stories
            yearFrom (integer): Starting year of comic series stories
            yearTo (integer): Ending year of comic series stories
            miniseries (boolean): Whether it's a miniseries
            photonovelSeries (boolean): Whether it's a photonovel series
            parentSeries (array): Comic series this comic series is included in
            childSeries (array): Child comic series included in this comic series
            publishers (array): Companies that published this comic series
            comics (array): Comics included in this comic series
        """
        self.uid = uid
        self.title = title
        self.publishedYearFrom = publishedYearFrom
        self.publishedMonthFrom = publishedMonthFrom
        self.publishedDayFrom = publishedDayFrom
        self.publishedYearTo = publishedYearTo
        self.publishedMonthTo = publishedMonthTo
        self.publishedDayTo = publishedDayTo
        self.numberOfIssues = numberOfIssues
        self.stardateFrom = stardateFrom
        self.stardateTo = stardateTo
        self.yearFrom = yearFrom
        self.yearTo = yearTo
        self.miniseries = miniseries
        self.photonovelSeries = photonovelSeries
        self.parentSeries = parentSeries
        self.childSeries = childSeries
        self.publishers = publishers
        self.comics = comics
class ComicStripFull:
    def __init__(self, uid, title, periodical=None, publishedYearFrom=None, publishedMonthFrom=None, publishedDayFrom=None, publishedYearTo=None, publishedMonthTo=None, publishedDayTo=None, numberOfPages=None, yearFrom=None, yearTo=None, comicSeries=None, writers=None, artists=None, characters=None):
        """Full comic strip, returned when queried using UID
        Args:
            uid (string): Comic strip unique ID
            title (string): Comic strip title
            periodical (string): Title of the periodical the comic strip was published in
            publishedYearFrom (integer): Year from which the comic strip was published
            publishedMonthFrom (integer): Month from which the comic strip was published
            publishedDayFrom (integer): Day from which the comic strip was published
            publishedYearTo (integer): Year to which the comic strip was published
            publishedMonthTo (integer): Month to which the comic strip was published
            publishedDayTo (integer): Day to which the comic strip was published
            numberOfPages (integer): Number of pages
            yearFrom (integer): Starting year of comic strip stories
            yearTo (integer): Ending year of comic strip stories
            comicSeries (array): Comic series this comic strip is included in
            writers (array): Writers involved in the comic strip
            artists (array): Artists involved in the comic strip
            characters (array): Characters appearing in the comic strip
        """
        self.uid = uid
        self.title = title
        self.periodical = periodical
        self.publishedYearFrom = publishedYearFrom
        self.publishedMonthFrom = publishedMonthFrom
        self.publishedDayFrom = publishedDayFrom
        self.publishedYearTo = publishedYearTo
        self.publishedMonthTo = publishedMonthTo
        self.publishedDayTo = publishedDayTo
        self.numberOfPages = numberOfPages
        self.yearFrom = yearFrom
        self.yearTo = yearTo
        self.comicSeries = comicSeries
        self.writers = writers
        self.artists = artists
        self.characters = characters
class ComicsFull:
    def __init__(self, uid, title, publishedYear=None, publishedMonth=None, publishedDay=None, coverYear=None, coverMonth=None, coverDay=None, numberOfPages=None, stardateFrom=None, stardateTo=None, yearFrom=None, yearTo=None, photonovel=None, adaptation=None, comicSeries=None, writers=None, artists=None, editors=None, staff=None, publishers=None, characters=None, references=None, comicCollections=None):
        """Full comics, returned when queried using UID
        Args:
            uid (string): Comics unique ID
            title (string): Comics title
            publishedYear (integer): Year the comics was published
            publishedMonth (integer): Month the comics was published
            publishedDay (integer): Day the comics was published
            coverYear (integer): Cover publication year
            coverMonth (integer): Cover publication month
            coverDay (integer): Cover publication day
            numberOfPages (integer): Number of pages
            stardateFrom (number): Starting stardate of comic story
            stardateTo (number): Ending stardate of comic story
            yearFrom (integer): Starting year of comic  story
            yearTo (integer): Ending year of comic story
            photonovel (boolean): Whether it's a photonovel
            adaptation (boolean): Whether it's an adaptation of an episode or a movie
            comicSeries (array): Comic series this comics is included in
            writers (array): Writers involved in the comics
            artists (array): Artists involved in the comics
            editors (array): Editors involved in the comics
            staff (array): Other staff involved in the comics
            publishers (array): Comics publishers
            characters (array): Characters appearing in the comics
            references (array): References
            comicCollections (array): Comic collections this comics is included in
        """
        self.uid = uid
        self.title = title
        self.publishedYear = publishedYear
        self.publishedMonth = publishedMonth
        self.publishedDay = publishedDay
        self.coverYear = coverYear
        self.coverMonth = coverMonth
        self.coverDay = coverDay
        self.numberOfPages = numberOfPages
        self.stardateFrom = stardateFrom
        self.stardateTo = stardateTo
        self.yearFrom = yearFrom
        self.yearTo = yearTo
        self.photonovel = photonovel
        self.adaptation = adaptation
        self.comicSeries = comicSeries
        self.writers = writers
        self.artists = artists
        self.editors = editors
        self.staff = staff
        self.publishers = publishers
        self.characters = characters
        self.references = references
        self.comicCollections = comicCollections
class CompanyFull:
    def __init__(self, uid, name, broadcaster=None, collectibleCompany=None, conglomerate=None, digitalVisualEffectsCompany=None, distributor=None, gameCompany=None, filmEquipmentCompany=None, makeUpEffectsStudio=None, mattePaintingCompany=None, modelAndMiniatureEffectsCompany=None, postProductionCompany=None, productionCompany=None, propCompany=None, recordLabel=None, specialEffectsCompany=None, tvAndFilmProductionCompany=None, videoGameCompany=None):
        """Full company, returned when queried using UID
        Args:
            uid (string): Company unique ID
            name (string): Company name
            broadcaster (boolean): Whether it's a broadcaster
            collectibleCompany (boolean): Whether it's a collectible company
            conglomerate (boolean): Whether it's a conglomerate
            digitalVisualEffectsCompany (boolean): Whether it's a digital visual effects company
            distributor (boolean): Whether it's a distributor
            gameCompany (boolean): Whether it's a game company
            filmEquipmentCompany (boolean): Whether it's a film equipment company
            makeUpEffectsStudio (boolean): Whether it's a make-up effects studio
            mattePaintingCompany (boolean): Whether it's a matte painting company
            modelAndMiniatureEffectsCompany (boolean): Whether it's a model and miniature effects company
            postProductionCompany (boolean): Whether it's a post-production company
            productionCompany (boolean): Whether it's a production company
            propCompany (boolean): Whether it's a prop company
            recordLabel (boolean): Whether it's a record label
            specialEffectsCompany (boolean): Whether it's a special effects company
            tvAndFilmProductionCompany (boolean): Whether it's a TV and film production company
            videoGameCompany (boolean): Whether it's a video game company
        """
        self.uid = uid
        self.name = name
        self.broadcaster = broadcaster
        self.collectibleCompany = collectibleCompany
        self.conglomerate = conglomerate
        self.digitalVisualEffectsCompany = digitalVisualEffectsCompany
        self.distributor = distributor
        self.gameCompany = gameCompany
        self.filmEquipmentCompany = filmEquipmentCompany
        self.makeUpEffectsStudio = makeUpEffectsStudio
        self.mattePaintingCompany = mattePaintingCompany
        self.modelAndMiniatureEffectsCompany = modelAndMiniatureEffectsCompany
        self.postProductionCompany = postProductionCompany
        self.productionCompany = productionCompany
        self.propCompany = propCompany
        self.recordLabel = recordLabel
        self.specialEffectsCompany = specialEffectsCompany
        self.tvAndFilmProductionCompany = tvAndFilmProductionCompany
        self.videoGameCompany = videoGameCompany
class ConflictFull:
    def __init__(self, uid, name, yearFrom=None, yearTo=None, earthConflict=None, federationWar=None, klingonWar=None, dominionWarBattle=None, alternateReality=None, locations=None, firstSideBelligerents=None, firstSideCommanders=None, secondSideBelligerents=None, secondSideCommanders=None):
        """Base conflict, returned in search results
        Args:
            uid (string): Conflict unique ID
            name (string): Conflict name
            yearFrom (integer): Starting year of the conflict
            yearTo (integer): Ending year of the conflict
            earthConflict (boolean): Whether it is an Earth conflict
            federationWar (boolean): Whether this conflict is a part of war involving Federation
            klingonWar (boolean): Whether this conflict is a part of war involving the Klingons
            dominionWarBattle (boolean): Whether this conflict is a Dominion war battle
            alternateReality (boolean): Whether this conflict is from alternate reality
            locations (array): Locations this conflict occurred at
            firstSideBelligerents (array): Organization involved in conflict on first side
            firstSideCommanders (array): Commanders involved in conflict on first side
            secondSideBelligerents (array): Organization involved in conflict on second side
            secondSideCommanders (array): Commanders involved in conflict on second side
        """
        self.uid = uid
        self.name = name
        self.yearFrom = yearFrom
        self.yearTo = yearTo
        self.earthConflict = earthConflict
        self.federationWar = federationWar
        self.klingonWar = klingonWar
        self.dominionWarBattle = dominionWarBattle
        self.alternateReality = alternateReality
        self.locations = locations
        self.firstSideBelligerents = firstSideBelligerents
        self.firstSideCommanders = firstSideCommanders
        self.secondSideBelligerents = secondSideBelligerents
        self.secondSideCommanders = secondSideCommanders
class ElementFull:
    def __init__(self, uid, name, symbol=None, atomicNumber=None, atomicWeight=None, transuranium=None, gammaSeries=None, hypersonicSeries=None, megaSeries=None, omegaSeries=None, transonicSeries=None, worldSeries=None):
        """Full element, returned when queried using UID
        Args:
            uid (string): Element unique ID
            name (string): Element name
            symbol (string): Element symbol
            atomicNumber (integer): Element atomic number
            atomicWeight (integer): Element atomic weight
            transuranium (boolean): Whether it's a transuranium
            gammaSeries (boolean): Whether it belongs to Gamma series
            hypersonicSeries (boolean): Whether it belongs to Hypersonic series
            megaSeries (boolean): Whether it belongs to Mega series
            omegaSeries (boolean): Whether it belongs to Omega series
            transonicSeries (boolean): Whether it belongs to Transonic series
            worldSeries (boolean): Whether it belongs to World series
        """
        self.uid = uid
        self.name = name
        self.symbol = symbol
        self.atomicNumber = atomicNumber
        self.atomicWeight = atomicWeight
        self.transuranium = transuranium
        self.gammaSeries = gammaSeries
        self.hypersonicSeries = hypersonicSeries
        self.megaSeries = megaSeries
        self.omegaSeries = omegaSeries
        self.transonicSeries = transonicSeries
        self.worldSeries = worldSeries
class EpisodeFull:
    def __init__(self, uid, title, titleGerman=None, titleItalian=None, titleJapanese=None, series=None, season=None, seasonNumber=None, episodeNumber=None, productionSerialNumber=None, featureLength=None, stardateFrom=None, stardateTo=None, yearFrom=None, yearTo=None, usAirDate=None, finalScriptDate=None, writers=None, teleplayAuthors=None, storyAuthors=None, directors=None, performers=None, stuntPerformers=None, standInPerformers=None, characters=None):
        """Full episode, returned when queried using UID
        Args:
            uid (string): Episode unique ID
            title (string): Episode title
            titleGerman (string): Episode title in German
            titleItalian (string): Episode title in Italian
            titleJapanese (string): Episode title in Japanese
            series (#/definitions/SeriesBase): Series this episode belongs to
            season (#/definitions/SeasonBase): Season this episode belongs to
            seasonNumber (integer): Season number
            episodeNumber (integer): Episode number in season
            productionSerialNumber (string): Production serial number
            featureLength (boolean): Whether it's a feature length episode
            stardateFrom (number): Starting stardate of episode story
            stardateTo (number): Ending stardate of episode story
            yearFrom (integer): Starting year of episode story
            yearTo (integer): Ending year of episode story
            usAirDate (string): Date the episode was first aired in the United States
            finalScriptDate (string): Date the episode script was completed
            writers (array): Writers involved in the episode
            teleplayAuthors (array): Teleplay authors involved in the episode
            storyAuthors (array): Story authors involved in the episode
            directors (array): Directors authors involved in the episode
            performers (array): Performers appearing in the episode
            stuntPerformers (array): Stunt performers appearing in the episode
            standInPerformers (array): Stand-in performers appearing in the episode
            characters (array): Characters appearing in the episode
        """
        self.uid = uid
        self.title = title
        self.titleGerman = titleGerman
        self.titleItalian = titleItalian
        self.titleJapanese = titleJapanese
        self.series = series
        self.season = season
        self.seasonNumber = seasonNumber
        self.episodeNumber = episodeNumber
        self.productionSerialNumber = productionSerialNumber
        self.featureLength = featureLength
        self.stardateFrom = stardateFrom
        self.stardateTo = stardateTo
        self.yearFrom = yearFrom
        self.yearTo = yearTo
        self.usAirDate = usAirDate
        self.finalScriptDate = finalScriptDate
        self.writers = writers
        self.teleplayAuthors = teleplayAuthors
        self.storyAuthors = storyAuthors
        self.directors = directors
        self.performers = performers
        self.stuntPerformers = stuntPerformers
        self.standInPerformers = standInPerformers
        self.characters = characters
class FoodFull:
    def __init__(self, uid, name, earthlyOrigin=None, dessert=None, fruit=None, herbOrSpice=None, sauce=None, soup=None, beverage=None, alcoholicBeverage=None, juice=None, tea=None):
        """Full food, returned when queried using UID
        Args:
            uid (string): Food unique ID
            name (string): Food name
            earthlyOrigin (boolean): Whether it's of earthly origin
            dessert (boolean): Whether it's a dessert
            fruit (boolean): Whether it's a fruit
            herbOrSpice (boolean): Whether it's an herb or a spice
            sauce (boolean): Whether it's a sauce
            soup (boolean): Whether it's a soup
            beverage (boolean): Whether it's a beverage
            alcoholicBeverage (boolean): Whether it's an alcoholic beverage
            juice (boolean): Whether it's a juice
            tea (boolean): Whether it's a tea
        """
        self.uid = uid
        self.name = name
        self.earthlyOrigin = earthlyOrigin
        self.dessert = dessert
        self.fruit = fruit
        self.herbOrSpice = herbOrSpice
        self.sauce = sauce
        self.soup = soup
        self.beverage = beverage
        self.alcoholicBeverage = alcoholicBeverage
        self.juice = juice
        self.tea = tea
class LiteratureFull:
    def __init__(self, uid, title, earthlyOrigin=None, shakespeareanWork=None, report=None, scientificLiterature=None, technicalManual=None, religiousLiterature=None):
        """Full literature, returned when queried using UID
        Args:
            uid (string): Literature unique ID
            title (string): Literature title
            earthlyOrigin (boolean): Whether it's of earthly origin
            shakespeareanWork (boolean): Whether it's a Shakespearean work
            report (boolean): Whether it's a report
            scientificLiterature (boolean): Whether it's a scientific literature
            technicalManual (boolean): Whether it's a technical manual
            religiousLiterature (boolean): Whether it's a religious literature
        """
        self.uid = uid
        self.title = title
        self.earthlyOrigin = earthlyOrigin
        self.shakespeareanWork = shakespeareanWork
        self.report = report
        self.scientificLiterature = scientificLiterature
        self.technicalManual = technicalManual
        self.religiousLiterature = religiousLiterature
class LocationFull:
    def __init__(self, uid, name, earthlyLocation=None, fictionalLocation=None, religiousLocation=None, geographicalLocation=None, bodyOfWater=None, country=None, subnationalEntity=None, settlement=None, usSettlement=None, bajoranSettlement=None, colony=None, landform=None, landmark=None, road=None, structure=None, shipyard=None, buildingInterior=None, establishment=None, medicalEstablishment=None, ds9Establishment=None, school=None, mirror=None, alternateReality=None):
        """Full location, returned when queried using UID
        Args:
            uid (string): Location unique ID
            name (string): Location name
            earthlyLocation (boolean): Whether it's an earthly location
            fictionalLocation (boolean): Whether it's a fictional location
            religiousLocation (boolean): Whether it's a religious location
            geographicalLocation (boolean): Whether it's a geographical location
            bodyOfWater (boolean): Whether it's a body of water
            country (boolean): Whether it's a country
            subnationalEntity (boolean): Whether it's a subnational entity
            settlement (boolean): Whether it's a settlement
            usSettlement (boolean): Whether it's a US settlement
            bajoranSettlement (boolean): Whether it's a Bajoran settlement
            colony (boolean): Whether it's a colony
            landform (boolean): Whether it's a landform
            landmark (boolean): Whether it's a landmark
            road (boolean): Whether it's a road
            structure (boolean): Whether it's a structure
            shipyard (boolean): Whether it's a shipyard
            buildingInterior (boolean): Whether it's a building interior
            establishment (boolean): Whether it's a establishment
            medicalEstablishment (boolean): Whether it's a medical establishment
            ds9Establishment (boolean): Whether it's a DS9 establishment
            school (boolean): Whether it's a school
            mirror (boolean): Whether this location is from mirror universe
            alternateReality (boolean): Whether this location is from alternate reality
        """
        self.uid = uid
        self.name = name
        self.earthlyLocation = earthlyLocation
        self.fictionalLocation = fictionalLocation
        self.religiousLocation = religiousLocation
        self.geographicalLocation = geographicalLocation
        self.bodyOfWater = bodyOfWater
        self.country = country
        self.subnationalEntity = subnationalEntity
        self.settlement = settlement
        self.usSettlement = usSettlement
        self.bajoranSettlement = bajoranSettlement
        self.colony = colony
        self.landform = landform
        self.landmark = landmark
        self.road = road
        self.structure = structure
        self.shipyard = shipyard
        self.buildingInterior = buildingInterior
        self.establishment = establishment
        self.medicalEstablishment = medicalEstablishment
        self.ds9Establishment = ds9Establishment
        self.school = school
        self.mirror = mirror
        self.alternateReality = alternateReality
class MagazineFull:
    def __init__(self, uid, title, publishedYear=None, publishedMonth=None, publishedDay=None, coverYear=None, coverMonth=None, coverDay=None, numberOfPages=None, issueNumber=None, magazineSeries=None, editors=None, publishers=None):
        """Full magazine, returned when queried using UID
        Args:
            uid (string): Magazine unique ID
            title (string): Magazine title
            publishedYear (integer): Year the magazine was published
            publishedMonth (integer): Month the magazine was published
            publishedDay (integer): Day the magazine was published
            coverYear (integer): Cover publication year
            coverMonth (integer): Cover publication month
            coverDay (integer): Cover publication day
            numberOfPages (integer): Number of pages
            issueNumber (string): Magazine issue number
            magazineSeries (array): Magazine series this magazine is included in
            editors (array): Editors involved in the magazine
            publishers (array): Magazine publishers
        """
        self.uid = uid
        self.title = title
        self.publishedYear = publishedYear
        self.publishedMonth = publishedMonth
        self.publishedDay = publishedDay
        self.coverYear = coverYear
        self.coverMonth = coverMonth
        self.coverDay = coverDay
        self.numberOfPages = numberOfPages
        self.issueNumber = issueNumber
        self.magazineSeries = magazineSeries
        self.editors = editors
        self.publishers = publishers
class MagazineSeriesFull:
    def __init__(self, uid, title, publishedYearFrom=None, publishedMonthFrom=None, publishedYearTo=None, publishedMonthTo=None, numberOfIssues=None, publishers=None, editors=None, magazines=None):
        """Full magazine series, returned when queried using UID
        Args:
            uid (string): Magazine series unique ID
            title (string): Magazine series title
            publishedYearFrom (integer): Year from which the magazine series was published
            publishedMonthFrom (integer): Month from which the magazine series was published
            publishedYearTo (integer): Year to which the magazine series was published
            publishedMonthTo (integer): Month to which the magazine series was published
            numberOfIssues (integer): Number of issues
            publishers (array): Companies that published this magazine series
            editors (array): Editors involved in the magazine series
            magazines (array): Magazines included in this magazine series
        """
        self.uid = uid
        self.title = title
        self.publishedYearFrom = publishedYearFrom
        self.publishedMonthFrom = publishedMonthFrom
        self.publishedYearTo = publishedYearTo
        self.publishedMonthTo = publishedMonthTo
        self.numberOfIssues = numberOfIssues
        self.publishers = publishers
        self.editors = editors
        self.magazines = magazines
class MaterialFull:
    def __init__(self, uid, name, chemicalCompound=None, biochemicalCompound=None, drug=None, poisonousSubstance=None, explosive=None, gemstone=None, alloyOrComposite=None, fuel=None, mineral=None, preciousMaterial=None):
        """Full material, returned when queried using UID
        Args:
            uid (string): Material unique ID
            name (string): Material name
            chemicalCompound (boolean): Whether it's a chemical compound
            biochemicalCompound (boolean): Whether it's a biochemical compound
            drug (boolean): Whether it's a drug
            poisonousSubstance (boolean): Whether it's a poisonous substance
            explosive (boolean): Whether it's an explosive
            gemstone (boolean): Whether it's a gemstone
            alloyOrComposite (boolean): Whether it's an alloy or a composite
            fuel (boolean): Whether it's a fuel
            mineral (boolean): Whether it's a mineral
            preciousMaterial (boolean): Whether it's a precious material
        """
        self.uid = uid
        self.name = name
        self.chemicalCompound = chemicalCompound
        self.biochemicalCompound = biochemicalCompound
        self.drug = drug
        self.poisonousSubstance = poisonousSubstance
        self.explosive = explosive
        self.gemstone = gemstone
        self.alloyOrComposite = alloyOrComposite
        self.fuel = fuel
        self.mineral = mineral
        self.preciousMaterial = preciousMaterial
class MedicalConditionFull:
    def __init__(self, uid, name, psychologicalCondition=None):
        """Full medical condition, returned when queried using UID
        Args:
            uid (string): Medical condition unique ID
            name (string): Medical condition name
            psychologicalCondition (boolean): Whether it's a psychological condition
        """
        self.uid = uid
        self.name = name
        self.psychologicalCondition = psychologicalCondition
class MovieFull:
    def __init__(self, uid, title, mainDirector=None, titleBulgarian=None, titleCatalan=None, titleChineseTraditional=None, titleGerman=None, titleItalian=None, titleJapanese=None, titlePolish=None, titleRussian=None, titleSerbian=None, titleSpanish=None, stardateFrom=None, stardateTo=None, yearFrom=None, yearTo=None, usReleaseDate=None, writers=None, screenplayAuthors=None, storyAuthors=None, directors=None, producers=None, staff=None, performers=None, stuntPerformers=None, standInPerformers=None, characters=None):
        """Full movie, returned when queried using UID
        Args:
            uid (string): Movie unique ID
            title (string): Movie title
            mainDirector (#/definitions/StaffBase): Director of the movie
            titleBulgarian (string): Movie title in Bulgarian
            titleCatalan (string): Movie title in Catalan
            titleChineseTraditional (string): Movie title in Chinese traditional
            titleGerman (string): Movie title in German
            titleItalian (string): Movie title in Italian
            titleJapanese (string): Movie title in Japanese
            titlePolish (string): Movie title in Polish
            titleRussian (string): Movie title in Russian
            titleSerbian (string): Movie title in Serbian
            titleSpanish (string): Movie title in Spanish
            stardateFrom (number): Starting stardate of movie story
            stardateTo (number): Ending stardate of movie story
            yearFrom (integer): Starting year of movie story
            yearTo (integer): Ending year of movie story
            usReleaseDate (string): Date the movie was first released in the United States
            writers (array): Writers involved in the movie
            screenplayAuthors (array): Screenplay authors involved in the movie
            storyAuthors (array): Story authors authors involved in the movie
            directors (array): Directors authors involved in the movie
            producers (array): Producers authors involved in the movie
            staff (array): Other staff involved in the movie
            performers (array): Performers appearing in the movie
            stuntPerformers (array): Stunt performers appearing in the movie
            standInPerformers (array): Stand-in performers appearing in the movie
            characters (array): Characters appearing in the movie
        """
        self.uid = uid
        self.title = title
        self.mainDirector = mainDirector
        self.titleBulgarian = titleBulgarian
        self.titleCatalan = titleCatalan
        self.titleChineseTraditional = titleChineseTraditional
        self.titleGerman = titleGerman
        self.titleItalian = titleItalian
        self.titleJapanese = titleJapanese
        self.titlePolish = titlePolish
        self.titleRussian = titleRussian
        self.titleSerbian = titleSerbian
        self.titleSpanish = titleSpanish
        self.stardateFrom = stardateFrom
        self.stardateTo = stardateTo
        self.yearFrom = yearFrom
        self.yearTo = yearTo
        self.usReleaseDate = usReleaseDate
        self.writers = writers
        self.screenplayAuthors = screenplayAuthors
        self.storyAuthors = storyAuthors
        self.directors = directors
        self.producers = producers
        self.staff = staff
        self.performers = performers
        self.stuntPerformers = stuntPerformers
        self.standInPerformers = standInPerformers
        self.characters = characters
class OccupationFull:
    def __init__(self, uid, name, legalOccupation=None, medicalOccupation=None, scientificOccupation=None, characters=None):
        """Full occupation, returned when queried using UID
        Args:
            uid (string): Occupation unique ID
            name (string): Occupation name
            legalOccupation (boolean): Whether it's a legal occupation
            medicalOccupation (boolean): Whether it's a medical occupation
            scientificOccupation (boolean): Whether it's a scientific occupation
            characters (array): Characters with this occupation
        """
        self.uid = uid
        self.name = name
        self.legalOccupation = legalOccupation
        self.medicalOccupation = medicalOccupation
        self.scientificOccupation = scientificOccupation
        self.characters = characters
class OrganizationFull:
    def __init__(self, uid, name, government=None, intergovernmentalOrganization=None, researchOrganization=None, sportOrganization=None, medicalOrganization=None, militaryOrganization=None, militaryUnit=None, governmentAgency=None, lawEnforcementAgency=None, prisonOrPenalColony=None, mirror=None, alternateReality=None, characters=None):
        """Full organization, returned when queried using UID
        Args:
            uid (string): Organization unique ID
            name (string): Organization name
            government (boolean): Whether it's a government
            intergovernmentalOrganization (boolean): Whether it's an intergovernmental organization
            researchOrganization (boolean): Whether it's a research organization
            sportOrganization (boolean): Whether it's a sport organization
            medicalOrganization (boolean): Whether it's a medical organization
            militaryOrganization (boolean): Whether it's a military organization
            militaryUnit (boolean): Whether it's a military unit
            governmentAgency (boolean): Whether it's a government agency
            lawEnforcementAgency (boolean): Whether it's a law enforcement agency
            prisonOrPenalColony (boolean): Whether it's a prison or penal colony
            mirror (boolean): Whether this organization is from mirror universe
            alternateReality (boolean): Whether this organization is from alternate reality
            characters (array): Characters belonging to this organization
        """
        self.uid = uid
        self.name = name
        self.government = government
        self.intergovernmentalOrganization = intergovernmentalOrganization
        self.researchOrganization = researchOrganization
        self.sportOrganization = sportOrganization
        self.medicalOrganization = medicalOrganization
        self.militaryOrganization = militaryOrganization
        self.militaryUnit = militaryUnit
        self.governmentAgency = governmentAgency
        self.lawEnforcementAgency = lawEnforcementAgency
        self.prisonOrPenalColony = prisonOrPenalColony
        self.mirror = mirror
        self.alternateReality = alternateReality
        self.characters = characters
class PerformerFull:
    def __init__(self, uid, name, birthName=None, gender=None, dateOfBirth=None, placeOfBirth=None, dateOfDeath=None, placeOfDeath=None, animalPerformer=None, disPerformer=None, ds9Performer=None, entPerformer=None, filmPerformer=None, standInPerformer=None, stuntPerformer=None, tasPerformer=None, tngPerformer=None, tosPerformer=None, videoGamePerformer=None, voicePerformer=None, voyPerformer=None, episodesPerformances=None, episodesStuntPerformances=None, episodesStandInPerformances=None, moviesPerformances=None, moviesStuntPerformances=None, moviesStandInPerformances=None, characters=None):
        """Full performer, returned when queried using UID
        Args:
            uid (string): Performer unique ID
            name (string): Performer name
            birthName (string): Performer birth name
            gender (#/definitions/Gender): Performer gender
            dateOfBirth (string): Date the performer was born
            placeOfBirth (string): Place the performer was born
            dateOfDeath (string): Date the performer died
            placeOfDeath (string): Place the performer died
            animalPerformer (boolean): Whether it's an animal performer
            disPerformer (boolean): Whether it's a performer that appeared in Star Trek: Discovery
            ds9Performer (boolean): Whether it's a performer that appeared in Star Trek: Deep Space Nine
            entPerformer (boolean): Whether it's a performer that appeared in Star Trek: Enterprise
            filmPerformer (boolean): Whether it's a performer that appeared in a Star Trek movie
            standInPerformer (boolean): Whether it's a stand-in performer
            stuntPerformer (boolean): Whether it's a stunt performer
            tasPerformer (boolean): Whether it's a performer that appeared in Star Trek: The Animated Series
            tngPerformer (boolean): Whether it's a performer that appeared in Star Trek: The Next Generation
            tosPerformer (boolean): Whether it's a performer that appeared in Star Trek: The Original Series
            videoGamePerformer (boolean): Whether it's a video game performer
            voicePerformer (boolean): Whether it's a voice performer
            voyPerformer (boolean): Whether it's a performer that appeared in Star Trek: Voyager
            episodesPerformances (array): Episodes in which this person appeared as a performer
            episodesStuntPerformances (array): Episodes in which this person appeared as a stunt performer
            episodesStandInPerformances (array): Episodes in which this person appeared as a stand-in performer
            moviesPerformances (array): Movies in which this person appeared as a performer
            moviesStuntPerformances (array): Movies in which this person appeared as a stunt performer
            moviesStandInPerformances (array): Movies in which this person appeared as a stand-in performer
            characters (array): Characters played by this performer
        """
        self.uid = uid
        self.name = name
        self.birthName = birthName
        self.gender = gender
        self.dateOfBirth = dateOfBirth
        self.placeOfBirth = placeOfBirth
        self.dateOfDeath = dateOfDeath
        self.placeOfDeath = placeOfDeath
        self.animalPerformer = animalPerformer
        self.disPerformer = disPerformer
        self.ds9Performer = ds9Performer
        self.entPerformer = entPerformer
        self.filmPerformer = filmPerformer
        self.standInPerformer = standInPerformer
        self.stuntPerformer = stuntPerformer
        self.tasPerformer = tasPerformer
        self.tngPerformer = tngPerformer
        self.tosPerformer = tosPerformer
        self.videoGamePerformer = videoGamePerformer
        self.voicePerformer = voicePerformer
        self.voyPerformer = voyPerformer
        self.episodesPerformances = episodesPerformances
        self.episodesStuntPerformances = episodesStuntPerformances
        self.episodesStandInPerformances = episodesStandInPerformances
        self.moviesPerformances = moviesPerformances
        self.moviesStuntPerformances = moviesStuntPerformances
        self.moviesStandInPerformances = moviesStandInPerformances
        self.characters = characters
class SeasonFull:
    def __init__(self, uid, title, series=None, seasonNumber=None, numberOfEpisodes=None, episodes=None):
        """Full location, returned when queried using UID
        Args:
            uid (string): Season unique ID
            title (string): Season title
            series (#/definitions/SeriesBase): Series this season belongs to
            seasonNumber (integer): Season number in series
            numberOfEpisodes (integer): Number of episodes in this season
            episodes (array): Episodes in this season
        """
        self.uid = uid
        self.title = title
        self.series = series
        self.seasonNumber = seasonNumber
        self.numberOfEpisodes = numberOfEpisodes
        self.episodes = episodes
class SeriesFull:
    def __init__(self, uid, title, abbreviation, productionStartYear=None, productionEndYear=None, originalRunStartDate=None, originalRunEndDate=None, seasonsCount=None, episodesCount=None, featureLengthEpisodesCount=None, productionCompany=None, originalBroadcaster=None, episodes=None, seasons=None):
        """Full series, returned when queried using UID
        Args:
            uid (string): Series unique ID
            title (string): Series title
            abbreviation (string): Series abbreviation
            productionStartYear (integer): Year the series production started
            productionEndYear (integer): Year the series production ended
            originalRunStartDate (string): Date the series originally ran from
            originalRunEndDate (string): Date the series originally ran to
            seasonsCount (integer): Number of seasons
            episodesCount (integer): Number of episodes
            featureLengthEpisodesCount (integer): Number of feature length episodes
            productionCompany (#/definitions/CompanyBase): Company that produced the series
            originalBroadcaster (#/definitions/CompanyBase): Company that originally broadcasted the series
            episodes (array): Episodes in the series
            seasons (array): Seasons in the series
        """
        self.uid = uid
        self.title = title
        self.abbreviation = abbreviation
        self.productionStartYear = productionStartYear
        self.productionEndYear = productionEndYear
        self.originalRunStartDate = originalRunStartDate
        self.originalRunEndDate = originalRunEndDate
        self.seasonsCount = seasonsCount
        self.episodesCount = episodesCount
        self.featureLengthEpisodesCount = featureLengthEpisodesCount
        self.productionCompany = productionCompany
        self.originalBroadcaster = originalBroadcaster
        self.episodes = episodes
        self.seasons = seasons
class SoundtrackFull:
    def __init__(self, uid, title, releaseDate=None, length=None, labels=None, composers=None, contributors=None, orchestrators=None, references=None):
        """Full soundtrack, returned when queried using UID
        Args:
            uid (string): Soundtrack unique ID
            title (string): Soundtrack title
            releaseDate (string): Release date
            length (integer): Length, in seconds
            labels (array): Labels this soundtrack was relesed by
            composers (array): Composers
            contributors (array): Other musicians that contributed to this soundtrack
            orchestrators (array): Orchestrators
            references (array): References
        """
        self.uid = uid
        self.title = title
        self.releaseDate = releaseDate
        self.length = length
        self.labels = labels
        self.composers = composers
        self.contributors = contributors
        self.orchestrators = orchestrators
        self.references = references
class SpacecraftFull:
    def __init__(self, uid, name, registry=None, status=None, dateStatus=None, spacecraftClass=None, owner=None, operator=None, spacecraftTypes=None):
        """Full spacecraft, returned when queried using UID
        Args:
            uid (string): Spacecraft unique ID
            name (string): Spacecraft name
            registry (string): Spacecraft registry
            status (string): Status of a spacecraft (in prime reality, if spacecraft was in more than one realities)
            dateStatus (string): Date the spacecraft status was last known
            spacecraftClass (#/definitions/SpacecraftClassBase): Spacecraft class
            owner (#/definitions/OrganizationBase): Owner
            operator (#/definitions/OrganizationBase): Operator
            spacecraftTypes (array): Spacecraft types
        """
        self.uid = uid
        self.name = name
        self.registry = registry
        self.status = status
        self.dateStatus = dateStatus
        self.spacecraftClass = spacecraftClass
        self.owner = owner
        self.operator = operator
        self.spacecraftTypes = spacecraftTypes
class SpacecraftClassFull:
    def __init__(self, uid, name, numberOfDecks=None, warpCapable=None, alternateReality=None, activeFrom=None, activeTo=None, species=None, owner=None, operator=None, affiliation=None, spacecraftTypes=None, spacecrafts=None):
        """Full spacecraft class, returned when queried using UID
        Args:
            uid (string): Spacecraft class unique ID
            name (string): Spacecraft class name
            numberOfDecks (integer): Number of decks
            warpCapable (boolean): Whether it's a warp-capable spacecraft class
            alternateReality (boolean): Whether this spacecraft class is from alternate reality
            activeFrom (string): Starting period when this spacecraft class was in use
            activeTo (string): Ending period when this spacecraft class was in use
            species (#/definitions/SpeciesHeader): Main species affiliated
            owner (#/definitions/OrganizationBase): Owner
            operator (#/definitions/OrganizationBase): Operator
            affiliation (#/definitions/OrganizationBase): Affiliation
            spacecraftTypes (array): Spacecraft types
            spacecrafts (array): Spacecrafts
        """
        self.uid = uid
        self.name = name
        self.numberOfDecks = numberOfDecks
        self.warpCapable = warpCapable
        self.alternateReality = alternateReality
        self.activeFrom = activeFrom
        self.activeTo = activeTo
        self.species = species
        self.owner = owner
        self.operator = operator
        self.affiliation = affiliation
        self.spacecraftTypes = spacecraftTypes
        self.spacecrafts = spacecrafts
class SpeciesFull:
    def __init__(self, uid, name, homeworld=None, quadrant=None, extinctSpecies=None, warpCapableSpecies=None, extraGalacticSpecies=None, humanoidSpecies=None, reptilianSpecies=None, nonCorporealSpecies=None, shapeshiftingSpecies=None, spaceborneSpecies=None, telepathicSpecies=None, transDimensionalSpecies=None, unnamedSpecies=None, alternateReality=None, characters=None):
        """Full species, returned when queried using UID
        Args:
            uid (string): Species unique ID
            name (string): Species name
            homeworld (#/definitions/AstronomicalObjectBase): Homeworld of the species
            quadrant (#/definitions/AstronomicalObjectBase): Quadrant the species originates from
            extinctSpecies (boolean): Whether it's an extinct species
            warpCapableSpecies (boolean): Whether it's a warp-capable species
            extraGalacticSpecies (boolean): Whether it's an extra-galactic species
            humanoidSpecies (boolean): Whether it's a humanoid species
            reptilianSpecies (boolean): Whether it's a reptilian species
            nonCorporealSpecies (boolean): Whether it's a non-corporeal species
            shapeshiftingSpecies (boolean): Whether it's a shapeshifting species
            spaceborneSpecies (boolean): Whether it's a spaceborne species
            telepathicSpecies (boolean): Whether it's a telepathic species
            transDimensionalSpecies (boolean): Whether it's a trans-dimensional species
            unnamedSpecies (boolean): Whether it's a unnamed species
            alternateReality (boolean): Whether this species is from alternate reality
            characters (array): Characters belonging to the species
        """
        self.uid = uid
        self.name = name
        self.homeworld = homeworld
        self.quadrant = quadrant
        self.extinctSpecies = extinctSpecies
        self.warpCapableSpecies = warpCapableSpecies
        self.extraGalacticSpecies = extraGalacticSpecies
        self.humanoidSpecies = humanoidSpecies
        self.reptilianSpecies = reptilianSpecies
        self.nonCorporealSpecies = nonCorporealSpecies
        self.shapeshiftingSpecies = shapeshiftingSpecies
        self.spaceborneSpecies = spaceborneSpecies
        self.telepathicSpecies = telepathicSpecies
        self.transDimensionalSpecies = transDimensionalSpecies
        self.unnamedSpecies = unnamedSpecies
        self.alternateReality = alternateReality
        self.characters = characters
class StaffFull:
    def __init__(self, uid, name, birthName=None, gender=None, dateOfBirth=None, placeOfBirth=None, dateOfDeath=None, placeOfDeath=None, artDepartment=None, artDirector=None, productionDesigner=None, cameraAndElectricalDepartment=None, cinematographer=None, castingDepartment=None, costumeDepartment=None, costumeDesigner=None, director=None, assistantOrSecondUnitDirector=None, exhibitAndAttractionStaff=None, filmEditor=None, linguist=None, locationStaff=None, makeupStaff=None, musicDepartment=None, composer=None, personalAssistant=None, producer=None, productionAssociate=None, productionStaff=None, publicationStaff=None, scienceConsultant=None, soundDepartment=None, specialAndVisualEffectsStaff=None, author=None, audioAuthor=None, calendarArtist=None, comicArtist=None, comicAuthor=None, comicColorArtist=None, comicInteriorArtist=None, comicInkArtist=None, comicPencilArtist=None, comicLetterArtist=None, comicStripArtist=None, gameArtist=None, gameAuthor=None, novelArtist=None, novelAuthor=None, referenceArtist=None, referenceAuthor=None, publicationArtist=None, publicationDesigner=None, publicationEditor=None, publicityArtist=None, cbsDigitalStaff=None, ilmProductionStaff=None, specialFeaturesStaff=None, storyEditor=None, studioExecutive=None, stuntDepartment=None, transportationDepartment=None, videoGameProductionStaff=None, writer=None, writtenEpisodes=None, teleplayAuthoredEpisodes=None, storyAuthoredEpisodes=None, directedEpisodes=None, episodes=None, writtenMovies=None, screenplayAuthoredMovies=None, storyAuthoredMovies=None, directedMovies=None, producedMovies=None, movies=None):
        """Full staff, returned when queried using UID
        Args:
            uid (string): Staff unique ID
            name (string): Staff name
            birthName (string): Staff birth name
            gender (#/definitions/Gender): Staff gender
            dateOfBirth (string): Date the staff was born
            placeOfBirth (string): Place the staff was born
            dateOfDeath (string): Date the staff died
            placeOfDeath (string): Place the staff died
            artDepartment (boolean): Whether this person is from art department
            artDirector (boolean): Whether this person is an art director
            productionDesigner (boolean): Whether this person is a production designer
            cameraAndElectricalDepartment (boolean): Whether this person is from camera and electrical department
            cinematographer (boolean): Whether this person is a cinematographer
            castingDepartment (boolean): Whether this person is from casting department
            costumeDepartment (boolean): Whether this person is from costume department
            costumeDesigner (boolean): Whether this person is a custume designer
            director (boolean): Whether this person is a director
            assistantOrSecondUnitDirector (boolean): Whether this person is an assistant or secound unit director director
            exhibitAndAttractionStaff (boolean): Whether this person is an exhibit and attraction staff
            filmEditor (boolean): Whether this person is a film editor
            linguist (boolean): Whether this person is a linguist
            locationStaff (boolean): Whether this person is a location staff
            makeupStaff (boolean): Whether this person is a make-up staff
            musicDepartment (boolean): Whether this person is from music department
            composer (boolean): Whether this person is a composer
            personalAssistant (boolean): Whether this person is a personal assistant
            producer (boolean): Whether this person is a producer
            productionAssociate (boolean): Whether this person is a production associate
            productionStaff (boolean): Whether this person is a production staff
            publicationStaff (boolean): Whether this person is a publication staff
            scienceConsultant (boolean): Whether this person is a science consultant
            soundDepartment (boolean): Whether this person is from sound department
            specialAndVisualEffectsStaff (boolean): Whether this person is a special and visual effects staff
            author (boolean): Whether this person is an author
            audioAuthor (boolean): Whether this person is an audio author
            calendarArtist (boolean): Whether this person is a calendar artist
            comicArtist (boolean): Whether this person is a comic artist
            comicAuthor (boolean): Whether this person is a comic author
            comicColorArtist (boolean): Whether this person is a comic color artist
            comicInteriorArtist (boolean): Whether this person is a comic interior artist
            comicInkArtist (boolean): Whether this person is a comic ink artist
            comicPencilArtist (boolean): Whether this person is a comic pencil artist
            comicLetterArtist (boolean): Whether this person is a comic letter artist
            comicStripArtist (boolean): Whether this person is a comic strip artist
            gameArtist (boolean): Whether this person is a game artist
            gameAuthor (boolean): Whether this person is a game author
            novelArtist (boolean): Whether this person is a novel artist
            novelAuthor (boolean): Whether this person is a novel author
            referenceArtist (boolean): Whether this person is a reference artist
            referenceAuthor (boolean): Whether this person is a reference author
            publicationArtist (boolean): Whether this person is a publication artist
            publicationDesigner (boolean): Whether this person is a publication designer
            publicationEditor (boolean): Whether this person is a publication editor
            publicityArtist (boolean): Whether this person is a publicity artist
            cbsDigitalStaff (boolean): Whether this person is a part of CBS digital staff
            ilmProductionStaff (boolean): Whether this person is a part of ILM production staff
            specialFeaturesStaff (boolean): Whether this person is a special features artist
            storyEditor (boolean): Whether this person is a story editor
            studioExecutive (boolean): Whether this person is a studio executive
            stuntDepartment (boolean): Whether this person is from stunt department
            transportationDepartment (boolean): Whether this person is from transportation department
            videoGameProductionStaff (boolean): Whether this person is video game production staff
            writer (boolean): Whether this person is a writer
            writtenEpisodes (array): Episodes written by this person
            teleplayAuthoredEpisodes (array): Episodes to which this person has written teleplay
            storyAuthoredEpisodes (array): Episodes to which this person has written story
            directedEpisodes (array): Episodes directed by this person
            episodes (array): Episodes on which this person worked
            writtenMovies (array): Movies written by this person
            screenplayAuthoredMovies (array): Movies to which this person has written screenplay
            storyAuthoredMovies (array): Movies to which this person has written story
            directedMovies (array): Movies directed by this person
            producedMovies (array): Movies produced by this person
            movies (array): Movies on which this person worked
        """
        self.uid = uid
        self.name = name
        self.birthName = birthName
        self.gender = gender
        self.dateOfBirth = dateOfBirth
        self.placeOfBirth = placeOfBirth
        self.dateOfDeath = dateOfDeath
        self.placeOfDeath = placeOfDeath
        self.artDepartment = artDepartment
        self.artDirector = artDirector
        self.productionDesigner = productionDesigner
        self.cameraAndElectricalDepartment = cameraAndElectricalDepartment
        self.cinematographer = cinematographer
        self.castingDepartment = castingDepartment
        self.costumeDepartment = costumeDepartment
        self.costumeDesigner = costumeDesigner
        self.director = director
        self.assistantOrSecondUnitDirector = assistantOrSecondUnitDirector
        self.exhibitAndAttractionStaff = exhibitAndAttractionStaff
        self.filmEditor = filmEditor
        self.linguist = linguist
        self.locationStaff = locationStaff
        self.makeupStaff = makeupStaff
        self.musicDepartment = musicDepartment
        self.composer = composer
        self.personalAssistant = personalAssistant
        self.producer = producer
        self.productionAssociate = productionAssociate
        self.productionStaff = productionStaff
        self.publicationStaff = publicationStaff
        self.scienceConsultant = scienceConsultant
        self.soundDepartment = soundDepartment
        self.specialAndVisualEffectsStaff = specialAndVisualEffectsStaff
        self.author = author
        self.audioAuthor = audioAuthor
        self.calendarArtist = calendarArtist
        self.comicArtist = comicArtist
        self.comicAuthor = comicAuthor
        self.comicColorArtist = comicColorArtist
        self.comicInteriorArtist = comicInteriorArtist
        self.comicInkArtist = comicInkArtist
        self.comicPencilArtist = comicPencilArtist
        self.comicLetterArtist = comicLetterArtist
        self.comicStripArtist = comicStripArtist
        self.gameArtist = gameArtist
        self.gameAuthor = gameAuthor
        self.novelArtist = novelArtist
        self.novelAuthor = novelAuthor
        self.referenceArtist = referenceArtist
        self.referenceAuthor = referenceAuthor
        self.publicationArtist = publicationArtist
        self.publicationDesigner = publicationDesigner
        self.publicationEditor = publicationEditor
        self.publicityArtist = publicityArtist
        self.cbsDigitalStaff = cbsDigitalStaff
        self.ilmProductionStaff = ilmProductionStaff
        self.specialFeaturesStaff = specialFeaturesStaff
        self.storyEditor = storyEditor
        self.studioExecutive = studioExecutive
        self.stuntDepartment = stuntDepartment
        self.transportationDepartment = transportationDepartment
        self.videoGameProductionStaff = videoGameProductionStaff
        self.writer = writer
        self.writtenEpisodes = writtenEpisodes
        self.teleplayAuthoredEpisodes = teleplayAuthoredEpisodes
        self.storyAuthoredEpisodes = storyAuthoredEpisodes
        self.directedEpisodes = directedEpisodes
        self.episodes = episodes
        self.writtenMovies = writtenMovies
        self.screenplayAuthoredMovies = screenplayAuthoredMovies
        self.storyAuthoredMovies = storyAuthoredMovies
        self.directedMovies = directedMovies
        self.producedMovies = producedMovies
        self.movies = movies
class TechnologyFull:
    def __init__(self, uid, name, borgTechnology=None, borgComponent=None, communicationsTechnology=None, computerTechnology=None, computerProgramming=None, subroutine=None, database=None, energyTechnology=None, fictionalTechnology=None, holographicTechnology=None, identificationTechnology=None, lifeSupportTechnology=None, sensorTechnology=None, shieldTechnology=None, tool=None, culinaryTool=None, engineeringTool=None, householdTool=None, medicalEquipment=None, transporterTechnology=None):
        """Full technology, returned when queried using UID
        Args:
            uid (string): Technology unique ID
            name (string): Technology name
            borgTechnology (boolean): Whether it's a Borg technology
            borgComponent (boolean): Whether it's a Borg component
            communicationsTechnology (boolean): Whether it's a communications technology
            computerTechnology (boolean): Whether it's a computer technology
            computerProgramming (boolean): Whether it's a technology related to computer programming
            subroutine (boolean): Whether it's a subroutine
            database (boolean): Whether it's a database
            energyTechnology (boolean): Whether it's a energy technology
            fictionalTechnology (boolean): Whether it's a fictional technology
            holographicTechnology (boolean): Whether it's a holographic technology
            identificationTechnology (boolean): Whether it's a identification technology
            lifeSupportTechnology (boolean): Whether it's a life support technology
            sensorTechnology (boolean): Whether it's a sensor technology
            shieldTechnology (boolean): Whether it's a shield technology
            tool (boolean): Whether it's a tool
            culinaryTool (boolean): Whether it's a culinary tool
            engineeringTool (boolean): Whether it's a engineering tool
            householdTool (boolean): Whether it's a household tool
            medicalEquipment (boolean): Whether it's a medical equipment
            transporterTechnology (boolean): Whether it's a transporter technology
        """
        self.uid = uid
        self.name = name
        self.borgTechnology = borgTechnology
        self.borgComponent = borgComponent
        self.communicationsTechnology = communicationsTechnology
        self.computerTechnology = computerTechnology
        self.computerProgramming = computerProgramming
        self.subroutine = subroutine
        self.database = database
        self.energyTechnology = energyTechnology
        self.fictionalTechnology = fictionalTechnology
        self.holographicTechnology = holographicTechnology
        self.identificationTechnology = identificationTechnology
        self.lifeSupportTechnology = lifeSupportTechnology
        self.sensorTechnology = sensorTechnology
        self.shieldTechnology = shieldTechnology
        self.tool = tool
        self.culinaryTool = culinaryTool
        self.engineeringTool = engineeringTool
        self.householdTool = householdTool
        self.medicalEquipment = medicalEquipment
        self.transporterTechnology = transporterTechnology
class TitleFull:
    def __init__(self, uid, name, militaryRank=None, fleetRank=None, religiousTitle=None, position=None, mirror=None, characters=None):
        """Full title, returned when queried using UID
        Args:
            uid (string): Title unique ID
            name (string): Title name
            militaryRank (boolean): Whether it's a military rank
            fleetRank (boolean): Whether it's a fleet rank
            religiousTitle (boolean): Whether it's a religious title
            position (boolean): Whether it's a position
            mirror (boolean): Whether this title is from mirror universe
            characters (array): Characters that holds this title
        """
        self.uid = uid
        self.name = name
        self.militaryRank = militaryRank
        self.fleetRank = fleetRank
        self.religiousTitle = religiousTitle
        self.position = position
        self.mirror = mirror
        self.characters = characters
class TradingCardFull:
    def __init__(self, uid, name, tradingCardSet=None, tradingCardDeck=None, number=None, releaseYear=None, productionRun=None):
        """Full trading card, returned when queried using UID
        Args:
            uid (string): Trading card unique ID
            name (string): Trading card name
            tradingCardSet (#/definitions/TradingCardSetBase): Trading card set this card belongs to
            tradingCardDeck (#/definitions/TradingCardDeckBase): Trading card deck this card belongs to
            number (string): Trading card number
            releaseYear (integer): Release year, if set was releases over multiple years
            productionRun (integer): Production run, if different from trading card set production run
        """
        self.uid = uid
        self.name = name
        self.tradingCardSet = tradingCardSet
        self.tradingCardDeck = tradingCardDeck
        self.number = number
        self.releaseYear = releaseYear
        self.productionRun = productionRun
class TradingCardDeckFull:
    def __init__(self, uid, name, frequency=None, tradingCardSet=None, tradingCards=None):
        """Full trading card deck, returned when queried using UID
        Args:
            uid (string): Trading card deck unique ID
            name (string): Trading card deck name
            frequency (string): Frequency with which this deck occur in it's set
            tradingCardSet (#/definitions/TradingCardSetHeader): Trading card set this deck belongs to
            tradingCards (array): Trading cards in this deck
        """
        self.uid = uid
        self.name = name
        self.frequency = frequency
        self.tradingCardSet = tradingCardSet
        self.tradingCards = tradingCards
class TradingCardSetFull:
    def __init__(self, uid, name, releaseYear=None, releaseMonth=None, releaseDay=None, cardsPerPack=None, packsPerBox=None, boxesPerCase=None, productionRun=None, productionRunUnit=None, cardWidth=None, cardHeight=None, manufacturers=None, tradingCardDecks=None, tradingCards=None, countriesOfOrigin=None):
        """Full trading card set, returned when queried using UID
        Args:
            uid (string): Trading card set unique ID
            name (string): Trading card set name
            releaseYear (integer): Release year
            releaseMonth (integer): Release month
            releaseDay (integer): Release day
            cardsPerPack (integer): Cards per deck
            packsPerBox (integer): Packs per box
            boxesPerCase (integer): Boxes per case
            productionRun (integer): Production run
            productionRunUnit (#/definitions/ProductionRunUnit): Production run unit
            cardWidth (number): Card width, in inches
            cardHeight (number): Card height, in inches
            manufacturers (array): Manufacturers
            tradingCardDecks (array): Trading card decks in this set
            tradingCards (array): Trading cards in this set
            countriesOfOrigin (array): Countries of origin
        """
        self.uid = uid
        self.name = name
        self.releaseYear = releaseYear
        self.releaseMonth = releaseMonth
        self.releaseDay = releaseDay
        self.cardsPerPack = cardsPerPack
        self.packsPerBox = packsPerBox
        self.boxesPerCase = boxesPerCase
        self.productionRun = productionRun
        self.productionRunUnit = productionRunUnit
        self.cardWidth = cardWidth
        self.cardHeight = cardHeight
        self.manufacturers = manufacturers
        self.tradingCardDecks = tradingCardDecks
        self.tradingCards = tradingCards
        self.countriesOfOrigin = countriesOfOrigin
class VideoGameFull:
    def __init__(self, uid, title, releaseDate=None, stardateFrom=None, stardateTo=None, yearFrom=None, yearTo=None, systemRequirements=None, publishers=None, developers=None, platforms=None, genres=None, ratings=None, references=None):
        """Full video game, returned when queried using UID
        Args:
            uid (string): Video game unique ID
            title (string): Video game title
            releaseDate (string): Release date
            stardateFrom (number): Starting stardate of video game story
            stardateTo (number): Ending stardate of video game story
            yearFrom (integer): Starting year of video game story
            yearTo (integer): Ending year of video game story
            systemRequirements (string): System requirements
            publishers (array): Publishers
            developers (array): Developers
            platforms (array): Platforms
            genres (array): Genres
            ratings (array): Ratings
            references (array): References
        """
        self.uid = uid
        self.title = title
        self.releaseDate = releaseDate
        self.stardateFrom = stardateFrom
        self.stardateTo = stardateTo
        self.yearFrom = yearFrom
        self.yearTo = yearTo
        self.systemRequirements = systemRequirements
        self.publishers = publishers
        self.developers = developers
        self.platforms = platforms
        self.genres = genres
        self.ratings = ratings
        self.references = references
class VideoReleaseFull:
    def __init__(self, uid, title, series=None, season=None, format=None, numberOfEpisodes=None, numberOfFeatureLengthEpisodes=None, numberOfDataCarriers=None, runTime=None, yearFrom=None, yearTo=None, regionFreeReleaseDate=None, region1AReleaseDate=None, region1SlimlineReleaseDate=None, region2BReleaseDate=None, region2SlimlineReleaseDate=None, region4AReleaseDate=None, region4SlimlineReleaseDate=None, amazonDigitalRelease=None, dailymotionDigitalRelease=None, googlePlayDigitalRelease=None, iTunesDigitalRelease=None, ultraVioletDigitalRelease=None, vimeoDigitalRelease=None, vuduDigitalRelease=None, xboxSmartGlassDigitalRelease=None, youTubeDigitalRelease=None, netflixDigitalRelease=None, references=None, ratings=None, languages=None, languagesSubtitles=None, languagesDubbed=None):
        """Full video release, returned when queried using UID
        Args:
            uid (string): Video release unique ID
            title (string): Video release title
            series (#/definitions/SeriesBase): Series this video release is associated with
            season (#/definitions/SeasonBase): Season this video release is associated with
            format (#/definitions/VideoReleaseFormat): Video release format
            numberOfEpisodes (integer): Number of episodes
            numberOfFeatureLengthEpisodes (integer): Number of feature-length episodes
            numberOfDataCarriers (integer): Number of data carriers (like DVD, VCD, VHS etc.)
            runTime (integer): Run time, in minutes
            yearFrom (integer): Starting year of video release story
            yearTo (integer): Ending year of video release story
            regionFreeReleaseDate (string): Region free release date
            region1AReleaseDate (string): Region 1/A release date
            region1SlimlineReleaseDate (string): Region 1 slimline release date
            region2BReleaseDate (string): Region 2/B release date
            region2SlimlineReleaseDate (string): Region 2 slimline release date
            region4AReleaseDate (string): Region 4 release date
            region4SlimlineReleaseDate (string): Region 4 slimline release date
            amazonDigitalRelease (boolean): Whether this video has been release on Amazon.com
            dailymotionDigitalRelease (boolean): Whether this video has been release on Dailymotion
            googlePlayDigitalRelease (boolean): Whether this video has been release on Google Play
            iTunesDigitalRelease (boolean): Whether this video has been release on iTunes
            ultraVioletDigitalRelease (boolean): Whether this video has been release on UltraViolet
            vimeoDigitalRelease (boolean): Whether this video has been release on Vimeo
            vuduDigitalRelease (boolean): Whether this video has been release on VUDU
            xboxSmartGlassDigitalRelease (boolean): Whether this video has been release on Xbox SmartGlass
            youTubeDigitalRelease (boolean): Whether this video has been release on YouTube
            netflixDigitalRelease (boolean): Whether this video has been release on Netflix
            references (array): References
            ratings (array): Ratings
            languages (array): Languages of audio track
            languagesSubtitles (array): Languages of subtitles
            languagesDubbed (array): Languages that are available with dubbing
        """
        self.uid = uid
        self.title = title
        self.series = series
        self.season = season
        self.format = format
        self.numberOfEpisodes = numberOfEpisodes
        self.numberOfFeatureLengthEpisodes = numberOfFeatureLengthEpisodes
        self.numberOfDataCarriers = numberOfDataCarriers
        self.runTime = runTime
        self.yearFrom = yearFrom
        self.yearTo = yearTo
        self.regionFreeReleaseDate = regionFreeReleaseDate
        self.region1AReleaseDate = region1AReleaseDate
        self.region1SlimlineReleaseDate = region1SlimlineReleaseDate
        self.region2BReleaseDate = region2BReleaseDate
        self.region2SlimlineReleaseDate = region2SlimlineReleaseDate
        self.region4AReleaseDate = region4AReleaseDate
        self.region4SlimlineReleaseDate = region4SlimlineReleaseDate
        self.amazonDigitalRelease = amazonDigitalRelease
        self.dailymotionDigitalRelease = dailymotionDigitalRelease
        self.googlePlayDigitalRelease = googlePlayDigitalRelease
        self.iTunesDigitalRelease = iTunesDigitalRelease
        self.ultraVioletDigitalRelease = ultraVioletDigitalRelease
        self.vimeoDigitalRelease = vimeoDigitalRelease
        self.vuduDigitalRelease = vuduDigitalRelease
        self.xboxSmartGlassDigitalRelease = xboxSmartGlassDigitalRelease
        self.youTubeDigitalRelease = youTubeDigitalRelease
        self.netflixDigitalRelease = netflixDigitalRelease
        self.references = references
        self.ratings = ratings
        self.languages = languages
        self.languagesSubtitles = languagesSubtitles
        self.languagesDubbed = languagesDubbed
class WeaponFull:
    def __init__(self, uid, name, handHeldWeapon=None, laserTechnology=None, plasmaTechnology=None, photonicTechnology=None, phaserTechnology=None, mirror=None, alternateReality=None):
        """Full weapon, returned when queried using UID
        Args:
            uid (string): Weapon unique ID
            name (string): Weapon name
            handHeldWeapon (boolean): Whether it's a hand-help weapon
            laserTechnology (boolean): Whether it's a laser technology
            plasmaTechnology (boolean): Whether it's a plasma technology
            photonicTechnology (boolean): Whether it's a photonic technology
            phaserTechnology (boolean): Whether it's a phaser technology
            mirror (boolean): Whether this weapon is from mirror universe
            alternateReality (boolean): Whether this weapon is from alternate reality
        """
        self.uid = uid
        self.name = name
        self.handHeldWeapon = handHeldWeapon
        self.laserTechnology = laserTechnology
        self.plasmaTechnology = plasmaTechnology
        self.photonicTechnology = photonicTechnology
        self.phaserTechnology = phaserTechnology
        self.mirror = mirror
        self.alternateReality = alternateReality
