from flask_restful import Resource, Api
from flask import request, Flask

from Restdemo.views import blue

student_dict = {
    '1': {'name': '令狐冲', 'age': 20, 'score': 90},
    '2': {'name': '黄蓉', 'age': 17, 'score': 100},
    '3': {'name': '小龙女', 'age': 16, 'score': 99},
}

app = Flask(__name__)
app.register_blueprint(blueprint=blue)
api = Api(app)


class Student(Resource):  # 继承了Resource这个抽象资源类，则为Restful资源。

    def get(self):  # get请求调用此方法
        return student_dict

    def post(self):
        stuname = request.form['stuname']  # 接收表单中的stuid参数
        stuage = request.form['stuage']
        stuscore = request.form['stuscore']
        new_stuid = int(max(student_dict.keys())) + 1
        # 模拟添加数据
        new_stu = {}
        new_stu['name'] = stuname
        new_stu['age'] = stuage
        new_stu['score'] = stuscore
        student_dict[str(new_stuid)] = new_stu
        print('添加成功，现在的学生数据是：', student_dict)
        return new_stu


api.add_resource(Student, '/students')  # 添加注册资源和接口

print('register successfully')
