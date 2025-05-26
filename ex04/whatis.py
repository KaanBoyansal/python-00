import argparse
import sys

def main():
	parser = argparse.ArgumentParser(description='Checks if the given number is odd or even.')
	parser.add_argument('nbr', help='number')

	args = parser.parse_args()

	if not isinstance(args.nbr, int):
		print("AssertionError: argument is not an integer")

if __name__ == "__main__":
	main()
