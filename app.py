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
        <div id='header'>
            <a href='https://www.instagram.com/lacomuna.lenchatrans/'
            style='text-align:center;display:block'
            rel='noopener noreferrer'
            target='_blank'>
            <b>La Comuna Lencha Trans</b>
        </div>

        <style>
        #header a {

           color: hotpink;
            }
        </style>
        """, unsafe_allow_html=True)

    # Read xlsx file as dataframe
    df = pd.read_excel('data/directorix-processed.xlsx', converters={'Teléfono': str})
    # Fill nan values on columns with a values
    df.fillna({'Teléfono':'----', 'Descripción_Trabajo':'', 'Aportación':''}, inplace=True)
    # Get unique values from several columns
    categories = pd.unique(df[['Habilidades1', 'Habilidades2', 'Habilidades3', 'Habilidades4']].values.ravel())
    # Remove nan values from array
    categories_cleanned = categories[~pd.isnull(categories)]
    # Insert value to numpy array
    categories_cleanned = np.insert(categories_cleanned, 0, '')
    # Insert containers laid out as columns
    col1, col2, col3= st.columns([2, 4, 2])
    with col2:
        # Select a value to filter from dataframe
        selected_category = st.selectbox('Selecciona una categoría:', sorted(categories_cleanned), index=0)
        results1 = df.loc[df['Habilidades1'] == selected_category]
        results2 = df.loc[df['Habilidades2'] == selected_category]
        results3 = df.loc[df['Habilidades3'] == selected_category]
        results4 = df.loc[df['Habilidades4'] == selected_category]
        results = pd.concat([results1, results2, results3, results4])
        # Filter data according to selection
        if selected_category:
            for i in results.index:
                name = df['Nombre'].loc[[i]].item()
                mail = df['Correo'].loc[[i]].item()
                contact = df['Contacto'].loc[[i]].item()
                phone = df['Teléfono'].loc[[i]].item()
                description = df['Descripción'].loc[[i]].item()
                description_work = df['Descripción_Trabajo'].loc[[i]].item()
                contribution = df['Aportación'].loc[[i]].item()
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
            <a href='https://docs.google.com/forms/d/e/1FAIpQLSeI73Pw3YGpsF0JqapU1UoqWlwCarbnIL2YEcONSMIZ14ZvLQ/viewform?pli=1'
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