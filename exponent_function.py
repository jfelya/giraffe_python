def power_func(base_num, pow_num):
    if pow_num == 0:
        return 1
    else:
        result = 1
        for i in range(pow_num):
            result = result * base_num
        return result


base_numm = int(input("Enter the base number: "))
pow_numm = int(input("Enter the power number: "))
print(power_func(base_numm, pow_numm))
