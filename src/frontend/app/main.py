from frontend.utils.tags import *
from backend.services.handler_front import main
import streamlit as st
import pandas as pd
import numpy as np



class App:
    def __init__(self):
        if "tags" not in st.session_state:
            st.session_state["tags"] = []
        if "input_tag" not in st.session_state:
            st.session_state["input_tag"] = ""
    
    
    def run(self):
        
        st.header('Ativa Logística')
        
        col1, col2 = st.columns([4, 1])
        with col1:
            # placeholder='Insira as Habilidades. Ex: Python, Azure, Looker'
            placeholder = 'Qual relatório quer tirar: Entradas e saídas, Ocupação'
            self.input_skills = st.text_input(label='Skills', placeholder=placeholder, label_visibility='collapsed', key="input_tag", on_change=add_tag)
        with col2:
            self.button_execute = st.button("Pesquisar", type='primary', on_click=main)

        col1, col2, col3 = st.columns(3)
        with col1:
            # placeholder='Localização'
            placeholder='Filial: ITA, VIX'
            self.input_localiza = st.text_input(label= 'Local', placeholder=placeholder) #terá que ser trocado por uma selectbox, assim poderemos inserir a lista de estados. Acredito que o nível de granularidade de filtro será de estado, pelo menos para o MVP.
        with col2:
            dates = {
                'Último dia': 1,
                'Últimos 3 dias': 3,
                'Últimos 7 dias': 7,
                'Últimos 15 dias': 15,
                'Últimos 30 dias': 30
            }
            
            self.selected_date_display = st.selectbox(
                'Date', dates.keys(), index=0
            )
        with col3:
            seniority = [
                'Estágio',
                'Júnior',
                'Pleno',
                'Sênior'
            ]
            # placeholder='Nível de Senioridade'
            placeholder = 'Depositante'
            self.selected_seniority_display = st.selectbox(
                'Seniority', seniority, placeholder=placeholder, index=None
            )


        for i, tag in enumerate(st.session_state.tags):
            col1, col2 = st.columns([0.9, 0.1])
            with col1:
                st.markdown(
                    f"""
                    <div style="
                        display:inline-flex;
                        align-items:center;
                        padding:6px 10px;
                        margin:4px;
                        border-radius:999px;
                        background:#285790;
                        border:2px solid #2FE552;
                        font-size:12px;
                        color:white;">
                        {tag}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
            with col2:
                if st.button("✖", key=f"remove_{i}"):
                    remove_tag(i)
                    st.rerun()





#---------Tags da lista de skills do user -----------#



## essas duas funções vao para alguma utils/helpers da vida


# st.header('DataMatch')

# jobs = [
#     {
#         "titulo": "Teste 1",
#         "empresa": "Lugar 1",
#         "local": "Little Farm, SP",
#         "fonte": "portaVidro",
#         "nivel": "Júnior",
#     },
#     {
#         "titulo": "Teste 2",
#         "empresa": "confidential",
#         "local": "Barueri, SP",
#         "fonte": "Link",
#         "nivel": "Sênior",
#     }
# ]

# for job in jobs:
#     with st.container():
#         st.markdown(f"""
#         <div style="
#             border: 1px solid #444;
#             border-radius: 6px;
#             padding: 11px;
#             margin-bottom: 9px;
#             background-color: #111;
#         ">
#             <h4 style="margin:0;">{job['titulo']}</h4>
#             <p style="margin:0; color: #aaa;">{job['empresa']}</p>
#             <p style="margin:0; font-size: 12px; color: #bbb;">Nível: {job['nivel']}</p>
#             <p style="margin:0; font-size: 11px; color: #999;">{job['local']} • {job['fonte']}</p>
#         </div>
#         """, unsafe_allow_html=True)




if __name__ == '__main__':
    stmlt = App()
    stmlt.run()









