import csv
import networkx as nx

#Criar um dicionário para cada atributo

nome_rotulo_vertice = {}
numero_votos_candidato = {}
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

###############################################

nos_partidos = []
arestas_partidos = []

with open("/home/akina/Dropbox/TCC/Dados/receitas_partidos.csv", "r") as csv_partidos:
    leitor_partidos = csv.reader(csv_partidos)
    registros_partidos = [n for n in leitor_partidos][1:]


for registro_partidos in registros_partidos:
    if registro_partidos[3] is not None and (
                registro_partidos[3] not in nos_partidos and registro_partidos[3] != "#NULO"):
        nos_partidos.append(registro_partidos[3])
        cnpj_prestador[nos_partidos[-1]] = registro_partidos[3]
        tipo_sequencial[nos_partidos[-1]] = "PARTIDO"
        sequencial[nos_partidos[-1]] = registro_partidos[4]
        uf[nos_partidos[-1]] = registro_partidos[5]
        sigla_partido[nos_partidos[-1]] = registro_partidos[7]
        nome_rotulo_vertice[nos_partidos[-1]] = (sigla_partido[nos_partidos[-1]] + " | " +
                                                 tipo_sequencial[nos_partidos[-1]] + " | " +
                                                 cnpj_prestador[nos_partidos[-1]])

for registro_partidos in registros_partidos:
    if registro_partidos[10] is not None and (
            registro_partidos[10] not in nos_partidos and registro_partidos[10] != "#NULO"):
        nos_partidos.append(registro_partidos[10])
        cpf_cnpj_doador[nos_partidos[-1]] = registro_partidos[10]
        nome_doador_receita[nos_partidos[-1]] = registro_partidos[12]
        nome_rotulo_vertice[nos_partidos[-1]] = (nome_doador_receita[nos_partidos[-1]] + " | " +
                                                 cpf_cnpj_doador[nos_partidos[-1]])

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
    if registro_comites[3] is not None and (
            registro_comites[3] not in nos_comites and registro_comites[3] != "#NULO"):
        nos_comites.append(registro_comites[3])
        cnpj_prestador[nos_comites[-1]] = registro_comites[3]
        tipo_sequencial[nos_comites[-1]] = "COMITE"
        sequencial[nos_comites[-1]] = registro_comites[4]
        uf[nos_comites[-1]] = registro_comites[5]
        sigla_partido[nos_comites[-1]] = registro_comites[7]
        nome_rotulo_vertice[nos_comites[-1]] = (sigla_partido[nos_comites[-1]] + " | " +
                                                tipo_sequencial[nos_comites[-1]] + " | " +
                                                cnpj_prestador[nos_comites[-1]])

for registro_comites in registros_comites:
    if registro_comites[10] is not None and (
            registro_comites[10] not in nos_comites and registro_comites[10] != "#NULO"):
        nos_comites.append(registro_comites[10])
        cpf_cnpj_doador[nos_comites[-1]] = registro_comites[10]
        nome_doador_receita[nos_comites[-1]] = registro_comites[12]
        nome_rotulo_vertice[nos_comites[-1]] = (nome_doador_receita[nos_comites[-1]] + " | " +
                                                cpf_cnpj_doador[nos_comites[-1]])

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
    if registro_candidatos[3] is not None and (
            registro_candidatos[3] not in nos_candidatos and registro_candidatos[3] != "#NULO"):
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
        nome_rotulo_vertice[nos_candidatos[-1]] = (sigla_partido[nos_candidatos[-1]] + " | " +
                                                   tipo_sequencial[nos_candidatos[-1]] + " | " +
                                                   nome_candidato[nos_candidatos[-1]] + " | " +
                                                   cnpj_prestador[nos_candidatos[-1]])

for registro_candidatos in registros_candidatos:
    if registro_candidatos[13] is not None and (
            registro_candidatos[13] not in nos_candidatos and registro_candidatos[13] != "#NULO"):
        nos_candidatos.append(registro_candidatos[13])
        cpf_cnpj_doador[nos_candidatos[-1]] = registro_candidatos[13]
        nome_doador_receita[nos_candidatos[-1]] = registro_candidatos[15]
        nome_rotulo_vertice[nos_candidatos[-1]] = (nome_doador_receita[nos_candidatos[-1]] + " | " +
                                                   cpf_cnpj_doador[nos_candidatos[-1]])

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
#Seleção dos nós com mesmo ID (prioridade CANDIDATO) - casos em que há candidatos que apareceram primeiro como doadores

aux_nos_partidos = []

for aux_partido in nos_partidos:
    if aux_partido not in nos_candidatos:
        aux_nos_partidos.append(aux_partido)

aux_nos_comites = []

for aux_comite in nos_comites:
    if aux_comite not in nos_candidatos:
        aux_nos_comites.append(aux_comite)


###############################################

DG = nx.DiGraph()
###############################################

