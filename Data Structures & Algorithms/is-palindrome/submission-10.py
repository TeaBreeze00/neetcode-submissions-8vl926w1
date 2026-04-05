class Solution:
    def isPalindrome(self, s: str) -> bool:
                
        pointer1 = 0
        pointer2 = len(s) - 1

        while pointer1 <= pointer2:

            while(pointer1 <= pointer2 and  not self.isAlphanumeric(s[pointer1])):
                pointer1 += 1

            while(pointer1 <= pointer2 and not self.isAlphanumeric(s[pointer2])):
                pointer2 -= 1    
            
            if pointer1 <= pointer2:
                if(s[pointer1].lower() != s[pointer2].lower()):
                    return False


            pointer1 += 1
            pointer2 -= 1

        return True   

    def isAlphanumeric(self, c) -> bool: # returns true if a character is alphanumeric
        return ((ord('A') <= ord(c) <= ord('Z')) or
        (ord('a') <= ord(c) <= ord('z')) or
        (ord('0') <= ord(c) <= ord('9')))

