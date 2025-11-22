import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import os 
from scipy.interpolate import interp1d
from sklearn.preprocessing import MinMaxScaler
import statistics as s
os.system("cls")

def welcome_message():
    st.markdown("""
    <h1 style='text-align: center; 
               font-family: "Monotype Corsiva", cursive; 
               font-size: 48px;  
               text-shadow: 1px 1px 2px #aaa;'>
        Data Analyzer
    </h1>
""", unsafe_allow_html=True)
    
    st.write("---")

    st.write("""
    <h5> Welcome to the Data Analyzer ,<br><br>
    This tool allows you to upload your data, explore them interactively and visualize 
    trends with multiple graphing options. You can analyze statistical properties, compare 
    relationships between variables and generate clear insights all through an 
    intuitive interface.<br><br>  
    Upload your files and let's begin your analysis instantly.</h5>""",unsafe_allow_html=True)

    st.write("---")

def final_message():
    st.write("---")
    st.caption("~ By Samrat Malla ")
    st.caption("Pulchwok Campus | Electrical Engineering")
    st.write("---")

def app_objective_message():
    st.write("""
<h3>App Objective: <br></h3>
<h5>The primary objective of <strong>Data Analyzer</strong> is to empower users with a seamless, 
code-free environment for exploring and understanding their data.<br><br>

This app is crafted to:<br><br>

- Simplify Data Handling : Allow users to upload Excel files and instantly access structured data views.<br><br>

- Enhance Visual Understanding : Provide intuitive 2D plots, bar graphs, and multigraphs to uncover trends, patterns, and relationships.<br><br>

- Support Informed Decision-Making : Deliver statistical summaries that help users interpret data with clarity and confidence.<br><br>

- Bridge Engineering & Insight : Blend technical precision with user-friendly design — making it ideal for students, professionals, and data enthusiasts alike.<br><br>

Ultimately, Data Analyzer aims to turn raw numbers into visual stories and actionable insights — fast, elegant, and accessible to all.
    """, unsafe_allow_html=True)


def about_app_message():
    st.write("""
<h3>About App: <br></h3>
<h5><strong>Data Analyzer</strong> is a powerful, user-friendly tool designed to transform raw Excel data 
into meaningful insights.<br><br>

Built with precision and clarity in mind, this app empowers users to:<br><br>

- Upload Excel Files : Seamlessly import .xlsx files for instant analysis.<br><br>

- Visualize in 2D Graphs : Plot clean, interactive 2D line graphs to explore trends and patterns.<br><br>

- Generate Bar Graphs & Multigraphs : Compare multiple variables side-by-side or overlay them for deeper correlation insights.<br><br>

- Perform Statistical Analysis : Instantly compute key metrics like mean, median, mode, standard deviation, and more — all without writing a single line of code.<br><br>

Whether you're a student, analyst, or engineer, <strong>Data Analyzer</strong> simplifies data exploration 
while maintaining technical depth. It’s built for clarity, speed, and elegance — just like the code behind it.
    """, unsafe_allow_html=True)

def app_objective_message():
    st.write("""
<h3>App Objective: <br></h3>
<h5>The primary objective of <strong>Data Analyzer</strong> is to empower users with a seamless, 
code-free environment for exploring and understanding their data.<br><br>

This app is crafted to:<br><br>

- Simplify Data Handling : Allow users to upload Excel files and instantly access structured data views.<br><br>

- Enhance Visual Understanding : Provide intuitive 2D plots, bar graphs, and multigraphs to uncover trends, patterns, and relationships.<br><br>

- Support Informed Decision-Making : Deliver statistical summaries that help users interpret data with clarity and confidence.<br><br>

- Bridge Engineering & Insight : Blend technical precision with user-friendly design — making it ideal for students, professionals, and data enthusiasts alike.<br><br>

Ultimately, Data Analyzer aims to turn raw numbers into visual stories and actionable insights — fast, elegant, and accessible to all.
    """, unsafe_allow_html=True)

