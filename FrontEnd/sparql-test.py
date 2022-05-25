from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("https://stad.gent/sparql")
sparql.setReturnFormat(JSON)

sparql.setQuery("""
    SELECT DISTINCT ?attraction ?coord
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
    for r in ret["results"]["bindings"]:
        print(r)
except Exception as e:
    print(e)
