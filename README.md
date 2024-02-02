# Arterial-Distension-Monitoring-Scheme-Using-FPGA-Based-Inference-Machine-in-Ultrasound-Scanner-Circuit-System
Python and matlab code used to design and validate the paper "An approach to monitoring arterial dilation using an FPGA-based inference machine in an ultrasound scanner circuit system".

# Frist SVM

* Requirement
    > python3.9

* Input data
    > Arterial-Distension-Monitoring-Scheme-Using-FPGA/dataset/1st_SVM_test.csv
    > ,feature_1,feature_2,feature_3,feature_4,feature_5,feature_6,feature_7,feature_8,feature_9,feature_10,label
4089,7.0625,9.8125,8.6875,29.062,61.5,62.25,222.19,362.31,198.38,192.12,1
89449,19.438,26.312,39.75,25.125,14.688,19.312,12.188,16.125,25.938,51.688,0
46737,127.19,142.38,181.56,111.38,57.125,42.75,34.0,44.25,47.312,76.875,0
11455,17.75,14.125,13.625,28.312,60.312,164.75,532.38,696.06,630.94,220.94,1
142144,16.312,15.25,10.25,13.438,23.375,17.812,16.0,18.438,21.25,89.5,0

* Usage
    > The frist SVM to estimate the wall-pattern score for 12 sub-regions within the scanning range.
        

# Second SVM

* Requirement
    > python3.9

* Input data
    > 

* Usage
    > The Second SVM to generate the inference result for probe positioning status.
    
