#!/opt/anaconda/envs/bd9/bin/python

import sys

state = {
        'current_key' : None,
        'values' : []
}

def emit(key, value):
        sys.stdout.write('{}\t{}\n'.format(key,value))

def reducer(line):
        key, value = line.strip().split('\t')
        if key != state['current_key'] and state['current_key'] != None:
                reduce()
                state['values'] = []
        state['current_key'] = key
        state['values'].append(value)

def reduce():
        word_count = len(state['values'])
        emit(state['current_key'], word_count)

def main():
        for line in sys.stdin:
                try:
                        reducer(line)
                except ValueError:
                        continue