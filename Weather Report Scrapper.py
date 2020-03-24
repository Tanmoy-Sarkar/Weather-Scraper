from bs4 import BeautifulSoup
import requests
#url of the website
url="https://www.timeanddate.com/weather/bangladesh/dhaka/ext"
#taking specifically only english language
headers = {"Accept-Language": "en-US,en;q=0.5"}
response=requests.get(url,headers=headers)
data=response.text

#parsing the html
soup=BeautifulSoup(data,"html.parser")
#finding all the values needed located in tr tag
weatherdatas=soup.findAll("tr")

#filename of the excel file
filename="weatherreport.csv"
headers="date,temperature,condition,feelslike,humidity,sunrise,sunset \n"
#opening the file and writing file headers
file=open(filename,"w")
file.write(headers)

#Scrapping the datas
for weather in weatherdatas:
    #particularly finding the values for the coloumns
    if (weather.find("span",{"class":"smaller soft"})):
        #getting date,temperature,condition,feelslike,humdity,sunrise and sunset sequentially
        date=weather.th.text
        print(date)
        temperature=weather.find("td","").text
        print(temperature)
        condition=weather.find("td",{"class":"small"}).text
        print(condition)
        feelslike=weather.find("td",{"class":"sep"}).text
        print(feelslike)
        infos=weather.findAll("td","")
        humidity=infos[6].text
        print(humidity)
        sunrise=infos[10].text
        print(sunrise)
        sunset=infos[11].text
        print(sunset)
        #writting all the values in csv file
        file.write(date+","+ temperature + "," +condition +"," +feelslike+ "," +humidity + "," +sunrise +"," + sunset + "\n")

file.close()
