def solution(s):

    ListOfStrings = []
    i = 0

    def addToList(e):
    #Add a estring to a list of strings.
        ListOfStrings.append(e[0: 2])
        return ListOfStrings

#Main function.
    if len(s)%2 != 0:
        s = f"{s}_"
    else:
        None
    while i < len(s):
        addToList(s)
        s = s[2:]
    return ListOfStrings
