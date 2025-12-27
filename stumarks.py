Student_marks={
    "omkar":85,
    "amit":78,
    "sneha":92,
    "riya":88
}
name=input("Enter Student name")
if name in Student_marks:
    print(f"Marks of {name} : {Student_marks[name]}")
else:
    print("Student not found in the record.")    