DG.add_nodes_from(nos_candidatos)
DG.add_weighted_edges_from(arestas_candidatos)

DG.add_nodes_from(aux_nos_partidos)
DG.add_weighted_edges_from(arestas_partidos)

DG.add_nodes_from(aux_nos_comites)
DG.add_weighted_edges_from(arestas_comites)

################################################

nx.set_node_attributes(DG, nome_rotulo_vertice, 'nome_rotulo_vertice')
nx.set_node_attributes(DG, numero_votos_candidato, 'numero_votos_candidato')
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

################################################

print("-----------------------------------------------------")
print("Remoção das arestas para o nó nulo e inserção da aresta no próprio nó não-nulo:")

#lista_nos_conectados = DG.node['#NULO']

lista_nodes = DG.edges()

for source, target in list(lista_nodes):
    if source == "#NULO":
        #print((DG.edges[source][target]))
        peso = DG[source][target]['weight']
        DG.remove_edge(source, target)
        DG.add_edge(target, target, weight=peso)
        #print((DG.edges[target][target]))


################################################

print("-----------------------------------------------------")
print("Identificação de campo nulo sobre rendimentos financeiros:")

print(DG.node['#NULO'])
DG.node['#NULO']['nome_rotulo_vertice'] = "RENDIMENTOS FINANCEIROS"
print(DG.node['#NULO']['nome_rotulo_vertice'])

################################################
print("-----------------------------------------------------")
print("Leitura e inserção dos números de votos para os candidatos:")


with open("/home/akina/Dropbox/TCC/Dados/Resultado_da_Eleicao_UTF-8.csv", "r") as csv_resultado:
    leitor_resultado = csv.reader(csv_resultado)
    registros_resultado = [n for n in leitor_resultado][1:]

#Para não incluir votos brancos ou nulos
for registro_resultado in registros_resultado:
    if registro_resultado[3] is not None and registro_resultado[7] is not None:
        for node in DG.nodes():
            if ("tipo_sequencial" in DG.node[node]):
                if(DG.node[node]["tipo_sequencial"] == "CANDIDATO"):
                    if (DG.node[node]['nome_candidato'] == registro_resultado[3]):
                        DG.node[node]['numero_votos_candidato'] = registro_resultado[7]
                    elif (registro_resultado[7] == "0"):
                        nome_concatenado = "# " + DG.node[node]['nome_candidato']
                        if(nome_concatenado == registro_resultado[3]):
                            DG.node[node]['numero_votos_candidato'] = registro_resultado[7]



###############################################

print("-----------------------------------------------------")
print("Informações sobre o grafo gerado:")
print(nx.info(DG))

print("Movimentação Financeira:")
print(DG.size(weight='weight'))

print("-----------------------------------------------------")
print("Exportação do arquivo GraphML com a rede:")

nx.write_graphml(DG, '/home/akina/Dropbox/TCC/Resultados/Graphml/rede_financiamento.graphml')


################################################

print("-----------------------------------------------------")
print("Exportação dos resultados dos cálculos de centralidade:")


################################################
print("1 - Cálculo da centralidade de autovetor")
#eigenvector_centrality_numpy(G, weight=None, max_iter=50, tol=0)

eigenvector_centrality = nx.eigenvector_centrality_numpy(DG, "weight", len(DG), 0)
#print(['{}, {:0.20f}'.format(node, eigenvector_centrality[node]) for node in eigenvector_centrality], file=open('/home/akina/Dropbox/TCC/Dados/teste_eigenvector_centrality.csv', "w"))


csv_file_eigenvector = '/home/akina/Dropbox/TCC/Resultados/Centralidades_Geral_Todos/eigenvector_centrality.csv'
with open(csv_file_eigenvector, "w") as output_eigenvector:
    writer = csv.writer(output_eigenvector)
    for node in sorted(eigenvector_centrality, key=lambda x: eigenvector_centrality[x], reverse=True):
        writer.writerow(
            ["{}".format(DG.node[node]["nome_rotulo_vertice"]), "{:0.20f}".format(eigenvector_centrality[node])])


csv_file_eigenvector_votos = '/home/akina/Dropbox/TCC/Resultados/Centralidades_Candidatos_Votos/votos_eigenvector_centrality.csv'
with open(csv_file_eigenvector_votos, "w") as output_eigenvector_votos:
    writer = csv.writer(output_eigenvector_votos)
    for node in sorted(eigenvector_centrality, key=lambda x: eigenvector_centrality[x], reverse=True):
        if ("tipo_sequencial" in DG.node[node]):
            if(DG.node[node]["tipo_sequencial"] == "CANDIDATO"):
                if("numero_votos_candidato" in DG.node[node]):
                    writer.writerow(
                        ["{}".format(DG.node[node]["nome_rotulo_vertice"]),
                         "{}".format(DG.node[node]["numero_votos_candidato"]),
                         "{:0.20f}".format(eigenvector_centrality[node])])


