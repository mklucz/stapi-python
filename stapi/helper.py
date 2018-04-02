import os 
import yaml

class Base():
    """base, base_response, full, full_response, main, rest_client, extract_ordered_properties
        snake_case, PascalCase, camelCase """
    def base(file_object):
        base_file = open("base.py", "w")
        for i in range(len(snake_case)):
            output_code = "class " + PascalCase[i]+ "Base" + ":" + "\n" + "    def __init__(self, "
            output_docstring = """"""
            file_string = os.getcwd() + "/yaml/" + snake_case[i] + "/entity/" + camelCase[i] + "Base.yaml"
            try:
                loaded_yaml = yaml.load(open(file_string))
                ordered_properties = extract_ordered_properties(file_string)
            except FileNotFoundError as e:
                print(e)
                continue
            output_docstring += '''\n        \"\"\"'''
            output_docstring += loaded_yaml["description"]
            output_docstring += """\n        Args:""" + "\n"
            for top_key, top_value in loaded_yaml.items():

                if top_key == "type":
                    continue
                elif top_key == "properties":
                    positional_arguments = ""
                    named_arguments = ""
                    assignments = """"""
                    for t in ordered_properties:
                        prop, flag = t[0], t[1]
                        if flag:
                            positional_arguments += prop + ", "
                            if "type" in top_value[prop]:
                                output_docstring += "            " + prop + " (" + top_value[prop]["type"] + "): " + top_value[prop]["description"] + "\n"
                                assignments +=  "        self." + prop + " = " + prop + "\n"
                            else:
                                output_docstring += "            " + prop + " (" + top_value[prop]["$ref"] + "): " + top_value[prop]["description"] + "\n"
                                assignments +=  "        self." + prop + " = " + prop + "\n"
                        else:
                            named_arguments += prop + "=None" + ", "
                            if "type" in top_value[prop]:
                                output_docstring += "            " + prop + " (" + top_value[prop]["type"] + "): " + top_value[prop]["description"] + "\n"
                                assignments +=  "        self." + prop + " = " + prop + "\n"
                            else:
                                output_docstring += "            " + prop + " (" + top_value[prop]["$ref"] + "): " + top_value[prop]["description"] + "\n"
                                assignments +=  "        self." + prop + " = " + prop + "\n"
                    output_code += positional_arguments
                    output_code += named_arguments
                    output_code = output_code[:-2] + "):"
                    output_docstring += "        \"\"\"\n"
                    

                    base_file.write(output_code)
                    base_file.write(output_docstring)
                    base_file.write(assignments)
        base_file.close()            

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

def lower_first_char(s):
    return s[0].lower() + s[1:]

def extract_ordered_properties(path_to_yaml_file):
    ordered_properties = []
    f = open(path_to_yaml_file)
    lines_list = [l for l in f.readlines()]
    loaded_yaml = yaml.load(open(path_to_yaml_file))
    for line in lines_list:
        if line.startswith("  ") and line[2] != " ":
            prop = line[2:-2]
            if prop in loaded_yaml["properties"]:
                # print(loaded_yaml["properties"][prop])
                if "required" in loaded_yaml["properties"][prop] and loaded_yaml["properties"][prop]["required"]:
                    ordered_properties.append((prop, True))
                else:
                    ordered_properties.append((prop, False))
    return ordered_properties

def helper_klasy_base():
    base_file = open("base.py", "w")
    for i in range(len(snake_case)):
        output_code = "class " + PascalCase[i]+ "Base" + ":" + "\n" + "    def __init__(self, "
        output_docstring = """"""
        file_string = os.getcwd() + "/yaml/" + snake_case[i] + "/entity/" + camelCase[i] + "Base.yaml"
        try:
            loaded_yaml = yaml.load(open(file_string))
            ordered_properties = extract_ordered_properties(file_string)
        except FileNotFoundError as e:
            print(e)
            continue
        output_docstring += '''\n        \"\"\"'''
        output_docstring += loaded_yaml["description"]
        output_docstring += """\n        Args:""" + "\n"
        for top_key, top_value in loaded_yaml.items():

            if top_key == "type":
                continue
            elif top_key == "properties":
                positional_arguments = ""
                named_arguments = ""
                assignments = """"""
                for t in ordered_properties:
                    prop, flag = t[0], t[1]
                    if flag:
                        positional_arguments += prop + ", "
                        if "type" in top_value[prop]:
                            output_docstring += "            " + prop + " (" + top_value[prop]["type"] + "): " + top_value[prop]["description"] + "\n"
                            assignments +=  "        self." + prop + " = " + prop + "\n"
                        else:
                            output_docstring += "            " + prop + " (" + top_value[prop]["$ref"] + "): " + top_value[prop]["description"] + "\n"
                            assignments +=  "        self." + prop + " = " + prop + "\n"
                    else:
                        named_arguments += prop + "=None" + ", "
                        if "type" in top_value[prop]:
                            output_docstring += "            " + prop + " (" + top_value[prop]["type"] + "): " + top_value[prop]["description"] + "\n"
                            assignments +=  "        self." + prop + " = " + prop + "\n"
                        else:
                            output_docstring += "            " + prop + " (" + top_value[prop]["$ref"] + "): " + top_value[prop]["description"] + "\n"
                            assignments +=  "        self." + prop + " = " + prop + "\n"
                output_code += positional_arguments
                output_code += named_arguments
                output_code = output_code[:-2] + "):"
                output_docstring += "        \"\"\"\n"
                

                base_file.write(output_code)
                base_file.write(output_docstring)
                base_file.write(assignments)
    base_file.close()            

