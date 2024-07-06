import json
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import datetime as dt
import plotly.express as px
import streamlit as st
from streamlit_option_menu import option_menu


df_final=pd.read_csv("C:/Users/USER/Desktop/Robin vs/guvi_projects/airbnb_final.csv")


#Streamlit Part:
st.set_page_config(layout="wide",
                   initial_sidebar_state="expanded")
st.header(':rainbow[Airbnb Analysis]')
st.write("***Airbnb Data Analysis***")

opt=st.radio(label="",options=["Home", "Analysis", "Insights"],
             index=0,
             format_func=lambda x:x.title(),
             horizontal=True,
             key="Menu")

if opt == "Home":

    st.write(" ")
    st.write(" ")     
    st.markdown("#### :Green[*OVERVIEW* ]")
    st.markdown("##### This project aims to analyze Airbnb data & perform data cleaning and preparation, develop interactive geospatial visualizations, and create dynamic plots to gain insights into pricing variations, availability patterns, and location-based trends in the Airbnb marketplace.")

    st.markdown("#### :Green[*DOMAIN* ] ")
    st.markdown(" ##### Travel Industry, Property Management and Tourism ")
    st.markdown("""
                #### :Green[*TECHNOLOGIES USED*]    
        
                ##### Python scripting, Data Preprocessing, Visualization,EDA, Streamlit, PowerBI


                """)
    

elif opt == "Analysis":
    st.write(" ")

    on=st.checkbox("Price Anlaysis")

    if on:
        st.write(" ")
        #Review Score And Price Analysis:
        review_score_price=df_final.groupby('Review_scores')['Price'].mean().reset_index()
        #review_score_price

        fig=px.bar(review_score_price, x='Review_scores', y='Price',title='Review Score And Avarage Price',width=800,height=600)
        
        st.plotly_chart(fig)

        #Avarage Price With Property type:
        avg_price_pro_type=df_final.groupby("Property_type")['Price'].mean().reset_index()
        avg_price_pro_type

        fig=px.line(avg_price_pro_type, x='Property_type', y='Price',title="Avarage Price with Property Types",
                width=800, height=600, color_discrete_sequence=px.colors.sequential.Viridis, hover_name="Property_type")


        fig.update_traces(mode='markers+lines')
        st.plotly_chart(fig)

        #Avarage Price with Host Location:
        avg_loca_price=df_final.groupby('Host_location')['Price'].mean().reset_index()
        avg_loca_price

        fig=px.line(avg_loca_price, x='Host_location', y='Price', title='Avarage price with Host Location',
             width=800, height=800,hover_name='Host_location', color_discrete_sequence=px.colors.sequential.Rainbow)

        st.plotly_chart(fig)

#Availaibility Analaysis:

    on = st.checkbox("Availability Analaysis")

    if on:
        st.write(" ")
        #Availaibility 365 with country:
        availa_coun=df_final.groupby('Country')['Availability_365'].mean().reset_index()
        availa_coun

        fig=px.pie(data_frame=df_final, names='Country', values='Availability_365', title=" Average Availaibility From Country",
                color_discrete_sequence=px.colors.sequential.Magenta_r, height=600, width=800, hole=0.2)

        st.plotly_chart(fig)

        #Avarage Availibility From Rooms with price:
        avg_room_avail=df_final.groupby('Room_type').agg({'Availability_365':'mean','Price':'mean'}).reset_index()

        fig=px.scatter_3d(avg_room_avail, x='Room_type', z='Availability_365', y='Price',
                        title='Avarage Availibility from Rooms', width=600, height=800, color='Availability_365',
                        color_continuous_scale='Plotly3',labels={'Room_type':'Room Type','Availability_365':'Avagrage Avail','price':'Price'})
        
        st.plotly_chart(fig)

        #Average Availaibility in Property types:
        avg_prop_avail=df_final.groupby('Property_type')['Availability_365'].mean()

        fig=px.strip(data_frame=df_final, x='Property_type', y='Availability_365',
                title="Average Availaibility with Property Types", 
                labels={'Property_type':'Property Types','Availability_365':'Average Availability (Days)'},
                width=800, height=600, hover_name='Property_type', color_discrete_sequence=px.colors.sequential.Magenta_r)
        
        st.plotly_chart(fig)

    on = st.checkbox("Rating Analysis")

    if on:
        st.write(" ")

