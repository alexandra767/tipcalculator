food_amount = float(input('Enter food amount $: '))
tip_percentage = float(input('Enter tip percentage %: ')) / 100

tip_amount = food_amount * tip_percentage

# total food_amount  + tip_amount
total = food_amount + tip_amount

print(f'🥘 Food Amount: ${food_amount}')
print(f'Food Amount: ${tip_amount}')
print(f'💰 Total Amount: ${total}')
      
      