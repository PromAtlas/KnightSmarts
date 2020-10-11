from bs4 import BeautifulSoup
import requests

class CollegeHelper:
    def __init__(self):
        self.thing = 1

    def get_school_id(self, school_name):
        school_name.replace(" ", "+")
        url = "https://nces.ed.gov/collegenavigator/?q=" + school_name + "&s=all&l=93"
        html = requests.get(url).content
        soup = BeautifulSoup(html, "html.parser")

        table = soup.find("table", {"class": "resultsTable"})
        link = table.find_next("a")["href"]
        school_id = link[len(link) - 6 :]

        return school_id

    def get_school_json(self, school_name):
        output = {}
        school_id = self.get_school_id(school_name)
        url = "https://nces.ed.gov/collegenavigator/?id=" + school_id
        html = requests.get(url).content
        soup = BeautifulSoup(html, "html.parser")

        dash = soup.find("div", {"class": "collegedash"})
        name = dash.find("span", {"class": "headerlg"})
        output["name"] = name.contents[0]
        output["address"] = name.next_sibling.next_sibling
        output["website"] = name.find_next("a").contents[0]

        net_price_tab = soup.find("div", {"id": "divctl00_cphCollegeNavBody_ucInstitutionMain_ctl02"})
        output["price"] = net_price_tab.find_next("tbody").contents[0].contents[3].contents[0]

        return output

# SAMPLE JSON
# {"name": "University of Central Florida", "address": 
# "4000 Central Florida Blvd, Orlando, Florida 32816", 
# "website": "www.ucf.edu/", "price": "11,617"}