class StringDS:
    
    def __init__(self):
        pass
    
    def isPalindrome(self,str):
        str2 = str[::-1]
        return str == str2
    
    
    
    
String_toll = StringDS()

res = String_toll.isPalindrome("HIH")
print(res)

