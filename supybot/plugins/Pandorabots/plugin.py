###
#	This file is part of supybot-pandorabots.

#	Foobar is free software: you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation, either version 2 of the License, or
#	(at your option) any later version.

#	Foobar is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.

#	You should have received a copy of the GNU General Public License
#	along with Foobar.  If not, see <http://www.gnu.org/licenses/>.
#
#	Copyleft 2010, Jiang Yio
###

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks

import urllib, re, random, time
from htmlentitydefs import name2codepoint

class Pandorabots(callbacks.Plugin):
	"""This plugin replies using the Pandorabots API upon intercepting an invalid command."""
	threaded = True
	callAfter = ['Triggers']
#	def ...(self,irc,msg,args,line):
#		return None
#	... = wrap(...)
	def __init__(self,irc):
		self.__parent = super(Pandorabots,self)
		self.__parent.__init__(irc)
		self.nicks = {}
		self.hashes = {}
	@staticmethod
	def decode_htmlentities(s):
		def substitute_entity(match):
			ent = match.group(3)
			if match.group(1) == "#":	# number, decimal or hexadecimal
				return unichr(int(ent)) if match.group(2) == '' else unichr(int('0x'+ent,16))
			else:	# name
				cp = name2codepoint.get(ent)
				return unichr(cp) if cp else match.group()
		return re.compile(r'&(#?)(x?)(\w+);').subn(substitute_entity,s)[0]
	@staticmethod
	def _randHash():
		return '%016x'%random.getrandbits(64)
	@classmethod
	def _post(cls,bot,hash,line):
		m = re.search(r'<that>([^<]+)</that>',urllib.urlopen('http://www.pandorabots.com/pandora/talk-xml',urllib.urlencode({'botid':bot,'custid':hash,'input':line})).read(),re.I)
		if m:
			return re.sub(r'\s+',' ',re.sub(r'<[^>]*?>','',cls.decode_htmlentities(re.sub(r'\s+',' ',m.group(1))))).strip()
		return None,None
	@classmethod
	def _identify(cls,bot,hash,name):
		return cls._post(bot,hash,'my name is %s'%name)
	def getHash(self,nick):
		nick = nick.lower()
		if nick not in self.nicks:
			self.nicks[nick] = self._randHash()
		return self.nicks[nick]
	def getResponse(self,irc,msg,line):
		hash = self.getHash(msg.nick)
		args = (self.registryValue('bot'),hash)
		if hash not in self.hashes or time.time()-self.hashes[hash] > 300:
			self._identify(*(args+(msg.nick,)))
		self.hashes[hash] = time.time()
		line = re.compile(r'\b'+re.escape(irc.nick)+r'\b',re.I).sub('you',re.compile(r'^'+re.escape(irc.nick)+r'\S',re.I).sub('',line))
		reply = self._post(*(args+(line,)))
#		checking = re.compile('\.+').search(line)
#		if checking.group()==line:
#			return None  
		if reply is None:
			return None
		name = self.registryValue('name')
		if len(name) > 0:
			return re.compile(r'\b(?:'+re.escape(name)+r')|(?:ALICE)\b',re.I).sub(irc.nick,reply)
		else:
			return re.compile(r'\bALICE\b',re.I).sub(irc.nick,reply)
	def invalidCommand(self,irc,msg,tokens):
		if irc.isChannel(msg.args[0]) and self.registryValue('react',msg.args[0]):
			channel = msg.args[0]
			reply = self.getResponse(irc,msg,ircutils.stripFormatting(msg.args[1]).strip())
			if reply is not None:
				irc.reply(reply, prefixNick=True)
	def pandorabots(self,irc,msg,args,line):
		"""<line>
		Fetches response from Pandorabots
		"""
		reply = self.getResponse(irc,msg,line)
		if reply is not None:
			irc.reply('%s'%reply, prefixNick=True)
		else:
			irc.reply('There was no response.', prefixNick=True)
	pandorabots = wrap(pandorabots,['text'])
	def doNick(self,irc,msg):
		try:
			del self.nicks[msg.nick.lower()]
		except KeyError:
			pass
		self.nicks[msg.args[0].lower()] = self._randHash()
		self._identify(self.registryValue('bot'),self.getHash(msg.args[0].lower()),msg.args[0])
#	def doKick(self,irc,msg):
#		del self.nicks[msg.args[1]]
#	def doPart(self,irc,msg):
#		del self.nicks[msg.nick.lower()]
	def doQuit(self,irc,msg):
		try:
			del self.nicks[msg.nick.lower()]
		except KeyError:
			pass
	def doPrivmsg(self, irc, msg):
		line = msg.args[1]
		if re.search(r'\bpoohbot\b', line, re.I):
			channel = msg.args[0]
			if not irc.isChannel(channel):
				return
			if callbacks.addressed(irc.nick, msg):
				return
			line = line.replace("PoohBot", " ")
			line = line.replace("poohbot", " ")
			line = line.replace("  ", " ")
			response = self.getResponse(irc, msg, line)
			irc.reply(response, prefixNick=True)
		else:
			return None
Class = Pandorabots
# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
