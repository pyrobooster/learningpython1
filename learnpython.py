print ("lets learn python")

# simply logic to eval booleans
def sleep_in(weekday , vacation):
  if weekday == True or vacation == True:
    return True
  else:
    return False

#this easier version accomplished the same thing
def sleep_in(weekday , vacation):
  if not weekday or vacation:
    return True
  else:
    return False

# iterate multiple times
str = "hi"
n = 3
print (str * n)

#concatiing and a greeting
name1 = "Bob"
if name1 == "Bob":
  print ("hello " + name1 + "!")

#messing with arrays (lists)
a = [1,2,6]
print(a)
print(a[0])
#finding the last element in an array
print (a[len(a)-1])
# the following is an easier short hand way
print(a[-1])

