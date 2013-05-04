#1. Find the digital root (sum digits until only one digit remains)
# No string conversion
def digital_root(num):
    if num/10==0:
        return num
    iter = 0
    while num>0:
        iter+=num%10
        num/=10
    return digital_root(iter)
# With a string conversion    
def digital_root_s(num):
    s = str(num)
    return int(s) if len(s)==1 else digital_root(sum([int(x) for x in s]))
