# 95587 Gustavo Almeida Aguiar

# FUNCAO AUXILIAR QUE VERIFICA SE O ARGUMENTO E NATURAL

def verifica_intposzero(num):
    
    return type(num) == int and num >= 0

def verifica_intpos(num):
    return type(num) == int and num > 0


#----------------------------------------------------------------------------------------------#

#TAD POSICAO

# CONSTRUTOR DA TAD POSICAO

def cria_posicao(x,y):
    
    """ cria_posicao(x,y) recebe os valores correspondentes das coordenadas de uma
    posicao e devolve a posicao correspondente.
    
    cria_posicao: coordenadax x coordenaday -> posicao """
    
    if not verifica_intposzero(x) or not verifica_intposzero(y):
        raise ValueError('cria_posicao: argumentos invalidos')
    return (x,y)

def cria_copia_posicao(pos):
    
    """ cria_copia_posicao(pos) recebe uma posicao e devolve uma copia nova da posicao.
    
    cria_copia_posicao: posicao -> posicao """
        
    return cria_posicao(pos[0], pos[1])

# SELETORES DA TAD POSICAO

def obter_pos_x(pos):    
    
    """ obter_pos_x(pos) devolve a componente x da posicao p.
    
    obter_pos_x: posicao -> coordenada x da posicao"""
    
    return pos[0]

def obter_pos_y(pos):   
    
    """ obter_pos_y(pos) devolve a componente y da posicao p.
    
    obter_pos_y: posicao -> coordenada y da posicao """
    
    return pos[1]

# RECONHECEDOR DA TAD POSICAO

def eh_posicao(pos):
    
    """ eh_posicao(pos) devolve True caso o seu argumento seja um TAD posicao e
    False caso contrario. 
    
    eh_posicao: posicao -> booleano """
    
    # tem de ser tuplo, de comprimento 2, e o x e y tem de ser inteiros positivos com zero
    
    return type(pos) == tuple and len(pos) == 2 and verifica_intposzero(obter_pos_x(pos)) and verifica_intposzero(obter_pos_y(pos))

# TESTE DA TAD POSICAO

def posicoes_iguais(pos1,pos2):
    
    """ posicoes_iguais(pos1, pos2) devolve True apenas se p1 e p2 sao posicoes iguais. 
    
    posicoes_iguais: posicao1 x posicao2 -> booleano """
    
    # se os x forem diferentes sao diferentes
    if obter_pos_x(pos1) != obter_pos_x(pos2):
        return False
    # ou se os y forem diferentes sao diferentes
    elif obter_pos_y(pos1) != obter_pos_y(pos2):
        return False
    return True

# TRANSFORMADOR DA TAD POSICAO

def posicao_para_str(pos):
    
    """ posicao_para_str(p) devolve a cadeia de caracteres '(x, y)' que representa o
    seu argumento, sendo os valores x e y as coordenadas de p. 
    
    posicao_para_str: posicao -> string contendo a posicao """
    
    # se for posicao valida
    if eh_posicao(pos):
        # passar o x e y para str
        x = str(obter_pos_x(pos))
        y = str(obter_pos_y(pos))
        # juntar tudo numa string
        st = '' + '(' + x + ', ' + y + ')'
    return st

# FUNCOES DE ALTO NIVEL

def obter_posicoes_adjacentes(pos):
    
    """ obter_posicoes_adjacentes(p) devolve um tuplo com as posicoes adjacentes da posicao
    p de acordo com a ordem de leitura de um labirinto.
    
    obter_posicoes_adjacentes: posicao -> tuplo de posicoes """

    if obter_pos_x(pos) == 0 and obter_pos_y(pos) == 0:
        return (cria_posicao(obter_pos_x(pos)+1, obter_pos_y(pos)), cria_posicao(obter_pos_x(pos), obter_pos_y(pos)+1)) 
    elif obter_pos_x(pos) == 0:
        return (cria_posicao(obter_pos_x(pos), obter_pos_y(pos)-1), cria_posicao(obter_pos_x(pos)+1, obter_pos_y(pos)), cria_posicao(obter_pos_x(pos), obter_pos_y(pos)+1))
    elif obter_pos_y(pos) == 0: 
        return (cria_posicao(obter_pos_x(pos)-1, obter_pos_y(pos)), cria_posicao(obter_pos_x(pos)+1, obter_pos_y(pos)), cria_posicao(obter_pos_x(pos), obter_pos_y(pos)+1))
    return (cria_posicao(obter_pos_x(pos), obter_pos_y(pos)-1), cria_posicao(obter_pos_x(pos)-1, obter_pos_y(pos)), \
                 cria_posicao(obter_pos_x(pos)+1, obter_pos_y(pos)), cria_posicao(obter_pos_x(pos), obter_pos_y(pos)+1))


#----------------------------------------------------------------------------------------------#

#TAD UNIDADE

# CONSTRUTOR DA TAD UNIDADE

def cria_unidade(pos, v, f, st):
    
    """ cria_unidade(p, v, f, str) recebe uma posicao p, dois valores inteiros maiores
    que 0 correspondentes a vida e forca da unidade, e uma cadeia de caracteres
    nao vazia correspondente ao exercito da unidade; e devolve a unidade correspondente. 
    
    cria_unidade: posicao x vida x forca x exercito -> unidade """
    
    try:
        # verifica se eh posicao valida
        if not eh_posicao(pos):
            raise
        # verifica se a vida eh um numero inteiro e se eh positivo
        if type(v) != int or not v > 0:
            raise
        # verifica se a forca eh um numero inteiro e se eh maior que zero
        if type(f) != int or not f > 0:
            raise
        # verifica se eh string ou se eh vazia
        if type(st) != str or len(st) == 0:
            raise
        unidade = {'posicao': pos, 'vida': v, 'forca': f, 'exercito': st} 
        return unidade
    except:
        raise ValueError('cria_unidade: argumentos invalidos')
        

# SELETORES DA TAD UNIDADE

def cria_copia_unidade(unidade):
    
    """ cria_copia_unidade(u) recebe uma unidade u e devolve uma nova copia da
    unidade. 
    
    cria_copia_unidade: unidade -> unidade """
    
    nova_unidade = {}
    
    nova_unidade['posicao'] = cria_copia_posicao(unidade['posicao'])
    nova_unidade['vida'] = obter_vida(unidade)
    nova_unidade['forca'] = obter_forca(unidade)
    nova_unidade['exercito'] = obter_exercito(unidade)
                                                 
    
    return nova_unidade

def obter_posicao(unidade):
    
    """ obter_posicao(u) devolve a posicao da unidade u. 
    
    obter_posicao: unidade -> posicao da unidade"""
    
    return unidade['posicao']

