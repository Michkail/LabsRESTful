numb = [1, 10, 20, 3, 10, 23, 12, 10]
asc = numb.sort()
desc = numb.sort(reverse=True)
if choice := input():
    if choice == 'asc':
        print(asc)
    if choice == 'desc':
        print(desc)
