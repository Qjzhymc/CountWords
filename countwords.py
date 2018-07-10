
def wordCount(filepath):
	count={}
	keys=[]
	with open(filepath) as f:
		for line in f:
			words=line.strip('\n').split(' ')
			for word in words:
				wordlist=count.keys()
				if word in wordlist:
					count[word]+=1
				else:
					count[word]=1
					keys.append(word)
	return count,keys
filepath='C:/Users/22467/Downloads/words.txt'		
count,keys=wordCount(filepath)

with open('C:/Users/22467/Downloads/Q1.txt','w') as fwrite:
	for i in  range(len(keys)):
		if i==len(keys)-1:
			fwrite.write(str(keys[i]+' '+str(i)+' '+str(count[keys[i]])))
		else:
			fwrite.write(str(keys[i]+' '+str(i)+' '+str(count[keys[i]])+'\n'))
		#print(str(keys[i]+' '+str(i)+' '+str(count[keys[i]])))
		





