#tính chỉ số BMI
def chieucao_cannang(chieucao,cannang):
    bmi=cannang/(chieucao*chieucao)
    if bmi <18.5:
        print("Chỉ số BMI của bạn là",bmi,"Gầy")
    elif bmi>=18.5 and bmi<=24.99:
        print("chỉ số BMI của bạn là",bmi,"Bình thường")
    else :
        print ("chỉ số BMI của bạn là",bmi,"Thừa cân")
print (chieucao_cannang(1.73,55))                