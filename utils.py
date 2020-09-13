import requests 
from bs4 import BeautifulSoup

def get_acr(term: str) -> object:

    if not term:
        return {"acr": "No term", "definition": "None"}

    URL = f'https://acronyms.thefreedictionary.com/{term}'

    r = requests.get(URL)
    soup = BeautifulSoup(r.text, 'html.parser')

    try:
        table = soup.find(id="AcrFinder")
        tr = table.findAll("tr")[1]
    except:
        return {"acr": "Not found", "definition": "None"}


    acronym = tr.find("td", class_="acr").text
    definition = tr.findAll("td")[1].text

    return {"acr": acronym, "definition": definition}