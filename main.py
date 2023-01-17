import streamlit as st
import pandas as pd
import numpy as np
import random


st.title("Web Team Anonymous ID Generator")

keyword = ""
keyword = st.text_input('Enter a Keyword')
if keyword != "":
    st.markdown("Your identifier is:")
    st.markdown(keyword + str(random.randint(1000000, 9999999)))
    st.markdown("\nPlease copy+paste this identifier into your application form and your anonymous demographic information form!")
