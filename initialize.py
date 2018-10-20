dictOfPOSWithWords= {}
dictOfPOSWithPOS ={}
transitionTable ={}
likelihoodTable={}

def initialize (file):
 with open(file, 'r') as inputFile:
    content= inputFile.readlines()
    #startend to make sure the first DT is "preceded" by it
    previous= "startEnd"
    
    for line in content:

      if not line.strip():
         previous ="startEnd"
         continue
      else :
         word_and_tag= line.strip("\n").split("\t")
         print("word and tag:", word_and_tag)
         word = word_and_tag[0].lower()
         tag = word_and_tag[1]
	 # populates the word dictionary
         if tag not in dictOfPOSWithWords:
             dictOfPOSWithWords[tag]={}
             dictOfPOSWithWords[tag][word]=1
         else:
             if word not in dictOfPOSWithWords[tag]:
            # print("aq gavichede lol")
                 dictOfPOSWithWords[tag][word]= 1
             else:
                 dictOfPOSWithWords[tag][word]=  dictOfPOSWithWords[tag][word]+1
            

            #populates the POS dictionary for emission with values following it: 

         if tag not in dictOfPOSWithPOS:
             dictOfPOSWithPOS[tag]={}
             dictOfPOSWithPOS[previous]=1
                
         else:
             print (previous)
             print (dictOfPOSWithPOS[tag])
             if previous not in dictOfPOSWithPOS[tag]:
                 dictOfPOSwithPOS[tag][previous]=1
             else:
                 dictOfPOSWithPOS[tag][previous]=  dictOfPOSWithPOS[tag][previous]+1
         previous = tag

 makeTransitionTable()
 makeLikelihoodTable()

#creates a probability table of emissions
def makeTransitionTable():
    for POS, POS_previous in dictOfPOSWithPOS.items():
        total=0
        transitionTable[POS]={}
        for key in POS_previous:
            total= total+ POS_previous[key]
        for key in POS_previous:
            likelihood= POS_previous[key]/total
            transitionTable[POS][key]=likelihood
        
#same method as above, but for words and POS 
def makeLikelihoodTable():
    for POS, word in dictOfPOSWithWords.items():
        total=0
        likelihoodTable[POS]={}
        for key in word:
            total= total+ word[key]
        for key in word:
            likelihood= word[key]/total
            likelihoodTable[POS][key]=likelihood



if __name__ == "__main__":
    file = "WSJ_02-21.pos"
    initialize(file)





    