def obter_vida(unidade):
    
    """ obter_vida(u) devolve o valor corresponde aos pontos de vida da unidade. 
    
    obter_vida: unidade -> numero inteiro correspondente ah vida da unidade """
    
    return unidade['vida']

def obter_forca(unidade):
    
    """ obter_forca(u) devolve o valor corresponde a forca de ataque da unidade. 
    
    obter_forca: unidade -> numero inteiro correspondente ah forca da unidade"""
    
    return unidade['forca']

def obter_exercito(unidade):
    
    """ obter_exercito(u) devolve a cadeia de carateres correspondente ao exercito da
    unidade. 
    
    obter_exercito: unidade -> string do exercito"""
    
    return unidade['exercito']

# MODIFICADORES DA TAD UNIDADE

def muda_posicao(u, p):
    
    """ muda_posicao(u, p) modifica destrutivamente a unidade u alterando a sua
    posicao com o novo valor p, e devolve a propria unidade. 
    
    muda_posicao: unidade x posicao -> unidade """
    
    # mudo a posicao da unidade para a posicao dada
    u['posicao'] = p  
    return u

def remove_vida(u, v):
    
    """ remove_vida(u, v) modifica destrutivamente a unidade u alterando os seus
    pontos de vida subtraindo o valor v, e devolve a propria unidade. 
    
    remove_vida: unidade x inteiro -> unidade """
    
    # tiro ah vida da unidade o valor v
    u['vida'] = (obter_vida(u) - v)    
    return u

# RECONHECEDOR DA TAD UNIDADE

def eh_unidade(u):
    
    """ eh_unidade(arg) devolve True caso o seu argumento seja um TAD unidade e
    False caso contrario. 
    
    eh_unidade: unidade -> booleano """  
    
    # verificacao geral da unidade
    if type(u) != dict or len(u) != 4:
        return False
    # verificacao das chaves
    if 'posicao' not in u:
        return False  
    if 'vida' not in u:
        return False
    if 'forca' not in u:
        return False
    if 'exercito' not in u:
        return False
    # verificar se eh posicao
    if not eh_posicao(obter_posicao(u)):
        return False
    # verificar se vida e forca sao maiores que zero
    if not verifica_intpos(obter_vida(u)) or not verifica_intpos(obter_forca(u)):
        return False
    # verificacao de string com dimensao maior que zero
    if type(obter_exercito(u)) != str or len(obter_exercito(u)) == 0:
        return False
    return True
        

# TESTE DA TAD UNIDADE

def unidades_iguais(u1,u2):
    
    """ unidades_iguais(u1, u2) devolve True apenas se u1 e u2 sao unidades iguais. 
    
    unidades_iguais: unidade1 x unidade2 -> booleano """
    
    # Verifica posicao
    if obter_posicao(u1) != obter_posicao(u2):
        return False
    
    #Verifica vida
    if obter_vida(u1) != obter_vida(u2):
        return False
    
    #Verifica forca
    if obter_forca(u1) != obter_forca(u2):
        return False
    
    #Verifica unidades exercito 2
    if obter_exercito(u1) != obter_exercito(u2):
        return False
    
    return True    
    

# TRANSFORMADORES DA TAD UNIDADE

def unidade_para_char(u):
    
    """ unidade_para_char(u) devolve a cadeia de caracteres dum unico elemento,
    correspondente ao primeiro caracter em maiuscula do exercito da unidade
    passada por argumento. 
    
    unidade_para_char: unidade -> string do primeiro carater do exercito em CAPS"""
    
    return obter_exercito(u)[0].capitalize()

def unidade_para_str(u):
    
    """ unidade_para_str(u) devolve a cadeia de caracteres que representa a unidade
    na forma 'char(upper(exercito))[vida, forca]@(posicao)' 
    
    unidade_para_str: unidade -> string da unidade """
    
    posicao_str = posicao_para_str(obter_posicao(u))    
    vida_str = str(obter_vida(u))
    forca_str = str(obter_forca(u))
    exercito_str = unidade_para_char(u)
    st = '' + exercito_str + '[' + vida_str + ', ' + forca_str + ']' + '@' + posicao_str
    return st

# FUNCOES DE ALTO NIVEL DA TAD UNIDADE

def unidade_ataca(u1,u2): 
    
    """ unidade_ataca(u1, u2) modifica destrutivamente a unidade u2 retirando o valor de
    pontos de vida correspondente a forca de ataque da unidade u1. A funcao devolve
    True se a unidade u2 for destruida ou False caso contrario. 
    
    unidade_ataca: unidade1 x unidade 2 -> booleano """
    
    # remove a vida
    remove_vida(u2, obter_forca(u1))
    
    return obter_vida(u2) <= 0


def ordenar_unidades(t_u):
    
    """ ordenar_unidades(t) devolve um tuplo contendo as mesmas unidades do tuplo
    fornecido como argumento, ordenadas de acordo com a ordem de leitura do labirinto. 
    
    ordenar_unidades: tuplo de unidades -> tuplo de unidades ordenado por ordem de leitura do labirinto"""
    
    return tuple(sorted(t_u, key=lambda x: [obter_pos_y(obter_posicao(x)), obter_pos_x(obter_posicao(x))]))


#----------------------------------------------------------------------------------------------#

# TAD MAPA 

# CONSTRUTOR DO TAD MAPA

