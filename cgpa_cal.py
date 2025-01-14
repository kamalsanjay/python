cgpa=[]
# sgpa=[]
# k=0
def Sgpa():
    sgpa=[]
    sems=8
    for i in range(sems):
    # k=1
        sub=int(input(f"Enter the n.o of subject in this sem-{i+1} : "))
        credit_points=[]
        grade_points=[]
        for i in range(sub):
            gp=input(f"enter the grades O, A+, A, B+, B, C, F for sub-{i+1}: ")
            if gp=="O":
                grade_points.append(10)
            if gp=="A+":
                grade_points.append(9)
            if gp=="A":
                grade_points.append(8)
            if gp=="B+":
                grade_points.append(7)
            if gp=="B":
                grade_points.append(6)
            if gp=="C":
                grade_points.append(5)

        for j in range(sub):
            cp=float(input(f"enter the credits for respective subjects i.e sub-{j+1} : "))
            credit_points.append(cp)

        print(credit_points)
        print(grade_points)
        
        c_sum=0
        cg_sum=0
        sgpa_=1
        for k in range(sub):
            cg_mul=credit_points[k]*grade_points[k]
            cg_sum+=cg_mul
            c_sum+=credit_points[k]
        # sgpa_=cg_sum/c_sum
        print(cg_sum)
        print(c_sum)
        AVG=cg_sum/c_sum
        print(AVG)
        sgpa.append(AVG)

        # k+=1
    return sgpa

def Cgpa(s):
    # avg=0
    sgpa_sum=0
    n=len(s)
    for i in range(n):
        sgpa_sum+=s[i]
    avg=sgpa_sum/n
    return avg

# li=Sgpa()

def main():
    # li=Sgpa()
    lis=[7.388888888888889, 7.7631578947368425, 6.714285714285714, 6.619047619047619, 6.340909090909091, 6.7272727272727275, 7.571428571428571, 7.75]
    # for i in range(2):
    #     call=input("enter sgpa or cgpa : ")
    #     if call=="sgpa":
    #         print(li)
    #     if call==cgpa:
    #         Cgpa(li)
    # print(li)
    print(Cgpa(lis))
if __name__=='__main__':
     main()