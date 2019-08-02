import urllib
import urllib.request
from bs4 import BeautifulSoup
from django.db import models

## webscraping the data first.

def make_soup(url):
	thepage = urllib.request.urlopen(url)
	soupdata = BeautifulSoup(thepage,"html.parser")
	return soupdata

soup = make_soup("https://mfarm.co.ke/trends")

Marketdatasaved = ""
for record in soup.findAll("tr"):
	#print (record.text)

    marketdata=""
    for data in record.findAll("td"):
        #print(data.text)
        marketdata = marketdata +","+ data.text
        #print(marketdata)
    Marketdatasaved=Marketdatasaved + "\n"+ marketdata[1:]
##print(marketdatasaved)  

# creating a model

class Marketdatasaved(models.Model):
      Id = models.IntegerField(primary_key= True)
      Name = models.CharField(max_length=255)
      Location= models.CharField(max_length=255)
      Quantity= models.IntegerField()
      Low_price= models.IntegerField()
      High_price= models.IntegerField()

class Meta:
      db_table = 'product'
      ordering = ['-created_at']   

def __unicode__(self):
       return self.Name
      