def cria_mapa(d, w, e1, e2):
    
    """ cria_mapa(d, w, e1, e2) recebe um tuplo d de 2 valores inteiros correspondentes
    as dimensoes Nx e Ny do labirinto seguindo as restricoes do 1 projecto,
    um tuplo w de 0 ou mais posicoes correspondentes as paredes que nao sao
    dos limites exteriores do labirinto, um tuplo e1 de 1 ou mais unidades do
    mesmo exercito, e um tuplo e2 de um ou mais unidades de um outro exercito;
    e devolve o mapa que representa internamente o labirinto e as unidades presentes.
    O construtor verifica a validade dos seus argumentos, gerando um
    ValueError com a mensagem 'cria mapa: argumentos invalidos' caso
    os seus argumentos nao sejam validos. 
    
    cria_mapa: dimensao x paredes_internas x exercito1 x exercito2 -> mapa"""
    
    try:
        
        mapa = {'dimensao': d, 'posicoes': w, 'exercito1': e1, 'exercito2': e2}
        
        # verificacao de dimensao
        if type(mapa['dimensao']) != tuple:
            raise
        if len(mapa['dimensao']) != 2:
            raise
        dimensao = cria_posicao(obter_pos_x(mapa['dimensao']), obter_pos_y(mapa['dimensao']))
        (nx, ny) = (obter_pos_x(dimensao), obter_pos_y(dimensao))
        if nx < 3 or ny < 3:
            raise
    
        # verificacao de cada posicao nas posicoes
        if type(mapa['posicoes']) != tuple:
            raise
        for posicao in mapa['posicoes']:
            (x,y) = (obter_pos_x(posicao), obter_pos_y(posicao))
            if not verifica_intposzero(x) or not verifica_intposzero(y):     
                raise
            else: 
                if x == 0 or y == 0 or x >= nx -1 or y >= ny - 1:       
                    raise
        
        # verificacao do exercito1
        if type(mapa['exercito1']) != tuple:
            raise
        if len(mapa['exercito1']) == 0:
            raise
        for i in range(len(mapa['exercito1'])):
            unidade = mapa['exercito1'][i]
            for j in range(i+1, len(mapa['exercito1'])):
                next_unidades = mapa['exercito1'][j]
                if unidade['exercito'] != next_unidades['exercito']:
                    raise
        
        # verificacao do exercito2
        if type(mapa['exercito2']) != tuple:
            raise
        if len(mapa['exercito2']) == 0:
            raise
        for i in range(len(mapa['exercito2'])):
            unidade = mapa['exercito2'][i]
            for j in range(i+1, len(mapa['exercito2'])):
                next_unidades = mapa['exercito2'][j]
                if unidade['exercito'] != next_unidades['exercito']:
                    raise        
    except:
        raise ValueError('cria_mapa: argumentos invalidos')
    
    return mapa

def cria_copia_mapa(mapa):
    
    novo_mapa = {}
    
    # copiar a dimensao do mapa
    novo_mapa['dimensao'] = cria_copia_posicao(mapa['dimensao'])
    # inicializacao das paredes internas
    novo_mapa['posicoes'] = ()
    # percorrer cada parede interna e juntar ahs posicoes
    for posicao in mapa['posicoes']:
        novo_mapa['posicoes'] = novo_mapa['posicoes'] + (cria_copia_posicao(posicao),)
    # inicializacao dos exercitos
    novo_mapa['exercito1'] = ()
    novo_mapa['exercito2'] = ()
    # percorrer cada exercito e copiar cada unidade e juntar aos exercitos
    for unidade1 in mapa['exercito1']:
        novo_mapa['exercito1'] = novo_mapa['exercito1'] + (cria_copia_unidade(unidade1),)
    for unidade2 in mapa['exercito2']:
        novo_mapa['exercito2'] = novo_mapa['exercito2'] + (cria_copia_unidade(unidade2),)
    # devolve o novo mapa
    return novo_mapa

# SELETORES DO TAD MAPA

def obter_tamanho(mapa):
    
    """ obter_tamanho(mapa) devolve um tuplo de dois valores inteiros correspondendo
    o primeiro deles a dimensao Nx e o segundo a dimensao Ny do mapa. 
    
    obter_tamanho: mapa -> tuplo"""
    
    return mapa['dimensao']

def obter_nome_exercitos(mapa):
    
    """ obter_nome_exercitos(mapa) devolve um tuplo ordenado com duas cadeias de
    caracteres correspondendo aos nomes dos exercitos do mapa.
    
    obter_nome_exercitos: mapa -> tuplo de exercitos """
    
    # se nao houverem unidades no exercito 1 apenas
    if len(mapa['exercito1']) == 0 and len(mapa['exercito2']) > 0:
        # devolvo o nome da primeira unidade do exercito 2
        return obter_exercito(mapa['exercito2'][0])
    # se nao houverem unidades no exercito 2 apenas
    elif len(mapa['exercito2']) == 0 and len(mapa['exercito1']) > 0:
        # devolvo o nome da primeira unidade do exercito 1
        return obter_exercito(mapa['exercito1'][0])
    # caso hajam unidades em ambos
    else:
        # criar tuplo com os dois exercitos
        nome_exercitos = (obter_exercito(mapa['exercito1'][0]), obter_exercito(mapa['exercito2'][0]))
        # devolver o tuplo com os dois exercitos por ordem alfabetica
        return tuple(sorted(nome_exercitos))

def obter_unidades_exercito(mapa, exercito):
    
    """ obter_unidades_exercito(mapa, exercito) devolve um tuplo contendo as 
    unidades do mapa pertencentes ao exercito indicado pela cadeia de caracteres 
    e, ordenadas em ordem de leitura do labirinto. 
    
    obter_unidades_exercito: mapa x exercito -> tuplo de unidades"""
    
    # inicializacao do resultado
    resultado = ()
    # juntar todas as unidades de cada exercito
    exercitos = mapa['exercito1'] + mapa['exercito2']
    # se ao percorrer cada unidade dessa juncao
    for unidade in exercitos:
        # o exercito dado for igual ao exercito da unidade a ser verificada
        if exercito == obter_exercito(unidade) :
            # meto no resultado
            resultado = resultado + (unidade,)
    # devolvo o resultado ordenado em ordem de leitura do labirinto
    return ordenar_unidades(resultado)

def obter_todas_unidades(mapa):
    
    """ obter todas unidades(m) devolve um tuplo contendo todas as unidades do
    mapa, ordenadas em ordem de leitura do labirinto. 
    
    obter_todas_unidades: mapa -> tuplo de unidades """
    
    # juntar todas as unidades de cada exercito
    exercitos = mapa['exercito1'] + mapa['exercito2']
    # ordenar a juncao em ordem de leitura do labirinto
    return ordenar_unidades(exercitos)

def obter_unidade(mapa, posicao):
    
    """ obter unidade(m, p) devolve a unidade do mapa que se encontra na posicao p. 
    
    obter_unidade: mapa x posicao -> unidade"""
    
    # se ao percorrer todas as unidades do mapa
    for unidade in obter_todas_unidades(mapa):
        # a posicao dada for igual ah posicao da unidade a ser verificada
        if posicao == obter_posicao(unidade):
            # retorna a propria unidade
            return unidade
            
        

# MODIFICADORES DO TAD MAPA
 
def eliminar_unidade(mapa, unidade): 
    
    """ eliminar unidade(mapa, unidade) modifica destrutivamente o mapa m \
    eliminando a unidade u do mapa e deixando livre a posicao onde se encontrava\
    a unidade. Devolve o proprio mapa.
    
    eliminar_unidade: mapa x unidade -> mapa """
    
    # passar para lista para poder mutar
    exercito1 = list(mapa['exercito1'])
    exercito2 = list(mapa['exercito2'])
    
    # se a unidade estiver no exercito 1
    if unidade in exercito1:
        # remove a unidade
        exercito1.remove(unidade)
    # se a unidade estiver no exercito 2
    elif unidade in exercito2:
        # remove a unidade
        exercito2.remove(unidade)
    
    # passar para tuplos de novo
    mapa['exercito1'] = tuple(exercito1)
    mapa['exercito2'] = tuple(exercito2)
    
    return mapa
    
