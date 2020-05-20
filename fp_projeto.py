UNIDADE = 2
PAREDE = 1
CORREDOR = 0
DIMENSAO_MINIMA = (3,3) # (colunas, linhas)

def eh_labirinto(def_labirinto):
  
  """ Esta funcao recebe um argumento de qualquer tipo e devolve True se o seu argumento corresponde a um labirinto e False caso contrario. """

  if not isinstance(def_labirinto, tuple):
    return False

  dim_horizontal = len(def_labirinto)
  
  # verifica se o labirinto tem linhas minimas = 3  
  if dim_horizontal < DIMENSAO_MINIMA[0]:
    return False
  
  # verifica se cada linha do labirinto e um tuplo
  # verifica se tem colunas minimas = 3
  # assumo o tamanho do primeiro tuplo do labirinto como o tamanho
  # da linha e verifico se ha algum diferente  
  for i in range(dim_horizontal):
    coluna = def_labirinto[i]

    if not isinstance(coluna, tuple):
      return False

    dim_vertical = len(coluna)
    if dim_vertical < DIMENSAO_MINIMA[1]:
      return False

    if dim_vertical != len(def_labirinto[0]):
      return False

    # primeira coluna parede?
    if i == 0:
      if coluna != (1,)*dim_vertical:
        return False
    # ultima coluna parede?
    elif i == dim_horizontal - 1:
      if coluna != (1,)*dim_vertical:
        return False
    else:
      # parede nos extremos?
      if coluna[0] != PAREDE or coluna[dim_vertical-1] != PAREDE:
        return False
      
    # e inteiro?
    for posicao in coluna:
      if not isinstance(posicao, int):
        return False
      # e diferente de 0 e 1 ?
      if posicao != PAREDE and posicao != CORREDOR:
        return False

  return True

def eh_posicao(posicao):
  
  """ Esta funcao recebe um argumento de qualquer tipo e devolve True se o seu argumento corresponde a uma posicao e False caso contrario. """

  # e tuplo?
  if not isinstance(posicao, tuple):
    return False
  
  #tem dimensao maior que 2?
  if len(posicao) != 2:
    return False

  (x, y) = posicao
  #x e y sao inteiros positivos?
  if not isinstance(x, int) or not isinstance(y, int) or x < 0 or y < 0:
    return False

  return True

def eh_conj_posicoes(posicoes):
  
  """ Esta funcao recebe um argumento de qualquer tipo e devolve True se o seu argumento corresponde a um conjunto de posicoes unicas e False caso contrario. """
  
  if not isinstance(posicoes, tuple):
    return False

  for i in range(len(posicoes)):
    posicao = posicoes[i]

    # e ponto valido?
    if not eh_posicao(posicao):
      return False
    # e repetido?
    for j in range(i+1, len(posicoes)):
      if posicao == posicoes[j]:
        return False

  return True

def tamanho_labirinto(labirinto):
  
  """ Esta funcao recebe um labirinto e devolve um tuplo de dois valores inteiros correspondendo o primeiro deles a dimensao Nx e o segundo a dimensao Ny do labirinto. """

  
  # e labirinto?
  if not eh_labirinto(labirinto):
    raise ValueError('tamanho_labirinto: argumento invalido')

  return (len(labirinto), len(labirinto[0]))

def eh_mapa_valido(labirinto, conj_posicoes):
  
  """ Esta funcao recebe um labirinto e um conjunto de posicoes correspondente as unidades presentes no labirinto, e devolve True se o segundo argumento corresponde a um conjunto de posicoes compativeis (nao ocupadas por paredes) dentro do labirinto e False caso contrario. """  
  
  if not eh_labirinto(labirinto):
    raise ValueError('eh_mapa_valido: algum dos argumentos e invalido')
  
  # e conjunto de posicoes?
  if not eh_conj_posicoes(conj_posicoes):
    raise ValueError('eh_mapa_valido: algum dos argumentos e invalido')

  (dim_horizontal, dim_vertical) = tamanho_labirinto(labirinto)

  for posicao in conj_posicoes:
    (x, y) = posicao
    # esta dentro do labirinto e e corredor?
    if x > dim_horizontal - 1 or y > dim_vertical - 1 or labirinto[x][y] == PAREDE:
      return False

  return True

