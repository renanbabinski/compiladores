from enum import Enum

class Token(Enum):
    # Key Words (Palavras Chave)
    KwStatements = 0
    KwAlgorithm = 1
    KwInteger = 2
    KwReal = 3
    KwAssign = 4
    KwTo = 5
    KwRead = 6
    KwPrint = 7
    KwIf = 8
    KwThen = 9
    KwWhile = 10
    KwBegin = 11
    KwEnd = 12

    # Operators (Operadores)
    OpAritMult = 13
    OpAritDiv = 14
    OpAritSum = 15 
    OpAritSub = 16
    OpRelSmaller = 17
    OpRelSmallerEqual = 18
    OpRelBigger = 19
    OpRelBiggerEqual = 20
    OpRelEqual = 21
    OpRelDiff = 22
    OpBoolAnd = 23
    OpBoolOr = 24

    # Characters
    Delim = 25
    OpenPar = 26
    ClosePar = 27
    Var = 28
    String = 29
    End = 30

    # Numbers
    NumInt = 31
    NumReal = 32



