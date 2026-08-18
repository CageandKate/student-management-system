# Python 学生管理系统

这是一个基于 Python 命令行的学生管理系统练习项目。项目使用面向对象和分层结构实现学生信息的增删改查，并通过 JSON 文件保存学生数据。

## 项目功能

- 添加学生
- 查看所有学生
- 按成绩降序查看学生
- 按成绩升序查看学生
- 根据 ID 查询学生
- 修改学生成绩
- 删除学生
- 自动保存和读取学生数据
- 对部分输入进行合法性校验

## 项目结构

```text
student_manegement_sys/
├── main.py
├── data/
│   └── students.json
├── models/
│   ├── __init__.py
│   └── student.py
├── services/
│   ├── __init__.py
│   └── student_manager.py
└── utils/
    ├── __init__.py
    └── file_utils.py
```

## 文件说明

### main.py

程序入口文件，负责：

- 显示菜单
- 接收用户输入
- 调用 `StudentManager` 完成具体操作
- 对菜单选项、年龄、成绩等输入做基础校验

### models/student.py

定义 `Student` 学生类，负责描述一个学生对象。

主要属性：

- `id`：学生 ID
- `name`：学生姓名
- `age`：学生年龄
- `score`：学生成绩

主要方法：

- `to_dict()`：将学生对象转换成字典，方便保存到 JSON 文件
- `from_dict()`：将字典转换成学生对象
- `update_score()`：修改学生成绩
- `update_age()`：修改学生年龄
- `is_valid_score()`：判断成绩是否合法
- `is_valid_age()`：判断年龄是否合法
- `is_passed()`：判断学生是否及格

### services/student_manager.py

定义 `StudentManager` 类，负责管理所有学生。

主要方法：

- `add_student()`：添加学生
- `show_students()`：显示所有学生
- `show_students_by_score()`：按成绩排序显示学生
- `find_student_by_id()`：根据 ID 查询学生
- `update_score()`：修改学生成绩
- `delete_student()`：删除学生
- `get_student_count()`：获取学生数量
- `save_students()`：保存学生数据

### utils/file_utils.py

负责 JSON 文件读写。

主要方法：

- `load_students()`：从 `data/students.json` 读取学生数据
- `save_students()`：将学生数据保存到 `data/students.json`

## 运行方式

在项目根目录执行：

```bash
cd student_manegement_sys
python main.py
```

如果你的电脑同时安装了多个 Python 版本，也可以尝试：

```bash
python3 main.py
```

## 菜单说明

运行后会看到如下菜单：

```text
====== Python 学生管理系统 ======
1. 添加学生
2. 查看所有学生
3. 查询学生
4. 修改成绩
5. 删除学生
0. 退出
```

输入对应数字即可执行功能。

## 查看学生排序

选择 `2. 查看所有学生` 后，可以继续选择输出方式：

```text
若按成绩降序输出请输入1，升序输出请输入2，默认输出请输入0
```

- 输入 `1`：按成绩从高到低显示
- 输入 `2`：按成绩从低到高显示
- 输入 `0`：按原始保存顺序显示

排序功能的核心代码在 `StudentManager.show_students_by_score()`：

```python
sorted_students = sorted(
    self.students,
    key=lambda student: student.score,
    reverse=reverse
)
```

其中：

- `key=lambda student: student.score` 表示按照学生成绩排序
- `reverse=True` 表示降序
- `reverse=False` 表示升序

## 数据格式

学生数据保存在：

```text
student_manegement_sys/data/students.json
```

数据格式示例：

```json
[
    {
        "id": 1,
        "name": "张三",
        "age": 18,
        "score": 90
    }
]
```

## 输入校验

当前系统已经对部分输入做了校验：

- 菜单选项必须是 `0-5` 之间的整数
- 年龄必须是 `1-120` 之间的整数
- 成绩必须是 `0-100` 之间的整数
- 姓名不能为空
- 学生 ID 不能重复

相关函数在 `main.py`：

```python
def input_int(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print("请输入整数")
        return None


def input_int_range(prompt, min_value, max_value):
    value = input_int(prompt)
    if value is None:
        return None
    if not min_value <= value <= max_value:
        print(f"请输入{min_value}-{max_value}之间的整数")
        return None
    return value
```

## 注意事项

当前代码中，查询学生功能已经使用 `print(result)` 输出学生信息，因为 `Student` 类通过 `__str__()` 定义了学生对象的显示格式。

如果要继续完善，可以考虑：

- 修改成绩和删除学生时也使用 `input_int()`，避免输入非数字时报错
- 给学生 ID 增加必须大于 0 的校验
- 添加修改姓名、修改年龄功能
- 添加按姓名查询功能
- 添加清空所有学生功能
- 添加单元测试

## 学习重点

这个项目适合复习以下 Python 知识：

- 变量和数据类型
- 条件判断
- 循环
- 函数封装
- 列表操作
- 字典和 JSON
- 文件读写
- 类和对象
- 静态方法
- 类方法
- 模块导入
- 简单项目分层