def mover_unidade(mapa, unidade, posicao):
    
    """ mover unidade(mapa, unidade, posicao) modifica destrutivamente o mapa m \
    e a unidade u alterando a posicao da unidade no mapa para a nova posicao p \
    e deixando livre a posicao onde se encontrava. Devolve o proprio mapa. 
    
    mover_uniade: mapa x unidade x posicao -> mapa"""
    
    # percorrer cada unidade do mapa
    for unit in obter_todas_unidades(mapa):
        # se a unidade que queremos mudar posicao la estiver contida
        if unit == unidade:
            # muda a sua posicao
            muda_posicao(unidade, posicao)
            
    return mapa
           
    
# RECONHECEDORES DO TAP MAPA

def eh_posicao_unidade(mapa, posicao):
    
    """ eh posicao unidade(m, p) devolve True apenas no caso da posicao p do mapa
    estar ocupada por uma unidade. """
    
    # percorre todas as unidades do mapa e ve se a posicao eh igual ah posicao \
    # de cada unidade
    for unidade in obter_todas_unidades(mapa):
        if posicao == obter_posicao(unidade):
            return True
        
    return False

def eh_posicao_corredor(mapa, posicao):
    
    """ eh posicao corredor(m, p) devolve True apenas no caso da posicao p do mapa
    corresponder a um corredor no labirinto (independentemente de estar ou nao
    ocupado por uma unidade). """
    
    # verifica se eh posicao valida, se nao eh parede e se esta dentro do mapa
    if eh_posicao(posicao):
        if posicao in mapa['posicoes']:
            return False
        if obter_pos_x(posicao) == 0 or obter_pos_y(posicao) == 0:
            return False
        if obter_pos_x(posicao) >= ( obter_pos_x(obter_tamanho(mapa)) - 1 ) or \
           obter_pos_y(posicao) >= ( obter_pos_y(obter_tamanho(mapa)) - 1 ):
            return False
    return True
        

def eh_posicao_parede(mapa, posicao):
    
    """ eh posicao parede(m, p) devolve True apenas no caso da posicao p do mapa
    corresponder a uma parede do labirinto. """
    
    # verifica se eh posicao valida e se eh uma parede
    if eh_posicao(posicao):
        if posicao in mapa['posicoes']:
            return True
        elif obter_pos_x(posicao) == 0 or obter_pos_x(posicao) == ( obter_pos_x(obter_tamanho(mapa)) -1 ):
            return True
        elif obter_pos_y(posicao) == 0 or obter_pos_y(posicao) == ( obter_pos_y(obter_tamanho(mapa)) - 1 ):
            return True
    return False

# TESTE DO TAD MAPA

def mapas_iguais(m1, m2):
    
    """ mapas_iguais(m1, m2) devolve True apenas se m1 e m2 forem mapas iguais. 
    
    mapas_iguais: mapa x mapa -> booleano """
    
    # Verifica dimensao
    if obter_tamanho(m1) != obter_tamanho(m2):
        return False
    
    #Verifica posicoes
    for posicao in m1['posicoes']:
        if posicao not in m2['posicoes']:
            return False
    
    #Verifica unidades exercito 1
    for unidade1 in m1['exercito1']:
        if unidade1 not in m2['exercito1']:
            return False
    
    #Verifica unidades exercito 2
    for unidade2 in m1['exercito2']:
        if unidade2 not in m2['exercito2']:
            return False
    
    return True
    

# TRANSFORMADOR DO TAD MAPA

def mapa_para_str(mapa):
    
    """ mapa_para_str(mapa) devolve uma cadeia de caracteres que representa o mapa
    como descrito no primeiro projeto, neste caso, com as unidades representadas
    pela sua representacao externa. 
    
    mapa_para_str: mapa -> string do mapa"""
    
    # inicializacao do mapa e variaveis nx e ny do mapa
    mapa_string = ''
    nx = obter_pos_x(obter_tamanho(mapa))
    ny = obter_pos_y(obter_tamanho(mapa))
    
    # percorrer o mapa
    for y in range(ny):
        for x in range(nx):
            posicao = (x, y)
            # se for parede, eh um #
            if eh_posicao_parede(mapa, posicao):
                mapa_string = mapa_string + '#'
            # se for unidade, eh o primeiro caracter maiusculo do exercito
            elif eh_posicao_unidade(mapa, posicao):
                mapa_string = mapa_string + unidade_para_char(obter_unidade(mapa, posicao))
            # se nao for nenhum dos acima, eh corredor .
            else:
                mapa_string = mapa_string + '.'
        # evitar um \n no fim
        if y != (ny - 1):
            mapa_string = mapa_string + '\n'
    return mapa_string

# FUNCOES DE ALTO NIVEL DO TAD MAPA

def obter_inimigos_adjacentes(mapa, unidade):
    
    """ obter_inimigos_adjacentes(mapa, unidade) devolve um tuplo contendo as \
    unidades inimigas adjacentes a unidade u de acordo com a ordem de leitura \
    do labirinto. 
    
    obter_inimigos_adjacentes: mapa x unidade -> tuplo de unidades"""
    
    # extrair posicoes adjacentes ah posicao da unidade
    adjacentes = obter_posicoes_adjacentes(obter_posicao(unidade))
    # extrair exercito da unidade
    exercito = obter_exercito(unidade)
    # extrair todas as unidades do mapa
    unidades = obter_todas_unidades(mapa)
    # inicializacao dos inimigos
    inimigos = ()
    
    # se ao percorrer cada unidade 
    for unidade in unidades:
        if obter_exercito(unidade) != exercito:
            if obter_posicao(unidade) in adjacentes:
                inimigos = inimigos + (obter_unidade(mapa, obter_posicao(unidade)),)
                
    return ordenar_unidades(inimigos)
                
                    
            

