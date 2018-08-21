import csv
import networkx as nx

#Criar um dicionário para cada atributo

nome_rotulo_vertice = {}
cnpj_prestador = {}
tipo_sequencial = {}
sequencial = {}
uf = {}
sigla_partido = {}
numero_candidato = {}
cargo_candidato = {}
nome_candidato = {}
cpf_candidato = {}
cpf_cnpj_doador = {}
nome_doador_receita = {}

#TODO mapear nome do rotulo

###############################################

nos_partidos = []
arestas_partidos = []

with open("/home/akina/Dropbox/TCC/Dados/receitas_partidos.csv", "r") as csv_partidos:
    leitor_partidos = csv.reader(csv_partidos)
    registros_partidos = [n for n in leitor_partidos][1:]


for registro_partidos in registros_partidos:
    if (registro_partidos[3] not in nos_partidos and registro_partidos[3] != "#NULO"):
        nos_partidos.append(registro_partidos[3])
        cnpj_prestador[nos_partidos[-1]] = registro_partidos[3]
        tipo_sequencial[nos_partidos[-1]] = "PARTIDO"
        sequencial[nos_partidos[-1]] = registro_partidos[4]
        uf[nos_partidos[-1]] = registro_partidos[5]
        sigla_partido[nos_partidos[-1]] = registro_partidos[7]
        nome_rotulo_vertice[-1] = sigla_partido[nos_partidos[-1]] + " " + sequencial[nos_partidos[-1]]


    if (registro_partidos[10] not in nos_partidos and registro_partidos[10] != "#NULO"):
        nos_partidos.append(registro_partidos[10])
        cpf_cnpj_doador[nos_partidos[-1]] = registro_partidos[10]
        nome_doador_receita[nos_partidos[-1]] = registro_partidos[12]

    aresta_partido = []
    auxiliar_match = None

    valor_receita_string = registro_partidos[19]
    valor_receita_ponto = valor_receita_string.replace(",", ".")
    valor_receita = float(valor_receita_ponto)  # type: float

    aresta_partido.append(registro_partidos[10])
    aresta_partido.append(registro_partidos[3])

    for sublist in arestas_partidos:
        if sublist[0] == aresta_partido[0] and sublist[1] == aresta_partido[1]:
            auxiliar_match = 1


    if auxiliar_match is None:
        aresta_partido.append(valor_receita)
        arestas_partidos.append(aresta_partido)
    else:
        for sublist in arestas_partidos:
            if sublist[0] == aresta_partido[0] and sublist[1] == aresta_partido[1]:
                sublist[2] = sublist[2] + valor_receita


print("\nResultados:\n")
print("Número de nós em arquivo de partidos: %d" % len(nos_partidos))
print("Número de arestas em arquivo de partidos: %d\n" % len(arestas_partidos))

###############################################

nos_comites = []
arestas_comites = []

with open("/home/akina/Dropbox/TCC/Dados/receitas_comites.csv", "r") as csv_comites:
    leitor_comites = csv.reader(csv_comites)
    registros_comites = [n for n in leitor_comites][1:]


