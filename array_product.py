
def left_right_products(inputs: list) -> list:
    print("inputs", inputs)

    n = len(inputs)
    outputs = [0] * n

    l_product = 1
    for idx in range(n):
        outputs[idx] = l_product
        l_product *= inputs[idx]
        
    print("first_pass", outputs)

    r_product = 1
    for idx in range(n - 1, -1, -1):
        outputs[idx] *= r_product
        r_product *= inputs[idx]
    
    print("second_pass", outputs)
    return outputs

inputs = [1, 2, 3, 4]
left_right_products(inputs=inputs)
