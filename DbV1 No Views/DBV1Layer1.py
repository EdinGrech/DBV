### INTERFACE - LAYER1
###    - PLAN -
###     BE ABLE TO ENTER TABLE DATA 
###     BE ABLE TO VIEW DATA FROM ACROSS 1. TABLE
###     BE ABLE TO SELECT A FIELD TO VIEW 
###     HAVE A SORT=(MIGHT GO INTO SRCFILER)
###     BE ABLE TO RELATE TABLES WITH SPECIFIC FIELDS=(MIGHT GO INTO SRCFILER)
###     BE ABLE TO VIEW RELATED TABLES=(MIGHT GO INTO SRCFILER)
###     BE ABLE TO EDIT TABLES=(MIGHT GO INTO SRCFILER)
###     =BACK END 
###     HAVE A BACK UP FILE LIKE A MASTER AND CHILD--(COULD BE ITS OWN MODULE) ## when being edited by users


####    FUTURE IMPROVEMENTS
### Future note make a function to create the menues automatically, seems a bit stupid to manually create them 
##- same goes for the input cheaks

##Note make sure that when functions finish they lead back to mainMenu()

import srcFilerV5
import os
from time import sleep

def inputIVal(vPrint,Low=None,Hi=None):#verifies inputs for intiger and can be given a range
    while True:
        try:
            saveItm=int(input(vPrint))
            if saveItm>=Low and saveItm<=Hi:
                return saveItm
            if Low==None and Hi==None:
                return saveItm
            else:
                print(f"Error, option out of range. Enter a number between {Low} and {Hi}")
        except:
            print("Error, Invalid Input, please enter a number from the options avalable")

def savermodule(fileName,workingList,genDetReturn):#saves list in a file picks which gendets to use######## improvement make it look for a file with the same name to give an over wwrite error
    if genDetReturn!=None:
        srcFilerV5.SaverList(fileName,workingList,genDetReturn[1],genDetReturn[2],genDetReturn[0])
    else:
        print("\tEntering Default Mode")
        srcFilerV5.SaverList(fileName,workingList)
    print("\n\t==Saves Process Complete==")

def readFileFinder(genDetReturn): #new mass change [0] to the ends of recevers
    workerViewList=[]
    operation=bool(0)
    while operation==bool(0):
        try:
            fileName=input("Enter File Name: ")
            if genDetReturn!=None:
                workerViewList=srcFilerV5.ReaderList(fileName,workerViewList,genDetReturn[1],genDetReturn[2],genDetReturn[0])
            else:
                print("\tEntering Default Mode")
                workerViewList=srcFilerV5.ReaderList(fileName,workerViewList)
            operation=bool(1)
        except(FileNotFoundError):
            print("File Not Found please enter an existing file Name\n")
            validInp=bool(0)
            while validInp==bool(0):
                try:
                    exit=int(input("would you like to return to Main Menu?\nEnter 1 to exit 2 to Retry: "))
                    validInp=bool(1)
                except:
                    print("Invalid Input Try Again")
            if exit==int(1):
                mainMenu()
    return workerViewList,fileName

def munuMaker(menuList):#creats very sexy menus when you give it the option and the commands you would like it to exe when selected, could use some upgrages IE add the ability to rin through the nested list to look for multiple commands
    for x in range(len(menuList)):    
        print("\t option",x+1,"\t"+menuList[x][0])
    inpOpt=inputIVal("Enter an option: ",1,x+1)
    exeCom=str(menuList[inpOpt-1][1])
    exec(exeCom)

def actualViewer(workerViewList):#this is what actually displays the stuff
    letCount=""
    for x in range(len(workerViewList[0])):
        if x==0:
            print(f"\n{workerViewList[0][x]}",end="")
        elif(x==len(workerViewList[0])):
            print(f"\t\t{workerViewList[0][x]}")   
        else:
            print(f"\t\t{workerViewList[0][x]}",end="")
        letCount=letCount+workerViewList[0][x]

    print("\n"+"-"*(len(letCount)+x*12))
    for y in range(len(workerViewList)-1):
        y=y+1
        for x in range(len(workerViewList[y])):
            if x!=0:
                print(f"\t\t{workerViewList[y][x]}",end="")
            else:
                print(f"\n\t{workerViewList[y][x]}",end="")
    print("\nFinished Operation")

