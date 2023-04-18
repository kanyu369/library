import os

#保存图书
def add_book():
    with open('Books.txt','a',encoding='utf-8') as file:
        book_id=int(input("请输入书号"))
        book_name=input("请输入书名")
        book_author=input("请输入作者")
        book_publish=input("请输入出版社")
        book_price=int(input("请输入价格"))
        book_numbers=int(input("请输入书目数量"))
        book={'编号': book_id, '书名': book_name, '作者': book_author, '出版社': book_publish,'数量': book_numbers,'价格':book_price}

        file.write(str(book))
        file.write('\n')


#查询图书
def find_book():
    get_id=int(input("请输入要查询的书目编号"))
    with open('Books.txt','r',encoding='utf-8') as file:
        books=file.readlines()

    for temp in books:
        book=eval(temp)
        if book['编号']==get_id:
            print(book)
            print('已完成查询'.center(160, '~'))
            break
    else:
        print('您查找的编号不存在'.center(160, '~'))



#修改图书
def change_book():
    get_id = int(input("请输入需要修改的图书的编号"))
    with open('Books.txt', 'r', encoding='utf-8') as file:
        books = file.readlines()

    for temp in books:
        book = eval(temp)
        if book['编号'] == get_id:
            print('当前书目信息为：', end='')
            print(book)
            books.remove(temp)
            print('请输入修改后的信息')
            book_id = int(input("请输入书号"))
            book_name = input("请输入书名")
            book_author = input("请输入作者")
            book_publish = input("请输入出版社")
            book_price = int(input("请输入价格"))
            book_numbers = int(input("请输入书目数量"))
            book2 = {'编号': book_id, '书名': book_name, '作者': book_author, '出版社': book_publish,
                     '数量': book_numbers, '价格': book_price}
            print('修改后数目信息为：', end='')
            print(book2)
            break
    else:
        print('你输入的编号不存在'.center(160, '~'))

    with open('Books.txt', 'w', encoding='utf-8') as f:
        f.write(str(book2) + '\n')

    with open('Books.txt', 'a', encoding='utf-8') as f:
        for temp in books:
            f.write(str(temp))
    print('已完成修改'.center(160, '~'))



#删除图书
def remove_book():
    id= int(input("请输入要删除的书目编号"))

    with open('Books.txt', 'r', encoding='utf-8') as file:
        books= file.readlines()

    for temp in books:
        book = eval(temp)
        if book['编号']==id:
            books.remove(temp)
            break
    else:
        print('你输入的编号不存在'.center(160, '~'))

    with open('Books.txt', 'w', encoding='utf-8') as f:
        for temp in books:
            f.write(str(temp))

    print('已完成删除'.center(160, '~'))