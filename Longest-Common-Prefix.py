class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
    #     prefix = ''
    #     char = []
    #     check_length = 0
    #     flag = True

    #     # checking each word other than the first one
    #     for i in range(1,len(strs)):

    #         if len(strs[0]) > len(strs[i]):
    #             check_length = len(str[i])
    #         else:
    #             check_length = len(strs[0])

    # #going through each letter to match with the letter of the first word
    #         for j in range(check_length):
    #             if word[j]  == strs[0][j]

    first_word = strs[0]
    common_letters = []
    #picking words other than the first word in the array
    for i in range(1,len(strs)):
        this_word = strs[i]

        if len(first_word) > len(this_word):
            check_length = len(this_word)
        else:
            check_length = len(first_word)
        
        for j in range(check_length):
            if first_word[j] == this_word[j]:
                common_letters.append(first_word[j])

            