def eh_posicao_livre(labirinto, conj_posicoes, posicao):
  
  """ Esta funcao recebe um labirinto, um conjunto de posicoes correspondente a unidades presentes no labirinto e uma posicao, e devolve True se a posicao corresponde a uma
posicao livre (nao ocupada nem por paredes, nem por unidades) dentro do labirinto e False caso contrario. """  
  
  try:
    # e mapa valido?
    if not eh_mapa_valido(labirinto, conj_posicoes):
      raise
    # e posicao?
    if not eh_posicao(posicao):
      raise

    (x, y) = posicao

    (dim_horizontal, dim_vertical) = tamanho_labirinto(labirinto)
    # esta dentro do labirinto?
    if x > dim_horizontal - 1 or y > dim_vertical - 1:
      raise
    # e uma posicao nao ocupada?
    return labirinto[x][y] == CORREDOR and posicao not in conj_posicoes
  except:
    raise ValueError('eh_posicao_livre: algum dos argumentos e invalido') from None

def posicoes_adjacentes(posicao):
  
  """ Esta funcao recebe uma posicao e devolve o conjunto de posicoes adjacentes da posicao em ordem de leitura de um labirinto. """    
  
  if not eh_posicao(posicao):
    raise ValueError('posicoes_adjacentes: argumento invalido')

  (x, y) = posicao

  up = (x, y - 1)
  left = (x - 1, y)
  down = (x, y + 1)
  right = (x + 1, y)

  # 0,0
  if x == 0 and y == 0:
    return (right, down)
  # primeira coluna
  elif x == 0:
    return (up, right, down)
  # primeira linha
  elif y == 0:
    return (left, right, down)

  return (up, left, right, down)

def mapa_str(labirinto, conj_posicoes):
  
  """ Esta funcao recebe um labirinto e um conjunto de posicoes correspondente as unidades presentes no labirinto e devolve a cadeia de caracteres que as representa (a representacao externa). """
  
  try:
    if not eh_mapa_valido(labirinto, conj_posicoes):
      raise

    resultado = ""

    (dim_horizontal, dim_vertical) = tamanho_labirinto(labirinto)

    labirinto_com_unidades = []

    # converter labirinto para lista
    for coluna in labirinto:
      labirinto_com_unidades.append(list(coluna))
    
    # escrever unidades do conj_posicoes
    for posicao_unidade in conj_posicoes:
      (x,y) = posicao_unidade

      labirinto_com_unidades[x][y] = UNIDADE

    for y in range(dim_vertical):
      for x in range(dim_horizontal):
        posicao = labirinto_com_unidades[x][y]

        if posicao == PAREDE:
          resultado += "#"
        elif posicao == CORREDOR:
          resultado += "."
        elif posicao == UNIDADE:
          resultado += "O"
      # evitar o \n no fim
      if y != dim_vertical - 1:
        resultado += "\n"

    return resultado
  except:
    raise ValueError('mapa_str: algum dos argumentos e invalido') from None

def obter_objetivos(labirinto, conj_posicoes, posicao_inicial):
  
  """ Esta funcao recebe um labirinto, um conjunto de posicoes correspondente as unidades presentes no labirinto e uma posicao correspondente a uma das unidades e devolve o conjunto de posicoes (em qualquer ordem) nao ocupadas dentro do labirinto correspondente a todos os possiveis objetivos da unidade correspondente a posicao dada. """  
  
  try:
    if not eh_mapa_valido(labirinto, conj_posicoes):
      raise 
    if not eh_conj_posicoes(conj_posicoes):
      raise 
    if posicao_inicial not in conj_posicoes or not eh_posicao(posicao_inicial):
      raise 

    (dim_horizontal, dim_vertical) = tamanho_labirinto(labirinto)

    resultado = ()

    for unidade in conj_posicoes:
      if unidade != posicao_inicial:
        pos_adjs = posicoes_adjacentes(unidade)
    
        for posicao_obj in pos_adjs:
          po = posicao_obj
          
          # e posicao livre e nao repetida?
          if eh_posicao_livre(labirinto,conj_posicoes,po) and po not in resultado:
            resultado = resultado + (po,)

    return resultado
  except:
    raise ValueError('obter_objetivos: algum dos argumentos e invalido')

