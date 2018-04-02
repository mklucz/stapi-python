from .common_search_criteria import *
class AnimalSearchCriteria(CommonSearchCriteria):
    def __init__(self, pageNumber, pageSize, sort, avian=None, canine=None, earthAnimal=None, earthInsect=None, feline=None, name=None):
        super(AnimalSearchCriteria, self).__init__(pageNumber, pageSize, sort)
        self.avian = avian
        self.canine = canine
        self.earthAnimal = earthAnimal
        self.earthInsect = earthInsect
        self.feline = feline
        self.name = name

class AstronomicalObjectSearchCriteria(CommonSearchCriteria):
    def __init__(self, pageNumber, pageSize, sort, astronomicalObjectType=None, locationUid=None, name=None):
        super(AstronomicalObjectSearchCriteria, self).__init__(pageNumber, pageSize, sort)
        self.astronomicalObjectType = astronomicalObjectType
        self.locationUid = locationUid
        self.name = name

class BookSearchCriteria(CommonSearchCriteria):
    def __init__(self, pageNumber, pageSize, sort, anthology=None, audiobook=None, audiobookAbridged=None, audiobookPublishedYearFrom=None, audiobookPublishedYearTo=None, audiobookRunTimeFrom=None, audiobookRunTimeTo=None, biographyBook=None, eBook=None, novel=None, novelization=None, numberOfPagesFrom=None, numberOfPagesTo=None, publishedYearFrom=None, publishedYearTo=None, referenceBook=None, rolePlayingBook=None, stardateFrom=None, stardateTo=None, title=None, yearFrom=None, yearTo=None):
        super(BookSearchCriteria, self).__init__(pageNumber, pageSize, sort)
        self.anthology = anthology
        self.audiobook = audiobook
        self.audiobookAbridged = audiobookAbridged
        self.audiobookPublishedYearFrom = audiobookPublishedYearFrom
        self.audiobookPublishedYearTo = audiobookPublishedYearTo
        self.audiobookRunTimeFrom = audiobookRunTimeFrom
        self.audiobookRunTimeTo = audiobookRunTimeTo
        self.biographyBook = biographyBook
        self.eBook = eBook
        self.novel = novel
        self.novelization = novelization
        self.numberOfPagesFrom = numberOfPagesFrom
        self.numberOfPagesTo = numberOfPagesTo
        self.publishedYearFrom = publishedYearFrom
        self.publishedYearTo = publishedYearTo
        self.referenceBook = referenceBook
        self.rolePlayingBook = rolePlayingBook
        self.stardateFrom = stardateFrom
        self.stardateTo = stardateTo
        self.title = title
        self.yearFrom = yearFrom
        self.yearTo = yearTo

class BookCollectionSearchCriteria(CommonSearchCriteria):
    def __init__(self, pageNumber, pageSize, sort, numberOfPagesFrom=None, numberOfPagesTo=None, publishedYearFrom=None, publishedYearTo=None, stardateFrom=None, stardateTo=None, title=None, yearFrom=None, yearTo=None):
        super(BookCollectionSearchCriteria, self).__init__(pageNumber, pageSize, sort)
        self.numberOfPagesFrom = numberOfPagesFrom
        self.numberOfPagesTo = numberOfPagesTo
        self.publishedYearFrom = publishedYearFrom
        self.publishedYearTo = publishedYearTo
        self.stardateFrom = stardateFrom
        self.stardateTo = stardateTo
        self.title = title
        self.yearFrom = yearFrom
        self.yearTo = yearTo

class BookSeriesSearchCriteria(CommonSearchCriteria):
    def __init__(self, pageNumber, pageSize, sort, eBookSeries=None, miniseries=None, numberOfBooksFrom=None, numberOfBooksTo=None, publishedYearFrom=None, publishedYearTo=None, title=None, yearFrom=None, yearTo=None):
        super(BookSeriesSearchCriteria, self).__init__(pageNumber, pageSize, sort)
        self.eBookSeries = eBookSeries
        self.miniseries = miniseries
        self.numberOfBooksFrom = numberOfBooksFrom
        self.numberOfBooksTo = numberOfBooksTo
        self.publishedYearFrom = publishedYearFrom
        self.publishedYearTo = publishedYearTo
        self.title = title
        self.yearFrom = yearFrom
        self.yearTo = yearTo

