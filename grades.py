import streamlit as st
import numpy as np

SLO = 20
HW = 8

st.markdown('# Math 10 Grade Calculator')

st.markdown('''Use this app to quickly calculate your grade in Math 10. Note: Part
        of passing Math 10 means turning in a final project planning worksheet
        and a final project that meets the  minimum requirements. This app
        assumes that these requirements are met.''')

st.markdown('## Student Learning Outcomes')
SLOtot = st.number_input("How many SLOs have you passed?",min_value=0,\
        max_value=SLO,step=1)

st.markdown('## Homework Assignments')
HWtot = st.number_input("How many homeworks have you passed?",min_value=0,\
         max_value=HW,step=1)

st.markdown('## Grade Computation')


studentgradelist = [SLOtot,HWtot]

def gradecheck(student):
    for grade in grades:
        for b in range(len(grades[grade])):
            #print([student[a] in grades[grade][b][a] for a in range(2)])     
            total = sum([student[a] in grades[grade][b][a] for a in range(2)])
            if total == 2:
                return grade
    return None


Aplus = ([20],[8])
A = (range(18,SLO+1),range(7,HW+1))

#XOR 6 homeworks
Aminusv1 =(range(18,SLO+1),range(6,7))

#XOR 17 SLOs
Aminusv2 = ([17],range(7,HW+1))


Bplus = ([16],range(6,HW+1))

B = (range(14,SLO+1),range(5,HW+1))

#XOR 4 satisfactory homeworks
Bminusv1 = (range(14,SLO+1),range(4,HW+1))

#XOR 13 SLOs
Bminusv2 =(range(13,SLO+1),range(5,HW+1))


Cplus = (range(12,SLO+1),range(5,HW+1))

C = (range(10,SLO+1),range(4,HW+1))

#XOR 3 satisfactory homeworks
Cminusv1 = (range(10,SLO+1),range(3,HW+1))

#XOR 9 SLOs
Cminusv2 = (range(9,SLO+1),range(4,HW+1))


grades = {"A+":[Aplus,],"A":[A,],"A-":[Aminusv1,Aminusv2],"B+":[Bplus,],"B":[B,],"B-":[Bminusv1,Bminusv2],"C+":[Cplus,],"C":[C,],"C-":[Cminusv1,Cminusv2]}

if gradecheck(studentgradelist) is None:
    st.write("No grade returned. Perhaps you do not meet minimum requirements for any grade category. If you believe this is in error please contact your instructor.")
else:
    grade = gradecheck(studentgradelist)
    st.write(f"Your grade: {grade}")
