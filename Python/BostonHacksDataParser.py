import json
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