class CharacterSearchCriteria(CommonSearchCriteria):
    def __init__(self, pageNumber, pageSize, sort, alternateReality=None, deceased=None, fictionalCharacter=None, gender=None, hologram=None, mirror=None, name=None):
        super(CharacterSearchCriteria, self).__init__(pageNumber, pageSize, sort)
        self.alternateReality = alternateReality
        self.deceased = deceased
        self.fictionalCharacter = fictionalCharacter
        self.gender = gender
        self.hologram = hologram
        self.mirror = mirror
        self.name = name

class ComicCollectionSearchCriteria(CommonSearchCriteria):
    def __init__(self, pageNumber, pageSize, sort, numberOfPagesFrom=None, numberOfPagesTo=None, photonovel=None, publishedYearFrom=None, publishedYearTo=None, stardateFrom=None, stardateTo=None, title=None, yearFrom=None, yearTo=None):
        super(ComicCollectionSearchCriteria, self).__init__(pageNumber, pageSize, sort)
        self.numberOfPagesFrom = numberOfPagesFrom
        self.numberOfPagesTo = numberOfPagesTo
        self.photonovel = photonovel
        self.publishedYearFrom = publishedYearFrom
        self.publishedYearTo = publishedYearTo
        self.stardateFrom = stardateFrom
        self.stardateTo = stardateTo
        self.title = title
        self.yearFrom = yearFrom
        self.yearTo = yearTo

class ComicSeriesSearchCriteria(CommonSearchCriteria):
    def __init__(self, pageNumber, pageSize, sort, miniseries=None, numberOfIssuesFrom=None, numberOfIssuesTo=None, photonovelSeries=None, publishedYearFrom=None, publishedYearTo=None, stardateFrom=None, stardateTo=None, title=None, yearFrom=None, yearTo=None):
        super(ComicSeriesSearchCriteria, self).__init__(pageNumber, pageSize, sort)
        self.miniseries = miniseries
        self.numberOfIssuesFrom = numberOfIssuesFrom
        self.numberOfIssuesTo = numberOfIssuesTo
        self.photonovelSeries = photonovelSeries
        self.publishedYearFrom = publishedYearFrom
        self.publishedYearTo = publishedYearTo
        self.stardateFrom = stardateFrom
        self.stardateTo = stardateTo
        self.title = title
        self.yearFrom = yearFrom
        self.yearTo = yearTo

class ComicStripSearchCriteria(CommonSearchCriteria):
    def __init__(self, pageNumber, pageSize, sort, numberOfPagesFrom=None, numberOfPagesTo=None, publishedYearFrom=None, publishedYearTo=None, title=None, yearFrom=None, yearTo=None):
        super(ComicStripSearchCriteria, self).__init__(pageNumber, pageSize, sort)
        self.numberOfPagesFrom = numberOfPagesFrom
        self.numberOfPagesTo = numberOfPagesTo
        self.publishedYearFrom = publishedYearFrom
        self.publishedYearTo = publishedYearTo
        self.title = title
        self.yearFrom = yearFrom
        self.yearTo = yearTo

class ComicsSearchCriteria(CommonSearchCriteria):
    def __init__(self, pageNumber, pageSize, sort, adaptation=None, numberOfPagesFrom=None, numberOfPagesTo=None, photonovel=None, publishedYearFrom=None, publishedYearTo=None, stardateFrom=None, stardateTo=None, title=None, yearFrom=None, yearTo=None):
        super(ComicsSearchCriteria, self).__init__(pageNumber, pageSize, sort)
        self.adaptation = adaptation
        self.numberOfPagesFrom = numberOfPagesFrom
        self.numberOfPagesTo = numberOfPagesTo
        self.photonovel = photonovel
        self.publishedYearFrom = publishedYearFrom
        self.publishedYearTo = publishedYearTo
        self.stardateFrom = stardateFrom
        self.stardateTo = stardateTo
        self.title = title
        self.yearFrom = yearFrom
        self.yearTo = yearTo

