<samp>
  
Purpose:
The purpose of this code repository is to provide a Python Based Sentiment Analysis Model built on top of a ranked retrieval system powered by a Vector Space Model. I have used the ISEAR dataset.

ISEAR: 
The International Survey on Emotion Antecedents and Reactions as a python dataset for MachineLearning

Basic documentation:
The isear.csv file is the actual extract of the dataset, which was provided as an access database.
The data has been cleaned and normalized a bit 

Simple working: 
A basic vector-space-model based sentiment analysis system. 

I simply treat different emotions as different documents in the corpus. The best result according to the ranked-retrieval will be most likely the emotion for the query.Since I've already preprocessed and put in the pkl files which contains the TF-IDF and the distinct words, there's no need to run the pro_main.py and tf_idf.py again. You can just run the interact.py file and put in the string as an input whose sentiment will be analysed.

Caution: Take the results with a pinch of salt. There is considerable scope for improvement in this work by better NLP techniques, a larger dataset among others. Small queries might not give an answer straight away.


Ansuman Dibyayoti Mohanty - 2016A7PS0043H 

</samp>