csv_file_eigenvector_votos = '/home/akina/Dropbox/TCC/Resultados/Centralidades_Candidatos_Inaptos/out_votos_eigenvector_centrality.csv'
with open(csv_file_eigenvector_votos, "w") as output_eigenvector_votos:
    writer = csv.writer(output_eigenvector_votos)
    for node in sorted(eigenvector_centrality, key=lambda x: eigenvector_centrality[x], reverse=True):
        if ("tipo_sequencial" in DG.node[node]):
            if(DG.node[node]["tipo_sequencial"] == "CANDIDATO"):
                if("numero_votos_candidato" not in DG.node[node]):
                    writer.writerow(
                        ["{}".format(DG.node[node]["nome_rotulo_vertice"]),
                         "{:0.20f}".format(eigenvector_centrality[node])])



csv_file_eigenvector_votos = '/home/akina/Dropbox/TCC/Resultados/Centralidades_Governador/votos_governador_eigenvector_centrality.csv'
with open(csv_file_eigenvector_votos, "w") as output_eigenvector_votos:
    writer = csv.writer(output_eigenvector_votos)
    for node in sorted(eigenvector_centrality, key=lambda x: eigenvector_centrality[x], reverse=True):
        if ("tipo_sequencial" in DG.node[node]):
            if(DG.node[node]["tipo_sequencial"] == "CANDIDATO"):
                if("numero_votos_candidato" in DG.node[node]):
                    if(DG.node[node]["cargo_candidato"] == "Governador"):
                        writer.writerow(
                            ["{}".format(DG.node[node]["nome_rotulo_vertice"]),
                             "{}".format(DG.node[node]["numero_votos_candidato"]),
                             "{:0.20f}".format(eigenvector_centrality[node])])


csv_file_eigenvector_votos = '/home/akina/Dropbox/TCC/Resultados/Centralidades_Senador/votos_senador_eigenvector_centrality.csv'
with open(csv_file_eigenvector_votos, "w") as output_eigenvector_votos:
    writer = csv.writer(output_eigenvector_votos)
    for node in sorted(eigenvector_centrality, key=lambda x: eigenvector_centrality[x], reverse=True):
        if ("tipo_sequencial" in DG.node[node]):
            if(DG.node[node]["tipo_sequencial"] == "CANDIDATO"):
                if("numero_votos_candidato" in DG.node[node]):
                    if(DG.node[node]["cargo_candidato"] == "Senador"):
                        writer.writerow(
                            ["{}".format(DG.node[node]["nome_rotulo_vertice"]),
                             "{}".format(DG.node[node]["numero_votos_candidato"]),
                             "{:0.20f}".format(eigenvector_centrality[node])])



csv_file_eigenvector_votos = '/home/akina/Dropbox/TCC/Resultados/Centralidades_DepFederal/votos_depfederal_eigenvector_centrality.csv'
with open(csv_file_eigenvector_votos, "w") as output_eigenvector_votos:
    writer = csv.writer(output_eigenvector_votos)
    for node in sorted(eigenvector_centrality, key=lambda x: eigenvector_centrality[x], reverse=True):
        if ("tipo_sequencial" in DG.node[node]):
            if(DG.node[node]["tipo_sequencial"] == "CANDIDATO"):
                if("numero_votos_candidato" in DG.node[node]):
                    if(DG.node[node]["cargo_candidato"] == "Deputado Federal"):
                        writer.writerow(
                            ["{}".format(DG.node[node]["nome_rotulo_vertice"]),
                             "{}".format(DG.node[node]["numero_votos_candidato"]),
                             "{:0.20f}".format(eigenvector_centrality[node])])



csv_file_eigenvector_votos = '/home/akina/Dropbox/TCC/Resultados/Centralidades_DepEstadual/votos_depestadual_eigenvector_centrality.csv'
with open(csv_file_eigenvector_votos, "w") as output_eigenvector_votos:
    writer = csv.writer(output_eigenvector_votos)
    for node in sorted(eigenvector_centrality, key=lambda x: eigenvector_centrality[x], reverse=True):
        if ("tipo_sequencial" in DG.node[node]):
            if(DG.node[node]["tipo_sequencial"] == "CANDIDATO"):
                if("numero_votos_candidato" in DG.node[node]):
                    if(DG.node[node]["cargo_candidato"] == "Deputado Estadual"):
                        writer.writerow(
                            ["{}".format(DG.node[node]["nome_rotulo_vertice"]),
                             "{}".format(DG.node[node]["numero_votos_candidato"]),
                             "{:0.20f}".format(eigenvector_centrality[node])])




################################################
print("2 - Cálculo da centralidade de grau")
#degree_centrality(G)

degree_centrality = nx.degree_centrality(DG)
#print(['{}, {:0.20f} \n'.format(node, degree_centrality[node]) for node in degree_centrality], file=open('/home/akina/Dropbox/TCC/Dados/teste_degree_centrality.csv', "w"))


