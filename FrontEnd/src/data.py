import pandas as pd
import json
from SPARQLWrapper import SPARQLWrapper, JSON

# can be changed to any of 5 languages: en (English), nl (Nederlands), de (German), fr (French), es (Spanish)
lang_of_interest = "en"
sparql = SPARQLWrapper("https://stad.gent/sparql")
sparql.setReturnFormat(JSON)
points_df = pd.DataFrame(columns=["name", "latitude", "longitude", "uri"])

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
            points_df = points_df.append({"name": r['name']['value'], "latitude": float(r['coord']['value'][:-1].split("(")[1].split(" ")[1]), "longitude": float(r['coord']['value'][:-1].split("(")[1].split(" ")[0]), "uri": str(r['attraction']['value'])}, ignore_index = True)

except Exception as e:
    print(e)

neighbourhoods_path = '../data/neighbourhoods.csv'
neighbourhoods_geo_path = '../data/neighbourhoods.geojson'

neighbourhoods = pd.read_csv(neighbourhoods_path, encoding_errors='ignore')
neighbourhoods_geo = geojson = json.loads(
    open(neighbourhoods_geo_path, 'r').read())
