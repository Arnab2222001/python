letter= ''' dear <|name|> 


you are selected !

date :  <|date|>'''
name=input("enter the name :- \n")
date=input("enter date\n")
letter= letter.replace("<|name|> ",name)
letter= letter.replace('<|date|>',date)
print(letter)