csv_file_degree = '/home/akina/Dropbox/TCC/Resultados/Centralidades_Geral_Todos/degree_centrality.csv'
with open(csv_file_degree, "w") as output_degree:
    writer = csv.writer(output_degree)
    for node in sorted(degree_centrality, key=lambda x: degree_centrality[x], reverse=True):
        writer.writerow(
            ["{}".format(DG.node[node]["nome_rotulo_vertice"]), "{:0.20f}".format(degree_centrality[node])])


csv_file_degree_votos = '/home/akina/Dropbox/TCC/Resultados/Centralidades_Candidatos_Votos/votos_degree_centrality.csv'
with open(csv_file_degree_votos, "w") as output_degree_votos:
    writer = csv.writer(output_degree_votos)
    for node in sorted(degree_centrality, key=lambda x: degree_centrality[x], reverse=True):
        if ("tipo_sequencial" in DG.node[node]):
            if(DG.node[node]["tipo_sequencial"] == "CANDIDATO"):
                if("numero_votos_candidato" in DG.node[node]):
                    writer.writerow(
                        ["{}".format(DG.node[node]["nome_rotulo_vertice"]),
                         "{}".format(DG.node[node]["numero_votos_candidato"]),
                         "{:0.20f}".format(degree_centrality[node])])


csv_file_degree_votos = '/home/akina/Dropbox/TCC/Resultados/Centralidades_Candidatos_Inaptos/out_votos_degree_centrality.csv'
with open(csv_file_degree_votos, "w") as output_degree_votos:
    writer = csv.writer(output_degree_votos)
    for node in sorted(degree_centrality, key=lambda x: degree_centrality[x], reverse=True):
        if ("tipo_sequencial" in DG.node[node]):
            if(DG.node[node]["tipo_sequencial"] == "CANDIDATO"):
                if("numero_votos_candidato" not in DG.node[node]):
                    writer.writerow(
                        ["{}".format(DG.node[node]["nome_rotulo_vertice"]),
                         "{:0.20f}".format(degree_centrality[node])])



csv_file_degree_votos = '/home/akina/Dropbox/TCC/Resultados/Centralidades_Governador/votos_governador_degree_centrality.csv'
with open(csv_file_degree_votos, "w") as output_degree_votos:
    writer = csv.writer(output_degree_votos)
    for node in sorted(degree_centrality, key=lambda x: degree_centrality[x], reverse=True):
        if ("tipo_sequencial" in DG.node[node]):
            if(DG.node[node]["tipo_sequencial"] == "CANDIDATO"):
                if("numero_votos_candidato" in DG.node[node]):
                    if(DG.node[node]["cargo_candidato"] == "Governador"):
                        writer.writerow(
                            ["{}".format(DG.node[node]["nome_rotulo_vertice"]),
                             "{}".format(DG.node[node]["numero_votos_candidato"]),
                             "{:0.20f}".format(degree_centrality[node])])


csv_file_degree_votos = '/home/akina/Dropbox/TCC/Resultados/Centralidades_Senador/votos_senador_degree_centrality.csv'
with open(csv_file_degree_votos, "w") as output_degree_votos:
    writer = csv.writer(output_degree_votos)
    for node in sorted(degree_centrality, key=lambda x: degree_centrality[x], reverse=True):
        if ("tipo_sequencial" in DG.node[node]):
            if(DG.node[node]["tipo_sequencial"] == "CANDIDATO"):
                if("numero_votos_candidato" in DG.node[node]):
                    if(DG.node[node]["cargo_candidato"] == "Senador"):
                        writer.writerow(
                            ["{}".format(DG.node[node]["nome_rotulo_vertice"]),
                             "{}".format(DG.node[node]["numero_votos_candidato"]),
                             "{:0.20f}".format(degree_centrality[node])])



csv_file_degree_votos = '/home/akina/Dropbox/TCC/Resultados/Centralidades_DepFederal/votos_depfederal_degree_centrality.csv'
with open(csv_file_degree_votos, "w") as output_degree_votos:
    writer = csv.writer(output_degree_votos)
    for node in sorted(degree_centrality, key=lambda x: degree_centrality[x], reverse=True):
        if ("tipo_sequencial" in DG.node[node]):
            if(DG.node[node]["tipo_sequencial"] == "CANDIDATO"):
                if("numero_votos_candidato" in DG.node[node]):
                    if(DG.node[node]["cargo_candidato"] == "Deputado Federal"):
                        writer.writerow(
                            ["{}".format(DG.node[node]["nome_rotulo_vertice"]),
                             "{}".format(DG.node[node]["numero_votos_candidato"]),
                             "{:0.20f}".format(degree_centrality[node])])



