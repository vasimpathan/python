## read_html, read_csv, read_excel, read_json etc
import pandas as pd
## type : html, excel, csv
def readFile(type,to_html="N"):
    if type=="html":
        html = pd.read_html("https://en.wikipedia.org/wiki/Mobile_country_code")
        if(to_html!="Y"): 
            print(html)
        else:
            html[0].to_html("pandas.html")
        ## To read particular table from above URL
        #print(html[0])
        #type(html[0])
        ## To read the table from above URL by using specific tag aur title matche
        #html = pd.read_html("https://en.wikipedia.org/wiki/Mobile_country_code",match="References and notes")
        #print(html)
    elif type=="excel":
        ## to read the excel 
        readme = pd.read_excel("C:/Users/Vasim/Desktop/Book1.xlsx")
        if(to_html!="Y"):
            print(readme)
        else:
            readme.to_html("pandas.html")
    elif type=="csv":
        ## # Try reading the CSV file with ISO-8859-1 encoding
        readme = pd.read_csv("SampleCSVFile_2kb.csv", encoding='ISO-8859-1')
        if(to_html!="Y"):
            print(readme)
        else:
            readme.to_html("pandas.html")
    elif type=="json":
        readme = pd.read_json("jsonfile.json")
        if(to_html!="Y"):
            print(readme)
        else:
            readme.to_html("pandas.html")
    else:
        print(f"Opp's You provided {type} type is not matchig..")

readFile('json',"Y") ## html | csv | excel | json | to_html : Y|N




