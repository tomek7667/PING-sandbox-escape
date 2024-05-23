import string
code = input('Your scientific computation: ')
code = ''.join([c for c in code if c in string.printable])
for keyword in ['eval', 'exec', 'import', 'open', 'system', 'os', 'builtins',
                '.', '[', ']']:
    if keyword in code:
        print('You are jailed!', keyword)
        break
else:
    exec(code)
