a, b = map(int, input().split())
c, d = map(int, input().split())
e, f = map(int, input().split())

# x축
X_list = [a, c, e]

# y축
Y_list = [b, d, f]

for i in range(3):
    if X_list.count(X_list[i]) == 1:
        g = X_list[i]
    if Y_list.count(Y_list[i]) == 1:
        h = Y_list[i]

print(g, h)