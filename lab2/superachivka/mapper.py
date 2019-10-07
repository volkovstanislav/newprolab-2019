#/opt/anaconda/envs/bd9/bin/python
import sys

def map(uid, timestamp, url):
        sys.stdout.write("{}\t{}\t{}\n".format(uid, timestamp, url))

def mapper(line):
        if len(line.strip().split("\t")) == 3:
                uid, timestamp, url = line.strip().split("\t")
                if ((uid.isdigit()) and (url != '-')):
                        map(uid, timestamp, url)

def main():
        for line in sys.stdin:
                mapper(line)

if __name__ == "__main__":
        main()