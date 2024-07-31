k = 29
m = 30
n = 17

def prob_dom(k, m, n):
    total = k + m + n
    total_pairs = total * (total -1)

    favorable_pairs = (
        k * (k - 1) + 
        2 * (k * m) +
        2 * (k * n) +
        m * (m - 1) * 0.75 +
        2 * (m * n) * 0.5
    )

    probability = favorable_pairs / total_pairs

    return probability

prob = prob_dom(k, m, n)

print(f"{prob:.6f}")