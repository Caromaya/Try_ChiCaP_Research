import sys

data = {}
first = True

# Process the first file
for line in open(sys.argv[1]):
    content = line.strip().split(";")
    if first:
        header = content[1:]
        first = False
        continue
    data[content[0].split(" ")[0]] = content[1:]

first = True
n_cols = len(header)

# Process the second file
for line in open(sys.argv[2]):
    content = line.strip().split(";")
    if first:
        print(line.strip() + ";" + ";".join(header))
        first = False
        continue

    content[0] = "-".join(content[0].replace("MIP", "").replace("-Research", "").rstrip("-").split("-")[0:2])
    
    try:
        print(line.strip() + ";" + ";".join(data[content[0]]))
    except KeyError:
        # Key not found in data dictionary, check for specific mappings
        if content[0] == "GMSB-066":
            print(line.strip() + ";" + ";".join(data.get("GMSB-ST066", ["NA"] * n_cols)))
        elif content[0] == "GMS-UP013":
            print(line.strip() + ";" + ";".join(data.get("GMSB-UP013", ["NA"] * n_cols)))
        elif content[0] == "GMS-UP011":
            print(line.strip() + ";" + ";".join(data.get("GMSB-UP011", ["NA"] * n_cols)))
        elif content[0] == "GMSB-UP0022":
            print(line.strip() + ";" + ";".join(data.get("GMSB-UP022", ["NA"] * n_cols)))
        else:
            print(line.strip() + ";" + ";".join(["NA"] * n_cols))