class CompanySearchCriteria(CommonSearchCriteria):
    def __init__(self, pageNumber, pageSize, sort, broadcaster=None, collectibleCompany=None, conglomerate=None, digitalVisualEffectsCompany=None, distributor=None, filmEquipmentCompany=None, gameCompany=None, makeUpEffectsStudio=None, mattePaintingCompany=None, modelAndMiniatureEffectsCompany=None, name=None, postProductionCompany=None, productionCompany=None, propCompany=None, recordLabel=None, specialEffectsCompany=None, tvAndFilmProductionCompany=None, videoGameCompany=None):
        super(CompanySearchCriteria, self).__init__(pageNumber, pageSize, sort)
        self.broadcaster = broadcaster
        self.collectibleCompany = collectibleCompany
        self.conglomerate = conglomerate
        self.digitalVisualEffectsCompany = digitalVisualEffectsCompany
        self.distributor = distributor
        self.filmEquipmentCompany = filmEquipmentCompany
        self.gameCompany = gameCompany
        self.makeUpEffectsStudio = makeUpEffectsStudio
        self.mattePaintingCompany = mattePaintingCompany
        self.modelAndMiniatureEffectsCompany = modelAndMiniatureEffectsCompany
        self.name = name
        self.postProductionCompany = postProductionCompany
        self.productionCompany = productionCompany
        self.propCompany = propCompany
        self.recordLabel = recordLabel
        self.specialEffectsCompany = specialEffectsCompany
        self.tvAndFilmProductionCompany = tvAndFilmProductionCompany
        self.videoGameCompany = videoGameCompany

class ConflictSearchCriteria(CommonSearchCriteria):
    def __init__(self, pageNumber, pageSize, sort, alternateReality=None, dominionWarBattle=None, earthConflict=None, federationWar=None, klingonWar=None, name=None, yearFrom=None, yearTo=None):
        super(ConflictSearchCriteria, self).__init__(pageNumber, pageSize, sort)
        self.alternateReality = alternateReality
        self.dominionWarBattle = dominionWarBattle
        self.earthConflict = earthConflict
        self.federationWar = federationWar
        self.klingonWar = klingonWar
        self.name = name
        self.yearFrom = yearFrom
        self.yearTo = yearTo

class ElementSearchCriteria(CommonSearchCriteria):
    def __init__(self, pageNumber, pageSize, sort, gammaSeries=None, hypersonicSeries=None, megaSeries=None, name=None, omegaSeries=None, symbol=None, transonicSeries=None, transuranium=None, worldSeries=None):
        super(ElementSearchCriteria, self).__init__(pageNumber, pageSize, sort)
        self.gammaSeries = gammaSeries
        self.hypersonicSeries = hypersonicSeries
        self.megaSeries = megaSeries
        self.name = name
        self.omegaSeries = omegaSeries
        self.symbol = symbol
        self.transonicSeries = transonicSeries
        self.transuranium = transuranium
        self.worldSeries = worldSeries

class EpisodeSearchCriteria(CommonSearchCriteria):
    def __init__(self, pageNumber, pageSize, sort, episodeNumberFrom=None, episodeNumberTo=None, featureLength=None, finalScriptDateFrom=None, finalScriptDateTo=None, productionSerialNumber=None, seasonNumberFrom=None, seasonNumberTo=None, stardateFrom=None, stardateTo=None, title=None, usAirDateFrom=None, usAirDateTo=None, yearFrom=None, yearTo=None):
        super(EpisodeSearchCriteria, self).__init__(pageNumber, pageSize, sort)
        self.episodeNumberFrom = episodeNumberFrom
        self.episodeNumberTo = episodeNumberTo
        self.featureLength = featureLength
        self.finalScriptDateFrom = finalScriptDateFrom
        self.finalScriptDateTo = finalScriptDateTo
        self.productionSerialNumber = productionSerialNumber
        self.seasonNumberFrom = seasonNumberFrom
        self.seasonNumberTo = seasonNumberTo
        self.stardateFrom = stardateFrom
        self.stardateTo = stardateTo
        self.title = title
        self.usAirDateFrom = usAirDateFrom
        self.usAirDateTo = usAirDateTo
        self.yearFrom = yearFrom
        self.yearTo = yearTo

class FoodSearchCriteria(CommonSearchCriteria):
    def __init__(self, pageNumber, pageSize, sort, alcoholicBeverage=None, beverage=None, dessert=None, earthlyOrigin=None, fruit=None, herbOrSpice=None, juice=None, name=None, sauce=None, soup=None, tea=None):
        super(FoodSearchCriteria, self).__init__(pageNumber, pageSize, sort)
        self.alcoholicBeverage = alcoholicBeverage
        self.beverage = beverage
        self.dessert = dessert
        self.earthlyOrigin = earthlyOrigin
        self.fruit = fruit
        self.herbOrSpice = herbOrSpice
        self.juice = juice
        self.name = name
        self.sauce = sauce
        self.soup = soup
        self.tea = tea

