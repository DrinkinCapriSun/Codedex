yuan = (float(input("What do you have left in yuan? ")))
yen = (float(input("What do you have left in yen? ")))
won = (float(input("What do you have left in won? ")))

dyuan = yuan * 0.14
dyen = yen * 0.0071
dwon = won * 0.00078

total = dyuan + dyen + dwon
print(total)