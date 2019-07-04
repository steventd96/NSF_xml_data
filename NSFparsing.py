import glob
import xml.etree.ElementTree as ET
import pandas as pd
import csv

'20**/*.xml'
def parse(string):
    files = glob.glob(string)
    df_main = pd.DataFrame()
    for file in files:
        tree = ET.parse(file)
        root = tree.getroot()
        full_tag_list = []
        tag_list  = []
        text_list = []
        df = pd.DataFrame()
        save_null_tag = ''
        for elem in root.iter():
            if elem.tag != 'rootTag' and elem.tag != 'Award':
                tag = elem.tag
                text = elem.text
                if text == '\n':
                    save_null_tag = tag
                else:
                    if save_null_tag != '':
                        concat_tag = save_null_tag + ' ' + tag
                        tag_list.append(concat_tag)
                        text_list.append(elem.text)
                    else:
                        tag_list.append(elem.tag)
                        text_list.append(elem.text)
        print(len(tag_list))
        print(len(text_list))
        df = pd.DataFrame(text_list).T
        df.columns = tag_list
        df_main = pd.concat([df_main,df],axis = 0, ignore_index = True)
        #print(df_main)

def get_tags(string):
    files = glob.glob(string)
    for file in files:
        tree = ET.parse(file)
        root = tree.getroot()
        full_tag_list = []
        tag_list = []
        for elem in root.iter():
            tag_list.append(elem.tag)



