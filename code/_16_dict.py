# Dictionary is an collection of key-value pairs, where keys are unique and each key have a value 
# (analogous to real dictionary with word-meaning pairs)


# Create an empty dictionary
phone_book = {}  
# phone_book = dict()
print(phone_book)


# Create a non-empty dictionary
phone_book = {
    "tintin": 4876465656,
    "deedee": 5516162344,
    "popeye": 2648165999,
    "bubbles": 3879566444
}
print(phone_book)


# Get length of dictionary
phone_book_length = len(phone_book)
print(phone_book_length)


# Accessing value using key/index
tintin_number = phone_book["tintin"]  # Raises a 'KeyError' if key is not present
# tintin_number = phone_book.get("tintin")  # Does not raise an error if key is not present; instead returns 'None'
print(tintin_number)


# Adding new entry
phone_book["saitama"] = 1456883991
print(phone_book)


# Updating an existing entry
phone_book["saitama"] = 1111111111
print(phone_book)


# Remove an existing entry
del phone_book["tintin"]
print(phone_book)


# Pop an existing entry
popped_entry = phone_book.pop("popeye")
print(popped_entry)
print(phone_book)


# Pop last inserted pair
popped_random_entry = phone_book.popitem()
print(popped_random_entry)
print(phone_book)


# Check if key exists
tintin_exists = "tintin" in phone_book
print(tintin_exists)
deedee_exists = "deedee" in phone_book
print(deedee_exists)


# Any values (mutable/immutable) are possible in dictionary
details_book = {
    "tintin": {
        "nickname": "T",
        "age": 17,
        "favorite_numbers": [7, 9, 8]
    },
    "bubbles": {
        "nickname": None,
        "age": 5,
        "favorite_numbers": [1, 2, 3]
    },
    "saitama": {
        "nickname": "One",
        "age": 37,
        "favorite_numbers": [1]
    }
}


tintin_age = details_book["tintin"]["age"]
print(tintin_age)


tintin_fav_third_number = details_book["tintin"]["favorite_numbers"][2]
print(tintin_fav_third_number)


for person in details_book:
    print(f'Name: {person}')
    for detail in details_book[person]:
        print(f'{detail} = {details_book[person][detail]}')