for registro_comites in registros_comites:
    if (registro_comites[3] not in nos_comites and registro_comites[3] != "#NULO"):
        nos_comites.append(registro_comites[3])
        cnpj_prestador[nos_comites[-1]] = registro_comites[3]
        tipo_sequencial[nos_comites[-1]] = "COMITE"
        sequencial[nos_comites[-1]] = registro_comites[4]
        uf[nos_comites[-1]] = registro_comites[5]
        sigla_partido[nos_comites[-1]] = registro_comites[7]
        nome_rotulo_vertice[-1] = sigla_partido[nos_comites[-1]] + " " + sequencial[nos_comites[-1]]


    if (registro_comites[10] not in nos_comites and registro_comites[10] != "#NULO"):
        nos_comites.append(registro_comites[10])
        cpf_cnpj_doador[nos_comites[-1]] = registro_comites[10]
        nome_doador_receita[nos_comites[-1]] = registro_comites[12]

    aresta_comite = []
    auxiliar_match = None

    valor_receita_string = registro_comites[19]
    valor_receita_ponto = valor_receita_string.replace(",", ".")
    valor_receita = float(valor_receita_ponto)  # type: float

    aresta_comite.append(registro_comites[10])
    aresta_comite.append(registro_comites[3])

    for sublist in arestas_comites:
        if sublist[0] == aresta_comite[0] and sublist[1] == aresta_comite[1]:
            auxiliar_match = 1


    if auxiliar_match is None:
        aresta_comite.append(valor_receita)
        arestas_comites.append(aresta_comite)
    else:
        for sublist in arestas_comites:
            if sublist[0] == aresta_comite[0] and sublist[1] == aresta_comite[1]:
                sublist[2] = sublist[2] + valor_receita



print("Número de nós em arquivo de cômites: %d" % len(nos_comites))
print("Número de arestas em arquivo de cômites: %d\n" % len(arestas_comites))

###############################################


nos_candidatos = []
arestas_candidatos = []

with open("/home/akina/Dropbox/TCC/Dados/receitas_candidatos.csv", "r") as csv_candidatos:
    leitor_candidatos = csv.reader(csv_candidatos)
    registros_candidatos = [n for n in leitor_candidatos][1:]


for registro_candidatos in registros_candidatos:
    if (registro_candidatos[3] not in nos_candidatos and registro_candidatos[3] != "#NULO"):
        nos_candidatos.append(registro_candidatos[3])
        cnpj_prestador[nos_candidatos[-1]] = registro_candidatos[3]
        tipo_sequencial[nos_candidatos[-1]] = "CANDIDATO"
        sequencial[nos_candidatos[-1]] = registro_candidatos[4]
        uf[nos_candidatos[-1]] = registro_candidatos[5]
        sigla_partido[nos_candidatos[-1]] = registro_candidatos[6]

        numero_candidato[nos_candidatos[-1]] = registro_candidatos[7]
        cargo_candidato[nos_candidatos[-1]] = registro_candidatos[8]
        nome_candidato[nos_candidatos[-1]] = registro_candidatos[9]
        cpf_candidato[nos_candidatos[-1]] = registro_candidatos[10]
        nome_rotulo_vertice[-1] = sigla_partido[nos_candidatos[-1]]  + " " + nome_candidato[nos_candidatos[-1]]

    if (registro_candidatos[13] not in nos_candidatos and registro_candidatos[13] != "#NULO"):
        nos_candidatos.append(registro_candidatos[13])
        cpf_cnpj_doador[nos_candidatos[-1]] = registro_candidatos[13]
        nome_doador_receita[nos_candidatos[-1]] = registro_candidatos[15]

    aresta_candidato = []
    auxiliar_match = None

    valor_receita_string = registro_candidatos[22]
    valor_receita_ponto = valor_receita_string.replace(",", ".")
    valor_receita = float(valor_receita_ponto)  # type: float

    aresta_candidato.append(registro_candidatos[13])
    aresta_candidato.append(registro_candidatos[3])

    for sublist in arestas_candidatos:
        if sublist[0] == aresta_candidato[0] and sublist[1] == aresta_candidato[1]:
            auxiliar_match = 1


    if auxiliar_match is None:
        aresta_candidato.append(valor_receita)
        arestas_candidatos.append(aresta_candidato)
    else:
        for sublist in arestas_candidatos:
            if sublist[0] == aresta_candidato[0] and sublist[1] == aresta_candidato[1]:
                sublist[2] = sublist[2] + valor_receita



print("Número de nós em arquivo de candidatos: %d" % len(nos_candidatos))
print("Número de arestas em arquivo de candidatos: %d\n" % len(arestas_candidatos))


###############################################

DG = nx.DiGraph()
###############################################

DG.add_nodes_from(nos_partidos)
DG.add_weighted_edges_from(arestas_partidos)

