#import the libraries required
import streamlit as st
from snowflake.snowpark.functions import col

st.title('Zena's Amazing Athleisure Catalog')
st.write('Pick a sweatshirt color or style')

#setup the connection in Streamlit
cnx = st.connection('snowflake')
session = cnx.session()

# load data
my_dataframe = session.table('ZENAS_ATHLEISURE_DB.PRODUCTS.CATALOG_FOR_WEBSITE').select(col('COLOR_OR_STYLE'))


st.selectbox( 'Select a style of Color',
              my_dataframe)
