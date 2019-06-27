import glob
import xml.etree.ElementTree as ET
import pandas as pd
import csv

'20**/*.xml'
def pase(string):
    files = glob.glob(string)
    df_main = pd.DataFrame()
    for file in files:
        print(file)
        tree = ET.parse(file)
        root = tree.getroot()
        full_tag_list = []
        tag_list  = []
        text_list = []
        df = pd.DataFrame()
        for elem in root.iter():
            tag_list.append(elem.tag)
            text_list.append(elem.text)
        print(tag_list)
        df = pd.DataFrame(text_list).T
        df.columns = tag_list
        df_main = pd.concat([df_main,df])

def get_tags(string):
    files = glob.glob(string)
    for file in files:
        tree = ET.parse(file)
        root = tree.getroot()
        full_tag_list = []
        tag_list = []
        for elem in root.iter():
            tag_list.append(elem.tag)



