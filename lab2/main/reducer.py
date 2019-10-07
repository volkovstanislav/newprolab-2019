#/opt/anaconda/envs/bd9/bin/python
import sys
import happybase

def reduce(uid, timestamp, url):
        if int(uid) % 256 == 93:
                connection = happybase.Connection('bd-master.newprolab.com')
                connection.open()
                table = connection.table('stanislav.volkov')
                table.put(uid, {'data:url': url.strip()}, int(timestamp))

def reducer(line):
        uid, timestamp, url = line.strip().split('\t')
        timestamp = int(float(timestamp) * 1000)
        reduce(uid, timestamp, url)

def main():
        for line in sys.stdin:
                reducer(line)

if __name__ == '__main__':
        main()