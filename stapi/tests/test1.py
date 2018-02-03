import stapi
rc = stapi.RestClient()
loracus = rc.astronomicalObject.get("ASMA0000012319")
print(loracus)
print(dir(loracus))
