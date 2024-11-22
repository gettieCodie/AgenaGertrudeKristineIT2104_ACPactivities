while True:
    
    total = float(input("Enter the total purchase amount: "))
    print(f"Initial purchase amount: {total:.2f}")

    if(total > 5000):
        discount = total * 0.1
        print(f"Discount: {discount:.2f}")

    else:
        discount = total*0.05
        print(f"Discount: {discount:.2f}")

    print(f"Final price: {total-discount:.2f}")

    loop = input("Do you want to try again? (yes/no): ").strip().lower()
    if loop != "yes":
        break
print("Thank you!")
