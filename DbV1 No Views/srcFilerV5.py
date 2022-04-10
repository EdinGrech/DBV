### IMPORT ONLY FUN() OPERATIONAL PARA REQ  fileName=NAME OF CSV FILE,shoppingList=UNRESTRICTED LIST WILL BE CLEARED,Seperator1=STRING SEPERATOR,Seperator2=SECONDARE STRING SEPERATOR

### FUNCTIONALITY TO ADD 
    ## MAKE SURE THAT IS ,Seperator1,Seperator2 ARE NOT FILLER THEY ARE DEFAULTED TO "," AND "\n"
    ## for the love of jesus add functuon that lets you set file type to (".txt",".csv")
    ## ADD SAVER fun()
    ## Relational fun() - save relationships between functions
        ## one to one - look at 2 tables and after finding the one record stops
        ## one to many - looks at second table completly 
        ## many to many - create a new file with related table primery key links

### new functions to add <-- not done
    ## sorters numbers and letters 
    ## field removal
    ## automatic primery key assigner

### wild discovery massive issue with csv mode.... field names are on the side not the top/ fix in next fersion ?

from operator import itemgetter

def ReaderList(fileName,shoppingList,Seperator1=",",Seperator2="\n",fileType=".txt"): #loads the csv file (separators ca nbe what ever really as long as there are 2) then first creats a bsic list of items then if second seperator is detected it sends the list to a converter
    if (len(shoppingList) == 0):
        if (Seperator2=="\n"):
            return Reader2nList(fileName,Seperator1,fileType)
        with open(fileName+fileType,'r') as csv_file:
            for line in csv_file:
                comaPos = int(1)
                while comaPos > 0:                  
                    comaPos=line.find(Seperator1)
                    sepi2=line.find(Seperator2)
                    if(comaPos==-1) and (sepi2==-1):
                        SavedItem=str(line)
                        shoppingList.append(SavedItem)
                        return shoppingList 
                    elif(sepi2 < comaPos):
                        if(Seperator2!="\n"):
                            SavedItem=str(line[:sepi2])
                            shoppingList.append(SavedItem)
                            line=line[sepi2+1:]
                        shoppingList=listconverter(line,csv_file,shoppingList,Seperator1,Seperator2)#list of lists converter
                        return shoppingList 
                    else:
                        SavedItem=str(line[:comaPos])
                        shoppingList.append(SavedItem)
                        line=line[comaPos+1:]
    else:
        shoppingList.clear()
        ReaderList(fileName,shoppingList,Seperator1,Seperator2)

def Reader2nList(fileName,Seperator1,fileType):
    r2ShoppingList=[]
    with open(fileName+fileType,'r') as This_file:
        for line in This_file:
            comaPos=line.find(Seperator1)
            SavedItem=str(line[:comaPos])
            r2ShoppingList.append(SavedItem)
        r2ShoppingList=[[val] for val in r2ShoppingList]
        return itemLoader(fileName,fileType,Seperator1,r2ShoppingList)

def itemLoader(fileName,fileType,Seperator1,r2ShoppingList):
    with open(fileName+fileType,'r') as This_file:
        for lineNo,line2 in enumerate(This_file):
            comaPos=line2.find(Seperator1)
            x=False
            while comaPos>0:
                comaPos=line2.find(Seperator1)
                sepi2=line2.find("\n")
                if x==True:
                    if comaPos!=-1:
                        r2ShoppingList[lineNo].append(str(line2[:comaPos]))
                        line2=line2[comaPos+1:]
                    elif sepi2==-1:
                        r2ShoppingList[lineNo].append(str(line2))
                    else:
                        r2ShoppingList[lineNo].append(str(line2[:sepi2]))
                else:
                    line2=line2[comaPos+1:]
                    x=True
        return r2ShoppingList

def listconverter(line,csv_file,shoppingList,Seperator1,Seperator2):
    shoppingList=[[val] for val in shoppingList]
    infoTransop=nestedListLoader(line,csv_file,shoppingList,Seperator1,Seperator2)#call nest loader
    return infoTransop
    
