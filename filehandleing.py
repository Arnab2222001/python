#eol=end of line character
#crud operetion
#c=create ,r=read,u=updating,d=delete
#the key function for working with the files
#r=read mode ,w=write mode,a=apand mode,x=create mode
#syntax for open file=open(filename,mood)
age=input('enter your age')
f=open("data.txt",'w')
f.write(age)
f.close