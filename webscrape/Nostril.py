from nostril import nonsense
from nostril import sanitize_string
import re
import os
import csv
import pandas as pd
import sys

CLEANR = re.compile('<.*?>') 

def cleanhtml(raw_html):
    cleantext = re.sub(CLEANR, ' ', raw_html)
    return cleantext

def cleanlist(arr,thres):
    temp=[]
    for i in range(len(arr)):
        # print(len(arr[i]))
        if(len(arr[i]) >= thres):
            temp.append(arr[i])
    return temp


path=os.getcwd()
path=path.replace("\\","/")
# path=path.rsplit('/',1)[0]
path_csvfile=path+"/webspider.csv"
maxInt = sys.maxsize
# print(path)
while True:
    # decrease the maxInt value by factor 10 as long as the OverflowError occurs.
    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt/10)
rows={"Script":[],"Link":[]}
symbols=['\0','`','~','!','@','#','$','%','^','&','*','*','(',')','+','=','{','[',']','}',':','\\','|',';','"',"'",'<',',','>','?','\n','\t','/']

with open(path_csvfile, encoding="mbcs") as fin:
    dr = csv.DictReader(fin) 
    for row in dr:
        rows["Script"].append(row["Script"])
        rows["Link"].append(row["Link"])
        # print(rows["Link"])
# print("\n\nR =",rows["Script"][3],"\n\n")

# for row in rows["Script"][1:len(rows)]:
#     row=cleanhtml(row)
#     for i in symbols:
#         row=str(row.replace(i,' '))
    # Corpus.append(cleanlist(row[0].split(),5))

discoveries={'String':[],"Category":[],'Link':[]}

# Custom = ['Itisatest', 'asfdfgdfgd', 'honda', 'ioFlXFndrInfo', 'Websitestobetested', 'https://www.geeksforgeeks.org','faiwtlwexu', 'asfgtqwafazfyiur', 'zxcvbnmlkjhgfdsaqwerty','AIzaSyD2Zp1IZkdqA8hk1ZIJtTDFjqV2f5A5Jjg']
Corpus=[]

# for i in Custom+Corpus:
#     while(len(i)<=5):
#         i+="o"
#     # print(i)
#     if(nonsense(i)):
#         discoveries.append(i)
#     print(i,": ",nonsense(i))

temp=[]
# CLEANR = re.compile('<.*?>') 
count=0
for row in rows["Script"]:
    # row=cleanhtml(row)
    for i in symbols:
        row=str(row.replace(i,' '))
    # print(row)
    temp.append(cleanlist(row.split(),6))
    count+=1
