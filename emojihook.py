#!python3

def convert_to_sed(key, val):
	return f"\t-e 's/{key}/{val}/g' \\"

def main():
	with open("emojis.txt", "r") as f:
		mapping = [line.strip().split() for line in f] # List pairs [ [a,b], [c,d], ... ]
		# mapping = {pair[0]:pair[1] for pair in mapping}
		mapping = [convert_to_sed(pair[0], pair[1]) for pair in mapping]
		mapping = "\n".join(mapping)
			
	with open("commit-msg.template", "r") as f:
		template = f.read()

	generated_hook = template.replace("@@conversion_table@@", mapping)
	print(generated_hook)

	with open("commit-msg", "w") as f:
		f.write(generated_hook)

if __name__ == '__main__':
	main()