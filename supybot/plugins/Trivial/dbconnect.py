import sqlite, datetime, time
import re, os

db = sqlite.connect('questions.db')
filename = file('randtrivia.txt')

id=0

for line in filename:
    id=id+1
    args = line.split('*')
    time = str(datetime.datetime.now())
    author = 'SYSTEM'
    enabled = 'True'
    cs = db.cursor()
##    cs.execute('''insert into log (author, name, added, oldvalue) values (%s, %s, %s, %s)''',
##                (editor, factoid.name, str(datetime.datetime.now()), factoid.value))
    try:
        cs.execute('''insert into questions(id,question,answer,altanswer1,added,author,enabled) values (%s, %s, %s, %s, %s, %s, %s)''',
                (id,args[0],args[1],args[2],time,author,enabled))
    except (IndexError), e:
        cs.execute('''insert into questions(id,question,answer,added,author,enabled) values (%s, %s, %s, %s, %s, %s)''',
                (id,args[0],args[1],time,author,enabled))
    db.commit()
    
    print id