class Data_Loader:
    def __init__(self,files):
        self.files = files

    def Program_Flow(self):

        st.write("---")
        self.file_names = [file.name for file in self.files]
        if self.files:
            self.selected_files = st.multiselect("SELECT A SINGLE FILE FOR ANALYSIS :",
                    options=self.file_names,max_selections=1)
            if self.selected_files:
                st.write("---")
                for file in self.files:
                    if file.name in self.selected_files:
                        self.file_parts = file.name.split(".")
                        data = pd.read_excel(file)

                        data.index.name = "INDEX"
                        self.data = data
                        self.data.dropna()

                        Data_Loader_object.display_data()

                        Data_Loader_object.visualize_options()

                        if self.choice =="BAR GRAPH":
                            Data_Loader_object.bar_graph()

                        if self.choice=="2D GRAPH":
                            Data_Loader_object.graph()

                        if self.choice =="LINE GRAPH":
                            Data_Loader_object.line_graph()

                        if self.choice == "MULTI GRAPH":
                            Data_Loader_object.multi_graph()
                                        
                        Data_Loader_object.statistical_analysis()
                        
                        Data_Loader_object.final_message()

                        

    def display_data(self):
        st.subheader("FILE READING SECTION :")
        st.write(f"<h3 style = 'text-align:center;'>{self.file_parts[0]}</h3>",
                                    unsafe_allow_html=True)
        st.caption("SHOWING FILE DATA :")
        st.write(self.data)
        st.write("---")

    def visualize_options(self):
        st.subheader("DATA VISUALIZATION SECTION :")
        st.caption("SELECT APPROPRIATE TYPE OF VISUALIZATION ")
        self.choice = st.radio(label="SELECT YOUR CHOICE :",options=["BAR GRAPH",
                    "2D GRAPH","MULTI GRAPH","NONE"])
        st.write("---")

    def multi_graph(self):
        st.write("MULTIPLE GRAPH VISUALIZATION :")
        st.caption("SELECTION FOR VISUALIZATION :")
        c1,c2 = st.columns(2)
        with c1:
            x_entity = st.selectbox(label = "SELECT X AXIS ENTITY :",
                                options = self.data.columns)
            x_data = np.array(self.data[x_entity])
            st.caption("SELECT SINGLE ENTITY IN X DIMENSION")

        with c2:
            y_entity_list = st.multiselect(label = "SELECT Y AXIS ENTITIES :",
                                options = self.data.columns)
            st.caption("SELECT MULTIPLE ENTITIES IN Y DIMENSION")
        
        st.write("---")

        fig,axs = plt.subplots()
        fig.suptitle("MULTIPLE GRAPH VISUALIZATION")
        y_scaled = MinMaxScaler().fit_transform(self.data[y_entity_list])
        for index,y_entity in enumerate(y_entity_list):
            y_data = y_scaled[:,index]
            axs.plot(x_data,y_data,"o--",label = f"{x_entity} vs {y_entity}")
        
        axs.grid(True)
        axs.set_xlabel("TIME (S)")
        axs.set_ylabel("NORMALIZED INDEX")
        plt.tight_layout()
        plt.legend()
        st.pyplot(fig)
        st.write("---")
            

    def bar_graph(self):
        st.write("BAR GRAPH VISUALIZATION :")
        st.caption("SELECTION FOR VISUALIZATION :")
        c1,c2 = st.columns(2)
        with c1:
            x_entity = st.selectbox(label = "SELECT X AXIS ENTITY :",
                                options = self.data.columns)
            x_data = np.array(self.data[x_entity])

        with c2:
            y_entity = st.selectbox(label = "SELECT Y AXIS ENTITY :",
                                options = self.data.columns)
            y_data = np.array(self.data[y_entity])
        
        st.write("---")

        if x_entity!=y_entity:
            fig,axs = plt.subplots()
            aesthetic_colors = [
    "#FF6F61",  # Coral Pink
    "#6B5B95",  # Royal Purple
    "#88B04B",  # Leaf Green
    "#F7CAC9",  # Rose Quartz
    "#92A8D1",  # Serenity Blue
    "#955251",  # Marsala
    "#B565A7",  # Orchid
    "#009B77",  # Teal
    "#DD4124",  # Tangerine
    "#45B8AC",  # Aqua Mint
    "#EFC050",  # Sunflower
    "#5B5EA6",  # Indigo
    "#9B2335",  # Crimson Red
    "#DFCFBE",  # Sand
    "#55B4B0",  # Turquoise
]
            
            fig.suptitle(f"{x_entity} vs {y_entity}",fontsize = 20)
            axs.bar(x_data,y_data,edgecolor = "black",color = aesthetic_colors)
            axs.set_xlabel(f"{x_entity}")
            axs.set_ylabel(f"{y_entity}")
            plt.tight_layout()
            st.pyplot(fig)      

            st.write("---")

    def final_message(self):
        st.write("---")
        st.caption("~ BY SAMRAT MALLA")
        st.caption("PULCHOWK CAMPUS | ELECTRICAL ENGINEERING")
        st.write("---")

    def graph(self):
        st.write("2D GRAPH VISUALIZATION :")
        st.caption("SELECTION FOR VISUALIZATION ")
        c1,c2 = st.columns(2)
        with c1:
            x_entity = st.selectbox(label = "SELECT X AXIS ENTITY :",
                                options = self.data.columns)
            x_data = np.array(self.data[x_entity])

        with c2:
            y_entity = st.selectbox(label = "SELECT Y AXIS ENTITY :",
                                options = self.data.columns)
            y_data = np.array(self.data[y_entity])
        
        st.write("---")
        st.caption("CHOICE FOR SMOOTHING THE CURVE")
        int_choice = st.radio(label="INTERPOLATION ON GRAPH :",options=["YES","NO"])
        st.write(("---"))

        if int_choice == "NO":
            if x_entity!=y_entity:
                fig,axs = plt.subplots()
                fig.suptitle(f"{x_entity} vs {y_entity}",fontsize = 20)
                axs.plot(x_data,y_data,"o--")
                axs.set_xlabel(f"{x_entity}")
                axs.set_xlim([min(x_data)-1,max(x_data)+1])
                axs.set_ylim([min(y_data)-1,max(y_data)+1])
                axs.set_ylabel(f"{y_entity}")
                axs.grid(True)
                plt.tight_layout()
                st.pyplot(fig)      
                st.write("---")

        else :
            if x_entity!=y_entity:
                fig,axs = plt.subplots()
                fig.suptitle(f"{x_entity} vs {y_entity}",fontsize = 20)
                y_f = interp1d(x_data,y_data,kind="cubic")
                x_data_new = np.linspace(min(x_data),max(x_data),1000)
                y_data_new = y_f(x_data_new)
                axs.plot(x_data_new,y_data_new,"--")
                axs.scatter(x_data,y_data)
                axs.set_xlabel(f"{x_entity}")
                axs.set_ylabel(f"{y_entity}")
                axs.grid(True)
                axs.set_xlim([min(x_data)-1,max(x_data)+1])
                axs.set_ylim([min(y_data)-1,max(y_data)+1])
                plt.tight_layout()
                st.pyplot(fig)      
                st.write("---")

    def statistical_analysis(self):
        st.subheader("STATISTICAL ANALYSIS SECTION :")
        st.caption("SELECTION OF DATA :")
        self.selection = st.selectbox(label = "SELECT ENTITY FOR ANALYSIS :",
            options = self.data.columns)    

        st.write("---")
        st.caption("DESCRIBING ENTITY STATISTICALLY :")
        st.write("QUANTITY :",self.selection)
        c1,c2 = st.columns(2)
        with c1:
           
            st.write(f"MAXIMUM VALUE : {max(self.data[self.selection])}")
            st.write(f"MINIMUM VALUE : {min(self.data[self.selection])}")
            st.write(f"MEDIAN VALUE : {round(np.median(self.data[self.selection]),3)}")
            st.write(f"MODE VALUE : {round(s.mode(self.data[self.selection]),3)}")

        with c2:
            st.write(f"STANDARD DEVIATION : {round(np.std(self.data[self.selection]),3)}")
            st.write(f"VARIANCE VALUE : {round(np.var(self.data[self.selection]),3)}")
            st.write(f"MEAN VALUE : {round(np.mean(self.data[self.selection]),3)}")
            st.write(f"RANGE VALUE : {np.round(round(np.max(self.data[self.selection]),2)
                                      -round(np.min(self.data[self.selection]),2),3)}")
        
        st.write("---")
            
        st.write("RELATIONSHIP :")
        st.caption("FINDING CORRELATION BETWEEN VARIABLES ")
        c1,c2 = st.columns(2)
        with c1:
            entity_1 = st.selectbox(label="SELECT FIRST ENTITY :",
                        options=self.data.columns)
            
        with c2:
            entity_2 = st.selectbox(label="SELECT SECOND ENTITY :",
                        options=self.data.columns)
        
        if entity_1!=entity_2:
            corr_coef = str(np.round(np.corrcoef
                        (self.data[entity_1],self.data[entity_2])[0,1],3))


            st.write("CORRELATION COEFFICIENT :",corr_coef)
            if float(corr_coef) >0:
                st.write("STATUS : DIRECT RELATIONSHIP")
            
            elif float(corr_coef)<0:
                st.write("STATUS : INVERSE RELATIONSHIP")
            
            else:
                st.write("STATUS : NO RELATIONSHIP")