def helper_klasy_full_response():
    full_response_file = open("full_response.py", "w")
    for klasa in lepsze_klasy:
        full_response_file.write("class " + klasa + "FullResponse" + ":")
        full_response_file.write("""
        def __init__(self, """ + klasa + """Full):
            self.""" + lower_first_char(klasa) + " = " + klasa + "Full")

        full_response_file.write("\n\n")
# helper_klasy_full_response()

def extract_searchable_attributes():
    # search_file = open("search.py", "w")
    searchable_attributes = {}
    for i in range(len(snake_case)):
        if snake_case[i] == "organization":
            searchable_attributes["organization"] = "name"
            continue
            # hardcoded as there seems to be an error in organizationSearch.path.yaml file
        path_to_yaml_file = os.getcwd() + "/yaml/" + snake_case[i] + "/path/" + camelCase[i] + "Search.path.yaml"
        if os.path.isfile(path_to_yaml_file):
            search_file = open(path_to_yaml_file)
            read_file = search_file.read()
            string_to_find = """  parameters:
    - name: pageNumber
      in: query
      type: integer
      format: int32
      description: Zero-based page number
    - name: pageSize
      in: query
      type: integer
      format: int32
      description: Page size
    - name: sort
      type: string
      in: query
      description: "Sorting, serialized like this: fieldName,ASC;anotherFieldName,DESC"
    - name: apiKey
      in: query
      type: string
      description: API key
"""
            index_of_the_interesting_part = read_file.find(string_to_find) + len(string_to_find)
            interesting_part = read_file[index_of_the_interesting_part:]
            where_to_stop = interesting_part.find("\n")
            # print(camelCase[i], interesting_part[:where_to_stop])
            searchable_attributes[camelCase[i]] = "title" if "title" in interesting_part[:where_to_stop] else "name"
    return searchable_attributes


def helper_klasy_main():
    main_file = open("main.py", "w")
    main_file.write( 
"""
from .full import *
from .base import *
from .full_response import *
from .base_response import *
from .search_criteria import *
try:
    from urllib.request import urlopen as urlopen
except ImportError:
    from urllib import urlopen as urlopen
from json import loads
import requests

""")
    searchable_attributes = extract_searchable_attributes()
    for i in range(len(lepsze_klasy)):
        try:
            get_file = open(os.getcwd() + "/yaml/" + snake_case[i] + "/path/" + camelCase[i] + ".path.yaml")
        except FileNotFoundError as e:
            print("no get_file", e)
            continue
        try:
            search_file = open(os.getcwd() + "/yaml/" + snake_case[i] + "/path/" + camelCase[i] + "Search.path.yaml")
        except FileNotFoundError as e:
            print("no search_file", e)
            # if get_file:
            #     continue  
            continue
        loaded_get_file = yaml.load(get_file)
        loaded_search_file = yaml.load(search_file)
        
        main_file.write("class " + PascalCase[i] + ":")
        main_file.write("""
        def __init__(self, url, apiKey):
            self.url = url
            self.apiKey = apiKey""")
        main_file.write("""
        def get(self, uid):
            url_to_open = self.url + "/api/v1/rest/""" + camelCase[i] + """?uid=" + uid
            fetched_data = urlopen(url_to_open)
            decoded_data = fetched_data.readlines()[0].decode("utf-8")
            parsed_data = loads(decoded_data)
            args_mapping = parsed_data[\"""" + camelCase[i] + """\"]
            return """ + PascalCase[i] + """Full(**args_mapping)
            """ + """
        def search(self, searchCriteria):
            url_to_post = self.url + "/api/v1/rest/""" + camelCase[i] + """/search?pageNumber=" + str(searchCriteria.pageNumber) + "&" + str(searchCriteria.pageSize) 
            data_to_post = searchCriteria.__dict__
            post_request = requests.post(url_to_post, data_to_post)
            response_text = post_request.text
            response_dict = loads(response_text)
            return response_dict
            """)
        main_file.write("\n")

    main_file.close()

