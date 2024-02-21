def calculate_discount(price, discount_percent):

  result = price  if(discount_percent < 20) else price - (price * (discount_percent/100))

  return result


price = int(input('Please enter orignal numeric Price of Item: '))

discount_percent = int(input('Please enter orignal numeric Price of Item: '))


final_price = calculate_discount(price , discount_percent)
print('Final price is: {} '.format(final_price))