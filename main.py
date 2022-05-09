from flask import Flask
from flask import jsonify
from flask import request
from common import mysql_operate  # 从common包中导入mysql_operate，使用其db

app = Flask(__name__)
# 初始化生成一个app对象，这个对象就是Flask的当前实例对象，后面的各个方法调用都是这个实例

# '''鉴权'''postman等接口测试工具中可在请求头中加入参数
# def auth():
#     if 'jianquan' not in request.headers: #在头部添加参数
#         return abort(401)
#     if request.headers['jianquan'] != 'pass':
#         return abort(403)

@app.route("/")    # 自定义路径
def index():
    # auth()
    return 'Hello!'

@app.route("/query")    # 自定义query路径
def get_all_users():
    # auth()
    """获取所有用户信息"""
    sql = "SELECT * FROM student"   # sql语句，可自行对应自己数据相应的表进行操作
    data = mysql_operate.db.select_db(sql)   # 用mysql_operate文件中的db的select_db方法进行查询
    # data = data[0]  #返回的是列表格式，取索引0，第一个元素，转化成字典格式
    print("获取所有用户信息 == >> {}".format(data))  # 在pycharm下打印信息
    app.config['JSON_AS_ASCII'] = False  #返回的json格式转化为汉字打印出来
    return jsonify(data)   #通过jsonify函数，返回的就是json字符串的格式


@app.route("/query/<school>",methods=["GET", "POST"])    # 自定义query路径
def get_school_users():
    # auth()
    """获取所有用户信息"""
    school = str(request.args.get('school'))  # school为页面端输入的值
    print(school)
    # student_names = str(request.args.get('student_names'))  # student_names为页面端输入的值
    # sql = "SELECT * FROM student WHERE school = '" + school + "'"  # 查询输入的url里面的参数school的值
    sql = "SELECT * FROM student WHERE school = school"  # 查询输入的url里面的参数school的值
    # sql = "SELECT * FROM student WHERE school = "school""  # 查询输入的url里面的参数school的值
    data = mysql_operate.db.select_db(sql)  # 输出school的值
    # sql = "SELECT * FROM student"   # sql语句，可自行对应自己数据相应的表进行操作
    # data = mysql_operate.db.select_db(sql)   # 用mysql_operate文件中的db的select_db方法进行查询
    # data = data[0]  #返回的是列表格式，取索引0，第一个元素，转化成字典格式
    print("获取对应的用户信息 == >> {}".format(data))  # 在pycharm下打印信息
    app.config['JSON_AS_ASCII'] = False  #返回的json格式转化为汉字打印出来
    return jsonify(data)   #通过jsonify函数，返回的就是json字符串的格式


@app.route("/query/<student_names>",methods=["GET", "POST"])    # 自定义query路径
def get_studentnames_users():
    # auth()
    """获取所有用户信息"""
    student_names = str(request.args.get('student_names'))  # student_names为页面端输入的值
    sql = "SELECT * FROM student WHERE student_names = '" + student_names + "'"  # 查询输入的url里面的参数school的值
    data = mysql_operate.db.select_db(sql)  # 输出school的值
    # sql = "SELECT * FROM student"   # sql语句，可自行对应自己数据相应的表进行操作
    # data = mysql_operate.db.select_db(sql)   # 用mysql_operate文件中的db的select_db方法进行查询
    print("获取对应用户信息 == >> {}".format(data))  # 在pycharm下打印信息
    app.config['JSON_AS_ASCII'] = False  #返回的json格式转化为汉字打印出来
    return jsonify(data)   #通过jsonify函数，返回的就是json字符串的格式

#添加数据库元素，判断数据库是否有请求的值，存在则返回已存在，不存在则自动添加
@app.route("/insert", methods=["GET", "POST"])  # 表示GET和POST方法都可以进行操作
def insert():
    # auth()
    """插入信息"""
    school = str(request.args.get('school'))   # school为页面端输入的值
    student_names= str(request.args.get('student_names')) #student_names为页面端输入的值
    sql = "SELECT * FROM student WHERE school = '" + school + "'"  #查询输入的url里面的参数school的值
    data = mysql_operate.db.select_db(sql) #输出school的值
    if data:     # 判断是否有返回数据，如果有则表示已经存在
        return '已存在'
    else:    # 如果没有，则插入新数据，新数据的值来源于url上输入的数据
        sql1 = "insert into student(student_names,school) values('" + school + "','" + student_names + "');" #插入url上输入的school和student_names的值
        mysql_operate.db.execute_db(sql1)
        return '添加成功'


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8888)   #
# flask默认是没有开启debug模式的，开启debug模式，可以查找代码里面的错误
# host = '127.0.0.1' 表示设置的ip，如果需要连接手机等设备，可以将手机和电脑连接同一个热点，将host设置成对应的ip
# port 为端口号，可自行设置
