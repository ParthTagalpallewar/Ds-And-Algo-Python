
def search(pat, txt):
	    #finding possible cases of pat
	    
	    possibleCobnination = []
	    
	    combination = ""
	    for i in range(0, len(pat)):
	        combination += pat[i-1]
	        
	        for j in range(0, len(pat)):
	        
	            if(i != j):
	                combination += pat[-1]
	        
	        possibleCobnination.append(combination)
	        
	    return possibleCobnination

print(search("for","a"))
