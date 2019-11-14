#!/opt/anaconda/envs/bd9/bin/python
import sys
from urllib.parse import urlparse, unquote
import re

def url2domain(url):
   try:
       a = urlparse(unquote(url.strip()))
       if (a.scheme in ['http','https']):
           b = re.search("(?:www\.)?(.*)",a.netloc).group(1)
           if b is not None:
               return str(b).strip()
           else:
               return ''
       else:
           return ''
   except:
       return


def map(uid, url):
	if url.startswith('http'):
		domain_url = url2domain(url)		
		sys.stdout.write("{}\t{}\n".format(uid, domain_url))

def mapper(line):
	if len(line.strip().split("\t")) == 3:
		uid, timestamp, url = line.strip().split("\t")
		if ((uid.isdigit()) & (url != '-')):
			map(uid, url)

def main():
	for line in sys.stdin:
		mapper(line)

if __name__ == "__main__":
	main()
