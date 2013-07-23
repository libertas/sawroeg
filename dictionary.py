
from sawguq import sawguq
from sawgeq import sawgeq


def searchWord(key, from_begin=True):
    if from_begin:
        return ((word, sawguq[word]) for word in sawguq if word.startswith(key))
    else:
        return ((word, sawguq[word]) for word in sawguq if key in word)


def searchExamples(key):
    result = ""
    for i in sawgeq:
        string = sawgeq[i]
        tlist = string.rsplit("\n")
        for j in tlist:
            if key in j:
                result += "%s    --<<%s>>\n" % (j, i)
                yield result


def newSearch(key, group):
    if group == "Gyaeuj":
        result = searchWord(key, True)
    elif group == "Gyang":
        result = searchWord(key, False)
    elif group == "Laeh":
        result = searchExamples(key)
    value = ""
    n = 0
    for i in result:
        n += 1
        value += "%d.%s\n" % (n, i)
    return value
