import re # module for processing regular expressions https://docs.python.org/3/library/re.html

# Initial prompt to user
line = input("Enter a phone number to validate or 'exit' when done. ")

# TODO Define your regex
# "[0-9]{3}-[0-9]{3}-[0-9]{4}"
phone_regex = "\+?[-\s]?\(?(\d{3})\)?\s?\-?(\d{3})\s?\-?(\d{4})"
# \+?([\d]{0,3})[-\s]?\(?(\d{3})\)?\s?\-?(\d{3})\s?\-?(\d{4})
while line != "exit":
    # TODO Find matches

    # a = re.findall(phone_regex, line)
    # matches = re.match("c", line)
    # matches = re.split("-", line)
    matches = re.search(phone_regex, line)


    # TODO If no match found, print that no number was found
    if matches == None:
        print('No number was found')
   
    
    # TODO Else, break number up into area code, prefix, and suffic
    else:
        # print(matches[1])
        print(f'Area code: {matches[1]} \nPrefix: {matches[2]} \nSuffix: {matches[3]}')

    
    # As a stretch goal, you can modify your regex to search for country codes
    # too and print that out as well!
    
    
    # Done validating, read in a new line
    line = input("Enter a phone number to validate or 'exit' when done. ")

    # r'\tTab' is called an r string, which stops handling backslashes in a special way
    # [] <-- a character set, e.g. [-.] match a dash or a dot.
    # don't need to escape the dot inside a character set with \
    # remember character sets can be long but just represent one character

    # carrot ^ means something different in a character set
    # matches everything that is not in that character set

    # can use a group () to say the whole group is optional:
    # (www\.)?

    # group 0 is everything that you captured

    # https://www.youtube.com/watch?v=K8L6KVGG-7o

    # this the one https://regex101.com/