# Corpus.append('AIzaSyD2Zp1IZkdqA8hk1ZIJtTDFjqV2f5A5Jjg')
# Regex_arr=[["XXXXXXXXXXXX","saidyfgiasgdiasybdiyasbdiasdkascubdkybasdhasihdkdug"],['Artifactory API Token','(?:\s|=|:|"|^)AKC[a-zA-Z0-9]{10,}'],['Artifactory Password','(?:\s|=|:|"|^)AP[\dABCDEF][a-zA-Z0-9]{8,}',1],['Authorization Basic','basic [a-zA-Z0-9_\\-:\\.=]+'],['Authorization Bearer','bearer [a-zA-Z0-9_\\-\\.=]+'],['AWS Client ID','(A3T[A-Z0-9]|AKIA|AGPA|AIDA|AROA|AIPA|ANPA|ANVA|ASIA)[A-Z0-9]{16}'],['AWS MWS Key','amzn\.mws\.[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}'],['AWS Secret Key','[0-9a-zA-Z\/+]{40}'],['Base64','(eyJ|YTo|Tzo|PD[89]|aHR0cHM6L|aHR0cDo|rO0)[a-zA-Z0-9+/]+={0,2}'],['Basic Auth Credentials','(?<=:\/\/)[a-zA-Z0-9]+:[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]+'],['Cloudinary Basic Auth','cloudinary:\/\/[0-9]{15}:[0-9A-Za-z]+@[a-z]+'],['Facebook Access Token','EAACEdEose0cBA[0-9A-Za-z]+'],['Google API Key','AIza[0-9A-Za-z\\-_]{35}'],['Google Drive/Gmail Oauth','[0-9]+-[0-9A-Za-z_]{32}\.apps\.googleusercontent\.com'],['Google Oauth Access Token','ya29\\.[0-9A-Za-z\\-_]+'],['Google Youtube Oauth','[0-9]+-[0-9A-Za-z_]{32}\.apps\.googleusercontent\\.com'],['Heroku API Key','[h|H][e|E][r|R][o|O][k|K][u|U].{0,30}[0-9A-F]{8}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{12}'],['IPv4','\b(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}\b'],['IPv6','(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))'],['LinkedIn Client ID','[0-9a-z]{12}'],['LinkedIn Secret Key','[0-9a-z]{16}'],['Mailchamp API Key','[0-9a-f]{32}-us[0-9]{1,2}'],['Mailgun API Key','key-[0-9a-zA-Z]{32}'],['Mailto:','(?<=mailto:)[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.-]+'],['MD5 Hash','[a-f0-9]{32}'],['Slack Token','xox[baprs]-([0-9a-zA-Z]{10,48})?'],['Square Access Token','sqOatp-[0-9A-Za-z\\-_]{22}'],['Square Oauth Secret','sq0csp-[ 0-9A-Za-z\\-_]{43}'],['Twitter Client ID','[0-9a-z]{18,25}'],['Twitter Oauth','[t|T][w|W][i|I][t|T][t|T][e|E][r|R].{0,30}[0-9a-zA-Z]{35,44}'],['Twitter Secret Key','[0-9a-z]{35,44}']]
Regex_arr=[["XXXXXXXXXXXX","helloworld",1],['Artifactory API Token','(?:\s|=|:|"|^)AKC[a-zA-Z0-9]{10,}',1],['Artifactory Password','(?:\s|=|:|"|^)AP[\dABCDEF][a-zA-Z0-9]{8,}',1,1],['Authorization Basic','basic [a-zA-Z0-9_\\-:\\.=]+',1],['Authorization Bearer','bearer [a-zA-Z0-9_\\-\\.=]+',1],['AWS Client ID','(A3T[A-Z0-9]|AKIA|AGPA|AIDA|AROA|AIPA|ANPA|ANVA|ASIA)[A-Z0-9]{16}',1],['AWS MWS Key','amzn\.mws\.[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}',1],['AWS Secret Key','[0-9a-zA-Z\/+]{40}',1],['Base64','(eyJ|YTo|Tzo|PD[89]|aHR0cHM6L|aHR0cDo|rO0)[a-zA-Z0-9+/]+={0,2}',1],['Basic Auth Credentials','(?<=:\/\/)[a-zA-Z0-9]+:[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]+',1],['Cloudinary Basic Auth','cloudinary:\/\/[0-9]{15}:[0-9A-Za-z]+@[a-z]+',1],["Discord App Token",'[A-Za-z\d]{24}\.[\w-]{6}\.[\w-]{27}',1],['Facebook Access Token','EAACEdEose0cBA[0-9A-Za-z]+',1],['Google API Key','AIza[0-9A-Za-z\\-_]{35}',1],['Google Drive/Gmail Oauth','[0-9]+-[0-9A-Za-z_]{32}\.apps\.googleusercontent\.com',1],['Google Oauth Access Token','ya29\\.[0-9A-Za-z\\-_]+',1],['Google Youtube Oauth','[0-9]+-[0-9A-Za-z_]{32}\.apps\.googleusercontent\\.com',1],['Heroku API Key','[h|H][e|E][r|R][o|O][k|K][u|U].{0,30}[0-9A-F]{8}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{12}',1],['IPv4','\b(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}\b',1],['IPv6','(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))',1],['LinkedIn Client ID','[0-9a-z]{12}',1],['LinkedIn Secret Key','[0-9a-z]{16}',1],['Mailchamp API Key','[0-9a-f]{32}-us[0-9]{1,2}',1],['Mailgun API Key','key-[0-9a-zA-Z]{32}',1],['Mailto:','(?<=mailto:)[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.-]+',1],['MD5 Hash','[a-f0-9]{32}',1],['Slack Token','xox[baprs]-([0-9a-zA-Z]{10,48})?',1],['Square Access Token','sqOatp-[0-9A-Za-z\\-_]{22}',1],['Square Oauth Secret','sq0csp-[ 0-9A-Za-z\\-_]{43}',1],['Twitter Client ID','[0-9a-z]{18,25}',1],['Twitter Oauth','[t|T][w|W][i|I][t|T][t|T][e|E][r|R].{0,30}[0-9a-zA-Z]{35,44}',1],['Twitter Secret Key','[0-9a-z]{35,44}']]

count=0
for i in temp:
    temp[count]=" ".join(i)
    count+=1
# print(temp)
ARRR=[]

count=0
for i in temp:
    regged=[]
    strt=[]
    for reg in Regex_arr:
        strt=i.split()
        reg[1]="^"+reg[1]+"$"
        for k in strt:
            x=re.match(reg[1],k)### x=re.findall(reg[1],i)
            if(x):
                x=x.group()###
                if(x):
                    regged.append([x,reg[0],count,reg[2]])
    if(regged):
        # print(regged)
        ARRR.append(regged)
    count+=1
# print(ARRR)
for i in ARRR:
    for j in i:
            Corpus.append(j)
# print(Corpus)
# x=re.findall('AIza[0-9a-zA-Z\\-_]{35}','AIzaSyD2Zp1IZkdqA8hk1ZIJtTDFjqV2f5A5Jjg')
# print(x)
count=0
# Corpus.append(["AIzaSyD2Yp1IZedqA9hk1aIJtTDFjqc2f5A5Jjg","TEST",0])
# print("\n\n",len(Corpus))
for i in Corpus:
    if(i[3]==0):
        discoveries['String'].append(i[0])
        discoveries['Category'].append(i[1])
        discoveries['Link'].append(rows["Link"][i[2]])
        continue
    sanitized_string=""
    sanitized_string=sanitize_string(i[0])
    while(len(sanitized_string)>=3 and len(sanitized_string)<=5):
        sanitized_string+="o"
    if(len(sanitized_string)>5 and len(sanitized_string)<150):
        #print(j)
        if(sanitized_string!='' and nonsense(sanitized_string)):
            discoveries['String'].append(i[0])
            discoveries['Category'].append(i[1])
            discoveries['Link'].append(rows["Link"][i[2]])
            # print(j,": ",nonsense(sanitized_string))
            # print(rows["Link"][count])
    count+=1
# for i in Corpus:
    # while(len(i)<=5):
    #     i+="o"
    # print(i)
    # if(nonsense(i)):
    #     discoveries.append(i)
    #     print(i,": ",nonsense(i))
# print("HelloWorldshdaasd",": ",nonsense("HelloWorldshdaasd"))
df=pd.DataFrame.from_dict(discoveries)
print(df)
path=os.getcwd()
path=path.replace("\\","/")
path_csvfile=path+"/output.csv"
# print (path_csvfile)
if os.path.exists(path_csvfile):
    os.remove(path_csvfile)
df.to_csv("output.csv")
