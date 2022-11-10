all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]


# def get_absent_student(all_array, present_array):
#     for i in all_students:
#         if i in present_array:
#             continue
#         return i


def get_absent_student(all_array, present_array):
    # 구현해보세요!
    stu = {}
    for key in all_array:
        stu[key] = True

    for key in present_array:
         del stu[key]

    for k in stu.keys():
        return k
    return

print(get_absent_student(all_students, present_students))