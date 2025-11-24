#list-->Data structure which can hold multiple values of multiple types.
#array -->data structures which can hold multiple values of same type .
list_of_clouds= ["aws","IBM","Azure","GCP","Oracle","Utho","alibaba"]
cloud="gcp" #Variable
print(list_of_clouds)
print(len(list_of_clouds))
#add a new cloud
list_of_clouds.append("salesForce")
list_of_clouds.insert(2,"Hiroku")
print(list_of_clouds)
#length of list_of_cloud 
print(len(list_of_clouds))

#insert
list_of_clouds.insert(0,"Hello_clouds")
print(list_of_clouds)

#go to for_loops.py 
# for x in list_of_clouds:
#     print(" ")
#     print("%s-->",x)