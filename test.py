
with open('./asoif.txt') as f:
    lines = ''.join(f.readlines())

    lines = lines.split('\n\n\n\n\n\n')
