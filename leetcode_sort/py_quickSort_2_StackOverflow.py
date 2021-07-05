class QuickSort:

    # https://stackoverflow.com/questions/18262306/quicksort-with-python
    # Simple implementation, but takes EXTRA SPACE
    # https: // www.youtube.com / watch?v = MZaf_9IZCrc
    def sort(self, array):
        """Sort the array by using quicksort."""

        less = []
        equal = []
        greater = []

        if len(array) > 1:
            pivot = array[0]
            for x in array:
                if x < pivot:
                    less.append(x)
                elif x == pivot:
                    equal.append(x)
                elif x > pivot:
                    greater.append(x)
            # Don't forget to return something!
            return self.sort(less) + equal + self.sort(greater)  # Just use the + operator to join lists
        # Note that you want equal ^^^^^ not pivot
        else:  # You need to handle the part at the end of the recursion - when you only have one element in your array, just return the array.
            return array




arr = [10, 7, 8, 9, 1, 5]
sol = QuickSort()
# n = len(arr)
# sol.quickSort(arr, 0, n-1)

sorted = sol.sort(arr)
print(" sorted -> ", sorted)
