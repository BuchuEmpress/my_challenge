# Student grade book system
# initializing empty dictionary
grade_book={}

# for design print dashes
def des():
    print("--" * 50)
    
print("=== STUDENT GRADE BOOK ===")
# function to add new student
def add_new_student(name):
    des()
    if name not in grade_book:
        grade_book[name]= []       #initializing empty list to store student grades for new students
        print(f"Added student: {name}")
        des()
    else:
        print(f"The name {name} already exists")
        des()
        

# function to add grade to a student, given the name and student
def add_grade_to_existing_student(name, grade_list):           # 
     if name in grade_book:
      grade_book[name].extend(grade_list)      # add new grades to the existing student's list of grades
     else:
      print(f"Name {name} is not in grade book")
        
# function to calculate average of student when student enters the name and scores which are inside the grade_list list 
def calculate_average(name):
    # print("DEBUG TYPE CHECK:", type(name))
    if name in grade_book and grade_book[name]:
        grades=grade_book[name]        # get student's grades
        if grades:    
         total=sum(grades)
         average= total/len(grades)
        return average
        
    else:
        print(f"Name {name} not in grade book")
        return None     
    
    
# function to tell the grade from the sccore given the name and grade list
def get_letter_grades(score):
    # if name in grade_book:
        if score > 89:
            return  "A+"
        elif score > 79 and score < 90:
            return  "B"
        elif score > 69 and score < 80:
            return  "c"
        elif score > 59 and score < 70 :
            return  "D"
        else:
            return "F"
        
def calculate_letter_grades(name):
    if name in grade_book:
        grades = grade_book[name]
        return [get_letter_grades(score) for score in grades]           # use a list comprehension to calculate the letter grade for each score
    else:
        print(f"Student '{name}' is not in grade book")
        return []      # return an empty list to indicate that no letter grades could be calculated
   

# function to display a specific student's name, average and grades given the name
def display_student(name):
    if name in grade_book:
        scores = grade_book[name]       #get the student's scores
        if not scores:
            print(f"{name}: Has no scores recorded")
            return
        letter_grades= calculate_letter_grades(name)  #calculate letter grades for student's scores
        average = calculate_average(name)      # calculate the average for student's scores
        print(f"\nName: {name}")
        print(f"Scores: {scores}")
        print(f"Letter grades: {letter_grades}")
        print(f"Average: {average:.2f}")
    else: 
        print(f"Name: {name} and grades: {letter_grades} not found for name gradebook")
 

# function to display all student names, averages and grades given their names 
def display_all_students():
    if not grade_book:
        print("Grade book is empty")
    for name in grade_book:    #.items():
        display_student(name)
        #  print(f"\nName: {name}")
        #  print(f"Scores: {grade_book[name]}")
        #  print(f"Average: {average:.2f}")
        #  print(f"Letter grades: {letter_grade}")
        

def find_highest_and_lowest_rank_student():
    student_averages = {}      #dictionary to stores the student averages, names and scores
    for name in grade_book:
        avg= calculate_average(name)    # calculating student's average by reusing the calculate average function
        if avg is not None:              # only add info to the dictionary if the average exists
            student_averages[name]=avg     #loop through each student and calculates their average
            
    if student_averages:                                               # checks if at least one student has valid scores
        total_sum = sum(student_averages.values())                      # sums all the students' averages
        total_students = len(student_averages)                           # counts for valid averages
        overall_average = total_sum / total_students                      # calculates average of all student averages
        top_student = max(student_averages, key=student_averages.get)                  #finds student with highest average
        bottom_student = min(student_averages, key=student_averages.get)                #finds student with lowest average
        print(f"\nOverall Average for All students: {overall_average:.2f}")
        print(f"\nTop student: {top_student} with average {student_averages[top_student]:.2f}")
        print(f"Lowest performing Student: {bottom_student} with average {student_averages[bottom_student]:.2f}")
    else:
        print("No student have recorded averages")
    
    
    

# data used to implement functions
name = "Joy Eternal"
grade_list = [50, 60, 67, 99, 89, 90]
name_2= "Laurel Laura"
grade_list_2 = [89, 34, 87, 60, 99, 45]
name_3="Lobo"

# calling the functions to implementation
add_new_student(name)
add_grade_to_existing_student(name, grade_list )



add_new_student(name_2)
add_grade_to_existing_student(name_2, grade_list_2 )

add_new_student(name_3)

find_highest_and_lowest_rank_student()
display_all_students()

