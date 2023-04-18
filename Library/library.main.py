#主页面
import Books_surfice as book
import User_surfice as user

#主程序
def main():
    key = 123456789
    print('1.查询图书')
    print('2.管理者选项')
    print('3.结束使用')
    a = int(input('请选择要执行的功能'))

    if a == 1:
        book.find_book()
        main()
    elif a == 2:
        b = int(input('请输入管理者密码'))
        if b == key:
            print("已进入管理者选项".center(160, '~'))
            print('1.添加图书')
            print('2.修改图书')
            print('3.删除图书')
            c = int(input('请选择要执行的功能'))
            if c == 1:
                book.add_book()
                main()
            elif c == 2:
                book.change_book()
                main()
            elif c == 3:
                book.remove_book()
                main()
        else:
            print('密码不正确，返回初始页面'.center(160, '~'))
            main()
    elif a==3:
        print("感谢您的使用".center(160, '~'))


print('欢迎来到图书管理系统'.center(160, '~'))
user.log_in()   #用户登录
main()