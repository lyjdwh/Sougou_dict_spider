import datetime

with open("sogou.txt", 'r') as f:
    lines = f.readlines()
    lines.sort()
    lines = lines[1:]

    output = []

    for i in range(len(lines)):
        if (i == 0 or lines[i] != lines[i - 1]):
            line = lines[i].strip().split()

            try:
                line[0] = line[0][1:]
            except:
                print(i, line)

            line[0] = line[0].replace("lue", "lve")
            line[0] = line[0].replace("nue", "nve")

            line[0], line[1] = line[1], line[0]

            line.append("0\n")
            output.append("\t".join(line))

with open("sorted_sogou.txt", "w+") as f:
    f.writelines(output)
