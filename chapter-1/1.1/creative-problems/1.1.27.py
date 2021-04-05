'''
Binomial Distrobution
Estimate the number of recursive calls that would be used by the code

public static double binomial(int n, int k, double p) {
    if((n == 0) && (k == 0)) return 1.0;
    if((n < 0) || (k < 0)) return 0.0; 
    return (1 - p) * binomial(n-1, k, p) + p * binomial(n-1, k-1, p);
}

to compute binomial(100, 50, 0.25). Develop a better implementation that
is based on saving the computed values in an array
'''

def binomial(n, k , p):
    if n == 0 and k == 0:
        return 1.0
    if n < 0 or k < 0:
        return 0.0
    return 1 - p * binomial(n-1, k, p) + binomial(n-1, k-1, p)

print(binomial(100, 50, 0.25))