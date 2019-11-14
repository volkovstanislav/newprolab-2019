#!/opt/anaconda/envs/bd9/bin/python
import sys

def reduce(uid, url):
	sys.stdout.write("{}\t{}\n".format(uid, url))

def reducer(line):
	uid, url = line.strip().split("\t")
	reduce(uid, url)

def main():
	for line in sys.stdin:
		reducer(line)

if __name__ == "__main__":
	main()
