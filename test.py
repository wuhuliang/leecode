#--coding:utf-8--

from name_function import get_full_name

print ("Enter 'q' at any time to quit.")
while True:
    first = raw_input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = raw_input("\nPlease gibe me a last name: ")
    if last == 'q':
        break

    formatted_name = get_full_name(first,last)
    print ("\tNeatly formatted name: " + formatted_name + '.')
