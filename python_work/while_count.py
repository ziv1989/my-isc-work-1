#Initialise the variables
my_list=[23,"hi",2.4e-10]
count=0

#Run the loop
while count<3:
    item=my_list[count]
    print item, my_list.index(item)
    count+=1