def obter_movimento(mapa, unit):
    '''
    A funcao obter_movimento devolve a posicao seguinte da unidade argumento
    de acordo com as regras de movimento das unidades no labirinto.

    obter_movimento: mapa x unidade -> posicao
    '''

    ######################
    # Funcoes auxiliares #
    ######################
    def pos_to_tuple(pos):
        return obter_pos_x(pos), obter_pos_y(pos)

    def tuple_to_pos(tup):
        return cria_posicao(tup[0], tup[1])

    def tira_repetidos(tup_posicoes):
        conj_tuplos = set(tuple(map(pos_to_tuple, tup_posicoes)))
        return tuple(map(tuple_to_pos, conj_tuplos))

    def obter_objetivos(source):
        enemy_side = tuple(filter(lambda u: u != obter_exercito(source), obter_nome_exercitos(mapa)))[0]
        target_units = obter_unidades_exercito(mapa, enemy_side)
        tup_com_repetidos = \
            tuple(adj
                  for other_unit in target_units
                  for adj in obter_posicoes_adjacentes(obter_posicao(other_unit))
                  if eh_posicao_corredor(mapa, adj) and not eh_posicao_unidade(mapa, adj))
        return tira_repetidos(tup_com_repetidos)

    def backtrack(target):
        result = ()
        while target is not None:
            result = (target,) + result
            target, _ = visited[target]
        return result

    ####################
    # Funcao principal #
    ####################
    # Nao mexer se ja esta' adjacente a inimigo
    if obter_inimigos_adjacentes(mapa, unit):
        return obter_posicao(unit)

    visited = {}
    # posicao a explorar, posicao anterior e distancia
    to_explore = [(pos_to_tuple(obter_posicao(unit)), None, 0)]
    # registro do numero de passos minimo ate primeira posicao objetivo
    min_dist = None
    # estrutura que guarda todas as posicoes objetivo a igual minima distancia
    min_dist_targets = []

    targets = tuple(pos_to_tuple(obj) for obj in obter_objetivos(unit))

    while to_explore:  # enquanto nao esteja vazio
        pos, previous, dist = to_explore.pop(0)

        if pos not in visited:  # posicao foi ja explorada?
            visited[pos] = (previous, dist)  # registro no conjunto de exploracao
            if pos in targets:  # se a posicao atual eh uma dos objetivos
                # se eh primeiro objetivo  ou se esta a  distancia minima
                if min_dist is None or dist == min_dist:
                    # acrescentor 'a lista de posicoes minimas
                    min_dist = dist
                    min_dist_targets.append(pos)
            else:  # nao 'e objetivo, acrescento adjacentes
                for adj in obter_posicoes_adjacentes(tuple_to_pos(pos)):
                    if eh_posicao_corredor(mapa, adj) and not eh_posicao_unidade(mapa, adj):
                        to_explore.append((pos_to_tuple(adj), pos, dist + 1))

        # Parar se estou a visitar posicoes mais distantes que o minimo,
        # ou se ja encontrei todos os objetivos
        if (min_dist is not None and dist > min_dist) or len(min_dist_targets) == len(targets):
            break

    # se encontrei pelo menos uma posicao objetivo, 
    # escolhe a de ordem de leitura menor e devolve o primeiro movimento
    if len(min_dist_targets) > 0:
        # primeiro dos objetivos em ordem de leitura
        tar = sorted(min_dist_targets, key=lambda x: (x[1], x[0]))[0]
        path = backtrack(tar)
        return tuple_to_pos(path[1])

    # Caso nenhuma posicao seja alcancavel
    return obter_posicao(unit)


# FUNCOES ADICIONAIS


def calcula_pontos(mapa, exercito):
    
    """ Funcao auxiliar que recebe um mapa e uma cadeia de caracteres correspondente ao nome
    de um dos exercitos do mapa e devolve a sua pontuacao. A pontuacao dum exercito eh
    o total dos pontos de vida de todas as unidades do exercito. 
    
    calcula_pontos: mapa x exercito -> pontuacao """
    
    # inicializacao da soma
    pontuacao = 0
    
    # caso existam unidades do exercito que queremos ver a pontuacao
    if obter_unidades_exercito(mapa, exercito) != ():
        # percorremos cada unidade
        for unidade in obter_unidades_exercito(mapa, exercito):
            # e acrescentamos ah nossa soma a sua vida
            pontuacao += obter_vida(unidade)
    return pontuacao


def simula_turno(mapa):
    
    """ Funcao auxiliar que modica o mapa fornecido como argumento de acordo com\
    a simulacao de um turno de batalha completo, e devolve o proprio mapa.
    
    simula_turno: mapa -> mapa """
    
    # percorrer cada unidade
    for unidade in obter_todas_unidades(mapa):
        if obter_vida(unidade) > 0 and len(mapa['exercito1']) > 0 and len(mapa['exercito2']) > 0:
            # se ainda tiver vida a unidade move-se de acordo com o obter_movimento
            mapa = mover_unidade(mapa, unidade, obter_movimento(mapa, unidade))
            # extrair os inimigos que estao adjacentes ah unidade
            inimigos = obter_inimigos_adjacentes(mapa, unidade)
            # se exisitirem inimigos
            if len(inimigos) > 0:
                # atacam a unidade e se ela ficar com vida nula ou negativa
                if unidade_ataca(unidade, inimigos[0]):
                    # eliminam a unidade
                    eliminar_unidade(mapa, inimigos[0])
    return mapa

def simula_batalha(setup, modo):
    
    """ Funcao principal que permite simular uma batalha completa. A batalha \
    termina quando um dos exercitos vence ou, se apos completar um turno de \
    batalha, nao ocorreu nenhuma alteracao ao mapa e ahs unidades. 
    
    simula_batalha: str x booleano -> str """
    
    
    # EXTRAIR DADOS DO FICHEIRO
    
    config = open(setup, 'r')
    dimensao = eval(config.readline())
    exercito_1 = eval(config.readline())
    e1 = exercito_1[0]
    vida_e1 = exercito_1[1]
    forca_e1 = exercito_1[2]
    exercito_2 = eval(config.readline())
    e2 = exercito_2[0]
    vida_e2 = exercito_2[1]
    forca_e2 = exercito_2[2]    
    posicoes = eval(config.readline())
    pos_e1 = eval(config.readline())
    pos_e2 = eval(config.readline())
    config.close()
    
    # INICIALIZACAO DOS EXERCITOS
    
    exercito1  = ()
    exercito2 = ()
    for posicao1 in pos_e1:
        exercito1 += (cria_unidade(posicao1, vida_e1, forca_e1, e1),)
                         
    for posicao2 in pos_e2:
        exercito2 += (cria_unidade(posicao2, vida_e2, forca_e2, e2),)
        
    # INICIALIZACAO DO MAPA
    
    mapa = cria_mapa(dimensao, posicoes, exercito1, exercito2)
    
    # ALGORITMO DO SIMULA BATALHA
    
    # ordenacao alfabetica dos exercitos
    exercitos = obter_nome_exercitos(mapa)
    exercito_1 = exercitos[0]
    exercito_2 = exercitos[1]    
    
    print(mapa_para_str(mapa))
    print('[ '+ exercito_1 + ':' + str(calcula_pontos(mapa, exercito_1)) + ' ' + exercito_2 + ':' + str(calcula_pontos(mapa, exercito_2)) + ' ]')
    
    # enquanto a pontuacao dos dois exercitos for positiva
    while calcula_pontos(mapa, exercito_1) > 0 and calcula_pontos(mapa, exercito_2) > 0:
        # se for modo verboso
        if modo:
            # guardar uma copia do mapa antes de um turno
            mapa_antes = cria_copia_mapa(mapa)
            # atualizar o mapa apos um turno
            mapa = simula_turno(mapa)
            # caso sejam iguais antes e depois do turno quebra o ciclo
            if mapas_iguais(mapa_antes, mapa):
                break
            # ir mostrando o mapa apos cada turno e as pontuacoes
            print(mapa_para_str(mapa))
            print('[ '+ exercito_1 + ':' + str(calcula_pontos(mapa, exercito_1)) + ' ' + exercito_2 + ':' + str(calcula_pontos(mapa, exercito_2)) + ' ]')
        # se for modo quiet
        if not modo:
            # guardar uma copia do mapa antes de um turno
            mapa_antes = cria_copia_mapa(mapa)
            # atualizar o mapa apos um turno
            mapa = simula_turno(mapa)
            # se forem iguais quebra o ciclo
            if mapas_iguais(mapa_antes, mapa):
                break
    # se for modo quiet mostra o mapa final e as pontuacoes finais
    if not modo:
        print(mapa_para_str(mapa))
        print('[ '+ exercito_1 + ':' + str(calcula_pontos(mapa, exercito_1)) + ' ' + exercito_2 + ':' + str(calcula_pontos(mapa, exercito_2)) + ' ]')
    
    # determinacao do resultado consoante a pontuacao de cada exercito
    if calcula_pontos(mapa, exercito_1) > 0 and calcula_pontos(mapa, exercito_2) > 0:
        return 'EMPATE'
    elif calcula_pontos(mapa, exercito_1) <= 0:
        return exercito_2
    else:
        return exercito_1

