#question 1:
from collections import Counter
 
def count_and_display_vowels(string):
    vowels = 'aeiouAEIOU'
    vowels_list = filter(lambda c: c in vowels, string)
    count = Counter(vowels_list)
    return count
 
string = "Guvi Geeks Network Private Limited"
print(count_and_display_vowels(string))


# question 2:
n=20
for i in range (n):
    for j in range(n-i-1):
        print(" ", end="")
    for j in range(i+1):
        print(j+1,end=" ")
    print("\n")


#question 3:
import re 
def rem_vowel(string): 
    return (re.sub("[aeiouAEIOU]","",string))             
string = "Guvi Geeks Network Private Limited"
print(rem_vowel(string)) 


#question 4:
S = "Python Programming Language"
a = ""
for i in S:
    if i not in a:
        a += i
print("Unique characters in s :",len(a))


#question 5:
def isPalindrome(s):
 
    rev = ''.join(reversed(s))
 
    if (s == rev):
        return True
    return False
 
s = "malayalam"
ans = isPalindrome(s)
 
if (ans):
    print("Yes")
else:
    print("No")



#question 7:
 #  import collections.Counter() + max()
from collections import Counter
 
test_str = "GeeksforGeeks"
 
# using collections.Counter() + max() to get Maximum frequency character in String
res = Counter(test_str)
res = max(res, key = res.get) 
 
# printing result 
print ("The maximum of all characters in GeeksforGeeks is : " + str(res))


#question 8:

from collections import Counter
# function to check if two strings are anagram
def check(s1, s2):
    if(Counter(s1) == Counter(s2)):
        print("True")
    else:
        print("False")
 #main program
s1 = "listen"
s2 = "silent"
check(s1, s2) 

    
#question 9:

string="Guvi Geeks Network Private Limited"
print(string)
#using split to count words
res=string.count(" ")+1
print(str(res))

