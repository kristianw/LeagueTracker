#/usr/bin/python3

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import re
import logging
import json
from bs4 import BeautifulSoup
import requests

class League:
    def __init__(self):
        url = ""
        name = ""
        season = ""
        gender = ""
        gameDay = ""
        section = ""
        rounds = ""
        teamName = ""

    def getLeagueInfo(self):
        pass

    def readConfigFile(self):
        try:
            with open('config.json') as jsonFile:
                configData = json.load(jsonFile)
                for data in configData['league']:
                    self.url = data['url']
                    self.teamName = data['teamName']
        except Exception as err:
            print(err)

    def setUpLeague(self):
        try:
            # Set up request and confirm URL can be accessed
            page = requests.get(self.url)
            if page.status_code == 200:
                # Extract HTML with BS 
                soup = BeautifulSoup(page.content, 'html.parser')

                # Find season fixture in HTML
                leagueFixture = soup.find_all('div', class_='roundlist')

            else:
                print("Unable to connect to webpage (Status %s): %s" % (page.status_code, self.url))


        except Exception as err:
            print(err)


class Round:
    def __init__( self):
        roundNumber = ""
        date = ""
        time = ""
        homeTeam = ""
        awayTeam = ""
        location = ""
        courtNumber = ""



if __name__ == '__main__':
    league = League()
    league.readConfigFile()
    league.setUpLeague()
