import sys
data={}

first=True
for line in open(sys.argv[2]):
	content=line.strip().split(";")
	if first:
		first=False
		header=";".join(content[1:])
		continue

	data[content[0]]=content[1:]

first=True
for line in open(sys.argv[1]):
	if first:
		print(line.strip()+";"+header)
		first=False
		continue
	content=line.strip().split(";")
  # Not sure if this works Jesper, but I tried!
  genes_to_search = content[4].split("|")

  try:
    # Search each gene individually in the ChiCaP file
    # Hoping both genes are not in the gene list...
    values_to_print = [";".join(data[gene]) for gene in genes_to_search]
    print(line.strip() + ";" + ";".join(values_to_print))
  except:
    print(line.strip() + ";" + ";".join(["NA"] * 5))
