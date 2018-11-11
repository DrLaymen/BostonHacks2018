import pandas as pd
import time
filename = "Sidewalk_Repair_311_Cases_small.csv"
df = pd.read_csv(filename, usecols=['Latitude', 'Longitude'])
df.drop_duplicates(subset=['Latitude', 'Longitude'], keep=False)

#print(df)

import google_streetview.api
import requests  
import json

dataFile = open("data.txt", "w")

for index, row in df.iterrows():

    # Import google_streetview for the api module

    long = row['Latitude']
    lat = row["Longitude"]
    coord = str(long) + "," + str(lat)
    # Define parameters for street view api
    params = [{
      'size': '600x300', # max 640x640 pixels
      #'location': '42.3577,-71.0693',
      'location': coord,
      'heading': '151.78',
      'pitch': '-0.76',
      'fov': '120',
      'key': 'INSERT_API_KEY'
    }]

    # Create a results object
    results = google_streetview.api.results(params)

    # Download images to directory 'downloads'
    #results.download_links('downloadsmap')
    results.save_links('links.txt')
    #print(results)
    time.sleep(0.5)
    linkFile = open("links.txt", "r")
    link = linkFile.read()
    dataFile.write(link+'\n')
   # print(link)
    url = ""
    image = {"Url": link}
    headers = { "Content-Type": "application/json", 
               "Prediction-Key": ""}
    r=requests.post(url, data=json.dumps(image), headers=headers)
    dataFile.write(r.text+'\n')
    #print(r.text)

dataFileWrite = open("BostonHacks.html", "w")
dataFileRead = open("data.txt", "r")
text = dataFileRead.readlines()
dataFileWrite.write('<!DOCTYPE html>\n')
dataFileWrite.write('<html>\n')
dataFileWrite.write('<head>\n')
dataFileWrite.write('<title>Sidewalk Data</title>\n')
dataFileWrite.write('<body>\n')
#print(text)
for i in range(0, len(text), 2):
    parse = text[i+1]
    parsed_json = json.loads(parse)
    prediction = parsed_json['predictions']
    #print(prediction[0]['probability'])
    if(prediction[0]['probability']>0.5):
        dataFileWrite.write("<br>")
        for j in prediction:
            #print(j)
            dataFileWrite.write(j['tagName']+':\n')
            dataFileWrite.write(str(round(j['probability']*100, 4))+'%')
            dataFileWrite.write('<br>')
            
        
        dataFileWrite.write('<img src="'+text[i]+'">'+'\n')
        dataFileWrite.write('<br>')


dataFileRead.close()
dataFileWrite.close()

#dataFileWrite.write('</body>')
#dataFileWrite.write("</html>")

