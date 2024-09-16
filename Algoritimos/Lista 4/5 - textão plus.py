texto = '''The Python Software Foundation and the global Python community welcome and encourage participation by
everyone. Our community is based on mutual respect, tolerance and encouragement, and we are working to
help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.'''
texto = texto.replace(',', ' ')
texto = texto.replace(':', ' ')
texto = texto.replace('.', ' ')

texto = texto.lower()

texto = texto.split()

t = 0
for i in texto:
    if i[0] in 'python' or i[-1] in 'python':
        i = int(len(i))
        if i > 4:
            t = t + 1
print(t)
