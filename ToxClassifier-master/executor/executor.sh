#!/bin/bash
echo ' ------------ RUNNING TOX CLASSIFIER -------------- '
echo ' :: Running vectorization; if it crashes, check if paths are fine (see readme)'
echo "----------"
input_data_file='../example/example_input.fa'
verbose=0
echo '../toxClassVectorize.py -I ${input_file} -O _v --verbose ${verbose} --classifynotb 1'
python2 ../toxClassVectorize.py -I ${input_data_file} -O _v --verbose 1 --classifynotb 1
echo ':: Vectorization done!'
echo "----------"
echo '::  Running predictor'
echo 'Rscript ../toxClassRClassifier.R --modelsPath ../MLModels/ --vectorsPath ./'
Rscript ../toxClassRClassifier.R --modelsPath ../MLModels/ --vectorsPath ./
echo "----------"
echo '::  Completed, check out.csv'
echo "----------"

# Remove tmp file
rm _*.bres
rm *.hmmtab
rm *.out
rm _v*.csv
rm __tmp*
rm *.log
