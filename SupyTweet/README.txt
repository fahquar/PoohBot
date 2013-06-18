Plugin for interacting with Twitter using OAuth.
For first use 'supytweet getauth' to get the authorization URI, after which you should privately send supybot 'supytweet PIN <pin>' to authorise and login

Uses a slightly modified version of oauth-python-twitter2 (http://code.google.com/p/oauth-python-twitter2/)
Requires (available via easy_install):
simplejson - http://pypi.python.org/pypi/simplejson/
oauth2 - http://pypi.python.org/pypi/oauth2
 httplib2 - http://pypi.python.org/pypi/httplib2

Web: https://sourceforge.net/projects/supytweet/
IRC: #supytweet on FreeNode
Twitter: @supytweet

Current commands;
 cotag     - Sets the ^XY cotag for each user that is appended to messages
 cotags    - List set cotags
 tweet     - Updates the twitter status
 retweet   - RT a status id
 reply     - Updates the twitter status in reply to another status id
 timeline  - Returns the last 20 tweets in the timeline
 mentions  - Returns the last 20 mentions
 dm        - Returns the last 20 direct messages (query only)
 following - Returns users the account is currently following
 followers - Users following account
 ratelimit - Returns the current API ratelimits
 status    - Returns authorized user and info
 updaterestart - Re-schedule the auto announces if they were turned off
 getauth   - Provide the authorization URL
 pin <PIN> - Attempt to authorize with <PIN>
 
Extras;
 Auto announcing of timeline, mentions and DMs, to multiple channels and/or users
 Options to hide protected tweets, for both timeline and DMs (Defaults to hidden)
 
TODO:
 un/follow - Un/follow a user
 reply - Prepend mesage with @user
 tweet / reply - Possbily add geotags
 logout - Destroy current auth token
 option for colouring parts of tweets (@#^) and usernames
