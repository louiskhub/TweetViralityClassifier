#!/bin/bash

# create directory if not yet existing
mkdir -p data/preprocessing/split/

# install all NLTK models
python -m nltk.downloader all -q

# add labels
echo "  creating labels"
python -m code.preprocessing.create_labels data/raw/ data/preprocessing/labeled.csv

# other preprocessing (removing punctuation etc.)
echo "  general preprocessing"
python -m code.preprocessing.run_preprocessing data/preprocessing/labeled.csv data/preprocessing/preprocessed.csv --prune_lang --pipeline tweet remove_urls lowercase expand punctuation standardize tokenize numbers lemmatize remove_stopwords -e data/preprocessing/pipeline.pickle

# split the data set
echo "  splitting the data set"
python -m code.preprocessing.split_data data/preprocessing/preprocessed.csv data/preprocessing/split/ -s 42