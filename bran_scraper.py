with open('./asoif.txt') as f:
    lines = f.readlines()
    t = ''.join(lines).split('\n\n\n\n\n\n')

    print(t)
