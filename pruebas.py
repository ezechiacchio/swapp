def funcion():
    try:
        raise Exception("error1")
        raise ZeroDivisionError("error2")
    except Exception as e:
        print(e)


funcion()