class LiteratureSearchCriteria(CommonSearchCriteria):
    def __init__(self, pageNumber, pageSize, sort, earthlyOrigin=None, religiousLiterature=None, report=None, scientificLiterature=None, shakespeareanWork=None, technicalManual=None, title=None):
        super(LiteratureSearchCriteria, self).__init__(pageNumber, pageSize, sort)
        self.earthlyOrigin = earthlyOrigin
        self.religiousLiterature = religiousLiterature
        self.report = report
        self.scientificLiterature = scientificLiterature
        self.shakespeareanWork = shakespeareanWork
        self.technicalManual = technicalManual
        self.title = title

class LocationSearchCriteria(CommonSearchCriteria):
    def __init__(self, pageNumber, pageSize, sort, alternateReality=None, bajoranSettlement=None, bodyOfWater=None, buildingInterior=None, colony=None, country=None, ds9Establishment=None, earthlyLocation=None, establishment=None, fictionalLocation=None, geographicalLocation=None, landform=None, landmark=None, medicalEstablishment=None, mirror=None, name=None, religiousLocation=None, road=None, school=None, settlement=None, shipyard=None, structure=None, subnationalEntity=None, usSettlement=None):
        super(LocationSearchCriteria, self).__init__(pageNumber, pageSize, sort)
        self.alternateReality = alternateReality
        self.bajoranSettlement = bajoranSettlement
        self.bodyOfWater = bodyOfWater
        self.buildingInterior = buildingInterior
        self.colony = colony
        self.country = country
        self.ds9Establishment = ds9Establishment
        self.earthlyLocation = earthlyLocation
        self.establishment = establishment
        self.fictionalLocation = fictionalLocation
        self.geographicalLocation = geographicalLocation
        self.landform = landform
        self.landmark = landmark
        self.medicalEstablishment = medicalEstablishment
        self.mirror = mirror
        self.name = name
        self.religiousLocation = religiousLocation
        self.road = road
        self.school = school
        self.settlement = settlement
        self.shipyard = shipyard
        self.structure = structure
        self.subnationalEntity = subnationalEntity
        self.usSettlement = usSettlement

class MagazineSearchCriteria(CommonSearchCriteria):
    def __init__(self, pageNumber, pageSize, sort, numberOfPagesFrom=None, numberOfPagesTo=None, publishedYearFrom=None, publishedYearTo=None, title=None):
        super(MagazineSearchCriteria, self).__init__(pageNumber, pageSize, sort)
        self.numberOfPagesFrom = numberOfPagesFrom
        self.numberOfPagesTo = numberOfPagesTo
        self.publishedYearFrom = publishedYearFrom
        self.publishedYearTo = publishedYearTo
        self.title = title

class MagazineSeriesSearchCriteria(CommonSearchCriteria):
    def __init__(self, pageNumber, pageSize, sort, numberOfIssuesFrom=None, numberOfIssuesTo=None, publishedYearFrom=None, publishedYearTo=None, title=None):
        super(MagazineSeriesSearchCriteria, self).__init__(pageNumber, pageSize, sort)
        self.numberOfIssuesFrom = numberOfIssuesFrom
        self.numberOfIssuesTo = numberOfIssuesTo
        self.publishedYearFrom = publishedYearFrom
        self.publishedYearTo = publishedYearTo
        self.title = title

class MaterialSearchCriteria(CommonSearchCriteria):
    def __init__(self, pageNumber, pageSize, sort, alloyOrComposite=None, biochemicalCompound=None, chemicalCompound=None, drug=None, explosive=None, fuel=None, gemstone=None, mineral=None, name=None, poisonousSubstance=None, preciousMaterial=None):
        super(MaterialSearchCriteria, self).__init__(pageNumber, pageSize, sort)
        self.alloyOrComposite = alloyOrComposite
        self.biochemicalCompound = biochemicalCompound
        self.chemicalCompound = chemicalCompound
        self.drug = drug
        self.explosive = explosive
        self.fuel = fuel
        self.gemstone = gemstone
        self.mineral = mineral
        self.name = name
        self.poisonousSubstance = poisonousSubstance
        self.preciousMaterial = preciousMaterial

class MedicalConditionSearchCriteria(CommonSearchCriteria):
    def __init__(self, pageNumber, pageSize, sort, name=None, psychologicalCondition=None):
        super(MedicalConditionSearchCriteria, self).__init__(pageNumber, pageSize, sort)
        self.name = name
        self.psychologicalCondition = psychologicalCondition

class MovieSearchCriteria(CommonSearchCriteria):
    def __init__(self, pageNumber, pageSize, sort, stardateFrom=None, stardateTo=None, title=None, usReleaseDateFrom=None, usReleaseDateTo=None, yearFrom=None, yearTo=None):
        super(MovieSearchCriteria, self).__init__(pageNumber, pageSize, sort)
        self.stardateFrom = stardateFrom
        self.stardateTo = stardateTo
        self.title = title
        self.usReleaseDateFrom = usReleaseDateFrom
        self.usReleaseDateTo = usReleaseDateTo
        self.yearFrom = yearFrom
        self.yearTo = yearTo

