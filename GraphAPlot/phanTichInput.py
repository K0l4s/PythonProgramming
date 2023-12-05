def chuanHoaHamSo(func):
    func = func.replace(" ", "")
    #Sec vaf csec
    func = func.replace("csc", "1/sin")
    func = func.replace("sec", "1/cos")
    
    #sin cos tan và cotg
    func = func.replace("sin", "np.sin")
    func = func.replace("cos", "np.cos")
    func = func.replace("tan", "np.tan")
    func = func.replace("cotg", "1/np.tan") 

    #căn bậc 2
    func = func.replace("sqrt", "np.sqrt")
    func = func.replace("√", "np.sqrt")
    #logarit
    func = func.replace("log2", "np.log2")
    func = func.replace("log10", "np.log10")
    func = func.replace("log", "np.log")

    #exp
    func = func.replace("exp", "np.exp")
    func = func.replace("e", "np.e")
    #pi
    func = func.replace("pi", "np.pi")
    #lũy thừa
    func = func.replace("^", "**")
    #arcsin, arccos, arctan
    func = func.replace("arcnp.sin", "np.arcsin")
    func = func.replace("arcnp.cos", "np.arccos")
    func = func.replace("arcnp.tan", "np.arctan")
    #arccotg
    func = func.replace("arc1/np.tan", "np.arctan(1/np.tan")
    
    if func.find("=") != -1:
        func = func.split("=")
        func = func[0] + "-(" + func[1] + ")"
    print(func)
    return func