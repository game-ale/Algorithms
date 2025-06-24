def count_numbers(pos, tight, leading_zero, state):
    if pos == len(digits):
        return 1 if is_valid(state) else 0

    if dp[pos][tight][leading_zero][state] is not None:
        return dp[pos][tight][leading_zero][state]

    limit = digits[pos] if tight else 9
    total = 0

    for d in range(0, limit + 1):
        new_tight = tight and (d == limit)
        new_leading_zero = leading_zero and d == 0
        new_state = update_state(state, d, new_leading_zero)
        total += count_numbers(pos + 1, new_tight, new_leading_zero, new_state)

    dp[pos][tight][leading_zero][state] = total
    return total
