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
my_dataframe = session.table('ZENAS_ATHLEISURE_DB.PRODUCTS.CATALOG_FOR_WEBSITE').select(col('COLOR_OR_STYLE'),col('DIRECT_URL'))

pd_df = my_dataframe.to_pandas()
selected_style = st.selectbox( 'Select a style of Color',
                    pd_df['COLOR_OR_STYLE'])
if selected_style:
  img = pd_df[pd_df.loc[pd_df['COLOR_OR_STYLE']==selected_style,'DIRECT_URL']].iloc[0]
  st.image(img)
