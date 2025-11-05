str1 = "How much cost this T-shirt?"
str2 = "T-shirt price is 5$"
str3 = "Can you shut down price?"
str4 = "No, I can't"

string = [str1,str2,str3,str4]
one_step = [x.upper() for x in string if "price" in x]
print(one_step)
