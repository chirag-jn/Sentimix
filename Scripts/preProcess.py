from defaults import *
import xmlschema
import xml.etree.ElementTree as ET
from optparse import OptionParser
import html

is_article = False

def setParser():
    parser = OptionParser()
    parser.add_option("--type", help="Article or Publisher", type=str, default='article')
    options, _ = parser.parse_args()
    return options

def validateXMLFiles():
    xmlschema.validate(article_training_data_loc, training_data_schema)
    xmlschema.validate(article_ground_truth_data_loc, ground_truth_schema)

def cleantext(text):
    '''Clean the text extracted from XML.'''
    text = text.lower()
    # text = text.replace("&amp;", "&")
    # text = text.replace(bytes("&amp", 'utf-8'), bytes("&", 'utf-8'))
    # text = text.replace("&gt;", ">")
    # text = text.replace("&lt;", "<")
    text = text.replace(bytes("<p>", 'utf-8'), bytes(" ", 'utf-8'))
    # text = text.replace("</p>", " ")
    text = text.replace(bytes("</p>", 'utf-8'), bytes(" ", 'utf-8'))
    # text = text.replace(" _", " ")
    text = text.replace(bytes(" _", 'utf-8'), bytes(" ", 'utf-8'))
    # text = text.replace("–", "-")
    text = text.replace(bytes("–", 'utf-8'), bytes("-", 'utf-8'))
    # text = text.replace("”", "\"")
    text = text.replace(bytes("”", 'utf-8'), bytes("\"", 'utf-8'))
    # text = text.replace("“", "\"")
    text = text.replace(bytes("“", 'utf-8'), bytes("\"", 'utf-8'))
    # text = text.replace("’", "'")
    text = text.replace(bytes("’", 'utf-8'), bytes("'", 'utf-8'))
    text = text.replace(bytes("  ", 'utf-8'), bytes(" ", 'utf-8'))
    return text

def parseTrainingData():
    if is_article:
        tree = ET.parse(article_training_data_loc)
        root = tree.getroot()
        # xmlstr = ET.tostring(root)
        # xmlstr = cleantext(xmlstr)
        # print(xmlstr)
        # root = ET.fromstring(xmlstr)
    else:
        tree = ET.parse(publisher_training_data_loc)
        root = tree.getroot()
    # root = tree.getroot()
    # print(root.tag)
    # print(root.attrib)
    for child in root:
        print(child.tag, child.attrib)
        print(type(child))
        print(dir(child))
        for i in child:
            print(i.text)
            for j in i:
                print(j.text)
            break
        # print(len(child))
        break

def getGroundTruth():
    if is_article:
        tree = ET.parse(article_ground_truth_data_loc)
    else:
        tree = ET.parse(publisher_ground_truth_data_loc)
    root = tree.getroot()
    is_hyper = {}
    for child in root:
        attrib = dict(child.attrib)
        is_hyper[attrib['id']] = {}
        if attrib['hyperpartisan'] == 'true':
            is_hyper[attrib['id']]['bias'] = True
        else:
            is_hyper[attrib['id']]['bias'] = False
        is_hyper[attrib['id']]['url'] = attrib['url']
    savePickle(is_hyper, 'article-ground-truth')
    return is_hyper

if __name__=='__main__':
    options = setParser()
    if options.type.lower() == 'article':
        is_article = True
    else:
        is_article = False
    validateXMLFiles()
    getGroundTruth()
    parseTrainingData()