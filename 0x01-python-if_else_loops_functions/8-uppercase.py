def uppercase(s):
    for char in s:
        if ord('a') <= ord(char) <= ord('z'):
            print(chr(ord(char) - ord('a') + ord('A')), end='')
        else:
            print(char, end='')

    # Print a new line at the end
    print()
