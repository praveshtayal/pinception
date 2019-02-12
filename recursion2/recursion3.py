def subsetSumToK(str, n, output[50], k):
    if(n<=0 || str==nullptr || output==nullptr) return 0
    if(n==1):
        if(str[0]==k):
            output[0][0] = 1
            output[0][1] = k
            return 1
        return 0

    count1 = subsetSumToK(str,n-1,output, k)
    i, j, count2 = subsetSumToK(str,n-1,output+count1, k-str[n-1])
    for i in range(0, n):(i=0; i<count2; i++):
        output[count1+i][0] += 1
        index = output[count1+i][0]
        output[count1+i][index] = str[n-1]
    count3 = 0
    if(k==str[n-1]):
        output[count1+count2][0] = 1
        output[count1+count2][1] = k
        count3 = 1
    return count1+count2+count3

def printSubsetSumToKHelper(str, n, k, out, outSize):
    if(n<=0 || str==nullptr || out==nullptr) return
    if(n==1):
        if(str[0]==k):
            print(k' '
            for i in range(0, n):(i=outSize-1; i>=0; i--) print(out[i]' '
            print()
        return

    if(k==str[n-1]):
        print(k' '
        for i in range(0, n):(i=outSize-1; i>=0; i--) print(out[i]' '
        print()
    printSubsetSumToKHelper(str,n-1,k,out,outSize)
    out[outSize++] = str[n-1]
    printSubsetSumToKHelper(str,n-1,k-str[n-1],out,outSize)

def printSubsetSumToK(str, n, k):
    out[THOUSAND]
    printSubsetSumToKHelper(str,n,k,out,0)

def initMap(unordered_map<string,string>& map):
    map["1"] = "a"; map["2"] = "b"; map["3"] = "c"; map["4"] = "d"
    map["5"] = "e"; map["6"] = "f"; map["7"] = "g"; map["8"] = "h"
    map["9"] = "i"; map["10"] = "j"; map["11"] = "k"; map["12"] = "l"
    map["13"] = "m"; map["14"] = "n"; map["15"] = "o"; map["16"] = "p"
    map["17"] = "q"; map["18"] = "r"; map["19"] = "s"; map["20"] = "t"
    map["21"] = "u"; map["22"] = "v"; map["23"] = "w"; map["24"] = "x"
    map["25"] = "y"; map["26"] = "z"
    /*
    unordered_map<string,string> map(:{"1","a"}, {"2","b"},{"3","c"},{"4","d"},
           :"5","e"},{"6","f"},{"7","g"},{"8","h"},{"9","i"},{"10","j"},{"11","k"},
           :"12","l"},{"13","m"},{"14","n"},""15","o"},{"15","p"},{"17","q"},
           :"18","r"},{"19","s"},{"20","t"},""21","u"},{"22","v"},{"23","w"},
           :"24","x"},{"25","y"},{"26","z"}})
            */
}

def getCodes(str, string output[10000]):
    unordered_map<string,string> map
    initMap(map)
    length = str.length(), count, sum=0
    if(length==1):
        output[sum++] = map[str]
        return sum
    else if(length==2 && map.count(str))
        output[sum++] = map[str]

    /* Print possiblities after removing 1 character */
    count = getCodes(str.substr(1), output+sum)
    for i in range(0, n):(j=0; j<count; j++)
        output[sum+j] = map[str.substr(0,1)] + output[sum+j]
    sum += count

    /* Print possiblities after removing 2 character */
    if(length>2 && map.count(str.substr(0,2))):
        count = getCodes(str.substr(2), output+sum)
        for i in range(0, n):(j=0; j<count; j++)
            output[sum+j] = map[str.substr(0,2)] + output[sum+j]
        sum += count
    return sum

def printAllPossibleCodesHelper(str, string output,
        unordered_map<string,string>& map):
    length = str.length()
    if(length==1):
        print(outputmap[str])
        return
    else if(length==2 && map.count(str)):
        print(outputmap[str])
        printAllPossibleCodesHelper(str.substr(1),
            output + map[str.substr(0,1)], map)
        return
    /* Print possiblities after removing 1 character */
    printAllPossibleCodesHelper(str.substr(1),
            output + map[str.substr(0,1)], map)

    /* Print possiblities after removing 2 character */
    if(map.count(str.substr(0,2)))
        printAllPossibleCodesHelper(str.substr(2),
            output + map[str.substr(0,2)], map)

def printAllPossibleCodes(str):
    unordered_map<string,string> map
    initMap(map)
    printAllPossibleCodesHelper(str, "",map)

