import string
user_str = input("Type your string to convert it into a hashtag: ")


if user_str:
    hashtag = ''

    for char in user_str:
        if char not in string.punctuation:
            hashtag += char

    hashtag = '#' + hashtag.title()
    hashtag = hashtag.replace(' ', '')
    hashtag = hashtag[:140]

    print(f"Origin string: {user_str}")
    print(f"Your hashtag is: {hashtag}")

else:
    print("You need to type something to create hashtag")












