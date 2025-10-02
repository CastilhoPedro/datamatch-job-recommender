import streamlit as st

def add_tag():
    tag = st.session_state.input_tag.strip()
    if tag:
        # evita duplicatas (opcional). Remova a checagem se quiser permitir duplicatas.
        if tag not in st.session_state.tags:
            st.session_state.tags.append(tag)
    # limpa o campo - isso está dentro do callback, então é permitido
    st.session_state.input_tag = ""

def remove_tag(idx):
    st.session_state.tags.pop(idx)