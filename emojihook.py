#!/usr/bin/env python3

def convert_to_sed(key, val):
	return f"\t-e 's/{key}/{val}/g' \\"

def convert_for_random(key, vals):
	space_vals = " ".join([f'"{v}"' for v in vals])
	return \
"""
ARR=({vals})
ARR_SIZE=${{#ARR[@]}}
RAND_IDX=$(($RANDOM % $ARR_SIZE))
RAND_ELEM=${{ARR[$RAND_IDX]}}
TEXT=$(echo "$TEXT" | sed -e "s/{key}/$RAND_ELEM/g")
""".format(key=key, vals=space_vals)

# TODO: Add "dev" target that generates a bash file that we can manually run
def main():
	random_table = []
	normal_table = []

	with open("emojis.txt", "r") as f:
		mapping = [line.strip().split() for line in f] # List pairs [ [a,b], [c,d], ... ]
		# note vals is "a" or "a, b, c" that we convert to ["a"] or ["a", "b", "c"]
		for key, vals in mapping:
			vals = vals.split(",")
			print(vals)
			if len(vals) == 1:
				normal_table.append((key, vals[0]))
			else:
				clean_vals = [v.strip() for v in vals]
				random_table.append((key, clean_vals))

		normal_table = [convert_to_sed(pair[0], pair[1]) for pair in normal_table]
		normal_code = "\n".join(normal_table)

		random_table = [convert_for_random(pair[0], pair[1]) for pair in random_table]
		random_code = "".join(random_table)
			
	with open("commit-msg.template", "r") as f:
		template = f.read()

	generated_hook = template.replace("@@conversion_table@@", normal_code)
	generated_hook = generated_hook.replace("@@random_table@@", random_code)
	print(generated_hook)

	with open("commit-msg", "w") as f:
		f.write(generated_hook)

if __name__ == '__main__':
	main()