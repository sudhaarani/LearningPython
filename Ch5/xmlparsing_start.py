# 
# Example file for parsing and processing XML
#
import xml.dom.minidom

def main():
    #  use the parse() function to load and parse an XML file
    d1 = xml.dom.minidom.parse("samplexml.xml")
  
  # print out the document node and the name of the first child tag
    print(d1.nodeName)
    print(d1.firstChild.tagName)
  
  # get a list of XML tags from the document and print each one
    sks = d1.getElementsByTagName("skill")
    for sk in sks:
        print(sk.getAttribute("name"))

  # create a new XML tag and add it into the document
    print("adding new tag and adding it")
    ad = d1.createElement("skill")
    ad.setAttribute("name", "jquery")
    d1.firstChild.appendChild(ad)

    sks = d1.getElementsByTagName("skill")
    for sk in sks:
        print(sk.getAttribute("name"))
#    own exmple
    g = d1.getElementsByTagName("firstname")
    print("value :", g.getText())


if __name__ == "__main__":
    main();

