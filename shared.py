'''
Created on Jan 12, 2017

@author: yazin
'''

validGrades = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D', 'F', 'W', 'P', 'NP', 'I']
gradeBreakdown = {'A+': 1, 'A':1, 'A-':0.925, 'B+':0.825, 'B':0.75, 'B-':0.675, 'C+':0.575, 'C':0.5, 'C-':0.425, 'D':0.25, 'F':0}
listOfTerms = {}
'''
This method strips the text of white spaces, tabs, and newlines and changes it to
upper case for consistency.
@param text: the text being changed.
@return: The changed text. 
'''
def sup(text):
    return text.upper().strip(' \s\t\n\r')
