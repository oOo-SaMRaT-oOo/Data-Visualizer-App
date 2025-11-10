import numpy as np
import scipy as sc
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import os 
os.system("cls")
    
st.sidebar.header("DATA VISUALIZER")
st.sidebar.caption("~ By Samrat Malla")
st.sidebar.write("---")
choice = st.sidebar.radio("DEAR USER SELECT YOUR ACTION :",
                options = ["START APP","APP OBJECTIVE","ABOUT APP"])

if choice =="START APP":
    st.write("<h1 style = 'text-align : center;'>DATA VISUALIZER </h1>",
            unsafe_allow_html=True)
    st.write("---")

    st.subheader("FILE INPUT :")   
    st.caption("PLEASE UPLOAD EXCEL FILES ")
    files = st.file_uploader("ENTER MULTIPLE FILES :",type=["xlsx"],
        accept_multiple_files=True) 

    st.write("---")

    if files :
        file_names = [file.name for file in files]
        st.caption("MULTIPLE VISUALIZATION IS ALLOWED")
        options = st.multiselect(label="SELECT FILE TO VISUALIZE ",
                                    options=file_names)
        if options:
            st.write("---")
            st.subheader("VISUALIZATION PROCESS :")
            st.caption("EXTRACTED DATA FROM FILE ")

            for file in files:
                if file.name in options:
                    data = pd.read_excel(file)
                    name = str(file.name).split(".")[0].upper()
                    st.write(f"<h3 style='text-align : center;'>FILE : {name}</h3>",
                                unsafe_allow_html=True)
                    st.table(data)
                    st.write("---")
                    choice = st.radio("ENTER TYPE OF VISUALIZATION :",
                                    options=["2D GRAPH","None"])
                    st.write("---")
                    
                    if choice=="2D GRAPH":
                        st.write("<h4>VISUALIZATION METHOD : 2D GRAPH",
                                unsafe_allow_html=True)
                        st.caption("SELECT TWO UNIQUE ENTITIES")
                        col1,col2 = st.columns(2)
                        with col1:
                            x_axis = st.selectbox("SELECT X-AXIS ENTITY",
                                                    options=data.columns)
                        with col2:
                            y_axis = st.selectbox("SELECT Y-AXIS ENTITY",
                                                    options = data.columns)
                            
                        if ( x_axis and y_axis) and (x_axis!=y_axis):
                            x_values = np.array(data[x_axis])
                            y_values = np.array(data[y_axis])

                            fig,axs = plt.subplots()
                            
                            col1,col2 = st.columns([5,0.9])
                            with col2:
                                st.write("<br><br><br>",unsafe_allow_html=True)
                                y_n = st.radio(label="INTERPOLATION ",
                                                options=["YES","NO"],)

                            with col1:
                                if y_n =="NO":
                                    st.write(f"<br>",unsafe_allow_html=True)
                                    st.caption("2D GRAPHICAL REPRESENTATION :")
                                    axs.plot(x_values,y_values,"o--",label = name)
                                    axs.set_title(f"{name} GRAPH")
                                    axs.set_xlabel(x_axis)
                                    axs.set_ylabel(y_axis)
                                    axs.grid(True)
                                    plt.legend()
                                    plt.tight_layout()
                                    st.pyplot(fig)
                            
                                if y_n =="YES":
                                    x_values = data[x_axis]
                                    y_values = data[y_axis]
                                    y_f = sc.interpolate.interp1d(x_values,
                                                                    y_values,kind="cubic")
                                    
                                    x_data = np.linspace(min(x_values),max(x_values),1000)
                                    y_data = y_f(x_data)

                                    st.write(f"<br>",unsafe_allow_html=True)
                                    st.caption("2D GRAPHICAL REPRESENTATION :")
                                    axs.plot(x_data,y_data,"--",label = name)
                                    axs.scatter(x_values,y_values)
                                    axs.set_title(f"{name} GRAPH")
                                    axs.set_xlabel(x_axis)
                                    axs.set_ylabel(y_axis)
                                    axs.grid(True)
                                    plt.legend()
                                    plt.tight_layout()
                                    st.pyplot(fig)


                            st.write("---")

                            st.write("<h4>STATISTICAL ANALYSIS :</h4>",unsafe_allow_html=True)
                            options = st.selectbox(label="SELECT ENTITY FOR STATISTICAL ANALYSIS :",
                                                    options=data.columns)
                            if options:
                                values = data[options]
                                mean = str(np.round(np.mean(values),4))
                                median = str(np.round(np.median(values),4))
                                max = str(np.round(np.max(values),4))
                                min = str(np.round(np.min(values),4))
                                std = str(np.round(np.std(values),4))
                                var = str(np.round(np.var(values),4))



                                st.write("---")
                                st.caption("DISPLAYING ANALYSIS :")
                                c1,c2 = st.columns(2)
                                with c1:
                                    st.write("MEAN VALUE :",mean)
                                    st.write("MEDIAN VALUE :",median)
                                    st.write("STANDARD DEVIATION VALUE :",std)
                                
                                with c2:
                                    st.write("MAX VALUE :",max)
                                    st.write("MIN VALUE :",min)
                                    st.write("VARIANCE VAUE :",var)

                                st.write("---")
                                
                                opt = st.multiselect("ENTER TWO QUANTITIES TO FIND RELATIONSHIP :",
                                                    data.columns,max_selections=2)
                                
                                if len(opt)==2:
                                    value_1 = data[opt[0]]
                                    value_2 = data[opt[1]]
                                    corr_coef = str(np.round(np.corrcoef(value_1,value_2)[0,1],4))
                                    
                                    if float(corr_coef)>0:
                                        status = "POSITIVE"
                                    elif float(corr_coef)<0:
                                        status = "NEGATIVE"
                                    else:
                                        status = "ZERO"
                                    
                                    st.caption("ON BASIS OF CORRELATION COEFFICIENT :")
                                    st.write(f"CORRELATION COEFFICIENT : {corr_coef}")
                                    st.write(f"RELATION SHIP STATUS : {status}",unsafe_allow_html=True)

                                                                        
                                    st.write("---")
                                    st.write("~ By Samrat Malla")
                                    st.caption("Pulchowk Campus | Electrical Engineering Student")
                                    st.write("---")



