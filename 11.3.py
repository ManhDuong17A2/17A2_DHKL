#tìm thú trong vườn thú 

list_animals=['ant','bear','cat','dog','elephant','fish','goat','hippo']
print("các con thú có trong sở thú là:",list_animals)
print('sóo lượng các con thú có trong sở thú là:',len(list_animals))
a=input("nhập thú bạn muốn tìm:"     )
try:
 for x in list_animals:
    if x==a:
        print (x,"có trong sở thú")
    else:
        câu_lệnh_lỗi_để_chuển_sang_excepttt
except:
   print ("thú bạn tìm không có trong sở thú ")