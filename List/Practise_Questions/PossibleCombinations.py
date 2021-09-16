def combo(line):
    b =[]
    one_line = list(line)
    for i in range(len(line)):
        for i in range(len(line)-1):
            one_line[i], one_line[i + 1] = one_line[i + 1] , one_line[i]
            b.append("".join(one_line))
    return b
