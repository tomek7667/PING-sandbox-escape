import string
code = input('Your scientific computation: ')
code = ''.join([c for c in code if c in string.printable])
forbidden = ['eval', 'exec', 'import', 'open', 'system', 'os', 'builtins']
for f in forbidden:
    code = code.replace(f, '')
exec(code)
