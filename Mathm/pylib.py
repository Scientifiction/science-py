def indexOf(arr,ele):
    try:
        return arr.index(ele)
    except ValueError:
        return -1;
def sattrin(f,attr):
    if isinstance(f, int) or isinstance(f, str):
        return False
    try:
        if f[attr]:
            return True
    finally:
        return attr in vars(f)
