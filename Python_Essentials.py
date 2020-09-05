#LISTS
list1=[1,2,'ram',[3,4,5],1,True]
list1.append(20)
print(list1.count(1))
list1.pop(1)
list1.insert(4,5)
list1.reverse()
print(list1)

#Dictionary
dict1= {"name":"ram",'age':24,"single?":True}
print(dict1.items())
dict1.update({'job..?': 'yes'})
print(dict1.values())
print(dict1.get("name"))
print(dict1.pop("job..?"))
print(dict1)

#SETS   
set1={"apples","Avakado",'kiwi'}
set2={"grapes","dragon Fruit"}
set3={"apples"}
set1.add("'bananas'")
print(set2.issubset(set1))
print(set1.issuperset(set3))
set1.discard('kiwi')
print(set1.intersection(set3))
print(set1)

#TUPLES 
tup=("rama",'Chandra','rama')
print(tup.count('rama'))
tup.index("Chandra")

#Strings
str1= 'rama chandra'
print(str1.capitalize())
print(str1.find('m'))
print(str1.isalnum())
print(str1.index('ch'))
print(str1.endswith('ra'))