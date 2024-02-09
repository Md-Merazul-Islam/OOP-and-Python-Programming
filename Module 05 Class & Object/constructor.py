
class our_hendle_rating:
    def __init__(self,Name,codechef,codeforces,):
        self.Name = Name
        self.codeforces = codeforces
        self.codechef = codechef
    
    def print_end(self,roll,clas):
        text = f'the end Roll : {roll} Class: {clas}'
        print(text)
#This is meraz info:
meraz = our_hendle_rating("Md Merazul Islam",1652,1385)
print(meraz.Name,meraz.codechef,meraz.codeforces)

#This is Antor info:
antor = our_hendle_rating("Md Antor Hassan",1004,1200)
print(antor.Name,antor.codechef,antor.codeforces)

#This is Alamin info:
alamin  = our_hendle_rating("Md Alamin hasssan",1009,1288)
print(alamin.Name,alamin.codechef,alamin.codechef)

#This is Fahad info:
fahad = our_hendle_rating("MD Fahad Hassan",1083,1089)
print(fahad.Name,fahad.codechef,fahad.codeforces)

#end msg
rating = our_hendle_rating("",298,974)
text_end = rating.print_end(672581,13)
# print(text_end)