csv_file_degree_votos = '/home/akina/Dropbox/TCC/Resultados/Centralidades_DepEstadual/votos_depestadual_degree_centrality.csv'
with open(csv_file_degree_votos, "w") as output_degree_votos:
    writer = csv.writer(output_degree_votos)
    for node in sorted(degree_centrality, key=lambda x: degree_centrality[x], reverse=True):
        if ("tipo_sequencial" in DG.node[node]):
            if(DG.node[node]["tipo_sequencial"] == "CANDIDATO"):
                if("numero_votos_candidato" in DG.node[node]):
                    if(DG.node[node]["cargo_candidato"] == "Deputado Estadual"):
                        writer.writerow(
                            ["{}".format(DG.node[node]["nome_rotulo_vertice"]),
                             "{}".format(DG.node[node]["numero_votos_candidato"]),
                             "{:0.20f}".format(degree_centrality[node])])



################################################
print("3 - Cálculo da centralidade de intermediação")
#betweenness_centrality(G, k=None, normalized=True, weight=None, endpoints=False, seed=None)

betweenness_centrality = nx.betweenness_centrality(DG, len(DG), True, "weight", False, None)
#print(['{}, {:0.20f} \n'.format(node, betweenness_centrality[node]) for node in betweenness_centrality], file=open('/home/akina/Dropbox/TCC/Dados/teste_betweenness_centrality.csv', "w"))


csv_file_betweenness = '/home/akina/Dropbox/TCC/Resultados/Centralidades_Geral_Todos/betweenness_centrality.csv'
with open(csv_file_betweenness, "w") as output_betweenness:
    writer = csv.writer(output_betweenness)
    for node in sorted(betweenness_centrality, key=lambda x: betweenness_centrality[x], reverse=True):
        writer.writerow(
            ["{}".format(DG.node[node]["nome_rotulo_vertice"]), "{:0.20f}".format(betweenness_centrality[node])])


csv_file_betweenness_votos = '/home/akina/Dropbox/TCC/Resultados/Centralidades_Candidatos_Votos/votos_betweenness_centrality.csv'
with open(csv_file_betweenness_votos, "w") as output_betweenness_votos:
    writer = csv.writer(output_betweenness_votos)
    for node in sorted(betweenness_centrality, key=lambda x: betweenness_centrality[x], reverse=True):
        if ("tipo_sequencial" in DG.node[node]):
            if(DG.node[node]["tipo_sequencial"] == "CANDIDATO"):
                if("numero_votos_candidato" in DG.node[node]):
                    writer.writerow(
                        ["{}".format(DG.node[node]["nome_rotulo_vertice"]),
                         "{}".format(DG.node[node]["numero_votos_candidato"]),
                         "{:0.20f}".format(betweenness_centrality[node])])


csv_file_betweenness_votos = '/home/akina/Dropbox/TCC/Resultados/Centralidades_Candidatos_Inaptos/out_votos_betweenness_centrality.csv'
with open(csv_file_betweenness_votos, "w") as output_betweenness_votos:
    writer = csv.writer(output_betweenness_votos)
    for node in sorted(betweenness_centrality, key=lambda x: betweenness_centrality[x], reverse=True):
        if ("tipo_sequencial" in DG.node[node]):
            if(DG.node[node]["tipo_sequencial"] == "CANDIDATO"):
                if("numero_votos_candidato" not in DG.node[node]):
                    writer.writerow(
                        ["{}".format(DG.node[node]["nome_rotulo_vertice"]),
                         "{:0.20f}".format(betweenness_centrality[node])])



csv_file_betweenness_votos = '/home/akina/Dropbox/TCC/Resultados/Centralidades_Governador/votos_governador_betweenness_centrality.csv'
with open(csv_file_betweenness_votos, "w") as output_betweenness_votos:
    writer = csv.writer(output_betweenness_votos)
    for node in sorted(betweenness_centrality, key=lambda x: betweenness_centrality[x], reverse=True):
        if ("tipo_sequencial" in DG.node[node]):
            if(DG.node[node]["tipo_sequencial"] == "CANDIDATO"):
                if("numero_votos_candidato" in DG.node[node]):
                    if(DG.node[node]["cargo_candidato"] == "Governador"):
                        writer.writerow(
                            ["{}".format(DG.node[node]["nome_rotulo_vertice"]),
                             "{}".format(DG.node[node]["numero_votos_candidato"]),
                             "{:0.20f}".format(betweenness_centrality[node])])


csv_file_betweenness_votos = '/home/akina/Dropbox/TCC/Resultados/Centralidades_Senador/votos_senador_betweenness_centrality.csv'
with open(csv_file_betweenness_votos, "w") as output_betweenness_votos:
    writer = csv.writer(output_betweenness_votos)
    for node in sorted(betweenness_centrality, key=lambda x: betweenness_centrality[x], reverse=True):
        if ("tipo_sequencial" in DG.node[node]):
            if(DG.node[node]["tipo_sequencial"] == "CANDIDATO"):
                if("numero_votos_candidato" in DG.node[node]):
                    if(DG.node[node]["cargo_candidato"] == "Senador"):
                        writer.writerow(
                            ["{}".format(DG.node[node]["nome_rotulo_vertice"]),
                             "{}".format(DG.node[node]["numero_votos_candidato"]),
                             "{:0.20f}".format(betweenness_centrality[node])])



