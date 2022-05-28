import pandas as pd
import json
from SPARQLWrapper import SPARQLWrapper, JSON

# can be changed to any of 5 languages: en (English), nl (Nederlands), de (German), fr (French), es (Spanish)

sparql = SPARQLWrapper("https://stad.gent/sparql")
sparql.setReturnFormat(JSON)
sparql2 = SPARQLWrapper("https://demo.openlinksw.com/sparql")
sparql2.setReturnFormat(JSON)

def getPoints(lang_of_interest):
    if lang_of_interest == None:
        lang_of_interest = "en" #set English as the default setting here

    points_df = pd.DataFrame(columns=["name", "desc", "latitude", "longitude", "uri"])
    sparql.setQuery("""
        SELECT DISTINCT ?name ?desc ?coord ?attraction
        WHERE {
            ?attraction a <http://schema.org/TouristAttraction>.
            ?attraction <http://schema.org/name> ?name
            FILTER (lang(?name) = 'lang_of_interest').
            ?attraction <http://schema.org/description> ?desc
            FILTER (lang(?desc) = 'lang_of_interest').
            ?attraction <http://purl.org/dc/terms/subject> <http://stad.gent/id/category/tourism/c30ce668-c471-4998-bfcb-fdb0688880d2>.
            ?attraction <http://schema.org/contactPoint> ?contact.
            ?contact <http://schema.org/geometry> ?geometry.
            ?geometry <http://www.opengis.net/ont/geosparql#asWKT> ?coord.
        }
        """.replace('lang_of_interest', lang_of_interest)
    )

    try:
        ret = sparql.queryAndConvert()
        for r in ret["results"]["bindings"]:
            points_df = points_df.append({"name": r['name']['value'], "desc": r['desc']['value'], "latitude": float(r['coord']['value'][:-1].split("(")[1].split(" ")[1]), "longitude": float(r['coord']['value'][:-1].split("(")[1].split(" ")[0]), "uri": str(r['attraction']['value'])}, ignore_index = True)
          
    except Exception as e:
        print(e)

    return points_df  

def getImages(attraction_uri):
    images = []
    sparql.setQuery("""
        SELECT  ?image
        WHERE {
            <attraction_uri> <http://schema.org/image> ?image
        }
        """.replace('attraction_uri', attraction_uri)
    )

    try:
        ret = sparql.queryAndConvert()
        for i, r in enumerate(ret["results"]["bindings"]):
            images.append({"key": str(i), "src": r['image']['value'], "img_style": {"height":"300px", "width":"100%", "object-fit":"cover"}})
          
    except Exception as e:
        print(e)

    return images  

def getRecords(attraction_uri):
    records_df = pd.DataFrame(columns=["title", "desc", "museum"])
    sparql2.setQuery("""
        PREFIX cidoc: <http://www.cidoc-crm.org/cidoc-crm/>
        PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
        SELECT DISTINCT ?title ?desc ?museum1 ?museum2
        WHERE {
          SERVICE <https://stad.gent/sparql> {
            SELECT DISTINCT ?title ?desc ?keeper ?museum1
            WHERE {
              <attraction_uri> <http://schema.org/name> ?name
              FILTER (lang(?name) = 'nl').
              ?object cidoc:P102_has_title ?title
              FILTER (regex(?title, ?name, "i")).
              OPTIONAL {?object cidoc:P3_has_note ?desc}
              ?object cidoc:P50_has_current_keeper ?keeper.
              OPTIONAL {?keeper skos:prefLabel ?museum1}
            }
          }
          OPTIONAL {
            SERVICE <https://query.wikidata.org/sparql> {
              ?keeper rdfs:label ?museum2
              FILTER (lang(?museum2) = "nl").
            }
          }
        }
        """.replace("attraction_uri", attraction_uri))
        
    try:
        ret = sparql2.queryAndConvert()
        
        for r in ret["results"]["bindings"]:
            museum = ""
            if 'museum1' in r: museum = r['museum1']['value']
            if 'museum2' in r: museum = r['museum2']['value']
            desc = ""
            if 'desc' in r: desc = r['desc']['value']
            records_df = records_df.append({"title": r['title']['value'], "desc": desc, "museum": museum}, ignore_index = True)
          
    except Exception as e:
        print(e)

    return records_df
