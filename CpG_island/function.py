#  compute probability of two models
def compute_p(models, frequency):
    p = 1
    for i, m in zip(models, frequency):
        for j, n in zip(i, m):
            if n == 0:
                continue
            else:
                p = p * (j ** n)
    return p
