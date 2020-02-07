Input file required: 2008Male00006.txt
Output file created: Georges_life.txt
Python script file: Evaluate_Raccoon_Life.txt

Script description below.

###############################################################################################
                        DESCRIPTION OF FUNCTIONS USED 
###############################################################################################

Function name: list_mean
The function takes a list of numbers as input and returns the mean of the numbers in the list.

Function name: list_cumulative_sum
The function takes a list of numbers as input and returns the cummulative sum of the numbers in the list.

Function name: calculate_dist
The function takes to lists of numbers as input. One list containing X coordinates and one containing Y coordinates.
It returns a list containing subsequent distances between points described by the two input lists.
Distance between 2 points (x1,y1) and (x2,y2) is calcualted using the math function sqrt.
Distance = math.sqrt((x2-x1])**2 + (y2-y1)**2)

Function name: list_elements_to_float
Function takes a list of numbersstored in string format as input. It typecasts the input into a float number list.

Function name: list_elements_to_int
Function takes a list of numbers stored in string format as input. It typecasts the input into a float number list first and then into an int number list.

###############################################################################################
                        DESCRIPTION OF CODE SECTIONS
###############################################################################################

Section 1: The text file 2008Male00006.txt is read into a list of lists 'lines'. While reading the text file, end of line charecter is removed using strip() function and each string between two ','s was read as list elements to seperate out all the words/number/string groups.

Section 2: The length of each line in list form was found to remove the last line with different length and the removed last line was stored in 'last_line'. 'lines' is re-assigned to 'lines[1:]' to seperate out the header line. Header line is stored in another list 'keys'.

Section 3: The data was initially read row-wise in section 1. Now the data is re-read from the list of lists ('lines') and stored in a dictionary 'dic' with keys being individual words/string groups in the header line. The value in each key is stored as a list containing the text data column-wise. Ex: the key 'Time' contains a list containing all the time describing strings. This way it becomes easy to convert strings to relevent data type later.

Section 4: The keys corresponding to value lists in 'dic' which have to be typecasted into float and int are stored in two lists, one for float and one for int. This makes it easy to call the required keys.
Nested for loops are used to call each list whose elements have to be typecasted and to re-assign the list with typecasted elements.

Section 5: calculate_dist and list_cumulative_sum functions are called to calculate the distance travelled by the racoon in its lifetime.

Section 6: An empty text file 'Georges_life.txt' is created. Using the functions defined before, the header information if written followed by a blank line ('\n\n' used to create a blank line). '\t' was used between two words/ints/floats in the data below the header file to make it tab delimited. The data is written using a loop where in each iteration, one row is filled with relevant data. Since the some data was previously typecasted to calculate differnt paramerts, they are reacsted into string using 'str()' before being writtnen in the file.