def nestedListLoader(line,csv_file,shoppingList,Seperator1,Seperator2):#this function will automaticaly load details about every item (each detail type is on a diffrent line/separator) untill there are not items left
    comaPos=1
    x=-1
    while comaPos > 0:
        x=x+1
        comaPos=line.find(Seperator1)
        sepi2=line.find(Seperator2)    
        if(comaPos==-1) and (sepi2==-1):
            SavedItem=str(line)
            shoppingList[x].append(SavedItem)
            shoppingList=shoppingList
            csv_file.close()
            return shoppingList
        elif(sepi2 < comaPos) and (sepi2!=-1):
            SavedItem=str(line[:sepi2])
            shoppingList[x].append(SavedItem)
            line=line[sepi2+1:]
            shoppingList=nestedListLoader(line,csv_file,shoppingList,Seperator1,Seperator2)#this is the issue, bug
            return shoppingList
        else:
            SavedItem=str(line[:comaPos])
            shoppingList[x].append(SavedItem)
            line=line[comaPos+1:]

##paramiters example
##shoppingList=[]
##print(ReaderList("testFile2-1",shoppingList,",","|",".csv"))

def SaverList(fileName,shoppingList,Seperator1=",",Seperator2="\n",fileType=".txt"):
    nestedListQ = any(isinstance(i, list) for i in shoppingList)
    ShoppingListFile=open(fileName+fileType,"w")
    if(nestedListQ==True):
        z=int(len(shoppingList))
        for i in range(len(shoppingList)):
            c=int(len(shoppingList[i]))
            for x in range(len(shoppingList[i])):
                ShoppingListFile.write(str(shoppingList[i][x]))
                if x < c-1:
                    ShoppingListFile.write(Seperator1)
            if i < z-1:
                    ShoppingListFile.write(Seperator2)
        ShoppingListFile.close()
    else:
        c=int(len(shoppingList))
        for x in range(len(shoppingList)):
            ShoppingListFile.write(str(shoppingList[x]))
            if x < c-1:
                ShoppingListFile.write(Seperator1)
        ShoppingListFile.close()

##paramiters example
##shoppingList=[["a",1],["b",2]]
##or
##shoppingList=[["PrimeryKey","1","2","3"],["Name","Meat","Veg","Fruit"]]
##shoppingList=[["Item","Carrots","chicken","oranges"],["Type","3","1","2"],["price","4$","9$","3$"]]
##SaverList("testFile2-1",shoppingList,",","|",".csv")
##SaverList("testFile1-1",shoppingList,",","|",".csv")

def one2one2many(fileName1,fileName2,relatedFieldName,newCPFieldName,relatedFieldNameTo,requiredFieldName,posOfCopyField=1,Seperator1=",",Seperator2="\n",fileType=".txt"):#requiredFieldName to shove in another list
    workingList1=[]
    workingList2=[]
    
    workingList2=ReaderList(fileName2,workingList2,Seperator1,Seperator2,fileType)
    workingList1=ReaderList(fileName1,workingList1,Seperator1,Seperator2,fileType)
    workingList1=copyLinkField(fileName1,relatedFieldName,newCPFieldName,posOfCopyField,Seperator1,Seperator2,fileType)
    
    RPos=workingList1[0].index(newCPFieldName)
    R2Pos=workingList2[0].index(relatedFieldNameTo)
    RE3Pos=workingList2[0].index(requiredFieldName)
    for x in range(len(workingList1)-1):
        PKFindMe=workingList1[x+1][RPos]
        for i in range(len(workingList2)-1):
            recVal=workingList2[i+1][R2Pos]
            if (recVal==PKFindMe):
                workingList1[x+1][RPos]=workingList2[i+1][RE3Pos]
    return workingList1

#examples to call function
## value of #workingList1/testFile1-1=[["PrimeryKey","1","2","3"],["Name","Meat","Veg","Fruit"]]
## value of #workingList2/testFile2-1=[["Item","Carrots","chicken","oranges"],["Type","3","1","2"],["price","4$","9$","3$"]]
##listName=[]        
##listName=one2one2many("testFile1-1","testFile2-1","Type","NewLink","PrimeryKey","Name",2,",","|",".csv")
##print(listName)

def many2many(bridgeFileName,PKFieldName1,PKFieldName2,RelListVals,Seperator1=",",Seperator2="\n",fileType=".txt"):
    RelListVals.insert(0,[PKFieldName1,PKFieldName2])
    SaverList(bridgeFileName,RelListVals,Seperator1,Seperator2,fileType)

##example
##RelListVals=[[1,4],[3,4],[3,2]]

