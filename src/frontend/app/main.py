from src.frontend.utils.tags import *
from src.backend.services.handler_front import *
import streamlit as st



class App:
    def __init__(self):
        
        session_states_items = {
            "tags": [],
            "input_tag": "",
            "show_loading_spinner": False,
            "show_jobs_list": False,
        }
        
        for k, v in session_states_items.items():
            if k not in st.session_state:
                st.session_state[k] = v

        


    def run(self):
        # st.header('DataMatch')
        st.header('Resumos de Cobrança Financeiro')
        
        col1, col2 = st.columns([4, 1])
        with col1:
            # placeholder='Insira as Habilidades. Ex: Python, Azure, Looker'
            placeholder = 'Qual relatório quer tirar: Entradas e saídas, Ocupação'
            self.input_skills = st.text_input(label='Skills', placeholder=placeholder, label_visibility='collapsed', key="input_tag", on_change=add_tag)
        with col2:
            if st.button("Pesquisar", type='primary'):
                st.session_state['show_loading_spinner'] = True
                

        col1, col2, col3 = st.columns(3)
        with col1:
            # placeholder='Localização'
            placeholder='Filial: ITA, VIX'
            self.input_localiza = st.text_input(label= 'Local', placeholder=placeholder, label_visibility='hidden') #terá que ser trocado por uma selectbox, assim poderemos inserir a lista de estados. Acredito que o nível de granularidade de filtro será de estado, pelo menos para o MVP.
        with col2:
            dates = {
                'Último dia': 1,
                'Últimos 3 dias': 3,
                'Últimos 7 dias': 7,
                'Últimos 15 dias': 15,
                'Últimos 30 dias': 30
            }
            
            self.selected_date_display = st.selectbox(
                'Date', dates.keys(), index=0, label_visibility='hidden'
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
                'Seniority', seniority, placeholder=placeholder, index=None, label_visibility= 'hidden'  
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
        
        
        self.container = st.empty() #precisa "marcar" onde quer deixar os elementos, porque o streamlit só sai enfiando uma coisa embaixo da outra e é nois.
        self.run_search_btn()
    
    
    def run_search_btn(self):
        self.load_jobs(
            skills= st.session_state.tags, 
            localization= self.input_localiza,
            date= self.selected_date_display,
            seniority= self.selected_seniority_display)
        
        self.show_jobs()
    
    def load_jobs(self, skills: list, localization: str, date: int, seniority: str):
        if st.session_state['show_loading_spinner']:
            label = "Carregando Relatórios..."
            # label = "Carregando Vagas Mais Aderentes..."
            with st.spinner(label, show_time=True):
                
                process_user_data(
                    skills=skills,
                    localization=localization,
                    date=date,
                    seniority=seniority
                )

            st.session_state['show_loading_spinner'] = False
            st.session_state['show_jobs_list'] = True
    
    def show_jobs(self):
        if st.session_state['show_jobs_list']:
            
            self.jobs = get_jobs()
            
            with self.container.container(height=500):
                for job in self.jobs:
                    st.markdown(f"""
            <a href="{job['link']}" target="_blank" style="text-decoration: none;">
                <div style="
                    border: 1px solid #444;
                    border-radius: 6px;
                    padding: 11px;
                    margin-bottom: 9px;
                    background-color: #111;
                ">
                    <h4 style="margin:0; color: #fff;">{job['titulo']}</h4>
                    <p style="margin:0; color: #aaa;">{job['empresa']}</p>
                    <p style="margin:0; font-size: 12px; color: #bbb;">Nível: {job['nivel']}</p>
                    <p style="margin:0; font-size: 11px; color: #999;">{job['local']} • {job['fonte']}</p>
                </div>
            </a>
            """, unsafe_allow_html=True)
        
        st.session_state['show_jobs_list'] = False


if __name__ == '__main__':
    stmlt = App()
    stmlt.run()









