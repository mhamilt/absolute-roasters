# Transform data between formats: CSV to JSON, JSON to CSV.
# Using the Companies House CSV structure as a starting point
# curl -X GET -u my_key: "https://api.company-information.service.gov.uk/advanced-search/companies?sic_codes=10832"

import json
import csv
import re
import requests
from tqdm import tqdm
from time import sleep

postcode_pattern = re.compile(r"[A-Z]{1,2}\d[\d|\w]?\s\d{1,2}[A-Z]{1,2}")
# postcode_pattern = re.compile(r"([A-Z]{1,2}\d{1,2})(\s\d{1,2}[A-Z]{1,2})")

postcode_url ="https://api.postcodes.io/postcodes/"
outcode_url = "https://api.postcodes.io/outcodes/"

def json2csv():
        
    headers = ["name", "location", "url", "postcode", "coord"]
   

    with open("../absolute_roasters.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    with open("output.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
                  
        for row in data:
            address = row.get('location', "")             
            match = postcode_pattern.search(address)
            entry = {key: row.get(key, "") for key in headers}
            postcode = "" if not match else match.group()
            entry['postcode'] = postcode
            print(entry)
            writer.writerow(entry)    

def removeDuplicates():
    with open("../companies-house-records.csv", "r", newline="", encoding="utf-8") as filein:
         with open("companies-house-unique.csv", "w", newline="", encoding="utf-8") as fileout:
            reader = csv.reader(filein)
            headers = next(reader)   # gets the first row                     
            writer  = csv.writer(fileout)
            writer.writerow(headers)
            
            company_numbers = set()
            
            for row in reader:                
                company_number = row[1]
                                
                if company_number in company_numbers:
                    continue
                
                company_numbers.add(company_number)
                writer.writerow(row)

def addPostcode():    
    
     with open("companies-house-unique.csv", "r", newline="", encoding="utf-8") as filein:
         with open("companies-house-postcodes.csv", "w", newline="", encoding="utf-8") as fileout:
            
            reader = csv.reader(filein)
            headers = next(reader)   # gets the first row            
            headers.append('postcode')
            writer  = csv.writer(fileout)
            writer.writerow(headers)
                    
            for row in reader:
                address = row[-1]
                match = postcode_pattern.search(address)                
                postcode = match.group() if match else ""
                entry = row
                entry.append(postcode)                
                writer.writerow(entry)    
    
def addlatlong():       
    postcode_url ="https://api.postcodes.io/postcodes/"
    outcode_url = "https://api.postcodes.io/outcodes/"
    
    with open("companies-house-postcodes.csv", "r", newline="", encoding="utf-8") as filein:
        with open("companies-house-complete.csv", "w", newline="", encoding="utf-8") as fileout:
            reader = csv.reader(filein)
            headers = next(reader)   # gets the first row            
            headers.append('lng')
            headers.append('lat')
            writer  = csv.writer(fileout)
            writer.writerow(headers)
                        
            for row in tqdm(reader, desc="Processing"):
                entry = row
                postcode = row[-1]       
                url = (postcode_url if ' ' in postcode else outcode_url) + postcode        
                r = requests.get(url)
                
                if r.json()['status'] == 404:
                    url = outcode_url + postcode.split()[0]                
                    r = requests.get(url)
                
                if r.json()['status'] == 200:
                    lng = r.json()['result']['longitude']
                    lat = r.json()['result']['latitude']
                    entry.append(lng)
                    entry.append(lat)
                else:
                    entry.append('')
                    entry.append('')

                writer.writerow(entry)                
    
def clean():
    with open("companies-house-unique.csv", "r", newline="", encoding="utf-8") as filein:
         with open("companies-house-clean.csv", "w", newline="", encoding="utf-8") as fileout:
            reader = csv.reader(filein)
            headers = next(reader)
            
            writer  = csv.writer(fileout)
            writer.writerow(headers)
            
            for row in tqdm(reader, desc="Processing"):
                entry = row 
                if not row[-1]:    
                    address = row[10]
                    match = postcode_pattern.search(address) 
                    postcode = match.group() if match else ""
                    
                    entry[-3] = postcode
                    
                    url = postcode_url + postcode
                    r = requests.get(url)
                    
                    if r.json()['status'] == 200:
                        lng = r.json()['result']['longitude']
                        lat = r.json()['result']['latitude']
                        entry[-2] = lng
                        entry[-1] = lat
                        
                writer.writerow(entry)
    
def cull():
      with open("companies-house-complete.csv", "r", newline="", encoding="utf-8") as filein:
        with open("companies-house-final.csv", "w", newline="", encoding="utf-8") as fileout:
            reader = csv.reader(filein)
            headers = next(reader)   # gets the first row                        
            writer  = csv.writer(fileout)
            writer.writerow(headers)
            
            for row in reader:
                if not row[-1]:
                    continue
                writer.writerow(row)


def makeCompaniesHouseGeoJSON():

    
    geojson = {
        "type": "FeatureCollection",
        "features":[]
    }
    
    with open("../companies-house-records.csv", "r", newline="", encoding="utf-8") as filein:
        reader = csv.reader(filein)
        next(reader)
        
        for row in reader:            
            entry = {
                "properties": {
                "location": row[10],
                "name": row[1],
                "status": row[2],                
                "marker-symbol": ("cafe" if row[2] == "Active" else "danger"),
                },
                "geometry": {
                    "type": "Point",
                    "coordinates": [row[-1], row[-2]]
                }                            
            }
            
            geojson['features'].append(entry)
            
            
        with open('companies_house.geojson', 'w', encoding='utf-8') as fileout:
            json.dump(geojson, fileout, ensure_ascii=False, indent=4)
    




if __name__ == "__main__":
    # addlatlong()
    # addPostcode()
    # removeDuplicates()
    # clean()
    # cull()
    makeCompaniesHouseGeoJSON()