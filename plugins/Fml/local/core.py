# Written for Aha2Y <3
#
 
import urllib2
import lxml.html
 
# hg clone https://github.com/lxml/lxml.git lxml
 
def sortByTag(data):
    D = {}
    for entry in data:
        L = entry.split(':')
        key = L[0].lower()
        contents = L[1][1:]
        D[key] = contents
    return D
 
class FML:
    def __init__(self):
        api = urllib2.urlopen("http://rscript.org/lookup.php?type=fml")
        data = lxml.html.parse(api)
        api.close()
       
        contents = data.xpath("//pre/text()")[0].split('\n')
        contents.sort()
        # lets remove the trash that will fuck the dict up
        del contents[0]
        del contents[0]
        contents.remove("START")
        contents.remove("END")
       
        data = sortByTag(contents)
       
        # lets sort it into something BEAUTIFUL :D
        self.id = data['id']
        self.cate = data['cate']
        self.text = data['text']
        self.agree = data['agree']
        self.deserved = data['deserved']
        self.comments = data['comments']
        self.comments = data['comments']