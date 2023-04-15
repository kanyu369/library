#用户登录1
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

log_in()