#Rating Analysis:

        #Average Review rating From Country:
        avg_review_coun=df_final.groupby('Country')['Review_scores'].mean().reset_index()
        avg_review_coun=avg_review_coun.sort_values(by='Review_scores')

        fig=px.box(data_frame=df_final, x='Country', y='Review_scores',title='Average Reviews From Country',
                width=800,height=600, hover_name='Country')
        
        st.plotly_chart(fig)

        #Average Rating From Rooms:
        avg_room_rating=df_final.groupby('Room_type')['Review_scores'].mean().reset_index()
        avg_room_rating

        fig=px.pie(data_frame=df_final, names='Room_type', values='Review_scores', title='Average Rating From Room Types',
                width=800, height=600, hole=0.2, color_discrete_sequence=px.colors.sequential.RdBu_r)
        
        st.plotly_chart(fig)

        #Average Review Score in Property Type:
        avg_rating_host_name=df_final.groupby('Property_type')['No_of_reviews'].mean().reset_index()
        avg_rating_host_name

        fig=px.area(data_frame=df_final, x='Property_type', 
                        y='No_of_reviews', title="Average Rating for Host",hover_name='Property_type',
                        width=1000, height=500)
        #fig.update_traces(mode='markers+lines')
        
        st.plotly_chart(fig)
       

#Mothly Price Analysis:
    on = st.checkbox("Monthly Price Analysis")

    if on:
        st.write(" ")

        #Weekily Price & Monthly price:
        week_month=df_final.groupby('Room_type')['monthly_price'].mean().reset_index()
        week_month

        fig=px.bar(data_frame=df_final, x='Room_type', y='monthly_price',title='Average Monthly Price Room Types',
                hover_name='Room_type', color='weekly_price')
       
        st.plotly_chart(fig)

        #Average Monthly Price in Country:
        avg_mon_host_name=df_final.groupby('Country')['monthly_price'].mean().reset_index()
        avg_mon_host_name

        fig=px.pie(data_frame=df_final, names='Country', values='monthly_price', title='Average Monthly Price In Country',
                width=800,height=600,hole=0.1,color='weekly_price')
        
        st.plotly_chart(fig)

    on = st.checkbox("Host Analysis")

    if on:
        st.write(" ")

        #Host Analysis:
        ave_host_resp=df_final.groupby('Country')['Host_response_rate'].mean().reset_index()
        ave_host_resp

        fig=px.histogram(data_frame=df_final, x='Country', y='Host_response_rate', title='Average Response host in country',
                        width=800, height=600)
        
        st.plotly_chart(fig)

        #Host Name and Price:
        avg_review_host=df_final.groupby('Host_name')['Price'].mean().reset_index()

        fig=px.bar(data_frame=df_final, x='Host_name', y='Price', title='Average Price in Host Name', 
                hover_name='Host_name',color_discrete_sequence=px.colors.sequential.Magenta_r,height=600)
        
        st.plotly_chart(fig)


    on = st.checkbox("Property Analysis")

    if on:
        st.write(" ")

        #Property Analysis:
        pr_df = df_final.groupby('Property_type',as_index=False)['Price'].mean().sort_values(by='Price')
        fig = px.bar(data_frame=pr_df,x='Property_type',y='Price',color='Price', hover_name='Property_type', title='Property Type In Price')
        
        st.plotly_chart(fig)

        #Availability 365 with Property Types:
        chart=df_final.groupby('Property_type',as_index=False)['Availability_365'].mean().sort_values(by='Availability_365')
        fig=px.line(data_frame=chart, x='Availability_365', y='Property_type', title='Property Type With Availability 365',
            width=800, height=600, hover_name='Property_type')

        st.plotly_chart(fig)

        #Review Score rating with Property Types:
        chart=df_final.groupby('Property_type',as_index=False)['Review_scores'].mean().sort_values(by='Review_scores')
        fig=px.bar(data_frame=chart, x='Review_scores', y='Property_type', title='Property Type With Availability 365',
            width=800, height=600, hover_name='Property_type')
        
        st.plotly_chart(fig)

    on = st.checkbox("Geospatial Visualization")

    if on:
        st.write(" ")

        #Geo Visulation:
        df_filtered = df_final[df_final['Availability_365'] < 365]
        fig = px.scatter_mapbox(df_filtered, lat="Latitude", lon="Longitude", color="Availability_365",
                                hover_name="Country", hover_data={ "Country": True, "Availability_365": True},
                                color_continuous_scale=px.colors.sequential.Viridis,
                                zoom=1,width=1300,height=700)
        fig.update_layout(mapbox_style="open-street-map", title="Listing Availability by Location")
        st.plotly_chart(fig)