st.sidebar.header("Data Analyzer App")
st.sidebar.write("---")
side_choice = st.sidebar.radio(label = " ",
                 options=["ANALYZE DATA","ABOUT APP","APP OBJECTIVE"])
st.sidebar.write("---")
st.sidebar.caption("~ By Samrat Malla")
st.sidebar.write("---")

if side_choice =="ANALYZE DATA":
    welcome_message()
    st.subheader("FILE UPLOADING SECTION :")
    files = st.file_uploader("UPLOAD EXCEL DATA FILES :",type="xlsx",
                            accept_multiple_files=True)
    Data_Loader_object = Data_Loader(files)
    Data_Loader_object.Program_Flow()

if side_choice == "ABOUT APP":
    st.markdown("""
    <h1 style='text-align: center; 
               font-family: "Monotype Corsiva", cursive; 
               font-size: 48px;  
               text-shadow: 1px 1px 2px #aaa;'>
        Data Analyzer
    </h1>
""", unsafe_allow_html=True)
    st.write("---")
    about_app_message()
    final_message()

if side_choice=="APP OBJECTIVE":
    st.markdown("""
    <h1 style='text-align: center; 
               font-family: "Monotype Corsiva", cursive; 
               font-size: 48px;  
               text-shadow: 1px 1px 2px #aaa;'>
        Data Analyzer
    </h1>
""", unsafe_allow_html=True)
    
    st.write("---")
    app_objective_message()
    final_message()
    
