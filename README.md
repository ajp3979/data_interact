# Data Interact
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


**Example 1:**
```
$ python data_interact.py ~/Downloads/aws_hunt_data.json --type json --orient table
```

**Example 2:**
```
$ python data_interact.py ~/Downloads/aws_hunt_data.csv --type csv
```

**Example Output:**
```
Input Data: /Users/andrewpritchett/Downloads/aws_hunt_data.json
Your object is 'd' and your df is 'df'.
Your df length: 643
Your df has 21 columns.
Your df columns: ['request_params', 'aws_region', 'event_name', 'user_arn', 'error_code', 'error_msg', 'timestamp', 'principal_id', 'access_key', 'account_id', 'event_source', 'user_name', 'user_agent', 'sourceip', 'avg_inter_arrival_time', 'machine', 'unique_event_names', 'ts', 'date', 'unique_days', 'uq_sources']
 
Entering Interaction: (press 'Ctrl-d' to exit)
 
For example, run: >>> df.head()
 
Python 3.7.4 (default, Aug 13 2019, 15:17:50) 
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> df.head()
   request_params aws_region             event_name                                           user_arn    error_code                                          error_msg                 timestamp  ... avg_inter_arrival_time machine unique_event_names                  ts       date unique_days uq_sources
0                  us-east-1                GetRole  arn:aws:sts::682973668593:assumed-role/Assume-...  AccessDenied  User: arn:aws:sts::682973668593:assumed-role/A... 2019-08-20 19:25:37+00:00  ...                    0.0   False                 33 2019-08-20 19:25:37 2019-08-20           1         16
56                 us-west-2    DescribeStackEvents  arn:aws:sts::682973668593:assumed-role/Assume-...  AccessDenied  User: arn:aws:sts::682973668593:assumed-role/A... 2019-08-20 19:25:32+00:00  ...                    0.0   False                 33 2019-08-20 19:25:32 2019-08-20           1         16
57                 us-west-2  ListFunctions20150331  arn:aws:sts::682973668593:assumed-role/Assume-...  AccessDenied  User: arn:aws:sts::682973668593:assumed-role/A... 2019-08-20 19:25:28+00:00  ...              3367342.5   False                 33 2019-08-20 19:25:28 2019-08-20           2         16
58                 us-west-2  ListFunctions20150331  arn:aws:sts::682973668593:assumed-role/Assume-...  AccessDenied  User: arn:aws:sts::682973668593:assumed-role/A... 2019-06-03 20:52:17+00:00  ...              3367342.5   False                 33 2019-06-03 20:52:17 2019-06-03           2         16
59                 us-west-2  ListFunctions20150331  arn:aws:sts::682973668593:assumed-role/Assume-...  AccessDenied  User: arn:aws:sts::682973668593:assumed-role/A... 2019-06-03 20:40:43+00:00  ...              3367342.5   False                 33 2019-06-03 20:40:43 2019-06-03           2         16

[5 rows x 21 columns]
>>> exit()
```

**NOTE:**
Use `ctrl-d` or type `exit()` to exit interactive Python console.
