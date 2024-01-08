#tính năm âm lịch 

def nam(a):
    can=""
    du10=a%10
    if du10 ==0:
        can=="Canh" 
    elif du10==1:
        can="Tân"    
    elif du10==2:
        can="Nhâm"    
    elif du10==3:
        can="Quý"
    elif du10==4:
        can="Giáp"
    elif du10==5:
        can="Ất"
    elif du10==6:
        can="Binh"
    elif du10==7:
        can="Đinh"
    elif du10==8:
        can="Mậu"
    elif du10==9:
        can="Kỷ"    
    chi=""
    du12=a%12
    if du12==0:
        chi==" Thân"
    elif du12==1:
        chi=" Dậu"
    elif du12==2:
        chi=" Tuất"
    elif du12==3:
        chi=" Hợi"
    elif du12==4:
        chi=" Tý"
    elif du12==5:
        chi=" SỬu"
    elif du12==6:
        chi=" Dần"
    elif du12==7:
        chi=" Mão"
    elif du12==8:
        chi=" Thìn"
    elif du12==9:
        chi=" Tỵ"
    elif du12==10:
        chi=" Ngọ"
    elif du12==11:
        chi=" Mùi"
    print ("năm",a,"lịch âm là năm",can+ chi)
print (nam(2017))

        
