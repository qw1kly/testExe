from bs4 import BeautifulSoup
import requests
from urllib.parse import quote
import time
import re
import csv


letters_num = {}

checked = []

letters = "АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЁЩЯЙЭ"

sub_letters = "вджилнпсухчщю"

for i in letters:
    letters_num[i] = 0

for i in letters:
    if i == 'А':
        url = f"https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&from={quote(f'<b>{i}<2%Fb>')}"
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")
        all_animals = soup.find_all('div', class_='mw-category-group')
        subjects = all_animals[2].text.split("\n")
        for j in range(1, len(subjects)):
            letters_num[subjects[j][0]]+=1
            checked.append(subjects[j])
    for j in range(len(sub_letters)):
        url = f"https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&from={quote(f'{i+sub_letters[j]}')}"
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")
        all_animals = soup.find_all('div', class_='mw-category-group')
        if len(all_animals) > 2:
            subjects = all_animals[2].text.split("\n")
        else:
            try:
                subjects = all_animals[1].text.split("\n")
            except:
                subjects = all_animals[0].text.split("\n")

        for j in range(1, len(subjects)):
            if subjects[j] not in checked and subjects[j][0] in letters:
                letters_num[subjects[j][0]] += 1
                checked.append(subjects[j])
    print(letters_num)

data = list(map(lambda x: list(x), letters_num.items()))

with open('beasts.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)