csv_file_betweenness_votos = '/home/akina/Dropbox/TCC/Resultados/Centralidades_DepFederal/votos_depfederal_betweenness_centrality.csv'
with open(csv_file_betweenness_votos, "w") as output_betweenness_votos:
    writer = csv.writer(output_betweenness_votos)
    for node in sorted(betweenness_centrality, key=lambda x: betweenness_centrality[x], reverse=True):
        if ("tipo_sequencial" in DG.node[node]):
            if(DG.node[node]["tipo_sequencial"] == "CANDIDATO"):
                if("numero_votos_candidato" in DG.node[node]):
                    if(DG.node[node]["cargo_candidato"] == "Deputado Federal"):
                        writer.writerow(
                            ["{}".format(DG.node[node]["nome_rotulo_vertice"]),
                             "{}".format(DG.node[node]["numero_votos_candidato"]),
                             "{:0.20f}".format(betweenness_centrality[node])])



csv_file_betweenness_votos = '/home/akina/Dropbox/TCC/Resultados/Centralidades_DepEstadual/votos_depestadual_betweenness_centrality.csv'
with open(csv_file_betweenness_votos, "w") as output_betweenness_votos:
    writer = csv.writer(output_betweenness_votos)
    for node in sorted(betweenness_centrality, key=lambda x: betweenness_centrality[x], reverse=True):
        if ("tipo_sequencial" in DG.node[node]):
            if(DG.node[node]["tipo_sequencial"] == "CANDIDATO"):
                if("numero_votos_candidato" in DG.node[node]):
                    if(DG.node[node]["cargo_candidato"] == "Deputado Estadual"):
                        writer.writerow(
                            ["{}".format(DG.node[node]["nome_rotulo_vertice"]),
                             "{}".format(DG.node[node]["numero_votos_candidato"]),
                             "{:0.20f}".format(betweenness_centrality[node])])



################################################
print("4 - Cálculo da centralidade de proximidade")
#closeness_centrality(G, u=None, distance=None, wf_improved=True, reverse=False)

closeness_centrality = nx.closeness_centrality(DG, None, None, True, True)
#print(['{}, {:0.20f} \n'.format(node, closeness_centrality[node]) for node in closeness_centrality], file=open('/home/akina/Dropbox/TCC/Dados/teste_closeness_centrality.csv', "w"))


csv_file_closeness = '/home/akina/Dropbox/TCC/Resultados/Centralidades_Geral_Todos/closeness_centrality.csv'
with open(csv_file_closeness, "w") as output_closeness:
    writer = csv.writer(output_closeness)
    for node in sorted(closeness_centrality, key=lambda x: closeness_centrality[x], reverse=True):
        writer.writerow(
            ["{}".format(DG.node[node]["nome_rotulo_vertice"]), "{:0.20f}".format(closeness_centrality[node])])


csv_file_closeness_votos = '/home/akina/Dropbox/TCC/Resultados/Centralidades_Candidatos_Votos/votos_closeness_centrality.csv'
with open(csv_file_closeness_votos, "w") as output_closeness_votos:
    writer = csv.writer(output_closeness_votos)
    for node in sorted(closeness_centrality, key=lambda x: closeness_centrality[x], reverse=True):
        if ("tipo_sequencial" in DG.node[node]):
            if(DG.node[node]["tipo_sequencial"] == "CANDIDATO"):
                if("numero_votos_candidato" in DG.node[node]):
                    writer.writerow(
                        ["{}".format(DG.node[node]["nome_rotulo_vertice"]),
                         "{}".format(DG.node[node]["numero_votos_candidato"]),
                         "{:0.20f}".format(closeness_centrality[node])])


csv_file_closeness_votos = '/home/akina/Dropbox/TCC/Resultados/Centralidades_Candidatos_Inaptos/out_votos_closeness_centrality.csv'
with open(csv_file_closeness_votos, "w") as output_closeness_votos:
    writer = csv.writer(output_closeness_votos)
    for node in sorted(closeness_centrality, key=lambda x: closeness_centrality[x], reverse=True):
        if ("tipo_sequencial" in DG.node[node]):
            if(DG.node[node]["tipo_sequencial"] == "CANDIDATO"):
                if("numero_votos_candidato" not in DG.node[node]):
                    writer.writerow(
                        ["{}".format(DG.node[node]["nome_rotulo_vertice"]),
                         "{:0.20f}".format(closeness_centrality[node])])



