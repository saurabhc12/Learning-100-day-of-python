#simple dic
dic = {
    "college": "engineering",
    "top": "mauli"
}
print(dic["college"])

#used to store praticular mark in one variable
#basically mapping

info = {"name" : "gaurav", "age" : 19 , "eligible": True}
print(info)

print(info['name'])
print(info.get('eligible')) #acces praticular value used get

print(info.keys())

for key in info.keys():
    print(info[key]) #if we want to print line by line we can used for