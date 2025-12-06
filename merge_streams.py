# Merge Timestamped Events

def merge_streams(a_stream: list[tuple], b_stream: list[tuple]) -> list[tuple]:
    a_ptr, b_ptr = 0, 0
    a_len, b_len = len(a_stream), len(b_stream)

    results = []

    while a_ptr < a_len and b_ptr < b_len:
        print(a_ptr, b_ptr, a_len, b_len)

        a = a_stream[a_ptr]
        b = b_stream[b_ptr]

        if a[0] <= b[0]:
            results.append(a)
            a_ptr += 1

        else:
            results.append(b)
            b_ptr += 1

    if a_ptr < a_len:
        results.extend(a_stream[a_ptr:])

    if b_ptr < b_len:
        results.extend(b_stream[b_ptr:])


    return results


a = [(1, "A1"), (3, "A3")]
b = [(2, "B2"), (3, "B3")]

results = merge_streams(a, b)

print(results)