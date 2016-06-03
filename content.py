def contentManagement():

    namesexercices = ["Balanceo","Braceo","Cambios de Sentido","Cruce al Frente","Cuarta Fase - Patineta"]
    namesexercices += ["Desplazamiento hacia atras","El Angel","Empuje Lateral","Frenado en T","La Garza"]
    namesexercices += ["Primera Fase - Familiarizarse","Salto con Patines","Segunda Fase - Elevacion de Rodillas"]
    namesexercices += ["Slalom","Tercera Fase - Caminar","Trenzado","Zig Zag con Balon","salto el aro"]
    namesexercices += ["carrito en curva","caida adelante y atras","zig zag pies juntos", "globos","posicion inicial", "posicion inicial" ,"carro"]
    exercices ={}
    levelsd = {}
    calentamientod = {}
    for i in namesexercices:
        #exercices[str(i)]=unicode((open("static/data/"+i+".txt", "r",).read(), 'utf-8'))
        exercices[str(i)]=(open("static/data/exercices/"+i+".txt", "r",).read()).replace("\n"," ")
    #print(exercices)
    
    levels = ["1", "2", "3", "4", "5", "6"]
    for i in levels:
        #exercices[str(i)]=unicode((open("static/data/"+i+".txt", "r",).read(), 'utf-8'))
        levelsd[str(i)]=(open("static/data/levels/Level"+i+".txt", "r",).read()).replace("\n"," ")
    #print(exercices)
    
    calentamiento = [1,2,3,4,5,6,7,8,9] 
    for i in calentamiento:
        #exercices[str(i)]=unicode((open("static/data/"+i+".txt", "r",).read(), 'utf-8'))
        calentamientod[str(i)]=(open("static/data/calentamiento/"+str(i)+".txt", "r",).read()).replace("\n"," ")
    #print(exercices)
    

    
    return levelsd,exercices,calentamientod
