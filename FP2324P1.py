#2.1.1
def eh_territorio(arg):
    """Esta função indica se um argumento é território

    Args:
        arg [(tuple)]: [tuplo que contem todo o território]

    Returns:
        [Bool]: [True or False, True se é território, False caso contrário]
    """    

    #Verifica arg como tuplo ou não e se pertence de A a Z (através do ASCII)
    if isinstance(arg, tuple) and 0 < len(arg) <= 26:
        comfirmação = 0 
        valor_montanhas = True

        #Avalia todos os elementros de arg se são tuplos de tamanhos de 0 a
        for horizontais in arg:                   
            if not isinstance(horizontais, tuple) or 0 > len(horizontais) or \
                len(horizontais) >= 100 :
                return False
            
            #Define tamanho padrao para caminhos horizontais
            tamanho_padrao = len(arg[0])
            if isinstance(horizontais, tuple) and len(horizontais) \
                == tamanho_padrao:
                comfirmação += 1

            #Verifica se intersecoes são montanhas (1) ou livres (0)
            for montanhas in horizontais:
                if montanhas not in (0, 1) or not type(montanhas) == int:
                    valor_montanhas = False

        #Reune todos os argumentos e comfirma
        return comfirmação == len(arg) and valor_montanhas 
    
    return False

#2.1.2
def obtem_ultima_intersecao(t):
    """Tem a função de, dando um território como argumento, obter a interseção 
    mais distante, sendo a ultima

    Args:
        t [(tuple)]: [tuplo que contem o território]

    Returns:
        [tuple]: [interseção como ultima na forma, como exemplo, ("A", 1)]
    """    
    letra = chr(64 + len(t)) #obtem a ultima letra das interseções usando ASCII
    numero = len(t[0]) #obtem o ultimo numero das interceções

    return (letra, numero)

#2.1.3
def eh_intersecao(arg):
    """Verifica se um argumento está no formato de interseção

    Args:
        arg ([tuplo]): [tuplo no formato, em exemplo, ("A", 1)]

    Returns:
        [bool]: [True or False, com True como sendo interseção, False caso contrário]
    """
    intersecao_possivel = True
    #Certefica-se que o a interseção tem apenas uma letra, de A a Z,
        #e a seguir um numero de 0 a 99, returnando falso ao nao cumprir com os
            # requesitos
    if not isinstance(arg,tuple) or len(arg) != 2 or not isinstance(arg[0],str)\
        or len(arg[0]) != 1 or 65 > ord(arg[0]) or 90 < ord(arg[0]) or not \
         isinstance(arg[1], int) or 1 > arg[1] or 99 < arg[1]:
        intersecao_possivel = False

    return intersecao_possivel

#2.1.4
def eh_intersecao_valida(t, i):
    """Verifica se uma interseção é valida no território dado

    Args:
        t ([tuple]): [tuplo que contem todo o território]
        i ([tuple]): [tuplo que contem a interseção na forma, como exemplo, ("A", 1)]

    Returns:
        [bool]: [True or False, sendo True uma interseção valida no território]
    """    
    #Passa valor de letra de A a Z para valor numérico correspondente (1 a 26)
    #Verifica os elementos dentro de elementos 
    return eh_intersecao(i) and (0 < (ord(i[0]) - 64) \
        and (ord(i[0]) - 64) <= len(t)) and (0 < i[1] and i[1] <= len(t[0]))

#2.1.5
def eh_intersecao_livre(t, i):
    """Verifica se uma interseção não tem montanha

    Args:
        t ([tuple]): [tuplo que contem o território]
        i ([tuple]): [tuplo que contem a interseção, por exemplo, ("A", 1)]

    Returns:
        [bool]: [True or False, com True sendo interceção livre]
    """    
    x = (ord(i[0]) - 65) #Define a coordenada horizontal a verificar
    y = i[1] - 1         #Define a coordenada vertical a verificar

    return t[x][y] == 0  #Verifica se é livre (0) ou não

