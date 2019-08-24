#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- coding: binary -*-

import re
from extraction import extract
from functions import Utilities
from core.info import notifications

class Take(Utilities):

    def __init__(self):
        notifications.__init__(self)

        # Variables
        self.__found = [] # Found items.
        self.__unique = {} # Unique items

        # Instantiations variables
        self.__extract = extract()
        self.__notify = notifications()

    def InstagramAccessToken(self, file):
        IATExtract = self.__extract.InstagramAccessTokens(file)

        if len(IATExtract) is 0:
            self.pi("{}No Instagram access tokens in {}".format(self.__notify.FAIL, file))

        if len(IATExtract) > 0:
            for instance in IATExtract:
                IATRegex = re.compile(r'[0-9]{7,10}\.[0-9a-f]{5,8}\.[0-9a-f]{32}')
                IATContainer = IATRegex.search(instance)
                IATs = IATContainer.group()
                self.__found.append(IATs)

            for item in self.__found:
                self.__unique[item] = 1

            self.pi("--------------------------------------------")
            self.pi("      EXTRACTED Instagram access tokens     ")
            self.pi("--------------------------------------------")

            count = 0
            for output in self.__unique:
                count += 1
                self.pi(self.__notify.INFO + output)

            if count is 1:
                self.pi("\n" + self.__notify.STATUS + "Extracted {} instagram access token from {}\n".format(str(count), file))

            elif count > 1:
                self.pi("\n" + self.__notify.STATUS + "Extracted {} instagram access tokens from {}\n".format(str(count), file))

    def IPv6Addresses(self, file):
        IPv6Extract = self.__extract.IPv6Addresses(file)

        if len(IPv6Extract) is 0:
            self.pi("{}No IPv6 addresses in {}".format(self.__notify.FAIL, file))

        if len(IPv6Extract) > 0: # legit file, containing at least 1 ipv6 number.
            for instance in IPv6Extract:
                IPv6Regex = re.compile(r'^\s*((([0-9A-Fa-f]{1,4}:){7}([0-9A-Fa-f]{1,4}|:))|(([0-9A-Fa-f]{1,4}:){6}(:[0-9A-Fa-f]{1,4}|((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){5}(((:[0-9A-Fa-f]{1,4}){1,2})|:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){4}(((:[0-9A-Fa-f]{1,4}){1,3})|((:[0-9A-Fa-f]{1,4})?:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){3}(((:[0-9A-Fa-f]{1,4}){1,4})|((:[0-9A-Fa-f]{1,4}){0,2}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){2}(((:[0-9A-Fa-f]{1,4}){1,5})|((:[0-9A-Fa-f]{1,4}){0,3}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){1}(((:[0-9A-Fa-f]{1,4}){1,6})|((:[0-9A-Fa-f]{1,4}){0,4}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(:(((:[0-9A-Fa-f]{1,4}){1,7})|((:[0-9A-Fa-f]{1,4}){0,5}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:)))(%.+)?\s*$')
                IPv6List = IPv6Regex.search(instance)
                IPv6s = IPv6List.group()
                self.__found.append(IPv6s)

            for item in FoundIPV6s: self.__unique[item] = 1

            self.pi("--------------------------")
            self.pi("      EXTRACTED IPv6s     ")
            self.pi("--------------------------")

            count = 0
            for output in self.__unique:
                count += 1
                self.pi(self.__notify.INFO + output)

            if count is 1:
                self.pi("\n" + self.__notify.STATUS + "Extracted {} IPv6 address from {}\n".format(str(count), file))

            elif count > 1:
                self.pi("\n" + self.__notify.STATUS + "Extracted {} IPv6 addresses from {}\n".format(str(count), file))

    def IPv4Addresses(self, file):
        IPv4Extract = self.__extract.IPv4Addresses(file) # Collected ipv4s

        if len(IPv4Extract) is 0:
            self.pi("{}No IPv4 addresses in {}".format(self.__notify.FAIL, file))

        if len(IPv4Extract) > 0: # legit file, containing at least 1 ipv4 address.
            for instance in IPv4Extract:
                IPv4Regex = re.compile(r'([0-9]+)(?:\.[0-9]+){3}')
                IPv4Container = IPv4Regex.search(instance)
                IPv4s = IPv4Container.group()
                self.__found.append(IPv4s)

            for item in self.__found:
                self.__unique[item] = 1

            self.pi("--------------------------")
            self.pi("      EXTRACTED IPV4s     ")
            self.pi("--------------------------")

            count = 0
            for output in self.__unique:
                count += 1
                self.pi(self.__notify.INFO + output)

            if count is 1:
                self.pi("\n" + self.__notify.STATUS + "Extracted {} IPv4 address from {}\n".format(str(count), file))

            elif count > 1:
                self.pi("\n" + self.__notify.STATUS + "Extracted {} IPv4 addresses from {}\n".format(str(count), file))

    def BTCAddresses(self, file):
        BTCWAExtract = self.__extract.BitcoinWalletAddress(file)

        if len(BTCWAExtract) is 0:
            self.pi("{}No Bitcoin addresses in {}".format(self.__notify.FAIL, file))

        if len(BTCWAExtract) > 0:
            for instance in BTCWAExtract:
                BTCWalletRegex = re.compile(r'(?<![a-km-zA-HJ-NP-Z0-9])[13][a-km-zA-HJ-NP-Z0-9]{26,30}(?![a-km-zA-HJ-NP-Z0-9])|(?<![a-km-zA-HJ-NP-Z0-9])[13][a-km-zA-HJ-NP-Z0-9]{33,35}(?![a-km-zA-HJ-NP-Z0-9])')
                wallet = BTCWalletRegex.findall(instance)

                for address in wallet:
                    self.__found.append(address)

            for item in self.__found:
                self.__unique[item] = 1

            self.pi("--------------------------")
            self.pi("  EXTRACTED BTC Addresses ")
            self.pi("--------------------------")

            count = 0
            for output in self.__unique:
                count += 1
                self.pi(self.__notify.INFO + output)

            if count is 1:
                self.pi("\n" + self.__notify.STATUS + "Extracted {} Bitcoin address from {}\n".format(str(count), file))

            elif count > 1:
                self.pi("\n" + self.__notify.STATUS + "Extracted {} Bitcoin addresses from {}\n".format(str(count), file))

    def FacebookAccessTokens(self, file):
        FATExtract = self.__extract.FacebookAccessTokens(file)

        if len(FATExtract) is 0:
            self.pi("{}No Facebook Access Tokens in {}".format(self.__notify.FAIL, file))

        if len(FATExtract) > 0:
            for instance in FATExtract:
                FATRegex = re.compile(r'(access_token\=[0-9]{15}\|(.*){27})')
                FATList = FATRegex.search(instance)
                FATs = FATList.group()
                self.__found.append(FATs)

            for item in self.__found:
                self.__unique[item] = 1

            self.pi("--------------------------")
            self.pi("  Facebook Access Tokens  ")
            self.pi("--------------------------")

            count = 0
            for output in self.__unique:
                count += 1
                self.pi(self.__notify.INFO + output)

            if count is 1:
                self.pi("\n" + self.__notify.STATUS + "Extracted {} Facebook Access Token from {}\n".format(str(count), file))

            elif count > 1:
                self.pi("\n" + self.__notify.STATUS + "Extracted {} Facebook Access Tokens from {}\n".format(str(count), file))

    def BlockchainIdentifiers(self, file):
        BCIDSExtract = self.__extract.BlockchainIdentifiers(file)
        if len(BCIDSExtract) is 0:
            self.pi("{}No Blockchain Identifiers in {}".format(self.__notify.FAIL, file))

        if len(BCIDSExtract) > 0:
            for instance in BCIDSExtract:
                BCIDSRegex = re.compile(r'[0-9a-f]{5,8}\-[0-9a-f]{4}\-[0-9a-f]{4}\-[0-9a-f]{4}\-[0-9a-f]{5,13}')
                BCIDSList = BCIDSRegex.search(instance)
                BCIDSs = BCIDSList.group()
                self.__found.append(BCIDSs)

            for item in self.__found:
                self.__unique[item] = 1

            self.pi("--------------------------")
            self.pi("  Blockchain Identifiers  ")
            self.pi("--------------------------")

            count = 0
            for output in self.__unique:
                count += 1
                self.pi(self.__notify.INFO + output)

            if count is 1:
                self.pi("\n" + self.__notify.STATUS + "Extracted {} Blockchain Identifier from {}\n".format(str(count), file))

            elif count > 1:
                self.pi("\n" + self.__notify.STATUS + "Extracted {} Blockchain Identifiers from {}\n".format(str(count), file))
