#! usr/bin/env python3

projects = {'RBP':'ybx1','microRNA':'miR-144','buffering':'RNA levels'}
# one way to print on object
fav_project ='RBP'
print(projects[fav_project]i)
fav_microRNA = 'microRNA'
print(projects[fav_microRNA])
#another way to print specific object
print(projects['RBP'])
#check if object is in the dict
'RBP' in projects
#add new object into dict
projects.update({'organism':'deer'})
fav_microRNA = 'organism'
print(projects[fav_microRNA])
#to print only keys of the library:
for project in projects:
	print(project)
#to print print key and values 
for project in projects:
	seq = projects[project]
	print(project, seq)
#use input to import the key you are interested in and then print the value of this key
fav_thing = input("Enter your favorite thing: ")
print(projects[fav_thing])
 while input not in projects # ask for the input until the input will be good (in projects). Loop is not finished!!! 
#change the value of fav organism:
projects['organism'] = 'zebrafish'
print(projects)
# use input to ask for a key, print it out, then ask for a value for this key, change it in the dictionary and print dictonary out
fav_thing = input("Enter your favorite thing: ")
print(projects[fav_thing])
new_value = input("Enter a new value for the thing : ")
projects['fav_thing'] = new_value
print(projects)


