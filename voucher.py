import streamlit as st
import pandas as pd
from database import *  
# import altair as alt
# from UI import *
# from matplotlib import pyplot as plt
# from streamlit_extras.dataframe_explorer import dataframe_explorer
import seaborn as sns 
import altair as alt
# from UI import *
from matplotlib import pyplot as plt
from streamlit_extras.dataframe_explorer import dataframe_explorer

theme_plotly = None

def app():   
    st.title(" 🚖 Voucher Taxi")
    st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)
    
    df = pd.read_excel('voucher.xlsx')
    # result = voucher_data()
    # df = pd.DataFrame(result, columns=['CreatedAt','User', 'Company', 'Department','BudgetCompany', 'Amount','Topup'])
    
    col1, col2=st.columns(2)
    
    with col1:
        # st.title("Select Date Range")
        start_date=st.date_input(label="Start Date")

    with col2:
        end_date=st.date_input(label="End Date")
        # st.error("Business Metrics between[ "+str(start_date)+"] and ["+str(end_date)+"]")

    #compare date
    df2 = df[(df['CreatedAt'] >= str(start_date)) & (df['CreatedAt'] <= str(end_date))]
    
    with st.expander("Filter Excel Dataset"):
        filtered_df = dataframe_explorer(df2, case=False)
        st.dataframe(filtered_df, use_container_width=True)

    b1, b2=st.columns(2)

    with b1:  
        st.subheader('Company & Amount', divider='rainbow',)
        source = pd.DataFrame({
                "Amount (Rp)": df2["Amount"],
                "BudgetCompany": df2["BudgetCompany"]
            })
        
        bar_chart = alt.Chart(source).mark_bar().encode(
                y="sum(Amount (Rp)):Q",
                x=alt.X("BudgetCompany:N", sort="-y")
            )
        st.altair_chart(bar_chart, use_container_width=True,theme=theme_plotly)
    with b2: 
        st.subheader('All Company & Amount', divider='rainbow',)
        energy_source = pd.DataFrame({
            "Amount (Rp)": df2["Amount"],
            "BudgetCompany": df2["BudgetCompany"],
            "Date": df2["CreatedAt"]
            })
        
        #bar Graph
        bar_chart = alt.Chart(energy_source).mark_bar().encode(
                x="month(Date):O",
                y="sum(Amount (Rp)):Q",
                color="BudgetCompany:N"
            )
        st.altair_chart(bar_chart, use_container_width=True,theme=theme_plotly)

    a1, a2=st.columns(2)

    with a1:  
        st.subheader('Department', divider='rainbow',)
        energy_source = pd.DataFrame({
            "Department": df2["Department"],
            "Topup": df2["Topup"],
            "Date": df2["CreatedAt"]
            })
        
        #bar Graph
        bar_chart = alt.Chart(energy_source).mark_bar().encode(
                x="month(Date):O",
                y="count(Topup):Q",
                color="Department:N"
            )
        st.altair_chart(bar_chart, use_container_width=True,theme=theme_plotly)
    with a2:  
        st.subheader('Department & User', divider='rainbow',)
        source = pd.DataFrame({
                "Department": df2["Department"],
                "Topup": df2["Topup"]
            })
        
        bar_chart = alt.Chart(source).mark_bar().encode(
                y="Topup:N",
                x=alt.X("Department:N", sort="-y")
            )
        st.altair_chart(bar_chart, use_container_width=True,theme=theme_plotly) 