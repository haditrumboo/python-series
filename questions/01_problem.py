def reverse(num):
    no = []

    for n in str(num):
        no.append(n)

    no.reverse()

    r = "".join(no)

    return r


num = 123456789
a = reverse(num)
print(a)
# ============================

a = "1234567"

b = list(a)
b.reverse()
b = "".join(b)

print(b)
# ========================================

a = "1234567"

print(a[::-1])

