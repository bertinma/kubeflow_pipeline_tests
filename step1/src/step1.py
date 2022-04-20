import os 
import argparse
from pathlib import Path 

def connect(args):
    sum = args.input + args.plus
    with open(args.output, 'w') as out_file:
        out_file.write(f"sum:{sum}\n")
    

    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output', type=str, help="destination to save dataset")
    parser.add_argument('-i', '--input', type=int, required=True)
    parser.add_argument('-p', '--plus', type=int, required=True)
    opt = parser.parse_args()
    
    Path(opt.output).parent.mkdir(parents=True, exist_ok=True)

    connect(opt)