import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image




def main():
    # Open image with PIL
    favicon = Image.open(f'./assets/icon.png')
    # Set title page and favicon
    st.set_page_config(
        page_title='Directorix Disidente', 
        page_icon = favicon, 
        layout = 'wide', 
        initial_sidebar_state = 'expanded',)
    # Set streamlit app title
    st.markdown(
        """
        <h1 style='text-align: center; color: #7b0cd7;'>Directorix Disidente</h1>
        """, unsafe_allow_html=True)
    # Insert containers laid out as columns
    col1, col2, col3= st.columns([3, 6, 3])
    # Set streamlit app description
    with col2:
        st.markdown(
        """
        <p style='text-align: justify;'>
            En <span id='description'>
            <a href='https://www.instagram.com/lacomuna.lenchatrans/' rel='noopener noreferrer' target='_blank'>
            La Comuna Lencha Trans</a></span>
             te damos la bienvenida a este directorix dónde nos dimos a la tarea de  
            reunir a comunidad disidente de la que puedas apoyarte para concluir proyectos,  
            materializar ideas y cualquier otro tipo de apoyo o acompañamiento que desees. 
            Esperamos que en esta red encuentres a quien buscas y juntxs construyamos cosas increíbles.
        </p>
        <style>
        #description a {

        color: hotpink;
            }
        </style>
        """, unsafe_allow_html=True)
    # Read xlsx file as dataframe
    df = pd.read_excel('./data/directorix-processed.xlsx', converters={'telefono': str})
    # Fill nan values on columns with a values
    df.fillna({'telefono':'----', 'descripcion_trabajo':'', 'aportacion':''}, inplace=True)
    # Get unique values from several columns
    categories = pd.unique(df[['habilidades1', 'habilidades2', 'habilidades3', 'habilidades4']].values.ravel())
    # Remove nan values from array
    categories_cleanned = categories[~pd.isnull(categories)]
    # Insert value to numpy array
    categories_cleanned = np.insert(categories_cleanned, 0, '')
    # Insert containers laid out as columns
    col1, col2, col3= st.columns([2, 4, 2])
    with col2:
        # Select a value to filter from dataframe
        selected_category = st.selectbox('Selecciona una categoría:', sorted(categories_cleanned), index=0)
        results1 = df.loc[df['habilidades1'] == selected_category]
        results2 = df.loc[df['habilidades2'] == selected_category]
        results3 = df.loc[df['habilidades3'] == selected_category]
        results4 = df.loc[df['habilidades4'] == selected_category]
        results = pd.concat([results1, results2, results3, results4])
        # Filter data according to selection
        if selected_category:
            for i in results.index:
                name = df['nombre'].loc[[i]].item()
                mail = df['correo'].loc[[i]].item()
                contact = df['contacto'].loc[[i]].item()
                phone = df['telefono'].loc[[i]].item()
                description = df['descripcion'].loc[[i]].item()
                description_work = df['descripcion_trabajo'].loc[[i]].item()
                contribution = df['aportacion'].loc[[i]].item()
                with st.expander(name, expanded=False):
                    st.markdown(f'{description}')
                    st.markdown('---')
                    st.markdown(f':envelope_with_arrow: {mail}')
                    st.markdown(f':wave: {contact}')
                    st.markdown(f':telephone_receiver: {phone}')
                    st.markdown(
                        f"""
                        <p style='color:#061bed;'>Descripción de mi trabajo:</p>  \n{description_work}
                        """, unsafe_allow_html=True)
                    st.markdown(
                        f"""
                        <p style='color:#061bed;'>¿Cómo deseo aportar a quienes me contacten?</p>  \n{contribution}
                        """, unsafe_allow_html=True)

    # Add footer link
    st.markdown(
        """
        ---
        <div id='footer'>
            <a href='https://ee.humanitarianresponse.info/x/s5znI8NZ'
            style='text-align:center;display:block'
            rel='noopener noreferrer'
            target='_blank'>
            <b>¿Quieres formar parte del <i>Directorix Disidente</i>?</b>
        </div>

        <style>
        #footer a {
           text-decoration:None;
           color: orange;
            }
        </style>
        """, unsafe_allow_html=True)

    # Hide streamlit menu and footer message
    hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                """    
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 


if __name__ == '__main__':
    main()