csv_file_closeness_votos = '/home/akina/Dropbox/TCC/Resultados/Centralidades_Governador/votos_governador_closeness_centrality.csv'
with open(csv_file_closeness_votos, "w") as output_closeness_votos:
    writer = csv.writer(output_closeness_votos)
    for node in sorted(closeness_centrality, key=lambda x: closeness_centrality[x], reverse=True):
        if ("tipo_sequencial" in DG.node[node]):
            if(DG.node[node]["tipo_sequencial"] == "CANDIDATO"):
                if("numero_votos_candidato" in DG.node[node]):
                    if(DG.node[node]["cargo_candidato"] == "Governador"):
                        writer.writerow(
                            ["{}".format(DG.node[node]["nome_rotulo_vertice"]),
                             "{}".format(DG.node[node]["numero_votos_candidato"]),
                             "{:0.20f}".format(closeness_centrality[node])])


csv_file_closeness_votos = '/home/akina/Dropbox/TCC/Resultados/Centralidades_Senador/votos_senador_closeness_centrality.csv'
with open(csv_file_closeness_votos, "w") as output_closeness_votos:
    writer = csv.writer(output_closeness_votos)
    for node in sorted(closeness_centrality, key=lambda x: closeness_centrality[x], reverse=True):
        if ("tipo_sequencial" in DG.node[node]):
            if(DG.node[node]["tipo_sequencial"] == "CANDIDATO"):
                if("numero_votos_candidato" in DG.node[node]):
                    if(DG.node[node]["cargo_candidato"] == "Senador"):
                        writer.writerow(
                            ["{}".format(DG.node[node]["nome_rotulo_vertice"]),
                             "{}".format(DG.node[node]["numero_votos_candidato"]),
                             "{:0.20f}".format(closeness_centrality[node])])



csv_file_closeness_votos = '/home/akina/Dropbox/TCC/Resultados/Centralidades_DepFederal/votos_depfederal_closeness_centrality.csv'
with open(csv_file_closeness_votos, "w") as output_closeness_votos:
    writer = csv.writer(output_closeness_votos)
    for node in sorted(closeness_centrality, key=lambda x: closeness_centrality[x], reverse=True):
        if ("tipo_sequencial" in DG.node[node]):
            if(DG.node[node]["tipo_sequencial"] == "CANDIDATO"):
                if("numero_votos_candidato" in DG.node[node]):
                    if(DG.node[node]["cargo_candidato"] == "Deputado Federal"):
                        writer.writerow(
                            ["{}".format(DG.node[node]["nome_rotulo_vertice"]),
                             "{}".format(DG.node[node]["numero_votos_candidato"]),
                             "{:0.20f}".format(closeness_centrality[node])])



csv_file_closeness_votos = '/home/akina/Dropbox/TCC/Resultados/Centralidades_DepEstadual/votos_depestadual_closeness_centrality.csv'
with open(csv_file_closeness_votos, "w") as output_closeness_votos:
    writer = csv.writer(output_closeness_votos)
    for node in sorted(closeness_centrality, key=lambda x: closeness_centrality[x], reverse=True):
        if ("tipo_sequencial" in DG.node[node]):
            if(DG.node[node]["tipo_sequencial"] == "CANDIDATO"):
                if("numero_votos_candidato" in DG.node[node]):
                    if(DG.node[node]["cargo_candidato"] == "Deputado Estadual"):
                        writer.writerow(
                            ["{}".format(DG.node[node]["nome_rotulo_vertice"]),
                             "{}".format(DG.node[node]["numero_votos_candidato"]),
                             "{:0.20f}".format(closeness_centrality[node])])



################################################
print("5 - Cálculo da centralidade de grau interna")
#in_degree_centrality(G)

in_degree_centrality = nx.in_degree_centrality(DG)
#print(['{}, {:0.20f} \n'.format(node, in_degree_centrality[node]) for node in in_degree_centrality], file=open('/home/akina/Dropbox/TCC/Dados/teste_in_degree_centrality.csv', "w"))


csv_file_in_degree = '/home/akina/Dropbox/TCC/Resultados/Centralidades_Geral_Todos/in_degree_centrality.csv'
with open(csv_file_in_degree, "w") as output_in_degree:
    writer = csv.writer(output_in_degree)
    for node in sorted(in_degree_centrality, key=lambda x: in_degree_centrality[x], reverse=True):
        writer.writerow(
            ["{}".format(DG.node[node]["nome_rotulo_vertice"]), "{:0.20f}".format(in_degree_centrality[node])])


csv_file_in_degree_votos = '/home/akina/Dropbox/TCC/Resultados/Centralidades_Candidatos_Votos/votos_in_degree_centrality.csv'
with open(csv_file_in_degree_votos, "w") as output_in_degree_votos:
    writer = csv.writer(output_in_degree_votos)
    for node in sorted(in_degree_centrality, key=lambda x: in_degree_centrality[x], reverse=True):
        if ("tipo_sequencial" in DG.node[node]):
            if(DG.node[node]["tipo_sequencial"] == "CANDIDATO"):
                if("numero_votos_candidato" in DG.node[node]):
                    writer.writerow(
                        ["{}".format(DG.node[node]["nome_rotulo_vertice"]),
                         "{}".format(DG.node[node]["numero_votos_candidato"]),
                         "{:0.20f}".format(in_degree_centrality[node])])


