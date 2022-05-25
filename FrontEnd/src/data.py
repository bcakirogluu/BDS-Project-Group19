import pandas as pd
import json
from SPARQLWrapper import SPARQLWrapper, JSON

lang_of_interest = "en" #can be changed to any of 5 languages: en (English), nl (Nederlands), de (German), fr (French), es (Spanish)
sparql = SPARQLWrapper("https://stad.gent/sparql")
sparql.setReturnFormat(JSON)
points_df = pd.DataFrame(columns=["name", "latitude", "longitude"])

sparql.setQuery("""
    SELECT DISTINCT ?name ?coord ?attraction
    WHERE {
        ?attraction a <http://schema.org/TouristAttraction>.
        ?attraction <http://schema.org/name> ?name.
        ?attraction <http://purl.org/dc/terms/subject> <http://stad.gent/id/category/tourism/c30ce668-c471-4998-bfcb-fdb0688880d2>.
        ?attraction <http://schema.org/contactPoint> ?contact.
        ?contact <http://schema.org/geometry> ?geometry.
        ?geometry <http://www.opengis.net/ont/geosparql#asWKT> ?coord.
    }
    """
)

try:
	ret = sparql.queryAndConvert()
	points = []
	
	for r in ret["results"]["bindings"]:
		if r['name']['xml:lang'] == lang_of_interest:  
			points_df = points_df.append({"name": r['name']['value'], "latitude": float(r['coord']['value'][:-1].split("(")[1].split(" ")[1]), "longitude": float(r['coord']['value'][:-1].split("(")[1].split(" ")[0])}, ignore_index = True)

except Exception as e:
    print(e)

#listings_path = 'C:/workspace/UGent/BigDataScience/Project/BDS-Project-Group19/FrontEnd/data/listings.csv'
# #listings_detailed_path = 'C:/workspace/UGent/BigDataScience/Project/FrontEnd/data/listings_detailed.csv'
# calendar_path = 'C:/workspace/UGent/BigDataScience/Project/BDS-Project-Group19/FrontEnd/data/calendar.csv'
neighbourhoods_path = 'C:/workspace/UGent/BigDataScience/Project/BDS-Project-Group19/FrontEnd/data/neighbourhoods.csv'
neighbourhoods_geo_path = 'C:/workspace/UGent/BigDataScience/Project/BDS-Project-Group19/FrontEnd/data/neighbourhoods.geojson'


#listings = pd.read_csv(listings_path, encoding_errors='ignore')
#listings_detailed = pd.read_csv(listings_detailed_path, encoding_errors='ignore')
#calendar = pd.read_csv(calendar_path, encoding_errors='ignore')
neighbourhoods = pd.read_csv(neighbourhoods_path, encoding_errors='ignore')
neighbourhoods_geo = geojson = json.loads(open(neighbourhoods_geo_path, 'r').read())
# room_types = list(listings['room_type'].unique())
# room_type_options = [{'label': room_type, 'value': room_type} for room_type in room_types]
# room_type_options.insert(0, {'label': 'All room types', 'value': 'all'})

#neighbourhoods = list(neighbourhoods['coordinates'])
# neighbourhood_options = [{'label': neighbourhood, 'value': neighbourhood} for neighbourhood in neighbourhoods]
# neighbourhood_options.insert(0, {'label': 'All neighbourhoods', 'value': 'all'})