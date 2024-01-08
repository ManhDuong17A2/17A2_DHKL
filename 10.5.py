#kiểm tra dữ liệu zip code vietnam 
try:
 zipcode=str(input("nhập mã zip:   ")) 
 if len(zipcode)==6:         
  listcode=list(zipcode)
  listint=[int(x) for x in listcode]
  print("mã zip code chính xác")
 
 else:
    print("mã zip code sai")
except : 
  print ("mã zip code sai")
