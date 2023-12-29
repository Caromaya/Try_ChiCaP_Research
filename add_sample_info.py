import sys

data = {}
first = True

# Process the first file
for line in open(sys.argv[1]):
    content = line.strip().split(",")
    if first:
        header = content[2:]
        first = False
        continue
    #print(content[1].split(" ")[0])
    #print(line.strip())
    data[content[1].split(" ")[0]] = content[2:]

first = True
n_cols = len(header)

#print(data)
#quit()

#if "GMSB-ST066" in data:
#    print("carro!")

# Process the second file
for line in open(sys.argv[2]):
    content = line.strip().split(",")
    if first:
        print(line.strip() + "," + ",".join(header))
        first = False
        continue

    #print(content[0])
    #print(data[content[0]])

    content[0] = "-".join(content[0].replace("MIP", "").replace("-Research", "").rstrip("-").split("-")[0:2])
    
    try:
        print(line.strip() + "," + ",".join(data[content[0]]))
    except KeyError:
        print(line.strip() + "," + ",".join(["NA"] * n_cols))
