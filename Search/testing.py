def check_if_duplicates(list):
    if len(list) == len(set(list)):
        return False
    else:
        return True


list_of_elems = ['Hello', 'Ok', 'this', 'is', 'a', 'test']
result = check_if_duplicates(list_of_elems)
if result:
    print('Yes, list contains duplicates')
else:
    print('No duplicates found in list')
