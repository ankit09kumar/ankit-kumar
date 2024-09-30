student = {
    "name" : "ankit kumar",
    "subject" : {
        "phy" : 78,
        "chemi" : 65,
        "maths" : 34,
        "pps" : 89,
    }
}

new_dict = {"name" : "neha kuamri" , "age" : 16}
student.update(new_dict)
#this commend is used to the inserts the specified items to the dictionary.
print(student.get("name"))
#this commend is used to the return the key according to value. 
print(student.items())
#this commmend is use to the print the whole elements with using tupple.
print(student.values())
#this commend is use to the print returns the all student value. 
print(len(student.keys()))
#this commend is used to the all key point with length and student element.
print(student.keys())
#this is commend is used to return the all keys .
print(student["subject"]["pps"])
#this commed is used only add  a subject.
print(student.get("name2"))
#this comend are you only none output.
student.update({"city" : "allahabad"})
#this commend is used only the update and add the value or sentence.
print(student)