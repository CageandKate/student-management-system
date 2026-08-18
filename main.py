from services.student_manager import StudentManager

def input_int(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print("请输入整数")
        return None

def input_int_range(prompt,min_value,max_value):
    value = input_int(prompt)
    if value is None:
        return None
    if not min_value <= value <= max_value:
        print(f"请输入{min_value}-{max_value}之间的整数")
        return None
    return value




def main():
    manager = StudentManager()
    while True:
        print("====== 学生管理系统 ======")
        print("1. 添加学生")
        print("2. 查看所有学生")
        print("3. 查询学生")
        print("4. 修改成绩")
        print("5. 删除学生")
        print("0. 退出")


        choice = input_int_range("请输入操作：",0,5)
        if choice is None:
            continue

        if choice == 0:
            break

        elif choice == 1:
            print("=====1. 添加学生=====")
            student_id = input_int("id:")
            if student_id is None:
                continue
            name = input("name:")
            age = input_int_range("age:",1,120)
            if age is None:
                continue
            score = input_int_range("score:",0,100)
            if score is None:
                continue
                
            result = manager.add_student(
                student_id,
                name,
                age,
                score
            )
            if result == "success":
                print("添加成功")
            elif result == "duplicate_id":
                print("ID已经存在")
            elif result == "invalid_name":
                print("姓名不能为空")
            elif result == "invalid_age":
                print("年龄必须大于0")
            elif result == "invalid_score":
                print("成绩必须在0-100之间")

        elif choice == 2:
            print("=====2. 查看所有学生信息=====")
            manager.show_students()

        elif choice == 3:
            print("=====3. 查询学生=====")
            student_id = int(input("请输入要查询学生的id："))
            result = manager.find_student_by_id(student_id)
            if result is not None:
                result.show_info()
            else:
                print("无该生")

        elif choice == 4:
            print("=====4. 修改成绩=====")
            student_id = int(input("请输入你要修改成绩的学生的id："))
            try:
                score = int(input("请输入你要修改的成绩："))
            except ValueError:
                print("成绩必须是整数")
                continue
            result = manager.update_score(student_id, score)
            if result == "success":
                print("修改成功！")
            elif result == "not_found":
                print("无该生")
            elif result == "invalid_score":
                print("成绩必须在0-100之间")

        elif choice == 5:
            print("=====5. 删除学生=====")
            student_id = int(input("请输入你要删除学生的id："))
            result = manager.delete_student(student_id)
            if result :
                print("删除成功！")
            
            else:
                print("无该生")

        else:
            print("非法输入")

if __name__ == "__main__":
    main()