import glob
import xml.etree.ElementTree as ET
import pandas as pd
import csv
import re

def findNumOfSubChild(child):
    i = 0
    for subchild in child.iter():
        i = i+1
    return i

'20**/*.xml'
def parse(string):
    files = glob.glob(string)
    df_main = pd.DataFrame()
    for file in files:
        try:
            tree = ET.parse(file)
        except ET.ParseError as e:
            print(e)
            print(file)
            continue
            '''
            with open(file, 'a') as f:
                f.write('</Award>\n')
                f.write('</rootTag>\n')
            tree = ET.parse(file)
            '''
        root = tree.getroot()
        tag_list  = []
        text_list = []
        df = pd.DataFrame()
        duplicate_tag_count = {}
        # Iterate through each elements 
        for elem in root.iter():
            # Ignore these two elements 
            if elem.tag != 'rootTag' and elem.tag != 'Award':
                tag = elem.tag
                text = elem.text
                if tag in tag_list:
                    try:
                        duplicate_tag_count[tag] = duplicate_tag_count[tag] +1
                    except KeyError:
                        duplicate_tag_count[tag] = 1
                    tag_list.append(tag + '_' + str(duplicate_tag_count[tag]))
                    text_list.append(elem.text)
                else:
                    tag_list.append(elem.tag)
                    text_list.append(elem.text)

        df = pd.DataFrame(text_list).T
        df.columns = tag_list
        df_main = df_main.append(df, sort=False)
    df_main.to_csv(string[:4] + '_data.csv')