###########################################
# TAD posicao                             #
# Operacoes basicas                       #
###########################################



from random import randint

def cria_posicao(x, y):
    if type(x) == int and type(y) == int and x >= 0 and y >= 0:
        return [ {'px':x, 'py':y}, 'strange', 'pos', randint(0, 10**6)]
    raise ValueError('cria_posicao: argumentos invalidos')


def cria_copia_posicao(pos):
    return [{'px':pos[0]['px'], 'py':pos[0]['py']}, 'strange', 'pos', randint(0, 10**6)]
   

def obter_pos_x(pos):
    return pos[0]['px']


def obter_pos_y(pos):
    return pos[0]['py']


def eh_posicao(pos):
    return isinstance(pos, list) and len(pos) == 4 and \
           type(pos[0]) == dict and len(pos[0]) == 2 and \
           'px' in pos[0] and 'py' in pos[0] and \
           type(pos[0]['px']) == int and pos[0]['px'] >= 0 and \
           type(pos[0]['py']) == int and pos[0]['py'] >= 0 and \
           pos[1] == 'strange' and pos[2] == 'pos' and isinstance(pos[3], int)


def posicoes_iguais(pos1, pos2):
    return obter_pos_x(pos1) == obter_pos_x(pos2) and \
           obter_pos_y(pos1) == obter_pos_y(pos2)


def posicao_para_str(pos):
    return str((obter_pos_x(pos), obter_pos_y(pos)))

###########################################
# TAD posicao                             #
# Funcoes de alto nivel                   #
###########################################

def obter_posicoes_adjacentes(pos):
    return tuple((cria_posicao(adj[0], adj[1])
                  for adj in ((obter_pos_x(pos)+dx, obter_pos_y(pos)+dy)
                              for dx, dy in ((0, -1), (-1, 0), (1, 0), (0, 1)))
                  if (adj[0] >= 0 and adj[1] >= 0)))
###########################################
# TAD unidade                             #
# Operacoes basicas                       #
###########################################

class UnidadeXYZ:
    def __init__(self, pos, life, power, side):
        self.xyz = [pos, life, power]
        self.xyz_side = ('error', side) 


def cria_unidade(pos, life, power, side):
    if eh_posicao(pos) and \
            type(life) == int and life > 0 and \
            type(power) == int and power > 0 and \
            isinstance(side, str) and len(side) >= 1:
        return UnidadeXYZ(pos, life, power, side)

    raise ValueError('cria_unidade: argumentos invalidos')


def cria_copia_unidade(unit):
    return UnidadeXYZ(cria_copia_posicao(unit.xyz[0]), unit.xyz[1], unit.xyz[2], unit.xyz_side[1])


def obter_posicao(unit):
    return unit.xyz[0]


def obter_exercito(unit):
    return unit.xyz_side[1]


def obter_forca(unit):
    return unit.xyz[2]


def obter_vida(unit):
    return unit.xyz[1]


def muda_posicao(unit, posicao):
    unit.xyz[0] = posicao
    return unit


def remove_vida(unit, damage):
    unit.xyz[1] = max(0, unit.xyz[1] - damage)
    return unit


def eh_unidade(unit):
    return isinstance(unit, UnidadeXYZ)


def unidades_iguais(unit1, unit2):
    return unit1.xyz[1] == unit2.xyz[1] and \
           unit1.xyz[2] == unit2.xyz[2] and \
           unit1.xyz_side[1] == unit2.xyz_side[1] and \
           posicoes_iguais(unit1.xyz[0], unit2.xyz[0])


def unidade_para_char(unit):
    return unit.xyz_side[1].upper()[0]


def unidade_para_str(unit):
    return '{}[{}, {}]@{}'.format(unidade_para_char(unit),
                                  obter_vida(unit), obter_forca(unit),
                                  posicao_para_str(obter_posicao(unit)))

###########################################
# TAD unidade                             #
# Funcoes de alto nivel                   #
###########################################

def unidade_ataca(unit1, unit2):
    hp = obter_forca(unit1)
    remove_vida(unit2, hp)
    return not obter_vida(unit2) > 0


def ordenar_unidades(tuplo):
    return tuple(sorted(tuplo, key=lambda u: (obter_pos_y(obter_posicao(u)), obter_pos_x(obter_posicao(u)))))



from random import randint