def copyLinkField(fileName1,CPFieldName,newCPFieldName,posOfCopyField,Seperator1=",",Seperator2="\n",fileType=".txt"):
    workingList1=[]
    workingList1=ReaderList(fileName1,workingList1,Seperator1,Seperator2,fileType)
    for x in range(len(workingList1[0])):
        FieldNameInList=str(workingList1[0][x])
        if FieldNameInList == CPFieldName:
            for i in range(len(workingList1)):
                if i==0:
                    workingList1[i].insert(posOfCopyField,newCPFieldName)
                else:
                    workingList1[i].insert(posOfCopyField,workingList1[i][x])
            break
    return workingList1

##example 
##copyLinkField("testFile1-1","Type","NewLink",2,",","|",".csv")
##print(one2one2many("testFile1-1","testFile2-1","Type","NewLink","PrimeryKey","Name",2,",","|",".csv"))

def one2one2manyNoCopy(fileName1,fileName2,relatedFieldName,relatedFieldNameTo,requiredFieldName,Seperator1=",",Seperator2="\n",fileType=".txt"):#requiredFieldName to shove in another list
    workingList1=[]
    workingList2=[]
    
    workingList2=ReaderList(fileName2,workingList2,Seperator1,Seperator2,fileType)
    workingList1=ReaderList(fileName1,workingList1,Seperator1,Seperator2,fileType)
    
    RPos=workingList1[0].index(relatedFieldName)
    R2Pos=workingList2[0].index(relatedFieldNameTo)
    RE3Pos=workingList2[0].index(requiredFieldName)
    for x in range(len(workingList1)-1):
        PKFindMe=workingList1[x+1][RPos]
        for i in range(len(workingList2)-1):
            recVal=workingList2[i+1][R2Pos]
            if (recVal==PKFindMe):
                workingList1[x+1][RPos]=workingList2[i+1][RE3Pos]
    return workingList1

#example
#use is to replace link field
#one2one2manyNoCopy("testFile1-1","testFile2-1","Type","PrimeryKey","Name",Seperator1=",",Seperator2="\n")

def listConverterDisp2SaveForm(shoppinglist):#pretty to ugly
    convList=[]
    for y in range(len(shoppinglist[0])):
        start=True
        for x in range(len(shoppinglist)):
            shovItm=shoppinglist[x][y]
            if start==True:
                convList.append(shovItm)
            else:
                convList[y].append(shovItm)
            if x==0:
                convList[y]=[convList[y]]
            start=False

    return convList

### its dose a think... ngl forgot but i will use it maybe ... one day ... some point
#listSort=[["filed 1","filed 2"],["2","4"],["8","3"]]
#print(listConverterDisp2SaveForm(listSort))

def listConverterSave2DipsForm(shoppinglist):#ugly to pretty
    convList=[]
    maxRange=int(0)
    for x in range(len(shoppinglist)):
        saveItm=shoppinglist[x][0]
        if x==0:
            convList.append(saveItm)
            convList=[convList]
        else:
            convList[0].append(saveItm)
        if maxRange<len(shoppinglist[x]):
            maxRange=int(len(shoppinglist[x]))
    for y in range(maxRange-1):
        for i in range(len(shoppinglist)):
            try:
                saveItm=shoppinglist[i][y+1]
                if i==0:
                    convList.append(saveItm) 
                    convList[convList.index(saveItm)]=[convList[y+1]]
                else:
                    convList[y+1].append(saveItm)
            except:
                print("Error, Table is incomplete, please finish it and try again")#could probably be inproved 
    return convList

#workingList1=[["PrimeryKey","1","2","3"],["Name","Meat","Veg","Fruit"]]        
#print(listConverterSave2DipsForm(workingList1))

def sorterAto(listSort,fieldNameSort,reverseVal=False):
    tempSortList=[]
    fieldSoPos=listSort[0].index(fieldNameSort)
    for x in range(len(listSort)-1):
        tempSortList.append(listSort[x+1])
    tempSortList=sorted(tempSortList,key=itemgetter(fieldSoPos),reverse=reverseVal)
    tempSortList.insert(0,listSort[0])
    return tempSortList

###exaple 
#listSort=[["filed 1","filed 2"],["2","4"],["8","3"]]
#print(sorterAto(listSort,"filed 2",reverseVal=False))
