import Books_surfice as book

#用户注册
def log_on():
    print("请注册账号")
    name=input("请输入姓名")
    number=input("请输入电话")
    password=input("请输入密码")
    repassword=input("请再次输入密码")
    account={'姓名':name,'电话':number,'密码':password}
    if password == repassword:
        print("注册成功，直接为您登录".center(160, '~'))
        with open('Users.txt','a',encoding='utf-8') as file:
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
    elif a=='是':
        name = input("请输入姓名")
        number = input("请输入电话")
        password = input("请输入密码")
        account = {'姓名': name, '电话': number, '密码': password}
        with open('Users.txt','r',encoding='utf-8') as file:
            have_log=file.readlines()   #readlines()返回一个列表

        for temp in have_log:
            b=eval(temp)
            if str(b)==str(account):
                print("已为你登录".center(160, '~'))
                break
        else:
            print("输入有误")
            log_in()
