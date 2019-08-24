#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- coding: binary -*-

# Native imports
import os
import sys
import random
import datetime

# Dependency imports.
import requests

class Utilities(object):

    def __init__(self):
        pass

    def pi(self, pdata=''):
        # Print information to the console.
        print pdata

    #Get Request
    def GetRequest(self, url):
        GetRequestSession = requests.Session()
        return GetRequestSession.get(url, headers=self.agent())

    #Post Request through get request format.
    def PostRequest(self, url, data):
        PostRequestSession = requests.Session()
        return PostRequestSession.get(url, params=data, headers=self.agent())

    # Useful for interactive operations
    def select(self, message):
        while True:
            select = raw_input("\n{}".format(message))
            return select

    # String boolean self-check.
    def string_bool_check(self, file_name, string): # Check if string is in a file.
        #return a NoneType if the string is not in the file.
        #.readlines() May be a problem is database files get too large.

        if os.path.exists(file_name) is False:
            MakeFile = open(file_name, 'a').close()

        if os.path.exists(file_name) is True:
            pass

        with open(file_name, 'r') as file:
            for item in file:
                item = item.replace("\n", '')
                if string.decode('utf-8').encode('utf-8') in item:
                    return True

    def agent(self):
        """Produces a valid Browser User-Agent string.
        """

        platform = random.choice(
        ['Macintosh',
        'Windows',
        'X11']
        )

        if platform == 'Macintosh':
            os  = random.choice(
            ['68K',
            'PPC']
            )

        elif platform == 'Windows':
            os  = random.choice(
            ['Win3.11',
            'WinNT3.51',
            'WinNT4.0',
            'Windows NT 5.0',
            'Windows NT 5.1',
            'Windows NT 5.2',
            'Windows NT 6.0',
            'Windows NT 6.1',
            'Windows NT 6.2',
            'Win 9x 4.90',
            'Win95',
            'Win98',
            'WindowsCE']
            )

        elif platform == 'X11':
            os  = random.choice(['Linux i686', 'Linux x86_64'])

        browser = random.choice(['chrome', 'firefox', 'ie'])

        if browser == 'chrome':
            webkit = str(random.randint(500, 599))
            version = str(random.randint(0, 28)) + '.0' + str(random.randint(0, 1500)) + '.' + str(random.randint(0, 999))
            return {"User-Agent":str('Mozilla/5.0 (' + str(os) + ') AppleWebKit/' + webkit + '.0 (KHTML, like Gecko) Chrome/' + version + ' Safari/' + webkit)}

        elif browser == 'firefox':
            currentYear = datetime.date.today().year
            year = str(random.randint(2000, currentYear))
            month = random.randint(1, 12)

            if month < 10:
                month = '0' + str(month)
            else:
                month = str(month)

            day = random.randint(1, 30)

            if day < 10:
                day = '0' + str(day)

            else:
                day = str(day)

            gecko = year + month + day
            version = str(random.randint(1, 21)) + '.0'
            return {"User-Agent":str('Mozilla/5.0 (' + os + '; rv:' + version + ') Gecko/' + gecko + ' Firefox/' + version)}

        elif browser == 'ie':

            version = str(random.randint(1, 10)) + '.0'
            engine = str(random.randint(1, 5)) + '.0'
            option = random.choice(
            [True,
            False]
            )

            if option == True:
                token = random.choice(['.NET CLR', 'SV1', 'Tablet PC', 'Win64; IA64', 'Win64; x64', 'WOW64']) + '; '
            else:
                token = ''
            return {"User-Agent":str('Mozilla/5.0 (compatible; MSIE ' + version + '; ' + os + '; ' + token + 'Trident/' + engine + ')')}