DG.add_nodes_from(nos_comites)
DG.add_weighted_edges_from(arestas_comites)

DG.add_nodes_from(nos_candidatos)
DG.add_weighted_edges_from(arestas_candidatos)

################################################

nx.set_node_attributes(DG, cnpj_prestador, 'cnpj_prestador')
nx.set_node_attributes(DG, tipo_sequencial,'tipo_sequencial')
nx.set_node_attributes(DG, sequencial, 'sequencial')
nx.set_node_attributes(DG, uf, 'uf')
nx.set_node_attributes(DG, sigla_partido, 'sigla_partido')
nx.set_node_attributes(DG, numero_candidato, 'numero_candidato')
nx.set_node_attributes(DG, cargo_candidato, 'cargo_candidato')
nx.set_node_attributes(DG, nome_candidato, 'nome_candidato')
nx.set_node_attributes(DG, cpf_candidato, 'cpf_candidato')
nx.set_node_attributes(DG, cpf_cnpj_doador, 'cpf_cnpj_doador')
nx.set_node_attributes(DG, nome_doador_receita, 'nome_doador_receita')

print("-----------------------------------------------------")
print("Informações sobre o grafo gerado:")
print(nx.info(DG))

print("-----------------------------------------------------")
print("Exportação do arquivo GraphML com a rede:")

#nx.write_graphml(DG, '/home/akina/Dropbox/TCC/Dados/rede_financiamento.graphml')


################################################

print("-----------------------------------------------------")
print("Exportação dos resultados dos cálculos de centralidade:")


################################################
print("1 - Cálculo da centralidade de autovetor")
#eigenvector_centrality_numpy(G, weight=None, max_iter=50, tol=0)

eigenvector_centrality = nx.eigenvector_centrality_numpy(DG, "weight", len(DG), 0)
#print(['{}, {:0.20f}'.format(node, eigenvector_centrality[node]) for node in eigenvector_centrality], file=open('/home/akina/Dropbox/TCC/Dados/teste_eigenvector_centrality.csv', "w"))

dict_nome_rotulo_vertice = nx.get_node_attributes(DG, 'nome_rotulo_vertice')

csv_file_eigenvector = '/home/akina/Dropbox/TCC/Dados/teste_eigenvector_centrality.csv'
with open(csv_file_eigenvector, "w") as output_eigenvector:
    writer = csv.writer(output_eigenvector)
    for node in sorted(eigenvector_centrality, key=lambda x: eigenvector_centrality[x], reverse=True):
        writer.writerow(["{}".format(DG.node[node]), "{:0.20f}".format(eigenvector_centrality[node])])


################################################
print("2 - Cálculo da centralidade de grau")
#degree_centrality(G)

degree_centrality = nx.degree_centrality(DG)
print(['{}, {:0.20f} \n'.format(node, degree_centrality[node]) for node in degree_centrality], file=open('/home/akina/Dropbox/TCC/Dados/teste_degree_centrality.csv', "w"))


################################################
print("3 - Cálculo da centralidade de intermediação")
#betweenness_centrality(G, k=None, normalized=True, weight=None, endpoints=False, seed=None)

betweenness_centrality = nx.betweenness_centrality(DG, len(DG), True, "weight", False, None)
print(['{}, {:0.20f} \n'.format(node, betweenness_centrality[node]) for node in betweenness_centrality], file=open('/home/akina/Dropbox/TCC/Dados/teste_betweenness_centrality.csv', "w"))


################################################
print("4 - Cálculo da centralidade de proximidade")
#closeness_centrality(G, u=None, distance=None, wf_improved=True, reverse=False)

closeness_centrality = nx.closeness_centrality(DG, None, None, True, True)
print(['{}, {:0.20f} \n'.format(node, closeness_centrality[node]) for node in closeness_centrality], file=open('/home/akina/Dropbox/TCC/Dados/teste_closeness_centrality.csve', "w"))