class OccupationSearchCriteria(CommonSearchCriteria):
    def __init__(self, pageNumber, pageSize, sort, legalOccupation=None, medicalOccupation=None, name=None, scientificOccupation=None):
        super(OccupationSearchCriteria, self).__init__(pageNumber, pageSize, sort)
        self.legalOccupation = legalOccupation
        self.medicalOccupation = medicalOccupation
        self.name = name
        self.scientificOccupation = scientificOccupation

class OrganizationSearchCriteria(CommonSearchCriteria):
    def __init__(self, pageNumber, pageSize, sort, alternateReality=None, government=None, governmentAgency=None, intergovernmentalOrganization=None, lawEnforcementAgency=None, medicalOrganization=None, militaryOrganization=None, militaryUnit=None, mirror=None, name=None, prisonOrPenalColony=None, researchOrganization=None, sportOrganization=None):
        super(OrganizationSearchCriteria, self).__init__(pageNumber, pageSize, sort)
        self.alternateReality = alternateReality
        self.government = government
        self.governmentAgency = governmentAgency
        self.intergovernmentalOrganization = intergovernmentalOrganization
        self.lawEnforcementAgency = lawEnforcementAgency
        self.medicalOrganization = medicalOrganization
        self.militaryOrganization = militaryOrganization
        self.militaryUnit = militaryUnit
        self.mirror = mirror
        self.name = name
        self.prisonOrPenalColony = prisonOrPenalColony
        self.researchOrganization = researchOrganization
        self.sportOrganization = sportOrganization

class PerformerSearchCriteria(CommonSearchCriteria):
    def __init__(self, pageNumber, pageSize, sort, animalPerformer=None, birthName=None, dateOfBirthFrom=None, dateOfBirthTo=None, dateOfDeathFrom=None, dateOfDeathTo=None, disPerformer=None, ds9Performer=None, entPerformer=None, filmPerformer=None, gender=None, name=None, placeOfBirth=None, placeOfDeath=None, standInPerformer=None, stuntPerformer=None, tasPerformer=None, tngPerformer=None, tosPerformer=None, videoGamePerformer=None, voicePerformer=None, voyPerformer=None):
        super(PerformerSearchCriteria, self).__init__(pageNumber, pageSize, sort)
        self.animalPerformer = animalPerformer
        self.birthName = birthName
        self.dateOfBirthFrom = dateOfBirthFrom
        self.dateOfBirthTo = dateOfBirthTo
        self.dateOfDeathFrom = dateOfDeathFrom
        self.dateOfDeathTo = dateOfDeathTo
        self.disPerformer = disPerformer
        self.ds9Performer = ds9Performer
        self.entPerformer = entPerformer
        self.filmPerformer = filmPerformer
        self.gender = gender
        self.name = name
        self.placeOfBirth = placeOfBirth
        self.placeOfDeath = placeOfDeath
        self.standInPerformer = standInPerformer
        self.stuntPerformer = stuntPerformer
        self.tasPerformer = tasPerformer
        self.tngPerformer = tngPerformer
        self.tosPerformer = tosPerformer
        self.videoGamePerformer = videoGamePerformer
        self.voicePerformer = voicePerformer
        self.voyPerformer = voyPerformer

class SeasonSearchCriteria(CommonSearchCriteria):
    def __init__(self, pageNumber, pageSize, sort, numberOfEpisodesFrom=None, numberOfEpisodesTo=None, seasonNumberFrom=None, seasonNumberTo=None, title=None):
        super(SeasonSearchCriteria, self).__init__(pageNumber, pageSize, sort)
        self.numberOfEpisodesFrom = numberOfEpisodesFrom
        self.numberOfEpisodesTo = numberOfEpisodesTo
        self.seasonNumberFrom = seasonNumberFrom
        self.seasonNumberTo = seasonNumberTo
        self.title = title

