s, t, x = map(int, input().split())
if s < t:
    print("Yes" if s <= x < t else "No")
else:
    print("Yes" if x < t or s <= x else "No")
    