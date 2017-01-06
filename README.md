# GPACalc

##Description:
_GPACalc_ is Python script which allows the user to calculate their term or cumulative GPA on a scale of 0 to 4. 
The script is geared towards college students.

###Dependencies:
The script requires that you have Python 2.7 installed. On Linux, Python may already be part of your distribution or may be available as a package. For Windows and Mac OS, please refer to the Python download page for installers and instructions.

##How to Run:
Simply download the script and invoke the Python interpreter in your terminal or command prompt manually as follows:
**`python gpacalc.py`**

Upon success, GPACalc will take you to the main instance where you will be prompted for input.

##How to Use:
After being prompted for input, please start by adding a term. To add a term, type **add \<term name\>**. Upon success, you'll get taken to that term's instance (**term name >**) where you can add courses and calculate the GPA for that term. To exit a term, input **[b]ack**. To go back to a term, input **go \<term name\>**. Below is a the full list of commands that GPACalc supports:


**General Commands**

![logo](http://i.snag.gy/3F75G.jpg) **ATTENTION**: `import` and `export` won't work unless you are in the main instance of GPACalc (i.e. not in a term instance). 

* To import your information from a file, type `import <path to file>`. For proper file structure, please refer to **sample.txt**.
* To export your information to a file, type `export <path to file>`. The exported file will have the same file structure as that required by the `import` command. 
* To exit the program, type `[e]xit`

**Term Commands:**
* To add a term, in the main instance, input `add <term name>`
* To calculate the GPA for a term, in that term's instance, input `[g]pa`
* To delete a term, in the main instance, input `del <term name>`
* To go to a term, in the main instance, input `go <term name>`
* To calculate the cumulative GPA, in the main instance, input `[g]pa`
* To view your list of terms, in the main instance, input `[l]ist`
* To clear your list of terms, in the main instance, and input `[c]lear`

**Course Commands:** (requires being in a term instance)
* To add a course, input `add <course name>, <letter grade>, <number of units>`
* To delete a course, input `del <course name>`
* To view your list of courses, input `[l]ist`
* To clear your list of courses, input `[c]lear`

Please note that none of the commands listed above are case sensitive; however, it's imperative that you follow the proper formatting when providing the script with your input.

##Frequently Asked Questions: 

Q: **Is there a limit to the number of terms or courses I can add?**
* A: No. You can add many terms and courses as you want.

Q: **Do P/NP (Pass/No Pass) courses are factored in?**
* A: No. P/NP courses are not factored in your GPA.

Q: **Do I (Incompletes) and W (Withdrawals) receive grade points?**
* A: No. I and W do not receive grade points and do not have an effect on your GPA.
