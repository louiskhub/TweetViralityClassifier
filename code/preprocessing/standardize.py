#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Preprocessor replaces UK spelling variations with their US equivalent to standardize spellings
@author: lmcdonald
"""

import re
from code.preprocessing.preprocessor import Preprocessor
from code.preprocessing.util.spellings import SPELLINGS_MAP


# substitutes UK spellings with US form
# credit: http://www.tysto.com/uk-us-spelling-list.html
class Standardizer(Preprocessor):

    # constructor
    def __init__(self, input_col, output):
        # input column "tweet", new output column
        super().__init__([input_col], output)
    
    # get preprocessed column based on data frame and internal variables
    def _get_values(self, inputs, spellings=SPELLINGS_MAP):
    
        # appends uk spellings to RegEx string ("centre|theatre|...")
        uk_spelling_pattern = re.compile('({})'.format('|'.join(spellings.keys())), 
                                      flags=re.IGNORECASE|re.DOTALL)

        # replace spellings with their mapping
        def standardize(uk_spelling):
            
            match = uk_spelling.group(0)

            if spellings.get(match):
                us_spelling = spellings.get(match)
            else:
                us_spelling = spellings.get(match.lower())

            return us_spelling
        
        # change UK spelling to US spelling
        column = inputs[0].str.replace(uk_spelling_pattern, standardize)
        return column