#2.1.6
def obtem_intersecoes_adjacentes(t, i):
    """Cria todas as interceções adjacentes de uma interseção

    Args:
        t ([tuple]): [tuplo que contem o território]
        i ([tuple]): [tuplo que contem a intercesão, por exemplo, ("B", 2)]

    Returns:
        [tuple]: [conjunto de interceções adjacentes de uma interceção, por 
        exemplo, (("A", 2), ("B", 1), ("B", 3), ("C", 2))]
    """    
    tamanho_horizontal = len(t) #Vê o tamanho horizontal máximo
    tamanho_vertical = len(t[0]) #Vê o tamanho vertical máximo

    adjacentes = ()

    #Baixo
    if 1 < i[1]:
        adjacentes += ((i[0], i[1] - 1), )

    #Esquerda
    if 1 < (ord(i[0]) - 64):
        adjacentes += ((chr(ord(i[0]) - 1), i[1]), )
    
    #Direita
    if (ord(i[0]) - 64) < tamanho_horizontal:
        adjacentes += ((chr(ord(i[0]) + 1), i[1]), )

    #Cima
    if i[1] < tamanho_vertical:
        adjacentes += ((i[0], i[1] + 1), )

    return adjacentes

#2.1.7
def ordena_intersecoes(tup):
    """Ordena os tuplos dentro de um Tuplo por linhas verticais e depois horizontais

    Args:
        tup ([tuple]): [tuplo com conjunto de tuplos de interseções
        , por exemplo, (("A", 1), ("B", 3), ("C", 2))]

    Returns:
        [tuple]: [tuplo ordenado com interceções na forma, por exemplo, 
        (("A", 1), ("C", 2), ("B", 3))]
    """    
    ordenado = tuple(sorted(tup)) #Organiza o tuplo por letras e numeros 
    #primeiro, caso esteja misturado

    if not ordenado:
        return ()

    #Verifica o maior número de caminhos verticais com o tuplo já organizado
    max_numero = max(e[-1] for e in tup) 
    ordem_leitura = () #Cria um tuplo para a ordem como leitura correta

    #Percorre todos os tuplos cujo os números sejam i (por ordem) e verifica se
    #é igual a I
    for i in range(0, max_numero + 1): 
        for e in ordenado:
            if e[1] == i:
                ordem_leitura += (e, )

    return ordem_leitura

#2.1.8
def territorio_para_str(t):
    """Cria uma representação gráfica do território

    Args:
        t ([tuple]): [tuplo que contem o território]

    Raises:
        ValueError: [caso não seja um território]

    Returns:
        [str]: [representação gráfica do território]
    """    
    if not eh_territorio(t):
        raise ValueError('territorio_para_str: argumento invalido') 

    visualizacao = '  '

    #Define o tamanho do território através do tamanho horizontal e vertical
    len_horizontal, len_vertical = len(t), len(t[0])

    #Adiciona as letras em cima da visualização
    for letra in range(len_horizontal): 
        visualizacao += ' ' + chr(65 + letra)
    
    #Adiciona os espaços, sendo "." caso diferente de 1 e "X" se igual a 1
    i = len_vertical - 1
    while 0 <= i:

        #Adiciona números na lateral esquerda, corrigindo o espaçamento dos numeros
        if i < 9:
            visualizacao += '\n ' + f'{i + 1}'
        else:
            visualizacao += '\n' + f'{i + 1}'

        #Ciclo para adição dos espaços, fazendo por sequencia de elementos 
        # dos tuplos do tuplo t
        for e in range(len_horizontal):
            if t[e][i] == 0:
                visualizacao += ' ' + '.'
            else:
                visualizacao += ' ' + 'X'
        
        #Adiciona números na lateral direita, 
        # utilização de if para correção do espaçamento dos numeros
        if i < 9:
            visualizacao += '  ' + f'{i + 1}'
        else:
            visualizacao += ' ' + f'{i + 1}'
        i -= 1

    #Adiciona as letras em baixo da visualização
    visualizacao += '\n  ' #Segue a str para baixo
    for letra in range(len_horizontal):
        visualizacao += ' ' + chr(65 + letra)

    return visualizacao