csv_file_in_degree_votos = '/home/akina/Dropbox/TCC/Resultados/Centralidades_Candidatos_Inaptos/out_votos_in_degree_centrality.csv'
with open(csv_file_in_degree_votos, "w") as output_in_degree_votos:
    writer = csv.writer(output_in_degree_votos)
    for node in sorted(in_degree_centrality, key=lambda x: in_degree_centrality[x], reverse=True):
        if ("tipo_sequencial" in DG.node[node]):
            if(DG.node[node]["tipo_sequencial"] == "CANDIDATO"):
                if("numero_votos_candidato" not in DG.node[node]):
                    writer.writerow(
                        ["{}".format(DG.node[node]["nome_rotulo_vertice"]),
                         "{:0.20f}".format(in_degree_centrality[node])])



csv_file_in_degree_votos = '/home/akina/Dropbox/TCC/Resultados/Centralidades_Governador/votos_governador_in_degree_centrality.csv'
with open(csv_file_in_degree_votos, "w") as output_in_degree_votos:
    writer = csv.writer(output_in_degree_votos)
    for node in sorted(in_degree_centrality, key=lambda x: in_degree_centrality[x], reverse=True):
        if ("tipo_sequencial" in DG.node[node]):
            if(DG.node[node]["tipo_sequencial"] == "CANDIDATO"):
                if("numero_votos_candidato" in DG.node[node]):
                    if(DG.node[node]["cargo_candidato"] == "Governador"):
                        writer.writerow(
                            ["{}".format(DG.node[node]["nome_rotulo_vertice"]),
                             "{}".format(DG.node[node]["numero_votos_candidato"]),
                             "{:0.20f}".format(in_degree_centrality[node])])


csv_file_in_degree_votos = '/home/akina/Dropbox/TCC/Resultados/Centralidades_Senador/votos_senador_in_degree_centrality.csv'
with open(csv_file_in_degree_votos, "w") as output_in_degree_votos:
    writer = csv.writer(output_in_degree_votos)
    for node in sorted(in_degree_centrality, key=lambda x: in_degree_centrality[x], reverse=True):
        if ("tipo_sequencial" in DG.node[node]):
            if(DG.node[node]["tipo_sequencial"] == "CANDIDATO"):
                if("numero_votos_candidato" in DG.node[node]):
                    if(DG.node[node]["cargo_candidato"] == "Senador"):
                        writer.writerow(
                            ["{}".format(DG.node[node]["nome_rotulo_vertice"]),
                             "{}".format(DG.node[node]["numero_votos_candidato"]),
                             "{:0.20f}".format(in_degree_centrality[node])])



csv_file_in_degree_votos = '/home/akina/Dropbox/TCC/Resultados/Centralidades_DepFederal/votos_depfederal_in_degree_centrality.csv'
with open(csv_file_in_degree_votos, "w") as output_in_degree_votos:
    writer = csv.writer(output_in_degree_votos)
    for node in sorted(in_degree_centrality, key=lambda x: in_degree_centrality[x], reverse=True):
        if ("tipo_sequencial" in DG.node[node]):
            if(DG.node[node]["tipo_sequencial"] == "CANDIDATO"):
                if("numero_votos_candidato" in DG.node[node]):
                    if(DG.node[node]["cargo_candidato"] == "Deputado Federal"):
                        writer.writerow(
                            ["{}".format(DG.node[node]["nome_rotulo_vertice"]),
                             "{}".format(DG.node[node]["numero_votos_candidato"]),
                             "{:0.20f}".format(in_degree_centrality[node])])



csv_file_in_degree_votos = '/home/akina/Dropbox/TCC/Resultados/Centralidades_DepEstadual/votos_depestadual_in_degree_centrality.csv'
with open(csv_file_in_degree_votos, "w") as output_in_degree_votos:
    writer = csv.writer(output_in_degree_votos)
    for node in sorted(in_degree_centrality, key=lambda x: in_degree_centrality[x], reverse=True):
        if ("tipo_sequencial" in DG.node[node]):
            if(DG.node[node]["tipo_sequencial"] == "CANDIDATO"):
                if("numero_votos_candidato" in DG.node[node]):
                    if(DG.node[node]["cargo_candidato"] == "Deputado Estadual"):
                        writer.writerow(
                            ["{}".format(DG.node[node]["nome_rotulo_vertice"]),
                             "{}".format(DG.node[node]["numero_votos_candidato"]),
                             "{:0.20f}".format(in_degree_centrality[node])])

