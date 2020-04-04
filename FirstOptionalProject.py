# These are the functions used for the Removal and the Sorting of the list
def RemoveDuplicates(onelist):
    List_Whithout_Dup = []
    for i, item in enumerate(onelist):
        if item not in List_Whithout_Dup:
            List_Whithout_Dup.append(onelist[i])
    return List_Whithout_Dup

def sortList(onelist):     #I assume that a simple bubblesort is enough
    ElementsBeingSwapped = True
    while ElementsBeingSwapped:
        ElementsBeingSwapped = False
        for i in range(len(onelist) - 1):
            if onelist[i] > onelist[i+1]:
                onelist[i], onelist[i+1] = onelist[i+1], onelist[i]
                ElementsBeingSwapped = True
    return onelist

#End of functions for the lists 
##########################################################################################


##########################################################################################
# These are the functions used for the Removal and the Sorting of the dictionary
def RemoveDuplicatesDictionary(OneDictionary):
    Dictionary_Whithout_Dup = {}
    for key in OneDictionary:
        if OneDictionary.get(key) not in Dictionary_Whithout_Dup.values():
            Dictionary_Whithout_Dup[key] = OneDictionary.get(key)
    return Dictionary_Whithout_Dup


def sortDictionary(OneDictionary):
    Sortedresult = {}
    keys = sorted(OneDictionary, key=OneDictionary.get)
    for key in keys:
        Sortedresult[key] = OneDictionary[key]

    return Sortedresult
    
#End of functions for the dictionary
########################################################################################### 







#Something like the main fuction, where I have implemented the functions 

list1 = [30, 28, 28, 16, 14, 14, 12, 10]
print(RemoveDuplicates(list1))
print(sortList(list1))

a_dict = {"a": 30, "b":28, "c":28,  "d":16, "e":14, "f":14, "g":12, "h":10}
print(RemoveDuplicatesDictionary(a_dict))
print(sortDictionary(a_dict))
##########################################################################################