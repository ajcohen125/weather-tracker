#Verifies that given links exist and sends alert if a link fails
import requests
import sys

broken_links_list = []

#FIXME - Read in links section could be configured as input depending on how we order things in main
#Read in links to be verified
with open(str(sys.argv[1]),"r") as input_file: #Closes file when finished

    #Verify links
    for link in input_file:
        response = requests.get(link.strip())
        if response.status_code != 200:
            broken_links_list.append(link)

                    
#Write file of broken links if needed
if broken_links_list:
    broken_links = open("broken_links.txt","a")
    
    #Logs Date & Time of Failure
    from datetime import datetime
    broken_links.write(datetime.now().strftime("%m/%d/%y - %I:%M %p\n"))

    #Logs Broken Links
    for link in broken_links_list:
        broken_links.write(link)
    broken_links.write("\n")
    broken_links.close()
    print("Some links need fixing")

else:
    print("All links are good")

#FIXME - Create main to require a success or fail from this script


#FIXME - Commets on stuff that need to be fixed
#Functionize this
#Don't use read and writes - lists and logs being passed around from main


#Make the following a different functions
#Check to make sure I can connect to the internet by pinging google or something
#Use try-catch to make sure internet
#use both ping method and request (curl) method
#Retry 5 times in 30 (maybe make it where you can pass in num tries and time between tries)
#Return an error code and message if it doesn't work after those tries and exit in main
#If no problems, return good


#Check data base connection (place holder and let Aaron fill in code)

