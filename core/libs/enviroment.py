#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- coding: binary -*-

import re
import os
import sys
from bs4 import BeautifulSoup
from functions import Utilities
from core.libs.paint import color
from core.info import notifications

 #BeautifulSoup([your markup], "lxml")
 #markup_type=markup_type))

class interactive(Utilities):

    # Offset of path component to delete when converting to raw
    REM_OFFSET = 2
    RAWBASE = "https://raw.github.com/"
    SEARCH = "https://github.com/search"

    def __init__(self):
        self.__notify = notifications()
        self.__color = color()

    def extract(self, data):
        soup = BeautifulSoup(data, "lxml")
        for item in soup.findAll("p", {"class":"title"}):
            p = item.findAll("a")
            # The second link is the reference ...
            yield p[1].get("href")

    def is_last_page(self, data):
        soup = BeautifulSoup(data, "lxml")
        if soup.find("p", {"class":"title"}):
            return False
        else:
            return True

    def raw_url(self, p):
        p = p.strip("/")
        parts = p.split("/")
        del parts[self.REM_OFFSET]
        return self.RAWBASE + "/".join(parts)

    def make_file_name(self, p):
        p = p.strip("/")
        parts = p.split("/")
        return parts[0] + "." + parts[1]

    def __quit(self, query):
        if query == 'q':
            self.pi('{}Exiting Treasure ...'.format(self.__notify.INFO))
            exit(0)

    def dump_code(self, query, listonly=False):
        self.__quit(query) # Check if users wants to quit.

        if query == '' or query == ' ':
            self.pi(' {} Empty code searches are not allowed.'.format(self.__notify.ERROR))
            exit(0)

        self.pi("\n {}Hunting for {}".format(self.__notify.INFO, query))

        page = 1
        breakpoint = 1
        while breakpoint == 1:
            params = dict(
                q = query,
                type = "Code",
                p = page
                )

            request = self.PostRequest(self.SEARCH, params)
            if self.is_last_page(request.content):
                self.pi('** No more results for {} **'.format(query))
                breakpoint = 2 # Break the while loop.
                break

            for u in self.extract(request.content):
                ru = self.raw_url(u)
                if listonly:
                    print ru
                else:
                    fn = self.make_file_name(u)
                    ret = self.GetRequest(ru)

                    # If the content is still available on github, take it.
                    if ret.status_code == 200:
                        code_dump_path = '{}.code.dump'.format(query.replace(' ', '_'))

                        # When found. Notify the user.
                        self.pi(" {}".format(self.__notify.FOUND) + ru.split('/')[-1] + " " + "from {}".format(ru.split('/')[3]))

                        # Dump all the code you find.
                        with open(code_dump_path, "a+") as file:
                            content_bool = self.string_bool_check(code_dump_path, ret.text.encode('utf-8'))
                            if content_bool is None:
                                try:
                                    # If there are any unicode errors, pass over them.
                                    file_content = ret.content.decode('utf-8').encode('utf-8')
                                except Exception:
                                    pass

                                file.write(file_content + '\n')
                                file.close()

                            elif content_bool is True:
                                pass
                    else:
                        pass
            page += 1

    def code_search(self):
        self.pi("""
 #######################################################
 #                                                     #
 #              """+self.__color.Y+"""Treasure"""+self.__color.N+""" - """+self.__color.G+"""HUNT"""+self.__color.N+""" """+self.__color.B+"""for"""+self.__color.N+""" """+self.__color.W+"""CODE"""+self.__color.N+"""               #
 #           Type q or ^C to exit """+self.__color.Y+"""Treasure"""+self.__color.N+"""             #
 #                                                     #
 # """+self.__color.R+"""Help ?"""+self.__color.N+""":                                             #
 # """+self.__color.C+"""1. https://help.github.com/articles/searching-code/"""+self.__color.N+""" #
 #                                                     #
 #######################################################""")

        breakpoint = 0 # Break point for the while loop.
        while breakpoint == 0:
            try:
                choice = self.select(" search|code: ")
                self.dump_code(choice)
            except KeyboardInterrupt:
                breakpoint == 1
                self.pi("\n{}Exiting Treasure ...".format(self.__notify.INFO))
                break
