from nltk.stem.snowball import SnowballStemmer
import pickle
import numpy as np
import math

def magnitude_normalize_columns(matrix):

	for j in range(len(matrix[0])):
		sum1=0
		for i in range(len(matrix)):
			sum1=sum1+((matrix[i][j])**2)
	
		sum1=math.sqrt(sum1)
		if(sum1==0):
			continue
		else:
			for i in range(len(matrix)):
				matrix[i][j]=float(matrix[i][j])/sum1

def magnitude_normalize_rows(matrix):
	for i in range(len(matrix)):
		sum1=0
		for j in range(len(matrix[0])):
			sum1=sum1+((matrix[i][j])**2)
	
		sum1=math.sqrt(sum1)
		if(sum1==0):
			continue
		else:
			for j in range(len(matrix[0])):
				matrix[i][j]=float(matrix[i][j])/sum1

stemmer=SnowballStemmer('english')

#Load the distinct words list
print("Please wait while initialization happens......")
with open('distinct.pkl','rb') as f:
	distinct_words=pickle.load(f)

#Load the TF_IDF vector
with open('tf_idf.pkl','rb') as f:
	TF_IDF_VECTOR=pickle.load(f)
magnitude_normalize_columns(TF_IDF_VECTOR)
print("Please enter the statement/tweet")
print()
###################################################################
testing=raw_input()
special_characters=['[',']','\\','/',',','"','@','#','.']

for i in special_characters:
	testing=testing.replace(i,"")

testing=testing.split(" ")
testing1=[]

for i in range(len(testing)):
	testing1.append(stemmer.stem(testing[i]))
	#print(testing1[i])

testing_row=[]
for i in range(len(distinct_words)):
	if(distinct_words[i] in testing1):
		testing_row.append(1)
	else:
		testing_row.append(0)
magnitude_normalize_rows([testing_row])
####################################################################
ans=np.matmul(testing_row,TF_IDF_VECTOR)
print(ans)
emotions=['Joy','Fear','Anger','Sadness','Disgust','Shame','Guilt']
mx=max(ans)
#print(ans)
#print(mx)
if(mx==0):
	print("No results found. Sorry, I think we are short on data.")
else:
	for i in range(len(ans)):
		ans[i]=ans[i]/(float)(mx)

	results=[]
	for i in range(len(ans)):
		results.append((ans[i],emotions[i]))
	results.sort()
	results=results[::-1]
	for i in results[:3]:
		print(i[1])



