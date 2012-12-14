# -*- coding: utf-8 -*-

# Redtube Plugin for Elisa Multimedia center
#
# Written by Koelie (koelie666@gmail.com)
# heavily based on Youtube plugin 
# and borrows code from the XMBC Redtube plugin

# Original Youtube plugin copyright notice:
# Elisa - Home multimedia server
# Copyright (C) 2006-2008 Fluendo Embedded S.L. (www.fluendo.com).
# All rights reserved.
#
# This file is available under one of two license agreements.
#
# This file is licensed under the GPL version 3.
# See "LICENSE.GPL" in the root of this distribution including a special
# exception to use Elisa with Fluendo's plugins.
#
# The GPL part of Elisa is also available under a commercial licensing
# agreement from Fluendo.
# See "LICENSE.Elisa" in the root directory of this distribution package
# for details on that license.

import urllib2
import traceback
from math import floor

class RedTubeClient:
  def get_videos(self, loc='new', page=1):
    data = urllib2.urlopen('http://www.redtube.com/' + loc + '?page=' + str(page))
    parser = redTube()
    parser.parse(data.read())
    return parser.get_entries()

  def get_flv_video_url(self, video_id):
    v_fileFloat = int(floor(float(video_id)/1000));
    p_file = "%07d" % (int(video_id))
    v_fileFloat = "%07d" % (int(v_fileFloat))
    
    map = ("R", "1", "5", "3", "4", "2", "O", "7", "K", "9", "H", "B", "C", "D", "X", "F", "G", "A", "I", "J", "8", "L", "M", "Z", "6", "P", "Q", "0", "S", "T", "U", "V", "W", "E", "Y", "N")
    mapping = ""
    myInt = 0;
    
    for a in range(7):
      myInt = myInt + int(p_file[a])*(a + 1)
    myChar = "%s" % (myInt)
    myInt = 0
    for a in range(len(myChar)):
      myInt = myInt + int(myChar[a])
            
    newChar = "%02d" % (myInt)

    mapping = mapping + map[ord(p_file[3]) - 48 + myInt + 3]
    mapping = mapping + newChar[1]
    mapping = mapping + map[ord(p_file[0]) - 48 + myInt + 2]
    mapping = mapping + map[ord(p_file[2]) - 48 + myInt + 1]
    mapping = mapping + map[ord(p_file[5]) - 48 + myInt + 6]
    mapping = mapping + map[ord(p_file[1]) - 48 + myInt + 5]
    mapping = mapping + newChar[0]
    mapping = mapping + map[ord(p_file[4]) - 48 + myInt + 7]
    mapping = mapping + map[ord(p_file[6]) - 48 + myInt + 4]
    
    flv_url = "http://dl.redtube.com/_videos_t4vn23s9jc5498tgj49icfj4678/%s/%s.flv" % (v_fileFloat, mapping)
    return flv_url


from sgmllib import SGMLParser

class redTubeEntry:
    def __init__(self, id):
        self.id = id
        self.description = ''
        self.thumbnail = ''

    def add_description(self, desc):
        self.description = self.description + desc

    def set_thumbnail(self, thumb):
        self.thumbnail = thumb

    def __str__(self):
        return self.id + ': ' + self.description + ', ' + self.thumbnail

class redTube(SGMLParser):
    def reset(self):
        SGMLParser.reset(self)
        self.entries = []
        self.curEntry = None
        self.lastId = None

    def start_a(self, attributes):
        link = None
        cssClass = None
        for name, value in attributes:
            if name == "href":
                link = value.split('/')[-1]
            elif name == "class":
                cssClass = value

        
        if(cssClass == 's'):
            self.curEntry = redTubeEntry(link)
            self.entries.append(self.curEntry)
        else:
            self.lastId = link

    def end_a(self):
        self.curEntry = None

    def handle_data(self,data):
        if(self.curEntry != None):
            self.curEntry.add_description(data)

    def start_img(self, attributes):
        src = None
        cssClass = None
        for name, value in attributes:
            if name == "src":
                src = value
            elif name == "class":
                cssClass = value
        
        if(cssClass == 't' and self.lastId != None):
          for entry in self.entries:
            if(entry.id == self.lastId):
              entry.set_thumbnail(src)
              break

    def get_entries(self):
        return self.entries

    def parse(self, s):
        "Parse the given string 's'."
        self.feed(s)
        self.close()


if __name__ == '__main__':
    cli = RedTubeClient()
    import pdb; pdb.set_trace()
