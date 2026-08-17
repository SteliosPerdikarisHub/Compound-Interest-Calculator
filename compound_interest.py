def positive_valid(value):
    while True:
        if value>0:
            break
        value=float(input('Enter positive value: '))
    return(value);




PV=float(input('Enter initial investment: '));
PV=positive_valid(PV);
Rate=float(input('Enter annual interest rate in percentage: '));
Rate=positive_valid(Rate);
Period=int(input('Enter investment period in years: '));
while True:
    if Period>=0:
        break
    Period=int(input('Enter non-negative value: '))

FV=PV*((1+(Rate/100))**Period);
Profit=FV-PV;
Total_Return=((FV-PV)/PV)*100;
print(f'Future value: ${FV:.2f}')
print(f'Profit: ${Profit:.2f}')
print(f'Total return: {Total_Return:.2f}%')
