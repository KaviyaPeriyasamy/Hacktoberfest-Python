
#set
s={10,20,30,40,50,60,70,80,90,100}
s1 = {1,2,3,4,5,6,7}
#set.add
s.add(152)
print('after adding Object' , s)

#Set.update(Objects)
s.update({300,987})
print('after Updating' , s)

#Set. discard(Object)
s.discard(100)
print('after discard ' , s)

#Set1|Set2
print('Union of two sets' ,  s|s1)

#Set1&Set2
print('Intersection of two sets' ,  s&s1)

#Set1 – Set2
print('Difference of two sets' ,  s-s1)
print('Difference of two sets' ,  s1-s)

#Set1 <= Set2
print('Set Comparision Process ' , s!=s1)