elif opt == "Insights":
                
     title = st.selectbox("Select the questions",
                        [
                        '01. Top 10 Host With Highest Number Of Listings',
                        '02. Total Listing in each Room Type',
                        '03. Availibility_365 in Property Types',
                        '04. Most Price In Property Types',
                        '05. Host Response average in Country',
                        '06. Monthly Price From Country'])


     if title == '01. Top 10 Host With Highest Number Of Listings':
                
                #Top 10 Host Names:

                df=df_final.groupby(['Host_name']).size().reset_index(name='Host_listings_count').sort_values(by='Host_listings_count',ascending=False)[:10]
                fig=px.bar(df, title='Top 10 Property Types', x='Host_listings_count', 
                        y='Host_name', orientation='h',color='Host_name',color_discrete_sequence=px.colors.sequential.Agsunset)
                fig.update_layout(showlegend=False)
                
                st.plotly_chart(fig)

     elif title == '02. Total Listing in each Room Type':
          
                #Total Lisiting in each Rooms:
                df=df_final.groupby(['Room_type']).size().reset_index(name='Host_listings_count')
                fig=px.pie(df, title='Total Listings in each Room_types', names='Room_type',width=800, height=600,hole=0.1,
                        values='Host_listings_count',color_discrete_sequence=px.colors.sequential.Rainbow)
                fig.update_traces(textposition='outside', textinfo='value+label')
                
                st.plotly_chart(fig)

     elif title == '03. Availibility_365 in Property Types':

                #Availability 365 with Property Types:
               chart=df_final.groupby(['Property_type']).size().reset_index(name='Availability_365')
               fig=px.line(data_frame=chart, x='Property_type', y='Availability_365', title='Property Type With Availability 365',
                width=800, height=600, hover_name='Property_type')
               
               st.plotly_chart(fig)

     elif title == '04. Most Price In Property Types':
           
                #Most Price In Property Types:

                
                most_price_pro_type=df_final.groupby(["Property_type"]).size().reset_index(name='Price')

                fig=px.line(most_price_pro_type, x='Property_type', y='Price',title="Most Price in Property Types",
                        width=800, height=600, color_discrete_sequence=px.colors.sequential.Viridis, hover_name="Property_type")

                fig.update_traces(mode='markers+lines')
                
                st.plotly_chart(fig)

     elif title == '05. Host Response average in Country':

                #Host Response in average country:
                 ave_host_resp=df_final.groupby('Country')['Host_response_rate'].mean().reset_index()

                 fig=px.histogram(data_frame=df_final, x='Country', y='Host_response_rate', title='Average Response host in country',
                 width=800, height=600)
                 
                 st.plotly_chart(fig)

     elif title == '06. Monthly Price From Country':
            
                avg_mon_host_name=df_final.groupby('Country')['monthly_price'].mean().reset_index()

                fig=px.pie(data_frame=df_final, names='Country', values='monthly_price', title='Average Monthly Price In Country',
                width=800,height=600,hole=0.1,color='weekly_price')
                
                st.plotly_chart(fig)

