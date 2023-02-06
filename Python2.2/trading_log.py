


total= 0
count= 0
profitable_days= []
unprofitable_days= []
trading_pnl = [ -224,  352, 252, 354, -544, -650,   56, 123, -43,  254, 325, -123,  47, 321,  123, 133, -151, 613, 232, -311 ]
min= 0
max= 0

for day in trading_pnl:
    count += 1
    total += day
    if day >= 0 and max: 
        max = day 
    elif day <= 0 and min:
        min= day

for i in trading_pnl: 
    if i >= 0: 
        profitable_days.append(int(i))
    else: 
        unprofitable_days.appernd(int(i))

        
    
days= len(trading_pnl)
print(F"Total trading days:", {days})
print(F"total profit/loss:", {total})
total = sum(trading_pnl)
average = total / count 

print(average)
print(count)
print(min(trading_pnl))
print(max(trading_pnl))

print(F"profitable days:", {profitable_days})
print(F"profitable days:", {unprofitable_days})


