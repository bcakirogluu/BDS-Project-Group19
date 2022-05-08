import pandas as pd
import json

listings_path = 'C:/workspace/UGent/BigDataScience/Project/FrontEnd/data/listings.csv'
#listings_detailed_path = 'C:/workspace/UGent/BigDataScience/Project/FrontEnd/data/listings_detailed.csv'
calendar_path = 'C:/workspace/UGent/BigDataScience/Project/FrontEnd/data/calendar.csv'
neighbourhoods_path = 'C:/workspace/UGent/BigDataScience/Project/FrontEnd/data/neighbourhoods.csv'
neighbourhoods_geo_path = 'C:/workspace/UGent/BigDataScience/Project/FrontEnd/data/neighbourhoods.geojson'

listings = pd.read_csv(listings_path, encoding_errors='ignore')
#listings_detailed = pd.read_csv(listings_detailed_path, encoding_errors='ignore')
calendar = pd.read_csv(calendar_path, encoding_errors='ignore')
neighbourhoods = pd.read_csv(neighbourhoods_path, encoding_errors='ignore')
neighbourhoods_geo = geojson = json.loads(open(neighbourhoods_geo_path, 'r').read())
room_types = list(listings['room_type'].unique())
room_type_options = [{'label': room_type, 'value': room_type} for room_type in room_types]
room_type_options.insert(0, {'label': 'All room types', 'value': 'all'})

#neighbourhoods = list(neighbourhoods['coordinates'])
# neighbourhood_options = [{'label': neighbourhood, 'value': neighbourhood} for neighbourhood in neighbourhoods]
# neighbourhood_options.insert(0, {'label': 'All neighbourhoods', 'value': 'all'})