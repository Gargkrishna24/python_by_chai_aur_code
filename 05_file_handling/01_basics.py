p= open(r'01_basics.py')
print(p.read())

r = open("supermn.txt",'w')
r.write("hello I am krishna i am writing inside the file")
r.close()

r = open("supermn.txt",'a')
r.write("I am Appending the text iside the superman .txt file")
