import json
import csv


with open('enpassRaw.json', 'r') as myfile:
    obj = json.load(myfile)

with open('enpassExported.csv', 'w', newline='') as csvfile:
    filewriter = csv.writer(csvfile, delimiter = ',', quotechar = '|', quoting = csv.QUOTE_MINIMAL)
    filewriter.writerow(['Name', 'Website', 'Login', 'Login2', 'Password'])

    for item in obj['items']:
        Login = ""
        Email = ""
        Pass = ""
        Website = ""
        Title = item['title']
        if 'fields' in item:
            for field in item['fields']:
                label = field['type']
                value = field['value']
                if label == "email":
                    Email = value
                elif label == "username":
                    Login = value
                elif label == "password":
                    Pass = value
                elif label == "url":
                    Website = value
        filewriter.writerow([Title, Website, Login, Email, Pass])
