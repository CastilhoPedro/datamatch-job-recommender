from src.frontend.utils.commom import *
from src.backend.services.handler_front import *
from src.utils.helper import *
import streamlit as st



class App:
    def __init__(self):
        
        session_states_items = {
            "tags": [],
            "input_tag": "",
            "show_loading_spinner": False,
            "show_jobs_list": False,
            "search_clicked": False
        }
        
        for k, v in session_states_items.items():
            if k not in st.session_state:
                st.session_state[k] = v

        


    def run(self):
        st.header('DataMatch')
        
        col1, col2 = st.columns([4, 1])
        with col1:
            placeholder='Insira as Habilidades. Ex: Python, Azure, Looker'
            self.input_skills = st.text_input(label='Skills', placeholder=placeholder, label_visibility='collapsed', key="input_tag", on_change=add_tag)
        with col2:
            if st.button("Pesquisar", type='primary'):
                st.session_state['show_loading_spinner'] = True
                st.session_state['search_clicked'] = True

        col1, col2, col3 = st.columns(3)
        with col1:
            placeholder='Localização'
            self.selected_localiza_display = st.selectbox(
                'Local', ufs_dict.keys(), index=None, label_visibility='hidden', placeholder=placeholder
            ) 
        with col2:
            placeholder = 'Data da Publicação'
            self.selected_date_display = st.selectbox(
                'Data', dates.keys(), index=None, label_visibility='hidden', placeholder=placeholder
            )
        with col3:
            placeholder='Nível de Senioridade'
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
                        background:#2B2C36;
                        border:2px solid #F74C4C;
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
        
        
        if st.session_state['search_clicked']:
            self.run_search_btn()
            st.session_state['search_clicked'] = False
    
    
    def run_search_btn(self):
        
        user_bundle = None
        
        if check_inputs(st.session_state.tags, self.selected_localiza_display, self.selected_date_display, self.selected_seniority_display):
            user_bundle = self.load_jobs(
                skills= st.session_state.tags, 
                localization= self.selected_localiza_display,
                date= self.selected_date_display,
                seniority= self.selected_seniority_display)
        
        
        if user_bundle is not None:
            self.show_jobs(user_bundle)
        
    
    def load_jobs(self, skills: list, localization: str, date: int, seniority: str):
        if st.session_state['show_loading_spinner']:
            
            label = "Carregando Vagas Mais Aderentes..."
            
            with st.spinner(label, show_time=True):
                import time
                time.sleep(3)
                user_bundle = process_user_data(
                    skills=skills,
                    localization=localization,
                    date=date,
                    seniority=seniority
                )
            if user_bundle is None:
                st.error("Não foi possível encontrar nenhuma vaga")
                return None
            else:
                st.session_state['show_loading_spinner'] = False
                st.session_state['show_jobs_list'] = True
                return user_bundle
    
    def show_jobs(self, jobs: list):
        if st.session_state['show_jobs_list']:
            if len(jobs) > 0:
                with self.container.container(height=500):
                    for job in jobs:
                        
                        st.markdown(f"""
                <a href="{"https://" + job['link']}" target="_blank" style="text-decoration: none;">  
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
            else:
                st.write("Nenhuma vaga encontrada...")
        
        


if __name__ == '__main__':
    stmlt = App()
    stmlt.run()









