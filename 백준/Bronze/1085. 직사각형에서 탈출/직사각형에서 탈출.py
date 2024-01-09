x, y, w, h = map(int, input().split())

a = h - y
b = y
c = w - x
d = x

length_list = [a, b, c, d]

print(min(length_list))