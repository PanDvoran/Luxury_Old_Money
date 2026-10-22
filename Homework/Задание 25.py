def is_palindrome(text):
    text = text.lower()

    for sign in ',.:!?':
        text = text.replace(sign, '')

    text = text.replace(' ', '')
    return text == text[::-1]


print(is_palindrome('A man, a plan, a canal: Panama'))
print(is_palindrome('0P'))
print(is_palindrome('a.'))
print(is_palindrome('aurora'))
