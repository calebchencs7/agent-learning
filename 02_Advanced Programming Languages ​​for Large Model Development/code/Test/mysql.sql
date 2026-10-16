"""
MySQL 表结构更改与数据查询
背景：
学校教务系统中的学生表需要根据业务变化进行调整。现在需要新增手机号字段、规范字段类型和字段名称，并完成一个基础条件查询。
题目：
现有学生表 t_student，表结构如下：

字段	含义
id	学生编号
name	姓名
age	年龄
请完成以下要求：
1.给 t_student 表新增一个字段 phone，类型为 varchar(20)，用于保存手机号。(2分)
2.将 age 字段类型修改为 int。(2分)
3.将 name 字段名称修改为 student_name，类型为 varchar(50)。(3分)
4.删除 phone 字段。(2分)
5.查询年龄大于 18 的学生姓名和年龄，并按照年龄从大到小排序。(3分)
"""



ALTER TABLE t_student ADD phone VARCHAR(20);
ALTER TABLE t_student MODIFY age INT;
ALTER TABLE t_student CHANGE name student_name VARCHAR(50);
ALTER TABLE t_student DROP COLUMN phone;
SELECT student_name, age FROM t_student WHERE age > 18 ORDER BY age DESC;