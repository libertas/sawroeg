try:
    import Levenshtein
except ImportError:
    try:
        import ctypes
        Levenshtein = ctypes.CDLL("levenshtein.so")
    except:
        import levenshtein as Levenshtein

def byLevenshtein(key,result_yield):
    lang="zha"
    try:
        str(key).encode('iso-8859-1')
    except UnicodeEncodeError:
        lang = "zh"
    result_list2d = []
    if lang == "zha":
        for i in result_yield:
            tmp=i.split(" ")[0]
            result_list2d.append([Levenshtein.distance(key,tmp), i])
    else:
        for i in result_yield:
            result_list2d.append([Levenshtein.distance(key,i), i])
    result_list2d.sort()
    result = ""
    for i in result_list2d:
        yield i[1]
