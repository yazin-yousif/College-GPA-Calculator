import sys
from term import Term
from shared import *

'''
Created on Dec 19, 2016
@author: Yazin Yousif
'''

'''
This method prompts the user for input.
@return: void
'''
def getUserInput(instance):
    if isinstance(instance, Term):
        userInput = raw_input(str(instance.getName()) + " > ")
        userInput = sup(userInput)
        if userInput.startswith("ADD "):
            instance.validateCourseInfo(userInput[4:], False)
        elif userInput == "GPA" or userInput == "G":
            instance.calculateGPA()
        elif userInput == "LIST" or userInput == "L":
            print "You've added the following courses to your list: " + str(instance.getCourses())
        elif userInput.startswith("DEL "):
            instance.deleteCourse(userInput[4:])
        elif userInput.startswith("CLEAR") or userInput == "C":
            del instance.__courses[:]
        elif userInput == "BACK" or userInput == "B":
            return getUserInput(None)
        elif userInput == "EXIT" or userInput == "E":
            collectGarbage(True)
        else:
            print("ERROR: Unrecognizable command. Please try again.")
        getUserInput(instance)
    else:
        userInput = raw_input("> ")
        userInput = sup(userInput)
        if userInput.startswith("ADD "):
            return addTerm(userInput[4:], False)
        elif userInput.startswith("GO "):
            return openTerm(userInput[3:])
        elif userInput.startswith("DEL "):
            return deleteTerm(userInput[4:])
        elif userInput.startswith("IMPORT "):
            return importInfo(userInput[7:])
        elif userInput.startswith("EXPORT "):
            return exportInfo(userInput[7:])
        elif userInput == "CLEAR" or userInput == "C":
            collectGarbage(False)
        elif userInput == "LIST" or userInput == "L":
            print "You've added the following terms to your list: " + str(listOfTerms.keys())
        elif userInput == "GPA" or userInput == "G":
            calculateCumulativeGPA()
        elif userInput == "EXIT" or userInput == "E":
            collectGarbage(True)
        else:
            print("ERROR: Unrecognizable command. Please try again.")
        getUserInput(None)

'''
This method handles the garbage collection.
@param exitProgram: indicates whether or not the script must quit.
@return: void 
'''
def collectGarbage(exitProgram):
    for value in listOfTerms.itervalues():
        value.__del__()
    listOfTerms.clear()
    if exitProgram:
        print("Thank you for using College GPA Calculator. Goodbye!")
        sys.exit() 

'''
This method calculates the cumulative GPA for all terms.
@return: The calculated GPA.
'''
def calculateCumulativeGPA():
    if len (listOfTerms) > 0:
        
        obtainableTotal = 0
        obtainedTotal = 0
        
        for value in listOfTerms.itervalues():
            for course in value.getCourses():
                letterGrade = sup(course[1])
                if letterGrade != 'W' and letterGrade != 'P' and letterGrade != 'NP' and letterGrade != 'I':
                    numOfUnits = int(course[2].strip())
                    obtainableTotal = obtainableTotal + numOfUnits
                    obtainedTotal = obtainedTotal + gradeBreakdown[letterGrade] * numOfUnits
        if (obtainableTotal == 0 or obtainedTotal == 0):
            print "Your cumulative GPA is 0"
        else:
            print "Your cumulative GPA is " + str((obtainedTotal / obtainableTotal) * 4)
            
    else:
        print "ERROR: Your list of terms is currently empty."

'''
This method adds a term to the list of terms.
@param userInput: contains the term name.
@return: void 
'''
def addTerm(userInput, fromImport):
    if userInput not in listOfTerms:
        listOfTerms[userInput] = Term(userInput)
        if (fromImport == False):
            getUserInput(listOfTerms[userInput])
    else:
        print ("ERROR: the term " + str(userInput) + " is already in the list.")
        if (fromImport == False):
            getUserInput(None)

'''
This method opens a term that's already been added to the list of terms.
@param userInput: contains the term name.
@return: void 
'''
def openTerm(userInput):
    if userInput in listOfTerms:
        getUserInput(listOfTerms[userInput])
    else:
        print ("The term " + userInput + " doesn't appear to be in the list.")
        getUserInput(None)

'''
This method deletes a term from the list of terms.
@param userInput: contains the term name.
@return: void 
'''
def deleteTerm(userInput):
    if userInput in listOfTerms.iterkeys():
        listOfTerms[userInput].__del__()
        del listOfTerms[userInput]
    else:
        print ("The term  " + userInput + " doesn't appear to be in the list.")
    getUserInput(None)
    
'''
This method allows the user to import their term and course information from a file
@param: source: the path to a file containing the information.
@return: void
'''
def importInfo(source):
    termAdded = False
    termName = ""
    try:   
        with open(source, 'r') as importedFile:
            for line in importedFile:
                if sup(line).startswith("#") == False:
                    if line.upper().startswith("TERM:"):
                        termName = sup(line.split(":")[1])
                        addTerm(termName, True)
                        termAdded = True
                    elif (termAdded):
                        courseInfo = sup(line)
                        if courseInfo != "" and len(courseInfo) > 0:
                            listOfTerms[termName].validateCourseInfo(courseInfo, True)
                        else:
                            pass
                    else:
                        termAdded = False
                        termName = ""
        print("Your term and course information have been imported successfully.")
    except IOError as err:
        print ("ERROR: Unable import information -- " + str(err))
    
    finally:
        getUserInput(None)

'''
This method allows the user to export their term and course information.
@param: source: the path to a file containing the information.
@return: void
'''
def exportInfo(path):
    if len(listOfTerms) == 0:
        print "ERROR: There is no data to export."
        getUserInput(None)
    try:
        output = open(path, 'w+')
        output.write("# This file was generated using College GPA Calculator -- https://github.com/yazin-yousif/College-GPA-Calculator" + '\n\n')
        for term in listOfTerms.itervalues():
            output.write("Term: " + term.getName() + '\n')
            for course in term.getCourses():
                output.write(str(course).strip("\\[\\]").replace("'", "") + '\n')
            output.write('\n')
        print "Your term and course information have been imported successfully!"
        output.close()
    except IOError as err:
        print("ERROR: Unable to import information -- " + str(err))
    finally:
        getUserInput(None)
        
if __name__ == "__main__":
    print ("Thank you for using College GPA Calculator by Yazin Yousif. Please start by adding a term.")
    print ("For help, please refer to the README file on GitHub: https://github.com/yazin-yousif/College-GPA-Calculator/" + "\n")
    getUserInput(None)
