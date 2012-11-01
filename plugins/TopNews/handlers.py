import logging
import os
import random
import simplejson

from xml.etree import ElementTree as ET
from datetime import timedelta, datetime, time

from google.appengine.api import urlfetch
from google.appengine.api import channel
from google.appengine.ext import db, deferred, webapp
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp.template import render

class ChannelClient(db.Model):
    clientid = db.TextProperty()
    timestamp = db.DateTimeProperty(auto_now_add=True)

class NewsItem(db.Model):
    title = db.StringProperty()
    link = db.StringProperty()
    description = db.TextProperty()


# NewsHandlers fetches an XML RSS news feed and displays it
class FetchNewsHandler(webapp.RequestHandler):
    def get(self):
        # delete old news items
        db.delete(NewsItem.all(keys_only=True))

        googleFeed = 'http://news.google.com/news?ned=us&topic=h&output=rss';
        # Other feeds to try...
        #cnnFeed = "http://rss.cnn.com/rss/cnn_topstories.rss";
        #yahooFeed = "http://rss.news.yahoo.com/rss/topstories";
        #reutersFeed = "http://feeds.reuters.com/reuters/topNews";
        #bbcFeed = "http://feeds.bbci.co.uk/news/rss.xml";

        # get, parse, and store feed items
        result = urlfetch.fetch(googleFeed)
        if result.status_code == 200:
          feedcontent = result.content

        tree = ET.XML(feedcontent)
        for elmt in tree.getiterator():
          if elmt.tag == 'title':
            newsitem = NewsItem()
            newsitem.title = elmt.text
            continue

          if elmt.tag == 'link':
            newsitem.link = elmt.text
            continue

          if elmt.tag == 'description':
            newsitem.description = elmt.text
            newsitem.put()

        # display stored feed items
        self.response.out.write("<html><body><h3>Here's all the news stuff</h3>")
        self.response.out.write('<b>Feed Content</b><br/>')
        news = db.GqlQuery("SELECT * FROM NewsItem")
        for ni in news:
          self.response.out.write('<br/><br/>title: ')
          self.response.out.write(ni.title)
          self.response.out.write('<br/><br/>link: ')
          self.response.out.write(ni.link)
          self.response.out.write('<br/><br/>description: ')
          self.response.out.write(ni.description)

        self.response.out.write('</body></html>')


class TokenHandler(webapp.RequestHandler):
    def get(self):
        clientid = str(random.random()*10000)
        token = channel.create_channel(clientid)
        client = ChannelClient()
        client.clientid = clientid
        client.put()
        self.response.out.write(token)

class MessageHandler(webapp.RequestHandler):
    def get(self):
        logging.info('in messagehandler, ready to broadcast')
        news = db.GqlQuery("SELECT * FROM NewsItem")
        for i,ni in enumerate(news):
            if not (ni.title is None and ni.link is None):
                deferred.defer(broadcastToClients, ni.title, ni.link, ni.description, _countdown=5*i)
        self.response.out.write('Messages queued!!!')

class CleanClientsHandler(webapp.RequestHandler):
    def get(self):
        twohoursago = datetime.now() - timedelta(minutes=120)
        clients = db.GqlQuery("SELECT * FROM ChannelClient")
        db.delete(id for id in ChannelClient().all() if id.timestamp < twohoursago)  

def broadcastToClients(title, link, description):
    clients = db.GqlQuery("SELECT * FROM ChannelClient")
    for id in clients:
      data_dict = {'title': title, 'link': link, 'description' : description}
      encodedmsg = simplejson.dumps(data_dict)
      channel.send_message(id.clientid, encodedmsg)


class MainHandler(webapp.RequestHandler):
    def get(self):
        tmpl = os.path.join(os.path.dirname(__file__), 'newsclient.html')
        self.response.out.write(render(tmpl, {}))

