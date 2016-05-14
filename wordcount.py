sw=input('How many words would you like to search? \n')
path=''
for i in range(int(sw)):
    word=input('Enter the word to determines its occurence count \n')
    wordlower=word.lower()
    fr=open(path,'r')
    data=fr.read()
    lowerdata=data.lower()
    spdata=lowerdata.split()
    wc=spdata.count(wordlower)
    print(wc)
    fr.close()
    
