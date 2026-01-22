import requests

URL ="http://api.open-notify.org/astros.json"

response = requests.get(URL)

if response.ok:
    print("Connected")
else:
    print("Check url")
output = response.json().get('people')
print(output)
#for person in output:
    #print(person.get('name'))

#ne = output.get('people').get('name')
#ct = output.get('people').get('craft')

#print(f"names and space craft name is {ne},{ct}")