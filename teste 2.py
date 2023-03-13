num = 2
fibonacci = [0, 1]
while fibonacci[-1] < num:
    next_num = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(next_num)
if num in fibonacci:
    print(f"{num} pertence à sequência de Fibonacci.")
else:
    print(f"{num} não pertence à sequência de Fibonacci.")
