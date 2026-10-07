"TD1"
#Exo1
arr=[25,11,56,11]
max = 0
for i in range (len(arr)-1):
    if arr[i]<arr[i+1]:
        max= arr[i+1]
    else :
        max=arr[i]
print(max)
        
#Exo 2 somme
S=0
for j in range (len(arr)):
    S=S+arr[j]
print(S)

#Exo 3 répet
Rep=0
compteur = 0
while compteur!=len(arr):
    for k in range (len(arr)-1):
        if arr[k]==arr[k+1]:
            Rep=arr[k]
            print(Rep)
    compteur+=1
        

#Exo 4 croissant décroissant
Cr=[]
Dcr=[]
while len(arr)!=0:
    for l in range(len(arr)-1):
        if arr[l]<arr[l+1]:
            max= arr[l+1]
        else :
            max=arr[l]
    Dcr.append(max)
    arr.pop(arr[max])
    
#Exo 5 copier les éléments dans un autre tableau
#Exo 6 somme de matrice
#Exo 7 produit matrice





#Exo 3 répet
arr=[25,11,56,11]
Rep=0
compteur = 1
while compteur<len(arr)+1:
    for k in range (len(arr)-1):
        if arr[0]==arr[k+compteur]:
            Rep=arr[0]
            print(Rep)
            compteur+=1
            

#TD2 

#smart sensor
import time
import paho.mqtt.client as mqtt
from faker import Faker
# let's connect to the MQTT broker
MQTT_BROKER_URL = "mqtt.eclipseprojects.io"
MQTT_PUBLISH_TOPIC = "temperature"
mqttc = mqtt.Client()
mqttc.connect(MQTT_BROKER_URL)
# Init faker our fake data provider
fake = Faker()
# Infinit loop of fake data sent to the Broker
while True:
 temperature = fake.random_int(min=0, max=5)
 mqttc.publish(MQTT_PUBLISH_TOPIC, temperature)
 print(f"Published new temperature measurement: {temperature}")
 time.sleep(1) 



#geocode
from __future__ import print_function
import geocoder
from builtins import *
#create a boolean containing False value
addressIsValid = False
#loop until the boolean is not False anymore
while not addressIsValid :

 #print some text in the console
 print("Please enter a valid address")

 #asks the user to enter the address
 textAddress = input() #for example ICAM Bretagne, Vannes, France

 #asks OpenStreetMap to geocode the address
 g = geocoder.osm(textAddress)
 #assign True/False regarding the previous operation's result
 addressIsValid = g.ok
 #if the address has been geocoded
 if addressIsValid :
     print("the address is valid")
     print("latitude" , g.lat)
     print("longitude" , g.lng)
 #if the address has NOT been geocoded
 else:
     print("the address is not valid")