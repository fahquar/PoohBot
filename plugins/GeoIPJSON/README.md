Supybot-GeoIPJSON
=================

Supybot plugin for doing GeoIP lookups.

Someone already did a standard GeoIP plugin that uses pygeoip and the GeoIPLite.dat. I'm not sure how reliable
or how updated it is, but there are quite a few free services on the Internet to do lookups. Now, if the bot 
is already connected to IRC, why not use an API instead of relying on a database? 

I found 2-3 free ones but decided on freegeoip. This could easily be adapted to many more.

Help:
Run the geoip command with a hostname/ip/user. It will query the database.

TODO:
- -getopt to configure some options
- output could also do better.
- alternate geoip providers like: http://developer.quova.com/docs#response
