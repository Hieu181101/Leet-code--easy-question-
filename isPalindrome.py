
#Solve this with string

class Solution(object):
    def isPalindrome(self, x):
        str_x = str(x)
        if str_x == str_x[::-1]:
            return True
        return False
    
#Solve this with using math modification only 

class Solution(object):
    def isPalindrome(self, x):
        if x < 0: return False   #Always false if negative 

        div = 1                     #check the divider for getting the first digit where 120 mod 100 = 1 or 1200 mod 2000 = 2
        while x >= 10 * div:
            div *= 10
        
        while x:
            right = x % 10         #get the right digit
            left = x // div        #get the first digit or the left

            if left != right: return False

            x = (x % div) // 10     #get rid of the left by mod div (see above) and get rid of the right by divide by 10
            div = div / 100         #remember to update the div since we get rid of 2 so it always divide by 100