def actual4FieldViewer(workerViewList,fieldViewList):#this is what actually displays the stuff
    
    letCount=""
    for op in range(len(fieldViewList)):
        if op == 0:
            print(f"\n{workerViewList[0][fieldViewList[op]]}",end="")
        else:
            print(f"\t\t{workerViewList[0][fieldViewList[op]]}",end="")
        letCount=letCount+workerViewList[0][fieldViewList[op-1]]
    print("\n"+"-"*(len(letCount)+op*12))##fix line printer to current#its okie ish rn
    
    for x in range(len(workerViewList)-1):
        x=x+1
        for op in range(len(fieldViewList)):
            if op == 0:
                print(f"\n{workerViewList[x][fieldViewList[op]]}",end="")
            else:
                print(f"\t\t{workerViewList[x][fieldViewList[op]]}",end="")

def listRemover(shoppingList,listPopAblePos):
    shoppingList.pop(listPopAblePos)
    return shoppingList



def mainMenu():
    options=[["View \tTable","viewTableSubMenu()"],["New \tTable","NewTableSubMenu()"],["Edit \tTable","EditTableSubMenu()"],["Relate \tTable","Pass"],["Remove \tFile","pass"],["Quit","quit()"]]
    print("\n\t\t==Main Menu==")
    munuMaker(options)

def fileRemover(): #currently not working not sure why [issue is the file selected dose not get removed], ### ok i think solution to get this working is to get the user to input the path as part of the general details <--- 
    print("\t==File Removal Process==")
    valInp=bool(False)
    while valInp==False:
        try:
            contSure=int(input("\nAre you sure you want to continue? \n -Enter 1 for yes\n -Enter 2 for no\n\nEnter option: "))
            valInp=True
        except:
            print("Invalid inputtry again")
    if contSure!=1:
        mainMenu()
    genDetOpt=int(input("\n\tHave File General Details Been fileld or use Default Paramiters?\n\n\t\tTo fill in type 1 else type 2 \n\t\tEnter Option Here: "))
    if genDetOpt==1:
        genDetReturn=generalDetails()
    else:
        genDetReturn=[".txt",",","\n"]
    fileName=input("\nEnter File Name To Remove: ")
    if os.path.exists(f"{fileName}+{genDetReturn[0]}"):#not working cos of paths?
        os.remove(f"{fileName}+{genDetReturn[0]}")
        print("\n\tFile has been removed, Returning to main menu")
        mainMenu()
    else:
        print("\n\tError: The file does not exist")
        fileRemover()

def viewTableSubMenu():#sub menu for diffrent table viewing methods
    VsubOpt=[["View Full Table","ViewFullTable()"],["View Select Fields","ViewSelectFields()"],["Return to Main Menu","mainMenu()"]]
    print("\n\t\t==Sub Menu==")
    munuMaker(VsubOpt)

def generalDetails():#used to enter file's general details (type,sep1,sep2)
    print("\n\t\t==General File Detail Entry==")
    global fileType
    global Seperator1
    global Seperator2
    fileType=input("Enter File Type, Example;'.txt': ")
    Seperator1=input("Enter File First Seperator, Example;',': ")
    Seperator2=input("Enter File First Seperator, Example;'\ n': ")
    print("\n-General Details Set, \n\tYou will not need to full this section in again unless you would \n\tlike to change oh the above values for future files.\n\n")

    return fileType,Seperator1,Seperator2

def ViewFullTable(): #displays all the fields in a table
    print("\n\t\t==Table Details Entry==")
    genDetOpt=int(input("\n\tHave File General Details Been fileld or use Default Paramiters?\n\n\t\tTo fill in type 1 else type 2 \n\t\tEnter Option Here: "))
    if genDetOpt==1:
        genDetReturn=generalDetails()
    else:
        genDetReturn=None
    workerViewList=readFileFinder(genDetReturn)[0]

    workerViewList=srcFilerV5.listConverterSave2DipsForm(workerViewList)
    #print(workerViewList)#debug make sure we can read
    workerViewList=sortQurPrompt(workerViewList)
    actualViewer(workerViewList)
    mainMenu()

