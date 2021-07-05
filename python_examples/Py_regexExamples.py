# https://www.w3schools.com/python/python_regex.asp

import re


# s = "A man, a plan, a canal: Panama 111 :"
# for i in range(len(s)):
#     if re.search('[a-zA-Z0-9]',s[i].lower()):
#         print(" alphanumeric -> ", s[i])
#     else:
#         print(" not alphanumeric -> ", s[i])


a1 = "an_ b1"
for i in range(len(a1)):
    print(" is a letter or number -> ", a1[i].isalnum(), " - ", a1[i].isalpha(), " - ", a1[i])

s1 = re.sub(r'[\W]+','',a1)
s2 = re.sub(r'[\w]+','',a1)
print("s1 -> ", s1, " s2 -> ", s2)


def isPalindrome_regex(self, s: str) -> bool:
    s = re.sub(r'[\W_]+', '', s)
    s = s.lower()
    return s == s[::-1]