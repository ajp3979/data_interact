# data_interact
Explore your data with Pandas and interactive Python!

```
usage: data_interact.py [-h] -t {csv,json,tsv}
                        [-o {split,records,index,columns,values,table}]
                        path


positional arguments:
  path                  the path to your input file

required arguments:
  -t, --type {csv,json,tsv}
                        Required: the input data type

optional arguments:
  -h, --help            show this help message and exit

  -o, --orient {split,records,index,columns,values,table}
                        Only required for JSON: define orientation of records
```


Example 1:
```
$ python data_interact.py ~/Downloads/aws_hunt_data.json --type json --orient table
```

Example 2:
```
$ python data_interact.py ~/Downloads/aws_hunt_data.csv --type csv
```

Use `ctrl-d` to exit interactive Python console.