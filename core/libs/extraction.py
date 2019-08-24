#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- coding: binary -*-

import re
import json
from functions import Utilities
from core.info import notifications

class extract(Utilities):

    def __init__(self):
        self.__found = [] # Found items.
        self.__unique = {} # Unique items.
        self.__notify = notifications()

    def InstagramAccessTokens(self, fwiat):
        tokensrch = re.compile(r'[0-9]{7,10}\.[0-9a-f]{5,8}\.[0-9a-f]{32}')
        with open(fwiat, 'rb') as FileWithAccessToken:
            for token in FileWithAccessToken:
                token = token.replace('\n', '')
                if tokensrch.findall(token):
                    self.__found.append(token)

        for item in self.__found:
            self.__unique[item] = 1

        #returns a list of unique link(s)
        return self.__unique.keys()

    # Grab Bitcoin Wallet Addresses
    def BitcoinWalletAddress(self, fwbw):
        btcwsrch = re.compile(r'(?<![a-km-zA-HJ-NP-Z0-9])[13][a-km-zA-HJ-NP-Z0-9]{26,30}(?![a-km-zA-HJ-NP-Z0-9])|(?<![a-km-zA-HJ-NP-Z0-9])[13][a-km-zA-HJ-NP-Z0-9]{33,35}(?![a-km-zA-HJ-NP-Z0-9])')
        with open(fwbw, 'rb') as FileWithBitcoinAddress:
            for wallet in FileWithBitcoinAddress:
                wallet = wallet.replace('\n', '')
                if btcwsrch.findall(wallet):
                    self.__found.append(wallet)

        for item in self.__found:
            self.__unique[item] = 1

        #returns a list of unique link(s)
        return self.__unique.keys()

    def IPv6Addresses(self, fowipv6):
        ipv6srch = re.compile(r"^\s*((([0-9A-Fa-f]{1,4}:){7}([0-9A-Fa-f]{1,4}|:))|(([0-9A-Fa-f]{1,4}:){6}(:[0-9A-Fa-f]{1,4}|((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){5}(((:[0-9A-Fa-f]{1,4}){1,2})|:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){4}(((:[0-9A-Fa-f]{1,4}){1,3})|((:[0-9A-Fa-f]{1,4})?:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){3}(((:[0-9A-Fa-f]{1,4}){1,4})|((:[0-9A-Fa-f]{1,4}){0,2}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){2}(((:[0-9A-Fa-f]{1,4}){1,5})|((:[0-9A-Fa-f]{1,4}){0,3}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){1}(((:[0-9A-Fa-f]{1,4}){1,6})|((:[0-9A-Fa-f]{1,4}){0,4}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(:(((:[0-9A-Fa-f]{1,4}){1,7})|((:[0-9A-Fa-f]{1,4}){0,5}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:)))(%.+)?\s*$")

        with open(fowipv6, 'rb') as FileWithCCN:
            for line in FileWithCCN:
                ipv6addr = line.replace('\n', '')
                if ipv6srch.findall(ipv6addr):
                    self.__found.append(ipv6addr)

        for item in self.__found:
            self.__unique[item] = 1

        return self.__unique.keys()

    def IPv4Addresses(self, foi):
        ipv4srch = re.compile(r'([0-9]+)(?:\.[0-9]+){3}')

        with open(foi, 'rb') as FileWithIPv4:
            for line in FileWithIPv4:
                ipv4 = line.replace('\n', '')
                if ipv4srch.findall(ipv4):
                    self.__found.append(ipv4)

        for item in self.__found:
            self.__unique[item] = 1

        return self.__unique.keys()

    def PublicSSHKeys(self, name):

        # Json API Response
        APIR = self.GetRequest("https://api.github.com/users/{}/keys".format(name)).json()

        try:
            if APIR.has_key('message') is True and APIR['message'] == "Not Found":
                print "{}{} doesn't exist.".format(notifications.ERROR, name)
                exit(0)
        except AttributeError:
            pass

        if APIR == []:
            print '' # Clean print.
            print "{}{} does not have any public ssh keys available at this time.".format(notifications.INFO, name)

        if APIR != []:

            # Length of the keys list array.
            lok = len(APIR)

            for i in APIR[0:lok]:

                print '' # Clean print | for readable format.
                print notifications.INFO + str(i['id']), 'Owns this SSH key.'
                print '----------------------------------'
                print i['key']

        print "" # Clean print

    def BlockchainIdentifiers(self, fobli):
        mailsrch = re.compile(r'[0-9a-f]{5,8}\-[0-9a-f]{4}\-[0-9a-f]{4}\-[0-9a-f]{4}\-[0-9a-f]{5,13}')
        with open(fobli, 'rb') as FileWithBlockchainIdentifiers:
            for line in FileWithBlockchainIdentifiers:
                identifiers = line.strip()
                if mailsrch.findall(identifiers):
                    self.__found.append(identifiers)

        for item in self.__found:
            self.__unique[item] = 1

        return self.__unique.keys()

    def FacebookAccessTokens(self, fofaat):
        mailsrch = re.compile(r'access_token\=[0-9]{15}\|(.*){27}')
        with open(fofaat, 'rb') as FacebookAccessTokens:
            for line in FacebookAccessTokens:
                token = line.strip()
                if mailsrch.findall(token):
                    self.__found.append(token)

        for item in self.__found:
            self.__unique[item] = 1

        return self.__unique.keys()
