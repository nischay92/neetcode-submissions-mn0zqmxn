class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #edge case : where s1 if larger than s2, permutation of s1 in s2 not possible
        if len(s1) > len(s2): return False
        # we first adjust the values of s1 characters to gather their counts.
        s1count, s2count = [0]*26, [0]*26
        for i in range(len(s1)):
            s1count[ord(s1[i]) - ord('a')] += 1
            s2count[ord(s2[i]) - ord('a')] += 1
        matches = 0
        for i in range(26):
            matches += (1 if s1count[i] == s2count[i] else 0)
        l = 0
        # we traverse through the s2 string now, we start from s1 
        # because we already fetched the character count.
        for r in range(len(s1),len(s2)):
            if matches == 26:
                return True
            # whenver we move right pointer, configure the index
            # check if new character matches with the one in s1
            index = ord(s2[r]) - ord('a')
            s2count[index] += 1
            if s1count[index] == s2count[index]:
                matches += 1
            elif s1count[index] + 1 == s2count[index]:
                matches -= 1
            # here we are also checking for the case where we remove the character
            # from the left of the window
            index = ord(s2[l]) - ord('a')
            s2count[index] -= 1
            if s1count[index] == s2count[index]:
                matches += 1
            elif s1count[index] - 1 == s2count[index]:
                matches -= 1
            l += 1
        return matches == 26
        

            