def ViewSelectFields():#opens select fields
    print("\n\t==Which Fields would you like the view?==")
    genDetOpt=int(input("\nHave File General Details Been fileld or use Default Paramiters?\n\n\t\tTo fill in type 1 else type 2 \n\t\tEnter Option Here: "))
    if genDetOpt==1:
        genDetReturn=generalDetails()
    else:
        genDetReturn=None
    workerViewList=readFileFinder(genDetReturn)[0]
    
    for x in range(len(workerViewList[0])):
        print("\tField",x+1,"\t"+workerViewList[0][x])
    stillEnterField=int(1)
    fieldViewList=[]
    while stillEnterField == int(1):
        viewFieldOpt=int(input("Enter Field Number you would like to view: "))
        fieldViewList.append(viewFieldOpt-1)
        inputCorrect=bool(0)
        while inputCorrect==bool(0):
            try:
                stillEnterField=int(input("Would you like to view more Fields\n\tEnter 1 for new Field\n\tEnter 0 to view entered Fields\n\tEnter Option: "))
                inputCorrect=bool(1)
            except:
                print("Invalid Input Try Again")
    workerViewList=sortQurPrompt(workerViewList,fieldViewList)
    actual4FieldViewer(workerViewList,fieldViewList)
    mainMenu()
    
def NewTableSubMenu(): #Sub menu for entering tables
    VsubOpt=[["Enter New Table","NewTableEntry()"],["Edit new Table Data","EditTableSubMenu()"],["Return to Main Menu","mainMenu()"]]
    print("\n\t\t==Sub Menu==")
    munuMaker(VsubOpt)

def NewTableEntry(): ### not tested #kinda tested ## make it pipeable ======
    workingList=[]
    enterField=bool(True)
    i=int(0)
    while enterField!=bool(False):
        newField=input(f"Enter Field name number {i+1}: ")
        workingList.append(newField)
        i=i+1
        inputCor=bool(False)
        while inputCor==bool(False):
            try:
                contQur=int(input("Would you like to Enter another field? \nEnter 1 to Enter New Field\nEnter 2 to start entering records\n\nEnter Option: "))
                inputCor=bool(True)
            except:
                print("Invalid input, please try again")
        if contQur!=1:
            enterField=bool(False)
    
    newRecord=bool(True)
    recCount=int(0)
    workingList=[[val] for val in workingList]
    while newRecord==True:
        recCount=recCount+1
        for x in range(len(workingList)):
            validInput=bool(False)
            while validInput==False:
                try:
                    recInfo=input(f"Enter record {recCount}'s Info for field {workingList[x][0]}: ")
                    workingList[x].append(recInfo)
                    validInput=bool(True)
                except:
                    print("Sorry there is an Issue, Avoid using special characters")
        inputCor=bool(False)
        while inputCor==bool(False):
            try:
                contQur=int(input("\n\nWould you like to Enter another Record? \nEnter 1 to Enter New Record\nEnter 2 to Exit and Save\n\nEnter Option: "))
                inputCor=bool(True)
            except:
                print("Invalid input, please try again")
        if contQur!=1:
            newRecord=bool(False)

    fileName=input("Time to save what would you like to call your file: ")
    valInp=bool(False)
    while valInp==False:
        try:
            genDetOpt=int(input("\n\tHave File General Details Been fileld or use Default Paramiters?\n\n\t\tTo fill in type 1 else type 2 \n\t\tEnter Option Here: "))
            valInp=True
        except:
            print("Error Invalid Input, Try again")
    if genDetOpt==1:
        genDetReturn=generalDetails()
    else:
        genDetReturn=None

    savermodule(fileName,workingList,genDetReturn)
    mainMenu()
    
def EditTableSubMenu():### not tested #kinda tested
    VsubOpt=[["View Table you want to edit","ViewFullTable()"],["Add Field","addField()"],["Remove Field","removeField()"],["Edit Record","EditRecordSubMenu()"],["Return to Main Menu","mainMenu()"]]
    print("\n\t\t==Sub Menu==")
    munuMaker(VsubOpt)
    
