import streamlit as st
import pandas as pd
import numpy as np

st.header('DataMatch')



col1, col2 = st.columns([4, 1])

with col1:
    input_skills = st.text_input(label='', placeholder='Insira as Habilidades. Ex: Python, Azure, Looker', label_visibility='collapsed')

with col2:
    button_execute = st.button("Pesquisar", type='primary')

col1, col2, col3 = st.columns(3)
with col1:
    input_localiza = st.text_input(label= '', placeholder='Localização') #terá que ser trocado por uma selectbox, assim poderemos inserir a lista de estados. Acredito que o nível de granularidade de filtro será de estado, pelo menos para o MVP.

with col2:
    dates = {
        'Último dia': 1,
        'Últimos 3 dias': 3,
        'Últimos 7 dias': 7,
        'Últimos 15 dias': 15,
        'Últimos 30 dias': 30
    }
    
    selected_date_display = st.selectbox(
        '', dates.keys(), index=0
    )

with col3:
    seniority = [
        'Estágio',
        'Júnior',
        'Pleno',
        'Sênior'
    ]
    
    selected_seniority_display = st.selectbox(
        '', seniority, placeholder='Nível de Senioridade', index=None
    )


jobs = [
    {
        "titulo": "Teste 1",
        "empresa": "Lugar 1",
        "local": "Little Farm, SP",
        "fonte": "portaVidro",
        "nivel": "Júnior",
    },
    {
        "titulo": "Teste 2",
        "empresa": "confidential",
        "local": "Barueri, SP",
        "fonte": "Link",
        "nivel": "Sênior",
    }
]

for job in jobs:
    with st.container():
        st.markdown(f"""
        <div style="
            border: 1px solid #444;
            border-radius: 6px;
            padding: 11px;
            margin-bottom: 9px;
            background-color: #111;
        ">
            <h4 style="margin:0;">{job['titulo']}</h4>
            <p style="margin:0; color: #aaa;">{job['empresa']}</p>
            <p style="margin:0; font-size: 12px; color: #bbb;">Nível: {job['nivel']}</p>
            <p style="margin:0; font-size: 11px; color: #999;">{job['local']} • {job['fonte']}</p>
        </div>
        """, unsafe_allow_html=True)













# num_rows = st.slider("Number of rows", 1, 10000, 500)
# np.random.seed(42)
# data = []
# for i in range(num_rows):
#     data.append(
#         {
#             "Preview": f"https://picsum.photos/400/200?lock={i}",
#             "Views": np.random.randint(0, 1000),
#             "Active": np.random.choice([True, False]),
#             "Category": np.random.choice(["🤖 LLM", "📊 Data", "⚙️ Tool"]),
#             "Progress": np.random.randint(1, 100),
#         }
#     )
# data = pd.DataFrame(data)

# config = {
#     "Preview": st.column_config.ImageColumn(),
#     "Progress": st.column_config.ProgressColumn(),
# }

# if st.toggle("Enable editing"):
#     edited_data = st.data_editor(data, column_config=config, use_container_width=True)
# else:
#     st.dataframe(data, column_config=config, use_container_width=True)

# countries = [
#     ("🇺🇸 United States", "USA"),
#     ("🇨 Canada", "CAN"),
#     ("  United Kingdom", "GBR"),
#     (" France", "FRA"),
#     ("🇪 Germany", "DEU"),
#     ("🇯🇵 Japan", "JPN"),
# ]


# selected_country_display = st.selectbox(
#     "Select a country:",
#     [country[0] for country in countries]
#     )

# # Extract the country code (or full name) from the selected display string if needed
# selected_country_code = None
# for display_name, code in countries:
#     if display_name == selected_country_display:
#         selected_country_code = code
#         break

# st.write(f"You selected: {selected_country_display} (Code: {selected_country_code})")