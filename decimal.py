a="123"
print(a.isdecimal())  #true
print(a.isdigit())    #true
print(a.isnumeric())  #true
a="-123"
print(a.isdecimal())  #false
print(a.isdigit())    #false
print(a.isnumeric())  #false
a="0"
print(a.isdecimal())  #true
print(a.isdigit())    #true
print(a.isnumeric())  #true
a="1/2"
print(a.isdecimal())  #false
print(a.isdigit())    #false
print(a.isnumeric())  #false
a="viii"
print(a.isdecimal())  #false
print(a.isdigit())    #false
print(a.isnumeric())  #false
print(a.isalpha())    #true
a="2.5"
print(a.isdecimal())  #false
print(a.isdigit())    #false
print(a.isnumeric())  #false