#2.2.1
def obtem_cadeia(t, i):
    """Obtem cadeias de montanhas para uma dada interseção

    Args:
        t ([tuple]): [tuplo que contem o território]
        i ([tuple]): [tuplo com interseção a obter cadeida, por exemplo, ("A", 2)]

    Raises:
        ValueError: [caso não seja território, um interseção ou interseção válida]

    Returns:
        [tuple]: [conjunto de tuplos que contem as interseções das cadeias]
    """    
    #função recursiva que obtem todos os adjacentes dos adjacentes e remove os 
    # já vistos, gerando a cadeia
    def obtem_cadeia_nrepetidos(atual, jádentro):
        jádentro.add(atual)
        cadeia_prov = obtem_intersecoes_adjacentes(t, atual)
        cadeia = (atual,)
            #Adiciona há "cadeia" todas as interseções que são equivalentes ao 
            # tipo de interseção inicial
        for e in cadeia_prov:
            if e not in jádentro and eh_intersecao_livre(t, atual) == \
             eh_intersecao_livre(t, e):
                cadeia += obtem_cadeia_nrepetidos(e, jádentro)
        
        return cadeia

    #Avalia se o tipo de interseção e território são válidos
    if not eh_territorio(t) or not eh_intersecao_valida(t, i):
        raise ValueError('obtem_cadeia: argumentos invalidos')
    
    #Chama a função privada criada para obter a cadeia
    return ordena_intersecoes(obtem_cadeia_nrepetidos(i, set()))

#2.2.2
def obtem_vale(t, i):
    """Obtem todos os vales ao redor de uma cadeia

    Args:
        t ([tuple]): [tuplo que contem o território]
        i ([tuple]): [tuplo que contem uma interseção de uma cadeia ou nao]

    Raises:
        ValueError: [caso nao seja território valido ou interseção valida]

    Returns:
        [tuple]: [tuplo que contem todas as interseções que sejam vales]
    """    
    #Avalia os tipos de variáveis introduzidas e se são válidas
    if not eh_territorio(t) or not eh_intersecao_valida(t, i) or \
        eh_intersecao_livre(t, i):
        raise ValueError("obtem_vale: argumentos invalidos")
    
    #obtem o conjunto de montanhas que forma a cadeia
    conjunto_montanhas = obtem_cadeia(t, i)
    vales = ()
    
    #Avalia as interseções adjacentes em cada montanha da cadeia e verifica se 
    # é livre e se já não foi vista
    for cada in conjunto_montanhas:
        poss_vales = obtem_intersecoes_adjacentes(t, cada)
        for e in poss_vales:
            if eh_intersecao_livre(t, e) == True and e not in vales:
                vales += (e, )

    return ordena_intersecoes(vales)

#2.3.1
def verifica_conexao(t,i1,i2):
    """Verifica a conecxão entre duas montanhas

    Args:
        t ([tuple]): [tuplo que contem todo o território]
        i1 ([tuple]): [tuplo da primeira interseção a verificar]
        i2 ([tuple]): [tuplo da segunda interseção a verificar]

    Raises:
        ValueError: [caso nao seja territorio valido ou i1, i2 interceções validas]

    Returns:
        [bool]: [True or False, sendo true montanhas conectadas]
    """    
    #Verifica o tipo de argumentos introduzido e se são válidos
    if not eh_territorio(t) or not eh_intersecao_valida(t, i1) \
        or not eh_intersecao_valida(t, i2):
        raise ValueError('verifica_conexao: argumentos invalidos')
    
    #Procura a cadeia formada pela interseção i1
    conexao_i1 = obtem_cadeia(t, i1)

    #Verifica se a interseção i2 está contida na cadeia i1, caso não, obtem o 
    # valor da conexao como False, caso contrário, obtem True
    conexao = False
    if i2 in conexao_i1:
        conexao = True

    return conexao

