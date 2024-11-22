import streamlit as st

def Gen_Eff(V,CL,IL,K,Rse,Ra):
    Eff=(K*V*IL-CL-CL)/(K*V*IL)*100
    CUL=(K*IL)**2*(Ra+Rse)
    return Eff,CUL


st.title("2305A2L52-PS11")
st.write("Calculate the Efficiency of DC series motor at various loads")


col1, col2 = st.columns(2)
with col1:
    with st.container(border=True):
        st.subheader("Input parameters")
        V = st.number_input("V:in Volt", value=230.0, min_value=0.0)
        IL = st.number_input("IL:in Amps", value=15.0, min_value=0.0) 
        Rse = st.number_input("Rse:in Ohms", value=0.20, min_value=0.0)
        Ra = st.number_input("Ra;in Ohms", value=0.10, min_value=0.0)
        CL = st.number_input("CL:in Watts", value=1.0, min_value=0.0)
        CL = st.number_input("CL:in Watts", value=100.0, min_value=0.0)
        K = st.number_input("Constant (K)", value=1.0, min_value=0.0)
        st.button("Compute")

with col2:
     with st.container(border=True):
          st.subheader("output parameters")
          Eff,CUL = Gen_Eff(V,CL,IL,K,Rse,Ra)
          st.write("Efficiency (Eff):",Eff,"%")
          st.write("copper losses (CU):",CUL,"Watts")
          st.write("output efficiency=94.2%")
          st.write("output cupper loss=67.5")