class SeriesSearchCriteria(CommonSearchCriteria):
    def __init__(self, pageNumber, pageSize, sort, abbreviation=None, originalRunEndDateFrom=None, originalRunEndDateTo=None, originalRunStartDateFrom=None, originalRunStartDateTo=None, productionEndYearFrom=None, productionEndYearTo=None, productionStartYearFrom=None, productionStartYearTo=None, title=None):
        super(SeriesSearchCriteria, self).__init__(pageNumber, pageSize, sort)
        self.abbreviation = abbreviation
        self.originalRunEndDateFrom = originalRunEndDateFrom
        self.originalRunEndDateTo = originalRunEndDateTo
        self.originalRunStartDateFrom = originalRunStartDateFrom
        self.originalRunStartDateTo = originalRunStartDateTo
        self.productionEndYearFrom = productionEndYearFrom
        self.productionEndYearTo = productionEndYearTo
        self.productionStartYearFrom = productionStartYearFrom
        self.productionStartYearTo = productionStartYearTo
        self.title = title

class SoundtrackSearchCriteria(CommonSearchCriteria):
    def __init__(self, pageNumber, pageSize, sort, lengthFrom=None, lengthTo=None, releaseDateFrom=None, releaseDateTo=None, title=None):
        super(SoundtrackSearchCriteria, self).__init__(pageNumber, pageSize, sort)
        self.lengthFrom = lengthFrom
        self.lengthTo = lengthTo
        self.releaseDateFrom = releaseDateFrom
        self.releaseDateTo = releaseDateTo
        self.title = title

class SpacecraftSearchCriteria(CommonSearchCriteria):
    def __init__(self, pageNumber, pageSize, sort, name=None):
        super(SpacecraftSearchCriteria, self).__init__(pageNumber, pageSize, sort)
        self.name = name

class SpacecraftClassSearchCriteria(CommonSearchCriteria):
    def __init__(self, pageNumber, pageSize, sort, alternateReality=None, name=None, warpCapableSpecies=None):
        super(SpacecraftClassSearchCriteria, self).__init__(pageNumber, pageSize, sort)
        self.alternateReality = alternateReality
        self.name = name
        self.warpCapableSpecies = warpCapableSpecies

class SpeciesSearchCriteria(CommonSearchCriteria):
    def __init__(self, pageNumber, pageSize, sort, alternateReality=None, extinctSpecies=None, extraGalacticSpecies=None, humanoidSpecies=None, name=None, nonCorporealSpecies=None, reptilianSpecies=None, shapeshiftingSpecies=None, spaceborneSpecies=None, telepathicSpecies=None, transDimensionalSpecies=None, unnamedSpecies=None, warpCapableSpecies=None):
        super(SpeciesSearchCriteria, self).__init__(pageNumber, pageSize, sort)
        self.alternateReality = alternateReality
        self.extinctSpecies = extinctSpecies
        self.extraGalacticSpecies = extraGalacticSpecies
        self.humanoidSpecies = humanoidSpecies
        self.name = name
        self.nonCorporealSpecies = nonCorporealSpecies
        self.reptilianSpecies = reptilianSpecies
        self.shapeshiftingSpecies = shapeshiftingSpecies
        self.spaceborneSpecies = spaceborneSpecies
        self.telepathicSpecies = telepathicSpecies
        self.transDimensionalSpecies = transDimensionalSpecies
        self.unnamedSpecies = unnamedSpecies
        self.warpCapableSpecies = warpCapableSpecies

