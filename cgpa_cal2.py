cgpa=[]
# sgpa=[]
 
credit_scores=[[1.5,0,1.5,4,4,3,4],[2.5,1.5,1,1,4,4,3,2],[1.5,0,1.5,3,3,4,2,3,3],
               [1.5,1,1.5,0,4,3,4,3,3],[1,0,1.5,1.5,0,3,3,3,3,3,3],[0,1.5,1,1.5,3,4,3,4,4],[1,2,3,1,3,3,3,3,2],[7,3,3,3]]
def Sgpa():
    sgpa=[]
    # sems=8
    iteration=0
    sems=int(input("enter the total n.o of sems : "))
    # for i in range(sems):
    while iteration<sems:
        credit_points=credit_scores[iteration]
        # sub=int(input(f"Enter the n.o of subject in this sem-{iteration+1} : "))
        sub=len(credit_points)
        print(f"sem-{iteration+1}")
        # credit_points=[]
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

        # for j in range(sub):
        #     cp=float(input(f"enter the credits for respective subjects i.e sub-{j+1} : "))
        #     credit_points.append(cp)
        

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
        iteration+=1
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
    li=Sgpa()
    # lis=[7.388888888888889, 7.7631578947368425, 6.714285714285714, 6.619047619047619, 6.340909090909091, 6.7272727272727275, 7.571428571428571, 7.75]
    print(li)
    print(Cgpa(li))
if __name__=='__main__':
     main()

# credit_scores=[[1.5,0,1.5,4,4,3,4],[2.5,1.5,1,1,4,4,3,2],[1.5,0,1.5,3,3,4,2,3,3],
#                [1.5,1,1.5,0,4,3,4,3,3],[1,0,1.5,1.5,0,3,3,3,3,3,3],[0,1.5,1,1.5,3,4,3,4,4],[1,2,3,1,3,3,3,3,2],[7,3,3,3]]