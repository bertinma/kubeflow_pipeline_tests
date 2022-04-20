import os 
import argparse
from pathlib import Path 

def connect(opt):
    x = 5
    # create and write in the .ini file 
    with open(opt.input, 'r') as f_in, open(opt.output, 'w') as f_out:
        while(1):
            line = f_in.readline()
            if not line:
                break
            line = int(line.rstrip('\n').split(':')[-1])
            f_out.write(f"{x * line}\n")
            # print("{} x {} = {}".format(line, x, x*line))
            

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', type=str)
    parser.add_argument('-o', '--output', type=str)
    opt = parser.parse_args()

    Path(opt.output).parent.mkdir(parents=True, exist_ok=True)

    connect(opt)