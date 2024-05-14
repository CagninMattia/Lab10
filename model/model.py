import networkx as nx

from database.DAO import DAO


class Model:

    def __init__(self):
        self.grafo = nx.Graph()
        self.diz_stati = {}
        self.lista_stati = []
        self.lista_archi = []

    def crea_grafo(self, anno):
        self.grafo.clear()
        self.lista_stati = self.aggiungi_vertici(anno)
        self.lista_archi = self.aggiungi_archi(anno)

    def aggiungi_vertici(self, anno):
        vertici = DAO.get_all_vertici(anno)
        self.grafo.add_nodes_from(vertici)
        for v in vertici:
            self.diz_stati[v.CCode] = v
        return vertici

    def aggiungi_archi(self, anno):
        archi = DAO.get_all_archi(anno)
        for arco in archi:
            self.grafo.add_edge(self.diz_stati[arco[0]], self.diz_stati[arco[1]])
        return archi

    def get_componenti_connesse(self):
        num_componenti = nx.number_connected_components(self.grafo)
        return num_componenti

    def get_num_nodi(self):
        return len(self.grafo.nodes)

    def get_num_collegamenti(self):
        return len(self.grafo.edges)

    def get_num_connessioni_paese(self):
        gradi = dict(self.grafo.degree())
        # Creazione del dizionario dei vicini per ogni paese
        vicini_per_paese = {}
        for paese in self.lista_stati:
            conta = 0
            for arco in self.lista_archi:
                if arco[0] == paese.CCode:
                    conta += 1
            vicini_per_paese[paese] = conta
        return vicini_per_paese

    def get_nodi_visitabili(self, stato):
        st = None
        for s in self.lista_stati:
            if s.StateNme == stato:
                st = s

        albero = nx.dfs_tree(self.grafo, st)
        visitabili = list(albero.nodes)
        visitabili.remove(st)  # Rimuovi lo stato stesso dalla lista
        return visitabili
