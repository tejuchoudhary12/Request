# import requests
# import json

# link ="http://saral.navgurukul.org/api/courses"
# calling_API = requests.get(link)
# myData = calling_API.json()
# with open ("saral_data.json","w")as my_file:
#     json.dump(myData,my_file,indent=4)
# for i in range(len(myData["availableCourses"])):
#     print(i+1,myData["availableCourses"][i]["name"],myData["availableCourses"][i]["id"])
# choose  = input("Enter the name of course you want to go through: ")
# link2 = "https://saral.navgurukul.org/api/courses/"+myData["availableCourses"][choose]["id"]+"/exercises"
# API = requests.get(link2)
# data = API.json()

def designerPdfViewer(h, word):
    maxi=0
    for i in range(len(word)):
        if(maxi< h[ord(word[i])-97]):
            maxi = h[ord(word[i])-97]
    return maxi*len(word))

   
