#1. Determine if a string is a palindrome
def is_palindrome(string):
    for i in range(len(string)/2):
        if string[i]!=string[-1*(i+1)]:
            return False
    return True

#2. Reverse a string (without built-ins)
def reverse(string):
    items = list(string) #convert to a list; strings are immutable
    for i in range(len(items)/2):
        items[i],items[-1*(i+1)]=items[-1*(i+1)],items[i]
    return ''.join(items)

#3. Interpret unix paths
# eg "/home/tmp/./../test" -> "/home/test"
# "/home/example/../../.." -> "/"
# Too many '..' are ignored. No trailing '/'
def unix_path(string):
    split = string.split("/")
    tmp = []
    for item in split:
        if item!='.' and len(item)>0:
            if item == '..':
                if len(tmp)>0:
                    tmp.pop()
            else:
                tmp.append(item)
    return '/'+'/'.join(tmp)
            
