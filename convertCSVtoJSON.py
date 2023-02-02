import csv
import json
 
def csv_to_json(csv_file_path, json_file_path):
    #create a dictionary
    data_dict = {}
 
    #Step 2
    with open(csv_file_path, encoding = 'utf-8') as csv_file_handler:
        csv_reader = csv.DictReader(csv_file_handler)
        
        nb = 0
        for rows in csv_reader:
            data_dict[nb] = rows
            nb = nb + 1
 
    #Step 3
    with open(json_file_path, 'w', encoding = 'utf-8') as json_file_handler:
        #Step 4
        json_file_handler.write(json.dumps(data_dict, indent = 4))
 
#Step 1
#csv_file_path = './Classeur1.csv'
csv_file_path = './Mental_Health_FAQ.csv'
json_file_path = './json/return.json'
 
csv_to_json(csv_file_path, json_file_path)