################################################################################
# TAD mapa: operacoes basicas
################################################################################
def cria_mapa(dim, walls, exerc1, exerc2):
    def is_int_ge(num, limit):
        return type(num) is int and num >= limit

    def in_mapa(dim_x, dim_y, pos):
        return obter_pos_x(pos)>0 and obter_pos_x(pos)<(dim_x-1) and \
           obter_pos_y(pos)>0 and obter_pos_y(pos)<(dim_y-1)


    if not (type(dim) is tuple and len(dim) == 2 and \
            is_int_ge(dim[0], 3) and is_int_ge(dim[1], 3) and \
            type(walls) is tuple and all(eh_posicao(p) and in_mapa(*dim,p) for p in walls) and \
            type(exerc1) is tuple and len(exerc1) > 0 and all(eh_unidade(u) for u in exerc1) and \
            type(exerc2) is tuple and len(exerc2) > 0 and all(eh_unidade(u) for u in exerc2)):
        raise ValueError('cria_mapa: argumentos invalidos')
    if obter_exercito(exerc2[0]) < obter_exercito(exerc1[0]):
        exerc1, exerc2 = exerc2, exerc1
    # Exemplo de uma representacao improvavel
    return ['blabla', dim, walls, (obter_exercito(exerc1[0]), obter_exercito(exerc2[0])), \
            exerc1, exerc2, 'bliblibli', randint(0, 10**6)]

def cria_copia_mapa(mapa):
    return ['blabla', mapa[1], tuple(cria_copia_posicao(pos) for pos in mapa[2]), mapa[3], \
            tuple(cria_copia_unidade(unid) for unid in mapa[4]), \
            tuple(cria_copia_unidade(unid) for unid in mapa[5]), 'bliblibli', randint(0, 10**6)]

def obter_tamanho(mapa):
    return mapa[1]

def obter_nome_exercitos(mapa):
    return mapa[3]

def obter_unidades_exercito(mapa, exercito):
    i = 4 if mapa[3][0] == exercito else 5
    return [] if not mapa[i] else ordenar_unidades(mapa[i])

def obter_todas_unidades(mapa):
    return ordenar_unidades(mapa[4] + mapa[5])

def obter_unidade(mapa, pos):
    return [unid for unid in obter_todas_unidades(mapa) if posicoes_iguais(pos, obter_posicao(unid))][0]

def eliminar_unidade(mapa, unid):
    i = 4 if unid in mapa[4] else 5
    mapa[i] = tuple(u for u in mapa[i] if not unidades_iguais(unid, u))
    return mapa

def mover_unidade(mapa, unid, pos):
    i = 4 if unid in mapa[4] else 5
    eliminar_unidade(mapa, unid)
    mapa[i] += (muda_posicao(unid, pos),)
    return mapa

def eh_posicao_unidade(mapa, pos):
    return any(posicoes_iguais(pos, obter_posicao(u)) for u in mapa[4]) or \
           any(posicoes_iguais(pos, obter_posicao(u)) for u in mapa[5])

def eh_posicao_parede(mapa, pos):
    return any(posicoes_iguais(pos, p) for p in mapa[2]) or \
           obter_pos_x(pos)==0 or obter_pos_x(pos)==(obter_tamanho(mapa)[0]-1) or \
           obter_pos_y(pos)==0 or obter_pos_y(pos)==(obter_tamanho(mapa)[1]-1)

def eh_posicao_corredor(mapa, pos):
    return not eh_posicao_parede(mapa, pos)

def mapas_iguais(mapa1, mapa2):
    def ordenar_posicoes(conj_pos):
        return sorted(conj_pos, key=lambda x: (obter_pos_y(x), obter_pos_x(x)))

    return obter_tamanho(mapa1) == obter_tamanho(mapa2) and \
           len(mapa1[2]) == len(mapa2[2]) and \
           all(posicoes_iguais(p1, p2)  for p1, p2 in zip(ordenar_posicoes(mapa1[2]), ordenar_posicoes(mapa2[2]))) and \
           len(obter_todas_unidades(mapa1)) == len(obter_todas_unidades(mapa2)) and \
           all(unidades_iguais(u1, u2)  for u1, u2 in zip(obter_todas_unidades(mapa1), obter_todas_unidades(mapa2)))
           

def mapa_para_str(mapa):
    sMapa = ''
    max_x, max_y = obter_tamanho(mapa)
    for y in range(max_y):
        for x in range(max_x):
            p = cria_posicao(x, y)
            if    eh_posicao_parede(mapa, p):  sMapa += '#'
            elif  eh_posicao_unidade(mapa, p): sMapa += unidade_para_char(obter_unidade(mapa, p))
            else: sMapa += '.'
        sMapa += '\n'
    return sMapa.rstrip()

##########################################
# TAD mapa - Funcoes movimento           #
#            alto nivel                  #
##########################################
def obter_inimigos_adjacentes(mapa, unit):
    '''
    A funcao obter_inimigos_adjacentes devolve um tuplo contendo as unidades
    inimigas adjacentes da unidade argumento em ordem de leitura do labirinto.

    obter_inimigos_adjacentes: mapa x unidade -> tuplo
    '''
    enemy_side = tuple(filter(lambda u: u != obter_exercito(unit), obter_nome_exercitos(mapa)))[0]
    return ordenar_unidades(tuple(obter_unidade(mapa, pos)
                                  for pos in obter_posicoes_adjacentes(obter_posicao(unit))
                                  if eh_posicao_unidade(mapa, pos)
                                  and obter_exercito(obter_unidade(mapa, pos)) == enemy_side))


def obter_movimento(mapa, unit):
    '''
    A funcao obter_movimento devolve a posicao seguinte da unidade argumento
    de acordo com as regras de movimento das unidades no labirinto.

    obter_movimento: mapa x unidade -> posicao
    '''

    ######################
    # Funcoes auxiliares #
    ######################
    def pos_to_tuple(pos):
        return obter_pos_x(pos), obter_pos_y(pos)

    def tuple_to_pos(tup):
        return cria_posicao(tup[0], tup[1])

    def tira_repetidos(tup_posicoes):
        conj_tuplos = set(tuple(map(pos_to_tuple, tup_posicoes)))
        return tuple(map(tuple_to_pos, conj_tuplos))

    def obter_objetivos(source):
        enemy_side = tuple(filter(lambda u: u != obter_exercito(source), obter_nome_exercitos(mapa)))[0]
        target_units = obter_unidades_exercito(mapa, enemy_side)
        tup_com_repetidos = \
            tuple(adj
                  for other_unit in target_units
                  for adj in obter_posicoes_adjacentes(obter_posicao(other_unit))
                  if eh_posicao_corredor(mapa, adj) and not eh_posicao_unidade(mapa, adj))
        return tira_repetidos(tup_com_repetidos)

    def backtrack(target):
        result = ()
        while target is not None:
            result = (target,) + result
            target, _ = visited[target]
        return result

    ####################
    # Funcao principal #
    ####################
    # Nao mexer se ja esta' adjacente a inimigo
    if obter_inimigos_adjacentes(mapa, unit):
        return obter_posicao(unit)

    visited = {}
    # posicao a explorar, posicao anterior e distancia
    to_explore = [(pos_to_tuple(obter_posicao(unit)), None, 0)]
    # registro do numero de passos minimo ate primeira posicao objetivo
    min_dist = None
    # estrutura que guarda todas as posicoes objetivo a igual minima distancia
    min_dist_targets = []

    targets = tuple(pos_to_tuple(obj) for obj in obter_objetivos(unit))

    while to_explore:  # enquanto nao esteja vazio
        pos, previous, dist = to_explore.pop(0)

        if pos not in visited:  # posicao foi ja explorada?
            visited[pos] = (previous, dist)  # registro no conjunto de exploracao
            if pos in targets:  # se a posicao atual eh uma dos objetivos
                # se eh primeiro objetivo  ou se esta a  distancia minima
                if min_dist is None or dist == min_dist:
                    # acrescentor 'a lista de posicoes minimas
                    min_dist = dist
                    min_dist_targets.append(pos)
            else:  # nao 'e objetivo, acrescento adjacentes
                for adj in obter_posicoes_adjacentes(tuple_to_pos(pos)):
                    if eh_posicao_corredor(mapa, adj) and not eh_posicao_unidade(mapa, adj):
                        to_explore.append((pos_to_tuple(adj), pos, dist + 1))

        # Parar se estou a visitar posicoes mais distantes que o minimo,
        # ou se ja encontrei todos os objetivos
        if (min_dist is not None and dist > min_dist) or len(min_dist_targets) == len(targets):
            break

    # se encontrei pelo menos uma posicao objetivo,
    # escolhe a de ordem de leitura menor e devolve o primeiro movimento
    if len(min_dist_targets) > 0:
        # primeiro dos objetivos em ordem de leitura
        tar = sorted(min_dist_targets, key=lambda x: (x[1], x[0]))[0]
        path = backtrack(tar)
        return tuple_to_pos(path[1])

    # Caso nenhuma posicao seja alcancavel
    return obter_posicao(unit)
