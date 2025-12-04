#cleans the data from uscities, stores in dictionary to be fed into main.py

#csv: "city","city_ascii","state_id","state_name","county_fips","county_name","lat","lng","population","density","source","military","incorporated","timezone","ranking","zips","id"
#dict: {city: [state_id, lat, lng, population]}

file = open("uscities.csv", "r")

file.readline()

cityPopulationDict = {"city": ["stateID", "lat", "lng", "population"]}

for lines in file:
    lines = lines.strip().split(",")

    cityName = lines[0]
    stateID = lines[2]
    lat = lines[6]
    lng = lines[7]
    population = lines[8].strip('"').strip("'")

    if float(population) > 100000:
        cityPopulationDict[cityName] = [stateID, lat, lng, population]

file.close()