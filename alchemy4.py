
def largest_k_digit_number(k):
    largest = "9" * k
    return int(largest)


def largest_divisible_by(k, x):
    largest_ = largest_k_digit_number(k)
    while largest_ % x != 0:
        largest_ -= 1

    return largest_


result = largest_divisible_by(3, 7)
print(result)

