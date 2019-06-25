"""
A dplyr wrapper for pandas

This is a monkey patch of the pandas dataframe adding
four dplyr methods:

arrange
filter
select
mutate

Examples
--------
>>> df = pd.DataFrame({'col1': [1, 2, 3, 4],
...                     'col2': [1, 2, 1, 2], 
...                     'col3': ['a', 'b', 'a', 'b']})
>>> df.filter('col2 == 2').shape
(2, 3)
>>> df.select('col1','col2').shape
(4, 2)

The most important usage is to pipe the results
from one method to the next
>>> (df.filter('col2 == 2')
...   .select('col1','col2')
...   .shape)
(2, 2)
"""

import pandas as pd

def arrange_not_sort(self, *args, **kwargs):
    return self.sort_values(*args, **kwargs)
pd.DataFrame.arrange = arrange_not_sort

def filter_not_query(self, query):
    return self.query(query)
pd.DataFrame.filter = filter_not_query

def select_not_loc(self, *args):
    arg_vec = [arg for arg in args]
    return self.loc[:,arg_vec]
pd.DataFrame.select = select_not_loc

def mutate_not_assign(self, **kwargs):
    return self.assign(**kwargs)
pd.DataFrame.mutate = mutate_not_assign