def fibonacy(x):
    if x <= 1:
        return x
    return fibonacy(x-1)+fibonacy(x-2)

print(fibonacy(5))