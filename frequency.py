import sys
import json
import re
import matplotlib.pyplot as plt
import numpy as np



Presedential_Candiates_List = ["Hillary Clinton", "Bernie Sanders", "Martin O'Malley",\
                                "Donald Trump","Jeb Bush","Carly Fiorina","Mike Huckabee","Marco Rubio"]
#Presedential_Candiates_List = ["Hillary Clinton", "Bernie Sanders","Donald Trump","Jeb Bush","Chris Christie"]
regex_list=[]
score_list=[0] * len(Presedential_Candiates_List)
count_list=[0] * len(Presedential_Candiates_List)
for canidate in Presedential_Candiates_List:
    regex_list.append(canidate.replace(" ", "|"))

def get_score(twitter_word_list,scores):
            Score = 0
            for each_word in twitter_word_list:
            #print "Actual Word",each_word
            	if each_word in scores:
                	Score =  Score + scores[each_word]
                	#print each_word,'Match',scores[each_word]
	    return Score	


def main():
    bernie_counter = 0
    hillary_counter = 0
    trump_counter = 0
    bss_score = 0 
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    sent_file.seek(0)
    tweet_file.seek(0)
    scores = {} # initialize an empty dictionary
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    line_list=tweet_file.readlines()
    for x in line_list:
        json_data = json.loads(x)
        if "text" in json_data:
            twitter_text=json_data["text"]
            encoded_twitter_text = twitter_text.encode('utf-8')
            twitter_word_list=encoded_twitter_text.split();
	    already_counted = [0] * len(Presedential_Candiates_List)
            for each_word in twitter_word_list:
		##Search for presidential Candidates Mentioned
		for i in range(0,len(Presedential_Candiates_List)):
			TEMP=re.search(regex_list[i],each_word, flags=re.I | re.X)
			if TEMP:
				count_list[i]=count_list[i]+1
				if (already_counted[i]==0):
                			score_list[i] = score_list[i]+get_score(twitter_word_list,scores);
					already_counted[i]=1

    sum_count=sum(count_list);
    for i in range(0,len(count_list)):
	count_list[i]=100*float(count_list[i])/sum_count
    fig, ax = plt.subplots()
    bar_width = 0.35
    opacity = 0.4
    n_groups = len(Presedential_Candiates_List)
    index = np.arange(n_groups)
    rects1 = plt.bar(index, count_list, bar_width,alpha=opacity,color='b')
    plt.ylabel('Relative % in Twitter Talk about Preidential Race')
    plt.xlabel('Presidential Candidates')
    plt.title('Which Presidential Candidates are being discussed the most on Twitter?')
    plt.xticks(index + bar_width, Presedential_Candiates_List)
    plt.legend()
    plt.tight_layout()
    plt.show()
    rects2 = plt.bar(index, score_list, bar_width,alpha=opacity,color='b')
    plt.ylabel('Score')
    plt.xlabel('Presidential Candidate')
    plt.title('Which Presidential Candidate Has What Connotation')
    plt.xticks(index + bar_width, Presedential_Candiates_List)
    plt.axhline(linewidth=4, color='r')
    plt.legend()
    plt.tight_layout()
    plt.show()
    tweet_file.close()
 

if __name__ == '__main__':
    main()
