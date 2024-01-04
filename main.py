import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

import itr, access, voucher, budget, bookingcar, parking, meeting, payment

st.set_page_config(
    page_title="Dashboard DAS", page_icon=":bar_chart:",layout="wide"
)

# st.sidebar.image("images/logo2.png")

class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title":title,
            "function":func,
        })

    def run():
        with st.sidebar:
            app = option_menu(
                menu_title='Dashboard DAS ',
                #icon didapat dari bootstrap
                options=['ITR','Access','Voucher','Budget','Booking Car','Parking','Meeting Room','Payment'],
                icons=['motherboard-fill','person-bounding-box','taxi-front-fill','coin','telephone-inbound-fill','p-square-fill','calendar-date','cash-coin'],
                menu_icon='bar-chart-line-fill',
                default_index=1,
                styles={
                    "container": {"padding": "5!important","background-color":'black'},
        "icon": {"color": "white", "font-size": "14px"}, 
        "nav-link": {"color":"white","font-size": "14px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
        "nav-link-selected": {"background-color": "#02ab21"},}
                
                )
            
        if app == "ITR":
            itr.app()
        if app == "Access":
            access.app()
        if app == "Voucher":
            voucher.app()
        if app == "Budget":
            budget.app()
        if app == "Booking Car":
            bookingcar.app()
        if app == "Parking":
            parking.app()
        if app == "Meeting Room":
            meeting.app()
        if app == "Payment":
            payment.app()

    run()  