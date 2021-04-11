#!/usr/bin/env python
# coding: utf-8

import requests
import os
from bs4 import BeautifulSoup

req = requests.get('http://unmotparjour.fr/random/')
soup = BeautifulSoup(req.text, 'html.parser')

def main() :

    ## Le mot
    os.system("clear")
    mot = soup.find_all('h1')[1].text
    print("\n \t" + mot)

    ## Information sur le mot
    mot = soup.find('div', class_='entry-content').text

    # Genre du mot
    print("\n\t" + mot.splitlines()[1] + "\n")

    # Definition du mot
    i = 2
    while (i < len(mot.splitlines())) :
        for j in range(5) :
            if (mot.splitlines()[i][0] == str(j)) :
                print("\n")
        print("\t" + mot.splitlines()[i])
        i+=1
    print("\n\n\n\n")
    
    input('press enter\n')

main()