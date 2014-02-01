try:
    import Levenshtein
except ImportError:
    try:
        import ctypes
        Levenshtein = ctypes.CDLL("levenshtein.so")
    except:
        import levenshtein as Levenshtein

def byLevenshtein(key,result):
    lang="zha"
    try:
        str(key).encode('iso-8859-1')
    except UnicodeEncodeError:
        lang = "zh"
    result_list = result.split("\n")
    result_list2d = []
    if lang == "zha":
        for i in result_list:
            tmp=i.split(" ")[0]
            result_list2d.append([Levenshtein.distance(key,tmp), "".join([i, "\n"])])
    else:
        for i in result_list:
            result_list2d.append([Levenshtein.distance(key,i), "".join([i, "\n"])])
    result_list2d.sort()
    result = ""
    for i in result_list2d:
        result += i[1]
    return result
