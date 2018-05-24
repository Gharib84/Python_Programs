print("The Invoice Program")
print()
client_type = input("Choice The Client Type (r/w ):\t")
total = float(input("Enter The Invoice Total\t"))
# validate client type 
if client_type.lower() == "r":
    if total >= 0 and total < 100:
        discount = 0
    elif total >= 100 and total < 250:
        discount = .1
    elif total >= 250 and total < 500:
        discount = .2
    elif total >= 500:
        discount = .25
elif client_type.lower() == "w":
    if total >= 0 and total < 100:
        discount = .5
    elif total >=100 and total < 500:
        discount = .25
    elif total >= 500:
        discount =  .02
else:
    discount = 0
discount_amount = round(total * discount ,2 )
new_invoice_total = total - discount_amount

# The OutPuts
print("The Invoice Total:\t" + str(total)) 
print("Discount Percent :\t" + str(discount))
print("Discount Amount :\t" + str(discount_amount))
print("New Invoice Total \t" + str(new_invoice_total))


     