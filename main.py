import xmltodict
import dicttoxml
import json
import sys


__author__ = "marcioz98"
__license__ = "MIT"
__version__ = "0.1.0"


def json2xml(filename):
    print("Converting {}...".format(filename), end="")
    
    with open(filename, "r") as input_file:
        xmlstring = json.loads(input_file.read())
        xmlstring = dicttoxml.dicttoxml(xmlstring, attr_type=False)
        
    with open("converted_" + filename.replace(".json", ".xml"), "w") as output_file:
        output_file.write(str(xmlstring, "utf-8"))
    
    print("...done!")


def xml2json(filename):
    print("Converting {}...".format(filename), end="")
    
    with open(filename, "r") as input_file:
        jsonstring = xmltodict.parse(input_file.read())
        jsonstring = json.dumps(jsonstring)

    with open("converted_" + filename.replace(".xml", ".json"), "w") as output_file:
        output_file.write(jsonstring)

    print("...done!")


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        ext = arg.split(".")[len(arg.split("."))-1]
        if ext == "json":
            json2xml(arg)
        elif ext == "xml":
            xml2json(arg)
        else:
            print("Cannot convert file {}!".format(arg))
