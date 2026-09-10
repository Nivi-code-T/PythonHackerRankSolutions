def split_line(line):
    word=line.split()
    return "-".join(word)

line=input()
print(split_line(line))
    