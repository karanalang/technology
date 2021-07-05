# https://stackoverflow.com/questions/5213033/sort-a-list-of-lists-with-a-custom-compare-function
# https://ao.gl/how-to-write-a-custom-comparator-in-python/
# https://softwareengineering.stackexchange.com/questions/151069/sorting-using-a-custom-definition-of-and-in-python


class my_int(int):

    def __lt__(a,b):
        return (a%b)%2 != 0

    def __gt__(a,b):
        return (a%b)%2 == 0


# x = [my_int(2),my_int(7), my_int(5), my_int(10)]
x = [my_int(2),my_int(7)]

print(sorted(x))
