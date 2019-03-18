import difflib
text1 = '''
hello world.
how are you.
nice to meet you.
'''
text1_lines = text1.splitlines()
text2 = '''
Hello World.
how are you!
Nice to meet you
'''
text2_lines = text2.splitlines()
dif = difflib.Differ()
diff = dif.compare(text1_lines, text1_lines)
print('\n'.join(list(diff)))
