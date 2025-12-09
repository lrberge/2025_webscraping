


# 1) get the HTML
import requests
page = requests.get("https://www.europarl.europa.eu/meps/en/full-list/all")

# 2) parse the HTML
from bs4 import BeautifulSoup
soup = BeautifulSoup(page.text, 'html.parser')

# 3) select the elements you want
all_elems = soup.select("a.erpl_member-list-item-content")

# 4) obtain the "text content" of the element with .get_text()

# exemple pour le nom
all_elems[0].select(".erpl_title-h4")[0].get_text().strip()

# on boucle pour obtenir tous les noms et pays

all_names = list()
all_countries = list()
for i in range(len(all_elems)):
  all_names.append(all_elems[i].select(".erpl_title-h4")[0].get_text().strip())
  all_countries.append(all_elems[i].select(".sln-additional-info")[1].get_text().strip())



#
# Exercice 2
#

# Objectif: obtenir les dates de naissance des 5 premiers députés

import time

all_births = list()
n_done = 0
for i in range(50):
  indiv = all_elems[i]

  print(f"scraping {all_names[i]}")

  # le lien
  url = indiv.get_attribute_list("href")[0]

  page_indiv = requests.get(url)
  soup_indiv = BeautifulSoup(page_indiv.text, 'html.parser')

  birth = soup_indiv.select("time.sln-birth-date")
  
  if len(birth) == 0:
    birth_fmt = "no birth date"
  else:
    n_done += 1
    birth_fmt = birth[0].get_text()
  
  all_births.append(birth_fmt)
  
  if n_done >= 5:
    break
  
  time.sleep(2)


