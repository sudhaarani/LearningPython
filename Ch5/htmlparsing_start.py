# 
# Example file for parsing and processing HTML
#

from html.parser import HTMLParser
metacount=0
linkcount=0

class MyHTMLParser(HTMLParser):
    print("inside class")

    def handle_comment(self, data):
        print("comment:" ,data)
        pos=self.getpos()
        print("\t at line: ", pos[0], " position:", pos[1])

    def handle_startendtag(self, tag, attrs):
        global metacount, linkcount
        if tag == "meta":
            metacount += 1

        if tag == "link":
            linkcount +=1

        print("start end tag:", tag)
        pos = self.getpos()
        print("\t at line: ", pos[0], " position:", pos[1])
        if attrs.__len__() > 0:
            print("attributes:")
            for i in attrs:
                print("\t",i[0]," : ", i[1])

    def handle_endtag(self, tag):
        print(" end tag:", tag)
        pos = self.getpos()
        print("\t at line: ", pos[0], " position:", pos[1])

    def handle_starttag(self, tag, attrs):
        print("start tag:", tag)
        pos = self.getpos()
        print("\t at line: ", pos[0], " position:", pos[1])
        if attrs.__len__() > 0:
            print("attributes:")
            for i in attrs:
                print("\t",i[0]," : ", i[1])

    # def handle_decl(self, decl):


    def handle_data(self, data):
        if data.isspace():
            return
        print("data:", data)
        pos = self.getpos()
        print("\t at line: ", pos[0], " position:", pos[1])

def main():
    # instantiate the parser and feed it some HTML
    parser = MyHTMLParser()
    f = open("samplehtml.html")
    if f.mode == 'r':
        con = f.read()
        parser.feed(con)

    print("total meta count:", metacount)
    print("total link count:", linkcount)

if __name__ == "__main__":
    main();
