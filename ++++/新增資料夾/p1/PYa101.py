#TODO

a=eval(input())
b=eval(input())
c=eval(input())
d=eval(input())

#輸入四個整數，然後將這四個整數以欄寬為5、欄與欄間隔一個空白字元，再以每列印兩個的方式，先列印向右靠齊，再列印向左靠齊，左右皆以直線 |（Vertical bar）作為邊界。
#向右靠齊
#TODO

print("|{:5d} {:>5d}|".format(a,b))
print("|{:5d} {:>5d}|".format(c,d))

#向左靠齊
#TODO
print("|{:<5d} {:<5d}|".format(a,b))
print("|{:<5d} {:<5d}|".format(c,d))