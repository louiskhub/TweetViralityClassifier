#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Discards rows written in a language other than the one specified
@author: lmcdonald
"""

import pandas as pd
import csv


# Discards rows of a dataset written in a language other than the specified target language by retrieving the language tag
# from the 'language' column in the dataset
class LanguagePruner():

    def __init__(self, df):
    
        self._df = df

    # Helper Function that retrieves the counts of each available language and stores it in a csv in data/preprocessing
    # For EDA
    def get_language_counts(self):
        
        output_df = (self._df.language).groupby(self._df.language).count()
        output_df.to_csv('./data/preprocessing/language_counts.csv', index = False, quoting = csv.QUOTE_NONNUMERIC, line_terminator = "\n")
    
    # Drop rows of other langugages
    def drop_rows_by_language(self, language = "en"):
        
        output_df = self._df.drop(self._df[self._df.language != language].index)
        
        return output_df
        


    