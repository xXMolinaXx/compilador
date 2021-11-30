import funciones
answerResult = {
    "integer": [],
    "decimal": [],
    "operators": [],
    "parenthesis": False,
    "answer": 0,
}
positionTokenElement = []
matematicalOperationString = input('por favor ingrese una operacion matematica ejemplo: 2*3(5/2)\n')
try:
    splittedString = funciones.splitString(matematicalOperationString)
    # funciones de analizador lexico
    allnumbers = funciones.getAllNumbers(matematicalOperationString)
    (answerResult["decimal"], answerResult['integer']) = funciones.isFloatorNot(allnumbers)
    answerResult['operators'] = set(funciones.getOperators(matematicalOperationString))
    answerResult['parenthesis'] = funciones.detectParenthesis(matematicalOperationString)
    # funciones analizador sintactico
    (position,Token,Element)=funciones.createListPositionTokenElement(splittedString)
    positionTokenElement.append(position)
    positionTokenElement.append(Token)
    positionTokenElement.append(Element)
    # funciones analizador sintactico
    answerResult['answer'] = eval(matematicalOperationString)
    print(' resultados => ',answerResult,' posicion, tipo de token, valor => ',positionTokenElement)
    ##resolviendo las operaciones en parenthesis
    (arrayOperationParenthesis, answer) = funciones.getParenthesisOperations(splittedString)
    for i in range(len(arrayOperationParenthesis)):
        matematicalOperationString = matematicalOperationString.replace(arrayOperationParenthesis[i],str(answer[i]))
    


except:
    if  positionTokenElement[2][0] == '*' or positionTokenElement[2][0] == '/':
        print('la cadena no de debe de empezar con los operadores / *')
    for el in positionTokenElement[0]:
            if positionTokenElement[1][el-1] == 'operador' :
                if positionTokenElement[1][el] == 'operador' :
                    print('no deben de haber dos operadores seguidos error en la posicion', el)
            if positionTokenElement[1][el-1] == 'parentesis' :
                if positionTokenElement[1][el-2] != 'operador' or positionTokenElement[1][el] != 'operador'  :
                    print('antes o despues de los parentesis debe de haber un operador, error en la posicion ', el)
