import glob
import xml.etree.ElementTree as ET
import pandas as pd
import csv
import re

'20**/*.xml'
def parse(string):
    files = glob.glob(string)
    df_main = pd.DataFrame()
    i =0
    for file in files:
        print(file)
        try:
            tree = ET.parse(file)
        except ET.ParseError:
            with open(file, 'a') as f:
                f.write('</Award>\n')
                f.write('</rootTag>\n')
            tree = ET.parse(file)
        root = tree.getroot()
        tag_list  = []
        text_list = []
        df = pd.DataFrame()
        save_null_tag = ''
        duplicate_tag_count = {}
        # Iterate through each elements 
        for elem in root.iter():
            # Ignore these two elements 
            if elem.tag != 'rootTag' and elem.tag != 'Award':
                tag = elem.tag
                text = elem.text
                # If text is null, that means it has a subchild. Save the tag 
                if text == '\n':
                    save_null_tag = tag
                else:
                    # If save_null_tag is not '', concat the tag 
                    if save_null_tag != '':
                        concat_tag = save_null_tag + ' ' + tag
                        if concat_tag in tag_list:
                            try:
                                duplicate_tag_count[concat_tag] = duplicate_tag_count[concat_tag] +1
                            except KeyError:
                                duplicate_tag_count[concat_tag] = 1
                            tag_list.append(save_null_tag + '_' + str(duplicate_tag_count[concat_tag])+ ' ' +tag)
                            text_list.append(elem.text)
                        else:
                            tag_list.append(concat_tag)
                            text_list.append(elem.text)
                    # If save_null_tag is '', 
                    else:
                        if tag in tag_list:
                            try:
                                duplicate_tag_count[concat_tag] = duplicate_tag_count[concat_tag] +1
                            except KeyError:
                                duplicate_tag_count[concat_tag] = 0
                            tag_list.append(save_null_tag + '_' + str(duplicate_tag_count[concat_tag])+ ' ' +tag)
                            text_list.append(elem.text)
                        else:
                            tag_list.append(elem.tag)
                            text_list.append(elem.text)
        df = pd.DataFrame(text_list).T
        df.columns = tag_list
        df_main = df_main.append(df)
        i = i +1
    df_main.to_csv(string[:4] + '_data.csv')






