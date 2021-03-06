
def f(A, x):
    return A[3]*x**3 + A[2]*x**2 + A[1]*x + A[0]

A = map(float, reversed(raw_input().split()))
lo, hi = map(float, raw_input().split())

result = None
f_lo, f_hi = f(A, lo), f(A, hi)
while True:
    f_lo, f_hi = f(A, lo), f(A, hi)
    if f_lo * f_hi <= 0:
        mid = (lo+hi) / 2
        f_mid = f(A, mid)
        if abs(f_mid) < 1e-9:
            result = mid
            break
        elif f_mid * f_lo >= 0:
            lo = mid
        elif f_mid * f_hi >= 0:
            hi = mid

print '%.2f' % result
    

    


