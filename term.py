from shared import *
'''
Created on Jan 12, 2017

@author: yazin
'''

class Term(object):

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
    def validateCourseInfo(self, userInput, fromImport):
   
        if len(userInput.split(',')) != 3:
            print "ERROR: Invalid input. Please try again: "
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

    '''
    This method checks if the course being added is already in the list.
    @param name: the name of the course.
    @return: True if duplicate, False if not.
    '''
    def isDuplicate(self, name):
        for course in (self.__courses):
            if sup(name) in course:
                print ("ERROR: " + str(name) + " is already in the list.")
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
                return
        print ("Your course doesn't appear to be in the list.")
        
    
    '''
    This method calculates the GPA for a single term.
    @return: The calculated GPA.
    '''
    def calculateGPA(self):
        if len(self.__courses) == 0:
            print "ERROR: Your list of courses is currently empty."
        else:
            obtainableTotal = 0
            obtainedTotal = 0
            for course in self.__courses:
                letterGrade = sup(course[1])
                if letterGrade != 'W' and letterGrade != 'P' and letterGrade != 'NP' and letterGrade != 'I':
                    numOfUnits = int(course[2].strip())
                    obtainableTotal = obtainableTotal + numOfUnits
                    obtainedTotal = obtainedTotal + gradeBreakdown[letterGrade] * numOfUnits
            
            if (obtainableTotal == 0 or obtainedTotal == 0):
                print "Your " + self.getName() + " GPA is 0"
            else:
                print "Your " + self.getName() + " GPA is " + str((obtainedTotal / obtainableTotal) * 4)
        return 
        
