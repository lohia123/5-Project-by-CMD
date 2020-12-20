start=int(input('enter star no='))
end=int(input('enter end no='))
for i in range(start, end):
    if i%2==0:
        print('even no=', i)
    else:
        print('odd no=', i)
