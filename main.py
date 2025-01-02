import csv
from nsdotpy.session import NSSession
import nationstates

# some parts taken from https://gist.github.com/Kractero/36a1230f9d00d8d8afbdd6fa4f2f2af0 , credits to Kractero and thank you!
class ExtendedSession(NSSession):
    def __init__(self, session_name, session_version, username, user_agent, keybind):
        super().__init__(session_name, session_version, username, user_agent, keybind)

    def inscribe_nation_card(self):
        self.logger.info(f"({rowcount}/{rows}) Inscribing {self.nation}")
        url = f"https://www.nationstates.net/page=deck/card={nation.dbid}/season=4"

        data = {
            "confirm_modify_my_card": "1"
        }

        self.request(url, data=data)

keybind = "space"
UA = ""
password = ""

session = ExtendedSession("Card Inscriber", "1.0.0", "Ducky", UA, keybind)
api = nationstates.Nationstates(f"Card Inscriber by Ducky used by {UA}")
rowcount = 0
rows = len(list(csv.reader(open('puppets.csv'))))

with open('puppets.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        if session.login(row[0], password): # replace password with row[1] if nation,password format
            rowcount+= 1
            nation = api.nation(row[0])
            session.inscribe_nation_card()