def obter_caminho(labirinto, conj_posicoes, posicao_inicial):
  
  """ Esta funcao recebe um labirinto, um conjunto de posicoes correspondente as unidades presentes no labirinto, e uma posicao correspondente a uma das unidades, e devolve um conjunto de posicoes (potencialmente vazio caso nao exista nenhuma unidade alcancavel) correspondente ao caminho de numero minimo de passos desde a posicao dada ate a posicao objetivo (ou seja, a posicao mais proxima de acordo com a ordem de leitura do labirinto que se encontra ao numero minimo de passos)."""
  
  try:
    objectivos_possiveis = obter_objetivos(labirinto, conj_posicoes, posicao_inicial)

    posicoes_adjacentes_inicial = posicoes_adjacentes(posicao_inicial)
    
    # alguma adjacente das unidades e a unidade inicial? se sim, devolve as
    # proprias unidades
    for unidade in conj_posicoes:
      if posicao_inicial in posicoes_adjacentes(unidade):
        return (posicao_inicial,)
      
     # adjacente e uma das unidades? se sim, devolve a inicial e a unidade
     # que tb e posicao adjacente
    for posicao_adj in posicoes_adjacentes_inicial:
      if posicao_adj in conj_posicoes:
        return (posicao_inicial, posicao_adj)

    fila_exploracao = [posicao_inicial, []]
    posicoes_visitadas = []

    # fila de exploracao nao vazia?
    while fila_exploracao:
      # posicao atual e a primeira posicao
      posicao_atual = fila_exploracao.pop(0)
      # caminho atual tira a nova primeira posicao da fila
      caminho_atual = fila_exploracao.pop(0)

      # e visitada?
      if posicao_atual not in posicoes_visitadas:
        # se nao mete nas posicoes visitadas
        posicoes_visitadas.append(posicao_atual)

        # atualiza o caminho com a posicao atual
        caminho_atual = caminho_atual + [posicao_atual]

        # posicao atual e posicao objetivo? se sim,
        # retorna o caminho
        if posicao_atual in objectivos_possiveis:
          return tuple(caminho_atual)
        else:
          for posicao_adjacente in posicoes_adjacentes(posicao_atual):
            # para cada posicao adjacente, metemos na fila de exploracao
            # e nela metemos tambem o nosso caminho ate agora
            if eh_posicao_livre(labirinto, conj_posicoes, posicao_adjacente):
              fila_exploracao.append(posicao_adjacente)
              fila_exploracao.append(caminho_atual)

    return ()
  except:
    raise ValueError('obter_caminho: algum dos argumentos e invalido') from None

def mover_unidade(labirinto, conj_posicoes, posicao_inicial):
  
  """ Esta funcao recebe um labirinto, um conjunto de posicoes correspondente as unidades presentes no labirinto, e uma posicao correspondente a uma das unidades, e devolve o conjunto de posicoes actualizado correspondente as unidades presentes no labirinto apos a unidade dada ter realizado um unco movimento. """
  
  try:
    
    caminho_min = obter_caminho(labirinto, conj_posicoes, posicao_inicial)
    if len(caminho_min)<2:
      return conj_posicoes
    
    proxima_posicao = caminho_min[1]

    # se a proxima posicao e uma unidade
    # retorno a propria unidade
    if proxima_posicao in conj_posicoes:
      return conj_posicoes

    # passar para listar para mutar
    conj_posicoes_lst = list(conj_posicoes)

    # iterar as unidades
    for i in range(len(conj_posicoes_lst)):
      # se for a posicao inicial metemos na proxima posicao para mover
      if conj_posicoes_lst[i] == posicao_inicial:
        conj_posicoes_lst[i] = proxima_posicao

    return tuple(conj_posicoes_lst)
  except:
    raise ValueError('mover_unidade: algum dos argumentos e invalido') from None
