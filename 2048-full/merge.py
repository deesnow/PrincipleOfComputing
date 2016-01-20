"""
Merge function for 2048 game.
"""

def order_list(line):
    
    """
    Ordering the input list for merge function
    """
    
    origin = line
    ordered = list()
    no_zeros = 0
    # push zero values back 
    for idx in range(len(origin)):
        if origin[idx] != 0:
            ordered.append(origin[idx])
        else:
            no_zeros += 1

    for idx in range(no_zeros):
        ordered.append(0)
        
    return ordered

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """    
    not_merged = order_list(line)
#     print not_merged    
    # Start merging
    skip = False
    for idx in range(len(not_merged)-1):
        if skip == False:
            if not_merged[idx] == not_merged[idx + 1]:
                not_merged[idx] += not_merged[idx + 1]
                not_merged[idx + 1] = 0
                skip = True
#                 print not_merged , idx
            else:
                continue
        else:
            skip = False
            continue
    merged = order_list(not_merged)    
    
    return merged


#Test phase

# line1 = [2, 0, 2, 4]
# 
# #print order_list(line1)
# 
# print line1
# 
# print merge(line1)
# 
#  
# line2 = [0, 0, 2, 2]
# print line2
# print merge(line2)
#  
# line3 = [2, 2, 0, 0]
# print line3
# print merge(line3)
# line4 = [2, 2, 2, 2, 2]
# print line4
# print merge(line4)
# line5 = [8, 16, 16, 8]
# print line5
# print merge(line5)

