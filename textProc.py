import json
import pandas as pd


def json2xlsx():
    my_list = [];

    with open('monarchies.txt') as f:
        lines = f.readlines() # list containing lines of file
        columns = [] # To store column names

        i = 1
        for line in lines:
            line = line.strip() # remove leading/trailing white spaces
            if line:
                d = {} # dictionary to store file data (each line)
                data = [item.strip() for item in line.split('.')]
                for index, elem in enumerate(data):
                    subdata = [content.strip() for content in data[1].split('-')]
                    d['monarchy'] = subdata[0]
                    d['country'] = subdata[1]


                my_list.append(d) # append dictionary to list

    # pretty printing list of dictionaries
    jsonString = json.dumps(my_list, indent=4)
    print(jsonString)

    with open('monarchies.json', 'w') as f:
        json.dump(my_list, f, indent=4)
        
    # Json to DataFrame
    df = pd.json_normalize(json.loads(jsonString))

    # DataFrame to Excel
    excel_filename = 'json_data_to_excel.xlsx'
    df.to_excel(excel_filename, index=False)

def xlsx2json():
    # Read excel document
    excel_data_df = pd.read_excel('json_data_to_excel.xlsx', sheet_name='Sheet1')

    # Convert excel to string 
    # (define orientation of document in this case from up to down)
    thisisjson = excel_data_df.to_json(orient='records')

    # Print out the result
    print('Excel Sheet to JSON:\n', thisisjson)

    # Make the string into a list to be able to input in to a JSON-file
    thisisjson_dict = json.loads(thisisjson)

    # Define file to write to and 'w' for write option -> json.dump() 
    # defining the list to write from and file to write to
    with open('data.json', 'w') as json_file:
        json.dump(thisisjson_dict, json_file, indent=4)    
    

xlsx2json()    