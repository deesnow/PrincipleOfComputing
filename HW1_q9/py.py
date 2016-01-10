def appendsums(lst):
    """
    Repeatedly append the sum of the current last three elements of lst to lst.
    """
    for i in range(25):
        new_value = lst[len(lst)-1] + lst[len(lst)-2] + lst[len(lst)-3] 
        lst.append(new_value)
        print lst
    return lst
     
     
     
    
    
    
    
sum_three = [0, 1, 2]
appendsums(sum_three)
print sum_three[20]
print "DONE"


