cryptocurrencyName = input('Enter the cryptocurrency name: ')
quantitycrypto = float(input('Enter the quantity of '+ str(cryptocurrencyName) + ' available: '))
quantityOfDaysPlayed = int(input('Enter the number of the days that you invest in ' + str(cryptocurrencyName)  + ': '))
gain = float(input('Enter the gain you had those days with ' + str(cryptocurrencyName) + ' with decimals included: '))

totalGain = quantitycrypto * gain /100 * quantityOfDaysPlayed 
totalQuantity = quantitycrypto + totalGain
print('the total gain win by you trading is :' + str(totalGain) + ', in  ' + str(quantityOfDaysPlayed) + ' days, you have now: '+ str(totalQuantity) )
