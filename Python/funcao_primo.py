def eh_primo(x):
    div = 0
    for i in range(1, (x+1)):
        if (x % i) == 0:
            div = div + 1
    if div == 2:
        return True
    else:
        return False

x = int(input())
if eh_primo(x):
	print('S')
else:
	print('N')
