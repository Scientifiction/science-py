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
    
class DotDict(dict):
    def __init__(self, *args, **kwargs):
        super(DotDict, self).__init__(*args, **kwargs)

    def __getattr__(self, key):
        value = self[key]
        if isinstance(value, dict):
            value = DotDict(value)
        return value
