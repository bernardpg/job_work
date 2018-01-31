#建立 GUI

#一個對比程式碼(option )


#一個 拉貨品庫存的對比(stock)

#一個 進貨庫存 (inputstock )









import os

# C:\Users\黃\Desktop
# SLS3_銷貨日報表.txt
##
my_path =input("輸入路徑")
os.chdir(my_path)
file=input("輸入檔案")
#
Fe=open(file)
Fe=Fe.readlines()
print (type(Fe))
i=0
d=open("報表.txt","w")
for item in Fe :
    i=i+1
    #print(type(item))
    
    if item.startswith("日期區間",4) :
        for k in range(4,60) :
            if Fe[i+k].startswith("總計",71):
                d.write(Fe[i+k])
                print(Fe[i+k])
                break 
            else:
                d.write(Fe[i+k])
            
                
d.close()
