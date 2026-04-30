def cal(marks,tc):
    if any(mark<40 for mark in marks):
        return "fail"
    total_marks = sum(marks)
    aggregate_p = ((total_marks)/(tc*100))*100
    if aggregate_p>75:
        grade="dist"
    elif aggregate_p>=60:
        grade="first div"
    elif aggregate_p>=50:
        grade="second div"
    elif aggregate_p>=40:
        grade="third div"
    return(aggregate_p,grade)
num_c= int(input())
marks=list(map(int,input().split()))
result = cal(marks,num_c)
if result=="fail":
    print("fail")
else:
    aggregate_p,grade=result
print(f"aggregate:{aggregate_p:.2f}")
print(f"grade:{grade}")