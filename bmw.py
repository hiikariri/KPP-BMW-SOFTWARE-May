import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.header("KPP BMW SOFTWARE")
st.subheader("Name : Maynaldi Sheva Revansa")
ecg = np.loadtxt('Data ECG.txt', dtype='float',)
ecg1 = ecg[10: 500]
st.line_chart(ecg1)
plt.figure(figsize=(18, 8))
plt.plot(ecg1, "green")
st.pyplot(plt)