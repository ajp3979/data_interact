import argparse
import os
import pandas as pd
import sys


class DataInput:

    def __init__(self, path, dtype, orient=None):
        self.path = path
        self.dtype = dtype
        self.orient = orient
        if self.dtype == "csv":
            self.df = pd.read_csv(self.path)
        elif self.dtype == "tsv":
            self.df = pd.read_csv(self.path, sep='\t')
        elif self.dtype == "json":
            if self.orient == None:
                sys.exit('Provide "--orient" parameter for JSON')
            else:
                self.df = pd.read_json(self.path, orient=self.orient, typ='frame')
        self.columns = list(self.df.columns.values)
        self.length = len(self.df.index)


def main():
    parser = argparse.ArgumentParser(description='Explore your data with Pandas!')
    parser.add_argument('path',
                       metavar='path',
                       type=str,
                       help='the path to your input file')
    parser.add_argument("-t", "--type",
                    choices=["csv", "json", "tsv"],
                    required=True,  help="Required: the input data type")
    parser.add_argument("-o", "--orient",
                    choices=["split", "records", "index", "columns", "values", "table"],
                    required=False,  help="For JSON: define orientation")

    args = parser.parse_args()
    path = args.path

    if not os.path.exists(path):
        print('The path specified does not exist')
        sys.exit()
    dtype = args.type
    orient = args.orient

    print("Input Data: {}".format(path))
    d = DataInput(path, dtype, orient)
    df = d.df
    columns = d.columns
    length = d.length
    print("Your object is 'd' and your df is 'df'.")
    print("Your df length: {}".format(length))
    print("Your df has {} columns.".format(len(columns)))
    print("Your df columns: {}".format(columns))
    print(" ")
    print("Entering Interaction: (press 'Ctrl-d' to exit)")
    print(" ")
    print("For example, run: >>> df.head()")
    print(" ")
    import code
    code.interact(local=locals())

if __name__ == "__main__":
    main()

