# Arterial-Distension-Monitoring-Scheme-Using-FPGA-Based-Inference-Machine-in-Ultrasound-Scanner-Circuit-System
Python and matlab code used to design and validate the paper "An approach to monitoring arterial dilation using an FPGA-based inference machine in an ultrasound scanner circuit system".

# Frist SVM

* Requirement
    > python3.9

* Usage
    > The frist SVM to estimate the wall-pattern score for 12 sub-regions within the scanning range.

* Input data
    * Location: Arterial-Distension-Monitoring-Scheme-Using-FPGA/dataset/1st_SVM_test.csv
    * Sample
      > |index|feature_1|feature_2|feature_3|feature_4|feature_5|feature_6|feature_7|feature_8|feature_9|feature_10|label|
      > |-----|---------|---------|---------|---------|---------|---------|---------|---------|---------|----------|-----|
      > |4089|7.0625|9.8125|8.6875|29.062|61.5|62.25|222.19|362.31|198.38|192.12|1|
      > |89449|19.438|26.312|39.75|25.125|14.688|19.312|12.188|16.125|25.938|51.688|0| 
      > |46737|127.19|142.38|181.56|111.38|57.125|42.75|34.0|44.25|47.312|76.875|0|
      > |11455|17.75|14.125|13.625|28.312|60.312|164.75|532.38|696.06|630.94|220.94|1|
      > |142144|16.312|15.25|10.25|13.438|23.375|17.812|16.0|18.438|21.25|89.5|0|
        

# Second SVM

* Requirement
    > python3.9

* Usage
    > The Second SVM to generate the inference result for probe positioning status.

* Input data
    > Location: Arterial-Distension-Monitoring-Scheme-Using-FPGA/dataset/1st_SVM_test.csv
    * Sample
      > |index|feature_1|feature_2|feature_4|feature_4|feature_5|feature_6|feature_7|feature_8|feature_9|feature_10|feature_11|feature_12|label|
      > |-----|---------|---------|---------|---------|---------|---------|---------|---------|---------|----------|----------|----------|-----|
> |36|0.13427331398268|0.111487177767828|0.559447397816133|1.0|0.401110706592335|0.140427965976242|0.818345760828998|0.840017243970373|0.271582214873681|0.233730208025495|0.240526719690664|0.282371729410752|1|
> |878|0.45519|0.97038|0.308|0.075559|0.71575|0.72484|0.13024|0.1696|0.23385|0.13813|0.11226|0.096997|1|
> |1303|0.11254|0.40439|0.7392|0.49049|0.2401|0.15539|0.1193|0.28848|0.16162|0.1433|0.11073|0.090916|0|
> |552|0.179946096632157|0.14871964691927|0.12779714716181|1.0|0.520426154365477|0.122359725137578|0.951459468356542|0.872367522515637|0.129455265152664|0.152283942462411|0.122512864533747|0.17951272260773|1|
> |517|0.190540329522089|0.188469602789336|0.0684739518524529|0.998401892134017|0.475436722997963|0.229245317145906|0.442897288670605|0.879980259478972|0.217705539871115|0.215050074431685|0.223310322841915|0.327669069465585|1|






    
