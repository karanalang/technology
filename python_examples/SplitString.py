import re

class SplitString:

    def splitString(self, paragraph:str):

        paragraph1 = re.sub(r'[\W]+',' ',paragraph)

        para = 'WAGr131414'
        p = re.match(r'[A-Za-z0-9]+', paragraph)
        print(" p -> ", p)

        print(re.match(r'[\w]+', para).string)

        print(" paragraph1 -> ", paragraph1)

        paragraph2 = re.sub(r'[!?\',;.]+', ' ', paragraph)

        print(" paragraph2 -> ", paragraph2)

        words = paragraph1.lower().split()
        print(" words ->", words)

        words1 = paragraph1.lower().split(' ')
        print(" words1 -> ", words1)

        pass




soln = SplitString()
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
soln.splitString(paragraph)