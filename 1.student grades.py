"""Python program that takes a student's name and multiple grades, then calculates highest, lowest, and average. 
Then saves results to a text file."""

name_student=input("enter name.")
grade_numbers=int(input("how many grades?"))
list_grades=[]
for i in range (grade_numbers):
    grade=int(input("enter the grade."))
    list_grades.append(grade)
highest=max(list_grades)
lowest=min(list_grades)
average=sum(list_grades)/len(list_grades)
with open("student_grades.txt","w") as f:
    f.writelines(["name="+name_student+"\n",
                  "highest grade="+str(highest)+"\n",
                  "lowest grade="+str(lowest)+"\n",
                  "average="+str(average)+"\n"])

    
    