class StaffSearchCriteria(CommonSearchCriteria):
    def __init__(self, pageNumber, pageSize, sort, artDepartment=None, artDirector=None, assistantOrSecondUnitDirector=None, audioAuthor=None, author=None, birthName=None, calendarArtist=None, cameraAndElectricalDepartment=None, castingDepartment=None, cbsDigitalStaff=None, cinematographer=None, comicArtist=None, comicAuthor=None, comicColorArtist=None, comicInkArtist=None, comicInteriorArtist=None, comicLetterArtist=None, comicPencilArtist=None, comicStripArtist=None, composer=None, costumeDepartment=None, costumeDesigner=None, dateOfBirthFrom=None, dateOfBirthTo=None, dateOfDeathFrom=None, dateOfDeathTo=None, director=None, exhibitAndAttractionStaff=None, filmEditor=None, gameArtist=None, gameAuthor=None, gender=None, ilmProductionStaff=None, linguist=None, locationStaff=None, makeupStaff=None, musicDepartment=None, name=None, novelArtist=None, novelAuthor=None, personalAssistant=None, placeOfBirth=None, placeOfDeath=None, producer=None, productionAssociate=None, productionDesigner=None, productionStaff=None, publicationArtist=None, publicationDesigner=None, publicationEditor=None, publicationStaff=None, publicityArtist=None, referenceArtist=None, referenceAuthor=None, scienceConsultant=None, soundDepartment=None, specialAndVisualEffectsStaff=None, specialFeaturesStaff=None, storyEditor=None, studioExecutive=None, stuntDepartment=None, transportationDepartment=None, videoGameProductionStaff=None, writer=None):
        super(StaffSearchCriteria, self).__init__(pageNumber, pageSize, sort)
        self.artDepartment = artDepartment
        self.artDirector = artDirector
        self.assistantOrSecondUnitDirector = assistantOrSecondUnitDirector
        self.audioAuthor = audioAuthor
        self.author = author
        self.birthName = birthName
        self.calendarArtist = calendarArtist
        self.cameraAndElectricalDepartment = cameraAndElectricalDepartment
        self.castingDepartment = castingDepartment
        self.cbsDigitalStaff = cbsDigitalStaff
        self.cinematographer = cinematographer
        self.comicArtist = comicArtist
        self.comicAuthor = comicAuthor
        self.comicColorArtist = comicColorArtist
        self.comicInkArtist = comicInkArtist
        self.comicInteriorArtist = comicInteriorArtist
        self.comicLetterArtist = comicLetterArtist
        self.comicPencilArtist = comicPencilArtist
        self.comicStripArtist = comicStripArtist
        self.composer = composer
        self.costumeDepartment = costumeDepartment
        self.costumeDesigner = costumeDesigner
        self.dateOfBirthFrom = dateOfBirthFrom
        self.dateOfBirthTo = dateOfBirthTo
        self.dateOfDeathFrom = dateOfDeathFrom
        self.dateOfDeathTo = dateOfDeathTo
        self.director = director
        self.exhibitAndAttractionStaff = exhibitAndAttractionStaff
        self.filmEditor = filmEditor
        self.gameArtist = gameArtist
        self.gameAuthor = gameAuthor
        self.gender = gender
        self.ilmProductionStaff = ilmProductionStaff
        self.linguist = linguist
        self.locationStaff = locationStaff
        self.makeupStaff = makeupStaff
        self.musicDepartment = musicDepartment
        self.name = name
        self.novelArtist = novelArtist
        self.novelAuthor = novelAuthor
        self.personalAssistant = personalAssistant
        self.placeOfBirth = placeOfBirth
        self.placeOfDeath = placeOfDeath
        self.producer = producer
        self.productionAssociate = productionAssociate
        self.productionDesigner = productionDesigner
        self.productionStaff = productionStaff
        self.publicationArtist = publicationArtist
        self.publicationDesigner = publicationDesigner
        self.publicationEditor = publicationEditor
        self.publicationStaff = publicationStaff
        self.publicityArtist = publicityArtist
        self.referenceArtist = referenceArtist
        self.referenceAuthor = referenceAuthor
        self.scienceConsultant = scienceConsultant
        self.soundDepartment = soundDepartment
        self.specialAndVisualEffectsStaff = specialAndVisualEffectsStaff
        self.specialFeaturesStaff = specialFeaturesStaff
        self.storyEditor = storyEditor
        self.studioExecutive = studioExecutive
        self.stuntDepartment = stuntDepartment
        self.transportationDepartment = transportationDepartment
        self.videoGameProductionStaff = videoGameProductionStaff
        self.writer = writer

class TechnologySearchCriteria(CommonSearchCriteria):
    def __init__(self, pageNumber, pageSize, sort, borgComponent=None, borgTechnology=None, communicationsTechnology=None, computerProgramming=None, computerTechnology=None, culinaryTool=None, database=None, energyTechnology=None, engineeringTool=None, fictionalTechnology=None, holographicTechnology=None, householdTool=None, identificationTechnology=None, lifeSupportTechnology=None, medicalEquipment=None, name=None, sensorTechnology=None, shieldTechnology=None, subroutine=None, tool=None, transporterTechnology=None):
        super(TechnologySearchCriteria, self).__init__(pageNumber, pageSize, sort)
        self.borgComponent = borgComponent
        self.borgTechnology = borgTechnology
        self.communicationsTechnology = communicationsTechnology
        self.computerProgramming = computerProgramming
        self.computerTechnology = computerTechnology
        self.culinaryTool = culinaryTool
        self.database = database
        self.energyTechnology = energyTechnology
        self.engineeringTool = engineeringTool
        self.fictionalTechnology = fictionalTechnology
        self.holographicTechnology = holographicTechnology
        self.householdTool = householdTool
        self.identificationTechnology = identificationTechnology
        self.lifeSupportTechnology = lifeSupportTechnology
        self.medicalEquipment = medicalEquipment
        self.name = name
        self.sensorTechnology = sensorTechnology
        self.shieldTechnology = shieldTechnology
        self.subroutine = subroutine
        self.tool = tool
        self.transporterTechnology = transporterTechnology

