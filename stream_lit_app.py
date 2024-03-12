#import the libraries required
import streamlit as st
from snowflake.snowpark.functions import col
import pandas as pd

st.title("Zena's Amazing Athleisure Catalog")
st.write('Pick a sweatshirt color or style')

#setup the connection in Streamlit
cnx = st.connection('snowflake')
session = cnx.session()

# load data
my_dataframe = session.table('ZENAS_ATHLEISURE_DB.PRODUCTS.CATALOG_FOR_WEBSITE').select(col('COLOR_OR_STYLE'),col('DIRECT_URL'),col('PRICE'),col('SIZE_LIST'))

pd_df = my_dataframe.to_pandas()
selected_style = st.selectbox( 'Select a style of Color',
                    pd_df['COLOR_OR_STYLE'])
if selected_style:
  img = pd_df[pd_df['COLOR_OR_STYLE']==selected_style]['DIRECT_URL'].iloc[0]
  PRICE = pd_df[pd_df['COLOR_OR_STYLE']==selected_style]['PRICE'].iloc[0]
  SIZE = pd_df[pd_df['COLOR_OR_STYLE']==selected_style]['SIZE_LIST'].iloc[0]
  st.image(img)
  st.subheader('Price')
  st.subheader( PRICE)
  st.subheader(SIZE)
