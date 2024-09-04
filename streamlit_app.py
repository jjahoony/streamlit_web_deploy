import streamlit as st
st.write('youtube view') 
view = [100,150,30]
view
st.bar_chart(view)
import pandas as pd
sview=pd.Series(view)
sview