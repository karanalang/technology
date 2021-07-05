# https://www.digitalocean.com/community/tutorials/how-to-index-and-slice-strings-in-python-3

class Python_String_Slicing:

    def stringSlice(self, S):

        print(" input S -> ", S)
        print(" from index 0 to index 5 (not including5) -> ", S[0:5])
        # print(" S[0::2] -> ", S[0::2])
        print(" 3rd element from end ", S[-3])
        print(" all from 5th element from backward to end of string -> ", S[-5:])
        print(" from 5th element to 1st element backwards (not including 1st element) ", S[-5:-1])

    def stringSlice_usingStride(self, S):
        print(" input S -> ", S)
        print('0th index to 5th index, every 1st elemnt (i.e. stride by 1) -> ',S[0:5:1])
        print('0th index to 5th index, every 2nd element (i.e. stride by 2) -> ', S[0:5:2])
        print('0th index to 5th index, every 2nd element (i.e. stride by 3) -> ', S[0:5:3])

        print('S[::2] -> ', S[::2])
        print('S[::2] -> ', S[::3])

        print(" S[::-1] reverse String -> ", S[::-1])
        print(" S[::-1] reverse String -> ", S[:-1])


    def string_countingMethods(self, S):

        print("S.count() - how many times letter appears in String -> ", S.count('h'))
        print("S.find, first index of letter in String ", S.find('e'))
        print("S.find, first index of letter in String, from index 5 -> ", S.find('e', 5))
        print("S.find, first index of string in String ", S.find('hello'))
        print("S.find, first index of string in String, backwards ", S.find('hello', -6))

        # searches for the position of the sequence “likes” between the index numbers of 40 and -6
        print(' serach between inndex 40 and -6, starting backwards -> ', S.find('likes', 40, -20))



sol = Python_String_Slicing()
S = 'hello there'
S2 = "01234567"
S1 = "Sammy likes to swim in the ocean, likes to spin up servers, and likes to smile."
hello= 'hello'
# sol.stringSlice(hello)
sol.stringSlice_usingStride(hello)
# sol.string_countingMethods(S1)