def addField():### new saving mode implimented#### add a way to warn when overwriting 
    print("\n\t\t==New Field Entry==")

    genDetOpt=inputIVal("\n\tHave File General Details Been fileld or use Default Paramiters?\n\n\t\tTo fill in type 1 else type 2 \n\t\tEnter Option Here: ",1,2)
    if genDetOpt==1:
        genDetReturn=generalDetails()
    else:
        genDetReturn=None

    workerEditingList=[]
    returner=readFileFinder(workerEditingList)
    workerEditingList=returner[0]
    fileName=returner[1]

    newFieldName=input("\n\n\tEnter new Field name: ")
    valInp=bool(False)
    while valInp==False:
        try:
            newFieldPos=int(input("\tEnter new field name position (be logical): "))
            newFieldPos=newFieldPos-1
            if newFieldPos<-1 or newFieldPos>len(workerEditingList)+2 :
                print(f"Out of range, try again with a number between 1-{len(workerEditingList)+1}")
            else:
                valInp=True
        except: 
            print("Invalid input not a number, Try again")

    workerEditingList[0].insert(newFieldPos,newFieldName)

    for x in range(len(workerEditingList[0])-1):
        workerEditingList[x+1].insert(newFieldPos,">undif<")#''','''#try to keep it "None" if list can append it

    workerEditingList=srcFilerV5.listConverterSave2DipsForm(workerEditingList)

    savermodule(fileName,workerEditingList,genDetReturn)
    EditTableSubMenu()

def addRecNumField(workerEditingList):### new saving mode implimented#### add a way to warn when overwriting 

    workerEditingList[0].insert(0,"Record number")
    for x in range(len(workerEditingList)-1):
        workerEditingList[x+1].insert(0,x+1)

    return workerEditingList,x

def EditRecordSubMenu():### menu
    VsubOpt=[["Add Record","addRecord()"],["Remove Record","removerRecord()"],["Edit Record","editRecord()"],["Return to Main Menu","mainMenu()"]]
    print("==Editing Sub Menu==")
    munuMaker(VsubOpt)

def addRecord(): ### works
    genDetOpt=inputIVal("\n\tHave File General Details Been fileld or use Default Paramiters?\n\n\t\tTo fill in type 1 else type 2 \n\t\tEnter Option Here: ",1,2)
    if genDetOpt==1:
        genDetReturn=generalDetails()
    else:
        genDetReturn=None

    workerViewList=[]
    returner=readFileFinder(genDetReturn)
    workerViewList=returner[0]
    fileName=returner[1]
    workerViewList=srcFilerV5.listConverterSave2DipsForm(workerViewList)

    contRec=int(2)
    while contRec==2:
        for x in range(len(workerViewList[0])):
            recItem=input("Enter new {workerViewList[0][x]}")
            if x==0:
                workerViewList.append([recItem])
            else:
                workerViewList[-1].append(recItem)
        contRec=inputIVal("\n\tWould you like to enter another record?\n\n\tEnter 1 to enter new record\n\tEnter 2 to return to menu\nEnter Option: ")
    
    workerViewList=srcFilerV5.listConverterDisp2SaveForm(workerViewList)
    actualViewer(workerViewList)

    saveopt=inputIVal("Would you liek to save this Table ?\nEnter 1 to save\n Enter 2 to abort\n\nEnter Option: ")
    if saveopt==1:
        savermodule(fileName,workerViewList,genDetReturn)
    EditRecordSubMenu()
    
def editRecord():#works
    genDetOpt=inputIVal("\n\tHave File General Details Been fileld or use Default Paramiters?\n\n\t\tTo fill in type 1 else type 2 \n\t\tEnter Option Here: ",1,2)
    if genDetOpt==1:
        genDetReturn=generalDetails()
    else:
        genDetReturn=None
    
    workerViewList=[]
    returner=readFileFinder(genDetReturn)
    workerViewList=returner[0]
    fileName=returner[1]
    returner1=addRecNumField(workerViewList)
    workerViewList=returner1[0]
    workerViewList=srcFilerV5.listConverterSave2DipsForm(workerViewList)
    actualViewer(workerViewList)

    recEditNum=(inputIVal("Enter the record number you would like to edit: ",1,returner1[1])-1)
    for x in range(len(workerViewList[recEditNum])):
        newItemReplace=input(f"Enter New data to replace {workerViewList[x]} in record {recEditNum}: ")
        workerViewList[recEditNum][x]=newItemReplace
    
    saveopt=inputIVal("Would you liek to save this Table ?\nEnter 1 to save\n Enter 2 to abort\n\nEnter Option: ")
    if saveopt==1:
        savermodule(fileName,workerViewList,genDetReturn)
    EditRecordSubMenu()

