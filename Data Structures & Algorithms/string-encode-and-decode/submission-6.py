class Solution:

    def encode(self, strs: List[str]) -> str:

        mystring = ""

        for s in strs:
            mystring += str(len(s)) + "#" + s

        return mystring    

    def decode(self, s: str) -> List[str]:
        
        #This is the list of string that I am going to return
        string_list = []

        # This is the plan, I have a string to this format: "#abs#def#klm" so I am going
        # to iterate over the string with 2 pointers, Everytime I encouter a # with my second pointer, I
        # am going to extract the characters between the first and second pointer,
        # Then I move the first pointer to the location of the second pointer

        # initializing the first pointer at the first location
        i = 0

        while i < len(s):
            j = i
            
            # continue searching through the array until you see a #
            while(s[j] != '#'):
                j += 1

            length = int(s[i:j]) # This is the length of the substring to be extracted
            i = j + 1
            j = i + length
            string_list.append(s[i:j])
            
            i = j

        return string_list    




