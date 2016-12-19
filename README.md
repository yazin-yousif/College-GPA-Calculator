# GPACalc

##Decription:
GPACalc is Python script which calculates the user's term or cumulative GPA on a scale of 0 to 4. To run the script, it is required that you have Python installed. On Linux, Python may already be part of your distribution or may be available as a package. For Windows and Mac OS, please refer to the Python download page for installers and instructions. The pipeline has been tested with Python 2.7, but it might also work with later versions of Python such as 3.5.

##How to Run:
Simply download the script and invoke the Python interpreter in your terminal or command prompt manually as follows:
**`python gpacalc.py`**

Once that's done, GPACalc will prompt you for input.

##How to Use:
After being prompted for input, please start by adding a term. To add a term, input **add \<term name\>**. Upon success, you'll get taken to that term instance where you can add courses and calculate the GPA for that term. To exit a term, input **[b]back**. To go back to a term, input **go \<term name\>**. Below is a the full list of commands that GPACalc supports:

**General/Term Options:**
* To add a term, type `add <term name>`.
* To delete a term, type `del <term name>`.
* To go to a term, type `go <term name>`.
* To calculate the GPA for a term, type `[g]pa`
* To calculate the cumulative GPA, exit the term instance and type `[g]pa`
* To view your list of terms, type `[l]ist`
* To clear your list of terms, type `[c]lear`
* To exit the program, type `[e]xit`

**Course Options:**
* To add a course, type `add <course name>, <letter grade>, <number of units>`
* To delete a course, type `del <course name>`
* To view your list of courses, type `[l]ist`
* To clear your list of courses, type `[c]lear`
* To calculate your GPA, type `[g]pa`
* To Exit the program, type `[e]xit`

Please note that none of the commands listed above are case sensitive; however, it's impertive that you follow the proper formatting when providing the script with your input.
