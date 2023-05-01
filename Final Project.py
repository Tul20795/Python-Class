import requests #lets you make a http request, i had to add it through command prompt after installing python correctly lol
import json #for converting Python objects like dictionaries and lists to JSON format and vice versa. Helpful for extracing data from API's


myAPI = "AIzaSyBob6jB2uwph5wZMtaeG5L-28i1r1QAwWo" #my google API, it was free unless i use a stupid amount of requests.

#get the zip code from user
Zipcode = input("Enter your zip code: ")

GoogleSearch = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query=rock+climbing+gyms+in+{Zipcode}&key={myAPI}" #base search of "rock climbing gyms in"
#makes a google search in google places API, uses the zipcode and personal API 

response = requests.get(GoogleSearch) # Uses the request to contact the HTTP and then google searches the text above.
DataExtraction = response.json() #returns the JSON data as a python dictionary.


results = DataExtraction['results'][:3] #Extracted Results with how many you would like. I only want 3
print("\nTop 3 results:\n")


#Making Data look decent
for result in results:
    name = result['name']
    location = result['formatted_address']
    print(f"Name: {name}\nLocation: {location}\n")


