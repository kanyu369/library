"""
  可以进行增加、修改、删除、查询图书 （基础）
 使用文件来保存图书内容 （基础）
 图书具有作者、书名、出版社....等属性，具体字段可自定义 （基础）
 开源到github中（后面我们会来一起评审代码）（基础）
 使用cushy-storage来保存图书内容（提升）
 使用面向对象的思路去做 （提升）
 项目中运用一些设计模式（如工厂模式、发布订阅者模式等） （提升）
"""

#用户注册
def log_on():
    print("请注册账号")
    name=input("请输入姓名")
    number=input("请输入电话")
    password=input("请输入密码")
    repassword=input("请再次输入密码")
    account={'姓名':name,'电话':number,'密码':password}
    if password == repassword:
        print("注册成功，直接为您登录")
        with open('account_data.txt','a',encoding='utf-8') as file:
            file.write(str(account))
            file.write('\n')
    else:
        print("两次输入不一样")
        log_on()

#用户登录
def log_in():
    print("请登录账号,没有账号请注册账号")
    a=input("是否已有账号（是/否）")
    if a=='否':
        print("为您跳转注册页面")
        log_on()
    else:
        name = input("请输入姓名")
        number = input("请输入电话")
        password = input("请输入密码")
        account = {'姓名': name, '电话': number, '密码': password}
        with open('account_data.txt','r',encoding='utf-8') as file:
            have_log=file.readlines()   #readlines()返回一个列表

        for temp in have_log:
            b=eval(temp)
            if b==account:
                print("已为你登录")
                return True

            else:
                print("输入有误")
                log_in()

#保存图书
def add_book():
    with open('book_warehouse.txt','a',encoding='utf-8') as file:
        book_id=int(input("请输入书号"))
        book_name=input("请输入书名")
        book_author=input("请输入作者")
        book_publish=input("请输入出版社")
        book_price=int(input("请输入价格"))
        book_numbers=int(input("请输入书目数量"))
        book_information={'编号': book_id, '书名': book_name, '作者': book_author, '出版社': book_publish,'数量': book_numbers,'价格':book_price}

        file.write(str(book_information),)
        file.write('\n')

#修改图书1
def change_book():
    with open('book_warehouse.txt','a',encoding='utf-8') as file:
        num=int(input("请输入需要修改的图书的编号"))
        book_contained=file.readlines()
    for temp in book_contained:
        b=eval(temp)
        if b['编号']==num:
            print(b)
            change_part=input('请输入您要修改的内容（编号、书名、作者、出版社、数量、价格）')
            for item in b:
                if item==change_part:
                    b[item]=input('请输入修改内容')


#查询图书
def find_book():
    num=int(input("请输入要查询的数目编号"))
    with open('book_warehouse.txt','r',encoding='utf-8') as file:
        book_contained = file.readlines()
    for temp in book_contained:
        b=eval(temp)
        if b['编号']==num:
            print(b)
        else:
            print('您查找的编号不存在')