# helper_klasy_main()

def helper_base_response():
    base_response_file = open("base_response.py", "w")
    for i in range(len(PascalCase)):
        base_response_file.write("class " + PascalCase[i] + "BaseResponse" + ":")
        base_response_file.write("""
        def __init__(self):
            pass\n\n""")
    base_response_file.close()

# helper_base_response()

def helper_full():
    full_file = open("full.py", "w")
    for i in range(len(PascalCase)):
        # full_file.write("class " + PascalCase[i] + "Full" + ":")
        output_code = "class " + PascalCase[i]+ "Full" + ":" + "\n" + "    def __init__(self, "
        output_docstring = """"""
        file_string = os.getcwd() + "/yaml/" + snake_case[i] + "/entity/" + camelCase[i] + "Full.yaml"
        try:
            loaded_yaml = yaml.load(open(file_string))
            ordered_properties = extract_ordered_properties(file_string)
        except FileNotFoundError as e:
            print(e)
            continue
        output_docstring += '''\n        \"\"\"'''
        output_docstring += loaded_yaml["description"]
        output_docstring += """\n        Args:""" + "\n"
        for top_key, top_value in loaded_yaml.items():
            if top_key == "type":
                continue
            elif top_key == "properties":
                positional_arguments = ""
                named_arguments = ""
                assignments = """"""
                for t in ordered_properties:
                    prop, flag = t[0], t[1]
                    if flag:
                        positional_arguments += prop + ", "
                        if "type" in top_value[prop]:
                            output_docstring += "            " + prop + " (" + top_value[prop]["type"] + "): " + top_value[prop]["description"] + "\n"
                            assignments +=  "        self." + prop + " = " + prop + "\n"
                        else:
                            output_docstring += "            " + prop + " (" + top_value[prop]["$ref"] + "): " + top_value[prop]["description"] + "\n"
                            assignments +=  "        self." + prop + " = " + prop + "\n"
                    else:
                        named_arguments += prop + "=None" + ", "
                        if "type" in top_value[prop]:
                            output_docstring += "            " + prop + " (" + top_value[prop]["type"] + "): " + top_value[prop]["description"] + "\n"
                            assignments +=  "        self." + prop + " = " + prop + "\n"
                        else:
                            output_docstring += "            " + prop + " (" + top_value[prop]["$ref"] + "): " + top_value[prop]["description"] + "\n"
                            assignments +=  "        self." + prop + " = " + prop + "\n"
                output_code += positional_arguments
                output_code += named_arguments
                output_code = output_code[:-2] + "):"
                output_docstring += "        \"\"\"\n"
                

                full_file.write(output_code)
                full_file.write(output_docstring)
                full_file.write(assignments)
    full_file.close()
# helper_full()

def helper_rest_client():
    for i in range(len(snake_case)):
        # print(os.getcwd() + "/yaml/" + snake_case[i] + "/path/" + snake_case[i] + "path.yaml")
        if os.path.isfile(os.getcwd() + "/stapi/yaml/" + snake_case[i] + "/path/" + camelCase[i] + ".path.yaml"):
            print("self." + camelCase[i] + " = " + PascalCase[i] + "(url, apiKey)")

# helper_rest_client()

def helper_searchCriteria():
    searchCriteria_file = open("search_criteria.py", "w")
    output_code = "from .common_search_criteria import *\n"
    for i in range(len(snake_case)):
        named_arguments = ", "
        assignments = ""
        file_string = os.getcwd() + "/yaml/" + snake_case[i] + "/path/" + camelCase[i] + "Search.path.yaml"
        try:
            loaded_yaml = yaml.load(open(file_string))
            # print(loaded_yaml["post"]["parameters"])
            formDataFields = []
            for field in loaded_yaml["post"]["parameters"]:
                if field["in"] == "formData":
                    formDataFields.append(field["name"])
            # print(formDataFields)
            formDataFields.sort()
            for entry in formDataFields:
                named_arguments += entry + "=None, "
                assignments +=  "        self." + entry + " = " + entry + "\n"
                # declarations += "self." + entry
            named_arguments = named_arguments[0:-2]
            named_arguments += "):"
            # print(named_arguments)
        except FileNotFoundError as e:
            print(e)
            continue

        
        output_code += "class " + PascalCase[i]+ "SearchCriteria" + "(CommonSearchCriteria):" + "\n" + "    def __init__(self, pageNumber, pageSize, sort" + named_arguments
        output_code += "\n        super(" + PascalCase[i] + "SearchCriteria, self).__init__(pageNumber, pageSize, sort)\n"
        output_code += assignments
        output_code += "\n"
    searchCriteria_file.write(output_code)
helper_searchCriteria()