class TitleSearchCriteria(CommonSearchCriteria):
    def __init__(self, pageNumber, pageSize, sort, fleetRank=None, militaryRank=None, mirror=None, name=None, position=None, religiousTitle=None):
        super(TitleSearchCriteria, self).__init__(pageNumber, pageSize, sort)
        self.fleetRank = fleetRank
        self.militaryRank = militaryRank
        self.mirror = mirror
        self.name = name
        self.position = position
        self.religiousTitle = religiousTitle

class TradingCardSearchCriteria(CommonSearchCriteria):
    def __init__(self, pageNumber, pageSize, sort, name=None, tradingCardDeckUid=None, tradingCardSetUid=None):
        super(TradingCardSearchCriteria, self).__init__(pageNumber, pageSize, sort)
        self.name = name
        self.tradingCardDeckUid = tradingCardDeckUid
        self.tradingCardSetUid = tradingCardSetUid

class TradingCardDeckSearchCriteria(CommonSearchCriteria):
    def __init__(self, pageNumber, pageSize, sort, name=None, tradingCardSetUid=None):
        super(TradingCardDeckSearchCriteria, self).__init__(pageNumber, pageSize, sort)
        self.name = name
        self.tradingCardSetUid = tradingCardSetUid

class TradingCardSetSearchCriteria(CommonSearchCriteria):
    def __init__(self, pageNumber, pageSize, sort, boxesPerCaseFrom=None, boxesPerCaseTo=None, cardHeightFrom=None, cardHeightTo=None, cardWidthFrom=None, cardWidthTo=None, cardsPerPackFrom=None, cardsPerPackTo=None, name=None, packsPerBoxFrom=None, packsPerBoxTo=None, productionRunFrom=None, productionRunTo=None, productionRunUnit=None, releaseYearFrom=None, releaseYearTo=None):
        super(TradingCardSetSearchCriteria, self).__init__(pageNumber, pageSize, sort)
        self.boxesPerCaseFrom = boxesPerCaseFrom
        self.boxesPerCaseTo = boxesPerCaseTo
        self.cardHeightFrom = cardHeightFrom
        self.cardHeightTo = cardHeightTo
        self.cardWidthFrom = cardWidthFrom
        self.cardWidthTo = cardWidthTo
        self.cardsPerPackFrom = cardsPerPackFrom
        self.cardsPerPackTo = cardsPerPackTo
        self.name = name
        self.packsPerBoxFrom = packsPerBoxFrom
        self.packsPerBoxTo = packsPerBoxTo
        self.productionRunFrom = productionRunFrom
        self.productionRunTo = productionRunTo
        self.productionRunUnit = productionRunUnit
        self.releaseYearFrom = releaseYearFrom
        self.releaseYearTo = releaseYearTo

class VideoGameSearchCriteria(CommonSearchCriteria):
    def __init__(self, pageNumber, pageSize, sort, releaseDateFrom=None, releaseDateTo=None, title=None):
        super(VideoGameSearchCriteria, self).__init__(pageNumber, pageSize, sort)
        self.releaseDateFrom = releaseDateFrom
        self.releaseDateTo = releaseDateTo
        self.title = title

class VideoReleaseSearchCriteria(CommonSearchCriteria):
    def __init__(self, pageNumber, pageSize, sort, runTimeFrom=None, runTimeTo=None, title=None, yearFrom=None, yearTo=None):
        super(VideoReleaseSearchCriteria, self).__init__(pageNumber, pageSize, sort)
        self.runTimeFrom = runTimeFrom
        self.runTimeTo = runTimeTo
        self.title = title
        self.yearFrom = yearFrom
        self.yearTo = yearTo

class WeaponSearchCriteria(CommonSearchCriteria):
    def __init__(self, pageNumber, pageSize, sort, alternateReality=None, handHeldWeapon=None, laserTechnology=None, mirror=None, name=None, phaserTechnology=None, photonicTechnology=None, plasmaTechnology=None):
        super(WeaponSearchCriteria, self).__init__(pageNumber, pageSize, sort)
        self.alternateReality = alternateReality
        self.handHeldWeapon = handHeldWeapon
        self.laserTechnology = laserTechnology
        self.mirror = mirror
        self.name = name
        self.phaserTechnology = phaserTechnology
        self.photonicTechnology = photonicTechnology
        self.plasmaTechnology = plasmaTechnology

