"""
    This is a short exercice to illustrate binary_search algorithm (chapter 1)
    from Grokking Algorithms book written by Aditya Y. Bhargava

    The binary_search function takes a sorted array and an item. If the item
    is in the array, the function returns its position.
"""

def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1

my_list = [1, 3, 5, 7, 9]
my_item = input("What's your proposition? ")

try:
    int(my_item)
    print(binary_search(my_list, int(my_item)))
except:
    print(f"{my_item} isn't a integer!")
