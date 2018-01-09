import urllib.request
import json
import os
import yaml
import pprint
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
entity_types.sort()

lepsze_klasy = ['Animal', 'AstronomicalObject', 'Book', 'BookCollection', 'BookSeries', 'Character', 'ComicCollection',
 'ComicSeries', 'ComicStrip', 'Comics', 'Common', 'Company', 'Conflict', 'ContentLanguage', 'ContentRating', 'Country',
  'Element', 'Episode', 'Food', 'Genre', 'Literature', 'Location', 'Magazine', 'MagazineSeries', 'Material',
   'MedicalCondition', 'Movie', 'Occupation', 'Organization', 'Performer', 'Platform', 'Reference', 'Season', 'Series',
    'Soundtrack', 'Spacecraft', 'SpacecraftClass', 'SpacecraftType', 'Species', 'Staff', 'Technology', 'Title',
     'TradingCard', 'TradingCardDeck', 'TradingCardSet', 'VideoGame', 'VideoRelease', 'Weapon']

snake_case = ['animal', 'astronomical_object', 'book', 'book_collection', 'book_series', 'character', 'comic_collection', 'comic_series', 'comic_strip', 'comics', 'common', 'company', 'conflict', 'content_language', 'content_rating', 'country', 'element', 'episode', 'food', 'genre', 'literature', 'location', 'magazine', 'magazine_series', 'material', 'medical_condition', 'movie', 'occupation', 'organization', 'performer', 'platform', 'reference', 'season', 'series', 'soundtrack', 'spacecraft', 'spacecraft_class', 'spacecraft_type', 'species', 'staff', 'technology', 'title', 'trading_card', 'trading_card_deck', 'trading_card_set', 'video_game', 'video_release', 'weapon']
PascalCase = lepsze_klasy
camelCase = [e[0].lower() + e[1:] for e in PascalCase]

# klasy = []
# for entity in entity_types:
#     klasy.append(entity[:1].upper() + entity[1:])
# # print(klasy)
# lepsze_klasy = []
# for klasa in klasy:
#     for i in range(len(klasa)-2):
#         if klasa[i] == "_":
#             # print(klasa)
#             klasa = klasa[:i] + klasa[i+1].upper() + klasa[i+2:]
#             # print(klasa)
#             # print("\n")
#     lepsze_klasy.append(klasa)
#     # print(klasa)
# lepsze_klasy.sort()
# print(lepsze_klasy)

class AnimalBase:
    def __init__(self, uid, name, earthAnimal=None):
        pass

def lower_first_char(s):
    return s[0].lower() + s[1:]
# for lasa in lepsze_klasy:
#     print("self." + lasa[0].lower() + lasa[1:] + " = " + lasa + "(url, apiKey)")

def extract_ordered_properties(path_to_yaml_file):
    ordered_properties = []
    f = open(path_to_yaml_file)
    lines_list = [l for l in f.readlines()]
    loaded_yaml = yaml.load(open(path_to_yaml_file))
    for line in lines_list:
        if line.startswith("  ") and line[2] != " ":
            prop = line[2:-2]
            if prop in loaded_yaml["properties"][prop]:
                print("kum")
                # TODO: zrobiś tak żeby wywalało listę wszystkich properties z flagą czy required czy nie


def helper_klasy_base():
    base_file = open("base.py", "w")
    for i in range(len(snake_case)):
        output_code = "class " + PascalCase[i] + ":" + "\n" + "    def __init__(self, uid, "
        output_docstring = """"""
        file_string = "/home/maciek/Documents/newprog/stapi/yaml/" + snake_case[i] + "/entity/" + camelCase[i] + "Base.yaml"
        loaded_yaml = yaml.load(open(file_string))
        
        # with open(file_string) as f:
        #     lines_from_yaml = f.readlines()
        # lines_from_yaml = [l.strip() for l in lines_from_yaml]
        # # print(lines_from_yaml)
        # ordered_required_properties = []
        # for j in range(len(lines_from_yaml)):
        #     if lines_from_yaml[j] == "required: true":
        #         ordered_required_properties.append(lines_from_yaml[j-2][:-1])
        # print(ordered_required_properties)
        extract_ordered_properties(file_string)

        output_docstring += '''\n        \"\"\"'''
        output_docstring += loaded_yaml["description"]
        output_docstring += """\n        Args:""" + "\n"
        for top_key, top_value in loaded_yaml.items():

            if top_key == "type":
                continue
            # elif top_key == "description":
            #     output_docstring += '''\"\"\"'''
            #     output_docstring += top_value
            #     output_docstring += """\nArgs:""" + "\n"
            elif top_key == "properties":
                ordered_properties = ["uid", "placeholder"]
                positional_arguments = ""
                named_arguments = ""
                assignments = """"""
                for key, value in sorted(top_value.items()):
                    if "required" not in value:
                        named_arguments += key + "=None, "
                        ordered_properties.append(key)
                    else:
                        if key != "uid":
                            positional_arguments += key + ", "
                            ordered_properties[1] = key
                for e in ordered_properties:
                    # print(top_value[e])
                    # print(file_string)
                    if "type" in top_value[e]:
                        output_docstring += "            " + e + " (" + top_value[e]["type"] + "): " + top_value[e]["description"] + "\n"
                        assignments +=  "        self." + e + " = " + e + "\n"
                    else:
                        output_docstring += "            " + e + " (" + top_value[e]["$ref"] + "): " + top_value[e]["description"] + "\n"
                        assignments +=  "        self." + e + " = " + e + "\n"
                output_code += positional_arguments
                output_code += named_arguments
                output_code = output_code[:-2] + ")"
                output_docstring += "        \"\"\"\n"
                

                base_file.write(output_code)
                base_file.write(output_docstring)
                base_file.write(assignments)
    base_file.close()            
                # print(output_code) ## WRITE TO FILE
                # print(output_docstring)
                # print(assignments)



        

helper_klasy_base()

def helper_klasy_full_response():
    full_response_file = open("full_response.py", "w")
    for klasa in lepsze_klasy:
        full_response_file.write("class " + klasa + "FullResponse" + ":")
        full_response_file.write("""
        def __init__(self, uid):
            self.uid = uid
            self.""" + lower_first_char(klasa) + " = " + klasa + "Full(uid)")

        full_response_file.write("\n\n")
# helper_klasy_full_response()

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