#Função que calcula todas as interseções possiveis
def total_interseção(t):
    """Função que calcula todas as interceções possiveis no território t

    Raises:
        ValueError: [caso não seja um território válido]

    Returns:
        [tuple]: [tuplo que contem todas as interseções]
    """    
    #Verifica se o argumento t introduzido é território
    if not eh_territorio(t):
        raise ValueError("calcula_numero_montanhas: argumento invalido")
    
    #Define variáveis
    tamanho_horizontal = len(t)
    tamanho_vertical = len(t[0])
    conjunto_de_coordenadas_total = ()

    #Vai criar um conjunto de interseções que existe no território
    for Hn in range(tamanho_horizontal):
        for Hv in range(1, tamanho_vertical + 1):
            conjunto_de_coordenadas_total += ((chr(65 + Hn), Hv), )

    return conjunto_de_coordenadas_total

#2.3.2
def calcula_numero_montanhas(t):
    """Calcula o número de montanhas que existe no território t

    Args:
        t ([tuple]): [tuplo que contem o território]

    Raises:
        ValueError: [caso t não seja território valido]

    Returns:
        [int]: [número de montanhas existentes no território]
    """    
    #Verifica argumentos
    if not eh_territorio(t):
        raise ValueError("calcula_numero_montanhas: argumento invalido")

    #Cria conjunto de todas as interseções e contador de montanhas
    conjunto_de_coordenadas_total = total_interseção(t)
    n_montanhas = 0
        
    for e in conjunto_de_coordenadas_total:
        if not eh_intersecao_livre(t, e):
            n_montanhas += 1

    return n_montanhas

#2.3.3
def calcula_numero_cadeias_montanhas(t):
    """Calcula o numero de cadeias de montanhas existentes no território

    Args:
        t ([tuple]): [tuplo que contem o território]

    Raises:
        ValueError: [caso t não seja território valido]

    Returns:
        [int]: [número de cadeias de montanhas existentes no território]
    """    
    #Verifica os argumentos introduzidos
    if not eh_territorio(t):
        raise ValueError("calcula_numero_cadeias_montanhas: argumento invalido")
    
    #Calcula todas as montanhas existente no território
    montanhas = ()
    total = total_interseção(t)
    for e in total:
        if not eh_intersecao_livre(t, e):
            montanhas += (e, )

    #Calcula o numero de cadeias existentes, utilizando a função obtem_cadeia
    #com todas as montanhas
    cadeias_vistas = ()
    numero = 0
    for e in montanhas:
        if e not in cadeias_vistas and obtem_cadeia(t, e):
            cadeias_vistas += obtem_cadeia(t, e)
            numero += 1

    return numero

#2.3.4
def calcula_tamanho_vales(t):
    """Calcula o numero de vales no território

    Args:
        t ([tuple]): [tuplo que contem o território]

    Raises:
        ValueError: [caso t não seja um território válido]

    Returns:
        [int]: [numero de vales total no território]
    """    
    #Verifica os argumentos introduzidos t como território
    if not eh_territorio(t):
        raise ValueError('calcula_tamanho_vales: argumento invalido')
    
    #Calcula todas as montanhas existentes e cria um tuplo com o conjunto
    montanhas = ()
    total = total_interseção(t)
    for e in total:
        if not eh_intersecao_livre(t, e):
            montanhas += (e, )

    #Calcula todas as cadeias e montanhas sozinhas e cria um tuplo
    cadeias = ()
    numero = 0  
    for e in montanhas:
        if montanhas not in cadeias and not eh_intersecao_livre(t, e):
            cadeias += (e, )

    #Calcula o numero de vales produzido por cadeias e montanhas sozinhas
    #através das adjacentes
    vales = ()
    numero_vales = 0
    for e in cadeias:
        adjacentes_prov = obtem_intersecoes_adjacentes(t, e)
        for v in adjacentes_prov:
            if v not in vales and eh_intersecao_livre(t, v):
                vales += (v, )
                numero_vales += 1

    return numero_vales