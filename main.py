import math

package_weight = float(input('Please enter package weight in pounds: '))
shipping_distance = int((input('Please enter number of miles to ship: ')))

five_hundred_segment = int(math.ceil((shipping_distance / 500)))

shipping_charge1 = '${:.2f}.'.format(five_hundred_segment * 1.5)
shipping_charge2 = '${:.2f}.'.format(five_hundred_segment * 3.75)
shipping_charge3 = '${:.2f}.'.format(five_hundred_segment * 5.25)

price_list = [shipping_charge1, shipping_charge2, shipping_charge3]

if 0 < package_weight <= 2:
    print('To ship a', package_weight, 'pound package', shipping_distance, end='')
    print(' miles, your shipping charge is', price_list[0])

if 2 < package_weight <= 6:
    print('To ship a', package_weight, 'pound package', shipping_distance, end='')
    print(' miles, your shipping charge is', price_list[1])

if 6 < package_weight <= 10:
    print('To ship a', package_weight, 'pound package', shipping_distance, end='')
    print(' miles, your shipping charge is', price_list[2])

if package_weight > 10:
    print('Sorry, we only ship packages of 10 pounds or less.')

if package_weight <= 0:
    print('Invalid input!')
