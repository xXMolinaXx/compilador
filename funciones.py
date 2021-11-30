import re


def getAllNumbers(matematicalOperationString):
    return re.findall(r'-?\d+\.?\d*', matematicalOperationString)


def isFloatorNot(array):
    floatList = []
    noFloatList = []
    for number in array:
        if bool(re.search('^[0-9]+.[0-9]+$', number)):
            floatList.append(number)
        else:
            noFloatList.append(number)
    return(floatList, noFloatList)


def getOperators(matematicalOperationString):
    return re.findall('[+-/*]', matematicalOperationString)


def detectParenthesis(matematicalOperationString):
    return bool(re.search('[()\[\]]', matematicalOperationString))

##divide la cadena en varios elementos, los elementos a los que divide son numeros operaciones aritmenticas y parentesis
def splitString(matematicalOperationString):
    arrayResult = []  # aqui se guarda toda la cadena partina por cada numero y cada operador segun el orden que se encontro
    stringConcat = ''
    for character in matematicalOperationString:
        if bool(re.search('[0-9.]', character)):
            stringConcat = stringConcat+character
        if bool(re.search('[\+\-\*\/\(\)]', character)):
            arrayResult.append(stringConcat)
            arrayResult.append(character)
            stringConcat = ''
    arrayResult.append(stringConcat)
    stringConcat = ''
    return arrayResult


def getParenthesisOperations(arrayString):
    operations = []
    result = []
    concatBool = False
    concatStringVar = ''
    i = 0
    for caracter in arrayString:
        if caracter == '(':
            concatBool = True
        if caracter == ')':
            concatBool = False
            concatStringVar = concatStringVar + caracter
            operations.append(concatStringVar)
            concatStringVar = ''
        if concatBool:
            concatStringVar = concatStringVar + caracter
        i = i+1
    for i in operations:
        result.append(eval(i))
    return(operations, result)

def createListPositionTokenElement (splitStringInput):
    position = []
    token = []
    element = []
    i = 1
    for el in splitStringInput:
        if el !='': 
            position.append(i)
            element.append(el)
            if bool(re.search('^[0-9]+.[0-9]+$', el)):
                token.append('decimal')
            if bool(re.search('^[0-9]+$', el)):
                token.append('entero') 
            if bool(re.search('[()\[\]]', el)):
                token.append('parentesis') 
            if bool(re.search('[\+\-\/\*]', el)):
                token.append('operador')
            i=i+1
    return (position,token,element)


