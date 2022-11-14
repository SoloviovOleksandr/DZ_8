
def month_number(a):
    if a == 1:
     return "Січень"
    if a == 2:
     return "Лютий"
    if a == 3:
     return "Березень"
    if a == 4:
     return "Квітень"
    if a == 5:
     return "Травень"
    if a == 6:
     return "Черевень"
    if a == 7:
     return "Липень"
    if a == 8:
     return "Серпень"
    if a == 9:
     return "Вересень"
    if a == 10:
     return "Жовтень"
    if a == 11:
     return "Листопад"
    if a == 12:
     return "Грудень"
    try:
      if a < 1 or a > 12:
       raise ValueError("Enter rigth number")

      if not type(a) is int:
         raise ValueError("Vvedit cile chuslo")
    except Exception as exec:
        return exec
    finally:
        print("All Value checked")

print(month_number(2.6777))
