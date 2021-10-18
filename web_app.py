#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 15:12:16 2021

@author: girishsolanki
"""

import streamlit as st
from io import StringIO
from components import sat_comps

st.image("https://www.northropgrumman.com/wp-content/uploads/space-facebook.jpg")
st.title("Get Shielding and Wiring calculations")
st.subheader("Upload .TXT file with box dimensions (in mm)")
uploaded_files = st.file_uploader(label = "Choose a file", type= ['txt'], accept_multiple_files=True)


if uploaded_files is not None:
    for uploaded_file in uploaded_files:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        
        # create object
        components = sat_comps(stringio)
    
        # get dimensions
        box_dims = components.get_dim()
    
        # get shielding and wiring calculations
        shielding = sum(list(map(components.cal_shielding,box_dims)))
        wiring = sum(list(map(components.cal_wiring,box_dims)))
        
        # Set metrics on GUI
        col1,col2,col3 = st.columns(3)
        col1.metric("File", uploaded_file.name)
        col2.metric("Shielding (mm square)", str(shielding))
        col3.metric("Wiring (mm)", str(wiring))