if choice == "APP OBJECTIVE":

    st.write("<h2 style = 'text-align :center;'>APP OBJECTIVE</h2>",
             unsafe_allow_html=True)
    st.write("---")
    st.write("""
The objective of this Data Visualizer App is to provide users with a simple, interactive,
and efficient platform to analyze and visualize data from Excel files. The app allows users 
to upload multiple datasets, explore their contents, and generate 2D graphical representations 
for better understanding of trends and relationships among variables.

Through integrated tools such as NumPy, SciPy, Matplotlib, and Pandas, users can:

1) Perform statistical analysis (mean, median, standard deviation, variance, etc.)

2) Explore correlations between different quantities

3) Apply interpolation techniques for smooth curve fitting

4) Instantly visualize data trends without needing external software

Ultimately, this app aims to bridge data analysis and visualization in one interactive 
environment, enabling students, researchers, and professionals to make insightful 
interpretations from raw data with minimal effort.""")
        
    st.write("---")
    st.write("~ By Samrat Malla")
    st.caption("Pulchowk Campus | Electrical Engineering Student")
    st.write("---")

                    
    

if choice == "ABOUT APP":
    st.write("<h2 style = 'text-align : center;'>ABOUT APP</h2>",unsafe_allow_html=True)
    st.write("---")

    st.write("""
The Data Visualizer App is a Python-based analytical tool built using Streamlit for 
seamless user interaction and visualization. It provides a clean and 
organized interface where users can upload multiple Excel files, view their data in 
tabular form, and create 2D plots to understand relationships between different variables.

The app integrates the power of:

NumPy and Pandas for data handling and computation

Matplotlib for clear and customizable graphical representation

SciPy for interpolation and curve fitting

In addition to visualization, the app performs statistical analysis such as calculating 
mean, median, variance, and correlation coefficients, helping users to derive meaningful 
insights from their datasets.

Developed by Samrat Malla, this app serves as a versatile platform for students, 
engineers, and data enthusiasts who want to analyze, visualize, and understand data
efficiently — all within a single, interactive web interface.""")

        
    st.write("---")
    st.write("~ By Samrat Malla")
    st.caption("Pulchowk Campus | Electrical Engineering Student")
    st.write("---")


                    

                


                    

                