###########################################
# Funcoes adicionais                      #
#                                         #
###########################################


def calcula_pontos(mapa, side):
    return sum(obter_vida(unit) for unit in obter_unidades_exercito(mapa, side))

###########################################
# Funcoes adicionais                      #
#                                         #
###########################################

def simula_turno(mapa):
    for pos in map(lambda u: obter_posicao(u), obter_todas_unidades(mapa)):
        if eh_posicao_unidade(mapa, pos):
            unit = obter_unidade(mapa, pos)
            # mover
            next_pos = obter_movimento(mapa, unit)
            mover_unidade(mapa, unit, next_pos)

            # atacar
            inimigos = obter_inimigos_adjacentes(mapa, unit)
            if inimigos:
                if unidade_ataca(unit, inimigos[0]):
                    eliminar_unidade(mapa, inimigos[0])

    return mapa
# ########################################################
# ################################################# TESTES

points = 0


############################### Redirect stdout ### BEGIN
import sys
class ListStream:
    def __init__(self):
        self.data = []
    def write(self, s):
        self.data.append(s)
    def flush(self):
        pass

############################### Redirect stdout ### END

############################### Handler to treat maxout stdout ### BEGIN
import signal
def handler(signum, frame):
    print ("Time is over!")
    raise Exception("end of time")

signal.signal(signal.SIGALRM, handler)
############################### Handler to treat maxout stdout ### END


try:
    signal.alarm(1)
    sys.stdout = x = ListStream()
    side = simula_batalha('input1_fp1920.txt', True)
    sys.stdout = sys.__stdout__
    res = ''.join(x.data)
    expected = '#######\n\
#E..R.#\n\
#...#.#\n\
#RR.#R#\n\
#######\n\
[ empire:30 rebellion:40 ]\n\
#######\n\
#..R..#\n\
#ER.#.#\n\
#R..#R#\n\
#######\n\
[ empire:26 rebellion:36 ]\n\
#######\n\
#.R...#\n\
#ER.#.#\n\
#R..#R#\n\
#######\n\
[ empire:22 rebellion:32 ]\n\
#######\n\
#R....#\n\
#ER.#.#\n\
#R..#R#\n\
#######\n\
[ empire:16 rebellion:28 ]\n\
#######\n\
#R....#\n\
#ER.#.#\n\
#R..#R#\n\
#######\n\
[ empire:10 rebellion:24 ]\n\
#######\n\
#.....#\n\
#ER.#R#\n\
#R..#.#\n\
#######\n\
[ empire:4 rebellion:22 ]\n\
#######\n\
#....R#\n\
#.R.#.#\n\
#R..#.#\n\
#######\n\
[ empire:0 rebellion:18 ]\n'

    if(res==expected and side == 'rebellion'):
        print('SIM_BATALHA Teste 1 --> OK')
        points += 1
    else:
        print('SIM_BATALHA Teste 1 --> FAIL')
except:
    sys.stdout = sys.__stdout__
    print('SIM_BATALHA Teste 1 --> FAIL')

############################### Redirect stdout ### END
try:
    signal.alarm(1)
    sys.stdout = x = ListStream()
    side = simula_batalha('input1_fp1920.txt', False)
    sys.stdout = sys.__stdout__
    res = ''.join(x.data)
    expected = '#######\n\
#E..R.#\n\
#...#.#\n\
#RR.#R#\n\
#######\n\
[ empire:30 rebellion:40 ]\n\
#######\n\
#....R#\n\
#.R.#.#\n\
#R..#.#\n\
#######\n\
[ empire:0 rebellion:18 ]\n'

    if(res==expected and side == 'rebellion'):
        print('SIM_BATALHA Teste 2 --> OK')
        points += 1
    else:
        print('SIM_BATALHA Teste 2 --> FAIL')
except:
    sys.stdout = sys.__stdout__
    print('SIM_BATALHA Teste 2 --> FAIL')


############################### Redirect stdout ### END
try:
    signal.alarm(1)
    sys.stdout = x = ListStream()
    side = simula_batalha('private_test_config6.txt', False)
    sys.stdout = sys.__stdout__
    res = ''.join(x.data)

    expected = '######\n\
#..G.#\n\
#E...#\n\
###G.#\n\
#GE#.#\n\
######\n\
[ elfos:40 goblins:60 ]\n\
######\n\
#....#\n\
#G...#\n\
###..#\n\
#.E#.#\n\
######\n\
[ elfos:10 goblins:4 ]\n'

    if(res==expected and side == 'EMPATE'):
        print('SIM_BATALHA Teste 3 --> OK')
        points += 1
    else:
        print('SIM_BATALHA Teste 3 --> FAIL')
except:
    sys.stdout = sys.__stdout__
    print('SIM_BATALHA Teste 3 --> FAIL')



val = 0.5
percent = points/3
print ('SIM_BATALHA GLOBAL --> {:2.1f} %'.format(100*percent), '({:.3f} val)'.format(val*percent))

signal.alarm(0)

