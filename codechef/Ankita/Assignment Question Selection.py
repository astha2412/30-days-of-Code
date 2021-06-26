'''
Sample Input:
75 3 5
15 50 35
6 3
11 1
13 4
27 1
18 2
Sample Output:
5 1 2 3 4 5
3 1 3 5
4 1 2 3 5
'''
lst = [int(x) for x in input().split()]
min_marks = lst[0]
no_of_students = lst[1]
no_of_q = lst[2]
hash_map ={}
hash_map2 ={}
marks_of_student =  [int(x) for x in input().split()]
for i in range(no_of_q):
    lst3 =  [int(x) for x in input().split()]
    marks = lst3[0]
    sub_parts = lst3[1]
    hash_map[marks] = sub_parts
    hash_map2[marks] = i+1
# print(hash_map)
lst4 = sorted(hash_map.items(),key=lambda x:x[1],reverse=True)
# print(lst4)
main_lst= []
for i in range(len(lst4)-1):
    if lst4[i][1] != lst4[i+1][1]:
        main_lst.append(lst4[i][0])
    else:
        if lst4[i][0]//lst4[i][1] < lst4[i+1][0]//lst4[i+1][1]:
            main_lst.append(lst4[i][0])
            main_lst.append(lst4[i+1][0])
        else:
            main_lst.append(lst4[i+1][0])
            main_lst.append(lst4[i][0])
        i=i+1

# print(main_lst)

for i in range(no_of_students):
    temp_lst = []
    student_marks = marks_of_student[i]
    j=0
    # print(student_marks)
    while(student_marks < min_marks):
        # print(main_lst[j])
        student_marks += main_lst[j]
        temp_lst.append(hash_map2[main_lst[j]])
        j=j+1
    temp_lst.sort()
    print(len(temp_lst),*temp_lst)