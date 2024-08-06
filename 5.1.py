import string
import keyword

user_variable = input("Enter your variable: ")
# user_variable = '_'
# user_variable = '__'
# user_variable = '___'
# user_variable = 'x'
# user_variable = 'getvalue__'
# user_variable = 'get value'
# user_variable = 'get!value'
# user_variable = 'some_super_puper_value'
# user_variable = 'Get_value'
# user_variable = 'get_Value'
# user_variable = 'getValue'
# user_variable = '3m'
# user_variable = 'm3'
# user_variable = 'assert'
# user_variable = 'assert_exception'



if user_variable:
    is_first_symbol_not_digit = not user_variable[0].isdigit()
    print("First digit check pass - ", is_first_symbol_not_digit)

    is_all_char_lowercase = True
    for char in user_variable:
        if char.isalpha():
            if char.isupper():
                is_all_char_lowercase = False
                break
    print("Lowercase check pass - ", is_all_char_lowercase)

    not_content_punctuation = True
    for char in user_variable:
        for punctuation in string.punctuation + ' ':
            if punctuation == '_':
                continue
            else:
                if char == punctuation:
                    not_content_punctuation = False
                    break
    print("Punctuation and Space check pass - ", not_content_punctuation)

    # not_content_duble_underscore = True
    # if not user_variable.find('__') == -1:
    #     not_content_duble_underscore = False
    # print("Underscore check pass - ", not_content_duble_underscore)

    no_multiple_underscores = True
    if len(user_variable) > 1:
        compare_var = len(user_variable)*'_'
        if compare_var == user_variable:
            no_multiple_underscores = False
    print("Multiple underscore check pass - ", no_multiple_underscores)



    if user_variable in keyword.kwlist:
        not_keyword = False
    else:
        not_keyword = True
    print("Not keyword: ", not_keyword)


    if is_first_symbol_not_digit and is_all_char_lowercase and not_content_punctuation and no_multiple_underscores and not_keyword:
        print(f"True. The variable '{user_variable}' is acceptable")
    else:
        print(f"False. The variable '{user_variable}' is unacceptable")
else:
    print("False. You entered an empty string.")