def removerRecord():#works
    genDetOpt=inputIVal("\n\tHave File General Details Been fileld or use Default Paramiters?\n\n\t\tTo fill in type 1 else type 2 \n\t\tEnter Option Here: ",1,2)
    if genDetOpt==1:
        genDetReturn=generalDetails()
    else:
        genDetReturn=None

    workerViewList=[]
    returner=readFileFinder(genDetReturn)
    workerViewList=returner[0]
    fileName=returner[1]
    workerViewList=srcFilerV5.listConverterSave2DipsForm(workerViewList)
    returner1=addRecNumField(workerViewList)
    workerViewList=returner1[0]
    actualViewer(workerViewList)

    recEditNum=(inputIVal("Enter the record number you would like to edit: ",1,returner1[1])-1)
    
    listRemover(workerViewList,recEditNum+1)

    print("Updating...\n")
    workerViewList=srcFilerV5.listConverterSave2DipsForm(workerViewList)
    actualViewer(workerViewList)

    saveopt=inputIVal("\n\nWould you liek to save this Table ?\nEnter 1 to save\nEnter 2 to abort\n\nEnter Option: ")
    if saveopt==1:
        savermodule(fileName,workerViewList,genDetReturn)
    EditRecordSubMenu()

def removeField():#works
    genDetOpt=inputIVal("\n\tHave File General Details Been fileld or use Default Paramiters?\n\n\t\tTo fill in type 1 else type 2 \n\t\tEnter Option Here: ",1,2)
    if genDetOpt==1:
        genDetReturn=generalDetails()
    else:
        genDetReturn=None

    workerViewList=[]
    returner=readFileFinder(genDetReturn)
    workerViewList=returner[0]
    fileName=returner[1]
    workerViewList=srcFilerV5.listConverterSave2DipsForm(workerViewList)
    actualViewer(workerViewList)

    workerViewList=srcFilerV5.listConverterDisp2SaveForm(workerViewList)
    fieldRevPos=inputIVal("Enter the Field position you would like to remove\n1 being the first field: ",1,len(workerViewList))

    workerViewList=listRemover(workerViewList,fieldRevPos)

    print("Updating...\n")
    workerViewList=srcFilerV5.listConverterSave2DipsForm(workerViewList)
    actualViewer(workerViewList)

    saveopt=inputIVal("\n\nWould you liek to save this Table ?\nEnter 1 to save\nEnter 2 to abort\n\nEnter Option: ")
    if saveopt==1:
        savermodule(fileName,workerViewList,genDetReturn)
    EditRecordSubMenu()

def tabelViewSaverSubMenu():
    options=[["View \tTable View","viewTableViews()"],["New \tTable View","NewTableView()"],["Edit \tTable View","EditTableView()"],["Remove \tTable View","removeTableView()"],["Return to main Menu","mainMenu()"],["Quit","quit()"]]
    print("\n\t\t==Table View Menu==")
    munuMaker(options)

def viewTableViews():
    pass

def NewTableView():
    pass

def EditTableView():
    pass

def removeTableView():
    pass

def sortingMenu(listSort,fieldNameSort=None):### working #
    print("\n\t==Sorting Sub Menu==")
    if fieldNameSort==None:
        valInp=False
        while valInp==False:
            print("Avalable Fields:\t",end="")
            for j in range(len(listSort[0])):
                if j != len(listSort[0])-1: 
                    print(f"{listSort[0][j]}|",end="")
                else:
                    print(f"{listSort[0][j]}")

            fieldNameSort=input("Enter field name to sort by: ")
            fieldNameSortLow=fieldNameSort.lower()
            indexVal=int(-1)
            #indexVal=listSort[0].index(fieldNameSort)#i like to make my life hard
            for x in range(len(listSort[0])):
                lItem=listSort[0][x].lower()
                if lItem==fieldNameSortLow:
                    indexVal=int(1)
            if indexVal!=-1:
                valInp=True
            else:
                print("Error, This field Dose not Exist")
                tryAgain=inputIVal("\nPress 1 to try again\nPress 2 to return to main menu\n\nEnter option: ",1,2)
                if tryAgain!=1:
                    mainMenu()

    reverse=inputIVal("Enter 1 For assending order\nEnter 2 for dissending order\n\nEnter Option: ",1,2)
    if reverse!=1:
        reverse=bool(True)
    else:
        reverse=bool(False)
    return srcFilerV5.sorterAto(listSort,fieldNameSort,reverse)

def sortQurPrompt(listSort,fieldNameSort=None):### simple sorter prompt
    saveItm=inputIVal("\n\nWould you like to sort your list?\nEnter 1 to sort\nEnter 2 to for reguler view\n\nEnter Option: ",1,2)
    if saveItm==1:
        return sortingMenu(listSort,fieldNameSort)               

mainMenu()