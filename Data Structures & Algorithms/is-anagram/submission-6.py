class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
#to be an anagram, it has to have same numbers of letters, and also
#be the same string just reversed. one way might be to reverse the second
#string and check if this new list is equal to the old list 

        # new_list = list(s)
        # betterlist = new_list.reverse

        # if new_list == list(t):
        #     return True
        # return False

# one mistake I made here was that I didnt see that the orders can be different
# convert to list, sort them, if they are equal, then true


        if sorted(s) == sorted(t):
            return True
        return False
