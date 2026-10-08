students = {
    101:{"NAME":"ADITI","SCORES":[78,85,90]},
    102:{"NAME":"SOHAM","SCORES":[88,95,70]},
    103:{"NAME":"RAM","SCORES":[98,75,80]},
    104:{"NAME":"RIYA","SCORES":[68,55,97]},
    105:{"NAME":"SIYA","SCORES":[91,65,89]}
}

for sid,details in students.items():
    avg = sum(details["SCORES"])/len(details["SCORES"])
    details["AVERAGE"]= avg
    details["PASSED"]= avg >=50

print("STUDENTS WHO PASSED : ")
for sid,details in students.items():
    if details["PASSED"]: 
        print (students)