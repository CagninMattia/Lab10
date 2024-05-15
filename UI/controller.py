import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCalcola(self, e):
        global anno
        anno_txt = self._view._txtAnno.value
        try:
            anno = int(anno_txt)
        except ValueError:
            self._view._txt_result.controls.clear()
            self._view._txt_result.controls.append(ft.Text("Errore: L'anno non è valido."))
            self._view.update_page()
            breakpoint()
        if 1816 <= anno <= 2016:
            self._view._txt_result.controls.clear()
            self._model.crea_grafo(anno)
            lista_stati = self._model.lista_stati
            numero_comp_conn = self._model.get_componenti_connesse()
            num_nodi = self._model.get_num_nodi()
            num_archi = self._model.get_num_collegamenti()
            vicini_per_paese = self._model.get_num_connessioni_paese()
            self._view._txt_result.controls.append(ft.Text("Grafo correttamente creato."))
            self._view._txt_result.controls.append(ft.Text(f"Il grafo ha {num_nodi} nodi."))
            self._view._txt_result.controls.append(ft.Text(f"Il grafo ha {num_archi} archi."))
            self._view._txt_result.controls.append(ft.Text(f"Il grafo ha {numero_comp_conn} componenti connesse."))
            for paese, num_vicini in vicini_per_paese.items():
                self._view._txt_result.controls.append(ft.Text(f"Il paese {paese} ha {num_vicini} vicini."))
            for s in lista_stati:
                self._view._dd_stato.options.append(ft.dropdown.Option(text=s.StateNme, key=s))
            self._view._btnCalcola2.disabled = False
            self._view.update_page()
        else:
            self._view._txt_result.controls.clear()
            self._view._txt_result.controls.append(ft.Text("Errore: Inserire anno compreso tra 1816 e 2016."))
            self._view.update_page()

    def handleCalcola2(self, e):
        self._view._txt_result.controls.clear()
        stato = self._view._dd_stato.value
        nodi_visitabili = self._model.get_nodi_visitabili(stato)
        for nodo in nodi_visitabili:
            self._view._txt_result.controls.append(ft.Text(f"{nodo}"))
        self._view.update_page()

        s
