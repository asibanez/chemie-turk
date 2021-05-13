import sys
import pandas as pd

def prefill(origin_path):
    destination_path = origin_path + '_prefilled'
    df = pd.read_csv(origin_path)
    keep = ["cveid", "description", "spans"] + [col for col in df.columns if col.endswith("-tag")]
    df = df[keep]
    df = df.rename(columns= lambda x: x.replace("tag", "fill"))
    df.to_csv(destination_path, index=None)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: prefill.py [origin_path]')
        exit()

    origin_path = sys.argv[1]
    prefill(origin_path)