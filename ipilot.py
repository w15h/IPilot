import requests, json, sys
from os import system, name

# Clear Function
def clear(): 

    if name == 'nt': 
        _ = system('cls') 

    else: 
        _ = system('clear') 

# Geo IP BASIC
def geo_ip_base():
    clear()

    ip = raw_input("Enter IP: ")

    r = requests.get('http://ip-api.com/json/' + ip)

    clear()

    print("Basic Geolocation")
    print("---------------")
    print("IP      " + r.json()['query'])
    print("CITY    " + r.json()['city'])
    print("ZIP     " + r.json()['zip'])
    print("STATE   " + r.json()['regionName'])
    print("COUNTRY " + r.json()['country'])

# Geo IP DETAIL
def geo_ip_detail():
    clear()

    ip = raw_input("Enter IP: ")

    r = requests.get('http://ip-api.com/json/' + ip)

    clear()

    print("Detailed Geolocation")
    print("---------------")
    print("IP      " + r.json()['query'])
    print("CITY    " + r.json()['city'])
    print("ZIP     " + r.json()['zip'])
    print("STATE   " + r.json()['regionName'])
    print("TIME    " + r.json()['timezone'])
    print("COUNTRY " + r.json()['country'])
    print("ISP     " + r.json()['isp'])
    print("AS      " + r.json()['as'])
    print("ORG     " + r.json()['org'])

# Geo Your IP BASIC
def geo_your_ip_base():
    clear()

    r = requests.get('http://ip-api.com/json/')

    clear()

    print("Basic Self Geolocation")
    print("---------------")
    print("IP      " + r.json()['query'])
    print("CITY    " + r.json()['city'])
    print("ZIP     " + r.json()['zip'])
    print("STATE   " + r.json()['regionName'])
    print("COUNTRY " + r.json()['country'])

# Geo Your IP DETAILED
def geo_your_ip_detail():
    clear()

    r = requests.get('http://ip-api.com/json/')

    clear()

    print("Detailed Self Geolocation")
    print("---------------")
    print("IP      " + r.json()['query'])
    print("CITY    " + r.json()['city'])
    print("ZIP     " + r.json()['zip'])
    print("STATE   " + r.json()['regionName'])
    print("TIME    " + r.json()['timezone'])
    print("COUNTRY " + r.json()['country'])
    print("ISP     " + r.json()['isp'])
    print("AS      " + r.json()['as'])
    print("ORG     " + r.json()['org'])



# Menu Function
def menu():
    clear()
    opt = ""
    print("""
        ______
        _\ _~-\___
=  = ==(____AA____D
            \_____\___________________,-~~~~~~~`-.._
            /     o O o o o o O O o o o o o o O o  |\_
            `~-.__        ___..----.. IPilot           )
                  `---~~\___________/------------`````
                  =  ===(_________D        by Joe
    """)
    print
    print("1) Geolocate IP(BASIC)")
    print("2) Geolocate IP(DETAILED)")
    print("3) Geolocate Your IP(BASIC)")
    print("4) Geolocate Your IP(DETAILED)")
    print("5) Exit IPilot")
    print
    opt = int(input("-> "))

    if opt == 1:
        back = ""
        geo_ip_base()
        back = int(input("1) Go Back "))

        if back == 1:
            menu()

    if opt == 2:
        back = ""
        geo_ip_detail()
        back = int(input("1) Go Back "))

        if back == 1:
            menu()

    if opt == 3:
        back = ""
        geo_your_ip_base()
        back = int(input("1) Go Back "))

        if back == 1:
            menu()

    if opt == 4:
        back = ""
        geo_your_ip_detail()
        back = int(input("1) Go Back "))

        if back == 1:
            menu()

    if opt == 5:
        clear()
        print("See ya!")
        sys.exit(0)

    else:
        menu()

menu()
