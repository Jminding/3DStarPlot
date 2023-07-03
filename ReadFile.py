# File: ReadFile.py
# Description: Read bsc5.dat file and make it into a csv
# Name: Jaymin Ding
# UT EID: jd54998
# Date: 6/23/23

import pandas as pd
import os

def read(): # A few lines glitch with pandas but they're fixed
    fin = open("Data/bsc5.dat")
    spacing = list(map(int, open("Data/spacing.txt").read().split())) # spacing for each line (read manually from a file)
    headers = open("Data/headers.txt").read().split() # headers (read manually from another file)
    fout = open("Data/bsc5.csv", "w")
    fout.write(",".join(headers) + "\n")
    for line in fin:
        for i in range(len(spacing)):
            fout.write(line[0:spacing[i]].strip())
            fout.write("," if i != len(spacing) - 1 else "")
            line = line[spacing[i]:]
        fout.write("\n")
    fin.close()
    fout.close()


def main(): # Run this function if you need to
    df = pd.read_csv(os.path.join("Data", "bsc5.csv"))
    # print(df)
    print(df.shape)
    print(df.head(5))
    print(df.tail(5))
    print(df.describe())
    print(df.info())


if __name__ == "__main__":
    main()