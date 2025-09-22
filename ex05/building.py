import sys
import string

def findSums(arg):
	"""Returns the sums of lower, upper, digits, and space characters in the given string as dictionary."""
	up = 0
	low = 0
	spc = 0
	dig = 0
	
	try:
		strs = str(arg) 
	except:
		print("Given parameter is not a string!")
		sys.exit(1)

	for tmp in strs:
		if tmp.islower():
			low += 1
		if tmp.isdigit():
			dig += 1
		if tmp.isupper():
			up += 1
		if tmp.isspace():
			spc += 1
	puncts = [ch for ch in strs if ch in string.punctuation]

	return {
		"punc": len(puncts), 
		"lowers": low, 
		"uppers": up, 
		"spaces": spc,
		"digits": dig, 
		"total": len(strs)}

def main():
	args = sys.argv

	if len(args) < 2:
		text = input("What is the text to count?\n")
	elif len(args) > 2:
		print("AssertionError: more than one argument is provided!")
		sys.exit(1)
	elif len(args[1]) == 0 or args[1] == None:
		print("PLease provide a string!")
		sys.exit(1)
	else:
		text = args[1]
	sums = findSums(text)
	print(f"The text contains {sums['total']} characters:\n{sums['uppers']} upper letters\n{sums['lowers']} lower letters\n{sums['punc']} punctuation marks\n{sums['spaces']} spaces\n{sums['digits']} digits")

if __name__ == "__main__":
	main()
