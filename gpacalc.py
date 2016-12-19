import sys
'''
Created on Dec 19, 2016
@author: Yazin Yousif
'''

validGrades = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D', 'F', 'W', 'P', 'NP', 'I']
gradeBreakdown = {'A+': 1, 'A':1, 'A-':0.925, 'B+':0.825, 'B':0.75, 'B-':0.675, 'C+':0.575, 'C':0.5, 'C-':0.425, 'D':0.25, 'F':0}

'''
This class contains all the methods related to a term.
'''
class Term:
 
    def __init__(self, name):
        self.__courses = []
        self.__name = name
    
    def __del__(self):
        return 0
    
    '''
    A simple getter method.
    @return: The name of a term.
    '''
    def getName(self):
        
        return self.__name
    
    '''
    A simple getter method.
    @return: The list of courses in a term.
    '''
    def getCourses(self):
        return self.__courses
    
    '''
    This method validates the course information. It takes a user input and look
    for the course name, letter grade and number of units, and validates them.
    @param userInput: the user input.
    @return: void.
    '''
    def validateCourseInfo(self, userInput):
   
        if len(userInput.split(',')) != 3:
            print "ERROR: Invalid input... Please try again: "
        else:
            letterGrade = sup(userInput.split(',')[1])
            numOfUnits = sup(userInput.split(',')[2])
            if letterGrade in validGrades:
                if numOfUnits.isdigit() == False or numOfUnits < 0:
                    print "ERROR: You've entered an invalid number of units: " + numOfUnits + " - Please try again."
                else:
                    if self.isDuplicate(sup(userInput.split(',')[0])) == False:
                        self.__courses.append([x.strip() for x in userInput.split(',')])
            else:
                print "ERROR: You've entered an invalid letter grade: " + letterGrade + " - Please try again."
        self.getUserInput(self.__name)

    '''
    This method checks if the course being added is already in the list.
    @param name: the name of the course.
    @return: True if duplicate, False if not.
    '''
    def isDuplicate(self, name):
        for course in (self.__courses):
            if sup(name) in course:
                print ("ERROR: This course is already in the list.")
                return True
        return False

    '''
    This method deletes a course from the list of courses.
    @return: void
    '''
    def deleteCourse(self, name):
        for course in (self.__courses):
            if sup(name) in course:
                self.__courses.remove(course)
                self.getUserInput(self.__name)
        print ("Your course doesn't appear to be in the list.")
        self.getUserInput(self.__name)
    
    
    '''
    This method calculates the GPA for a single term.
    @return: The calculated GPA.
    '''
    def calculateGPA(self):
    
        if len(self.__courses) == 0:
            print "ERROR: Your list of courses is currently empty."
            self.getUserInput(self.__name)
        
        obtainableTotal = 0
        obtainedTotal = 0
        
        for course in self.__courses:
            letterGrade = sup(course[1])
            if letterGrade != 'W' and letterGrade != 'P' and letterGrade != 'NP' and letterGrade != 'I':
                numOfUnits = int(course[2].strip())
                obtainableTotal = obtainableTotal + numOfUnits
                obtainedTotal = obtainedTotal + gradeBreakdown[letterGrade] * numOfUnits
        
        if (obtainableTotal == 0 or obtainedTotal == 0):
            return 0
        else:
            return (obtainedTotal / obtainableTotal) * 4

    
    '''
    This method prompts the user for input.
    @param: termName: the name of the term.
    @return: void
    '''
    def getUserInput(self, termName):
        userInput = raw_input(str(termName) + " > ")
        userInput = sup(userInput)
        if userInput.startswith("ADD "):
            return self.validateCourseInfo(userInput[4:])
        elif userInput == "GPA" or userInput == "G":
            print "Your " + termName + " GPA is " + str(self.calculateGPA())
        elif userInput == "LIST" or userInput == "L":
            print "You've added the following courses to your list: " + str(self.__courses)
        elif userInput.startswith("DEL "):
            return self.deleteCourse(userInput[4:])
        elif userInput.startswith("CLEAR") or userInput == "C":
            del self.__courses[:]
        elif userInput == "BACK" or userInput == "B":
            getUserInput()
        elif userInput == "EXIT" or userInput == "E":
            collectGarbage(True)
        else:
            print("ERROR: Unrecognizable command. Please try again.")
        self.getUserInput(termName)
 
listOfTerms = {}   

'''
This method strips the text of white spaces, tabs, and newlines and changes it to
upper case for consistency.
@param text: the text being changed.
@return: The changed text. 
'''
def sup(text):
    return text.upper().strip(' \s\t\n\r')

'''
This method prompts the user for input.
@return: void
'''
def getUserInput():
    userInput = raw_input("> ")
    userInput = sup(userInput)
    if userInput.startswith("ADD "):
        return addTerm(userInput[4:])
    elif userInput.startswith("GO "):
        return openTerm(userInput[3:])
    elif userInput.startswith("DEL "):
        return deleteTerm(userInput[4:])
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
    getUserInput()

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
def addTerm(userInput):
    if userInput not in listOfTerms:
        listOfTerms[userInput] = Term(userInput)
        listOfTerms[userInput].getUserInput(listOfTerms[userInput].getName())
    else:
        print ("ERROR: the term " + str(userInput) + " is already in the list. Please try again.")
        getUserInput()

'''
This method opens a term that's already been added to the list of terms.
@param userInput: contains the term name.
@return: void 
'''
def openTerm(userInput):
    if userInput in listOfTerms:
        listOfTerms[userInput].getUserInput(listOfTerms[userInput].getName())
    else:
        print ("The term " + userInput + " doesn't appear to be in the list.")
        getUserInput()

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
    getUserInput()
    
'''
This method displays instructions.
@return: void 
'''
def displayHelp():
    print ("--------------------------------------------------------------------------------------------------")
    print ("Thank you for using Yazin's GPA Calculator. Please start by adding a term.\n")
    print ("General/Term options -- To:")
    print ("  - Add a term, type 'add <term name>'")
    print ("  - Delete a term, type 'del <term name>'")
    print ("  - Clear your list of terms, type '[c]lear'")
    print ("  - Calculate your cumulative GPA, type '[g]pa'")
    print ("  - Exit a term (i.e. go back), type '[b]ack'")
    print ("  - Go to a term that's already been added, type 'go <term name>'")
    print ("  - Exit the program at any moment, type '[e]xit' or press Ctrl+C\n")
    print ("Course options -- To:")
    print ("  - Add a course, type 'add <course name>, <letter grade>, <number of units>'")
    print ("  - Delete a course, type '[d]el <course name>'")
    print ("  - To output your list of courses, type '[l]ist'")
    print ("  - To clear your list of courses, type '[c]lear'")
    print ("  - Calculate your term GPA, type '[g]pa'")
    print ("--------------------------------------------------------------------------------------------------\n")

'''
Python's equivalent of Java's main.
@return: void 
'''
def init():
    displayHelp()
    getUserInput()

init()