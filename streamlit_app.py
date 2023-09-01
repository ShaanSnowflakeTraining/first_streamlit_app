import streamlit

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 and Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinage & Rocket Smoothie')
streamlit.text('🐔 Hard boiled free range eggs')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas as pd
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

## Adding a list so customers can choose the fruits they want in thier smoothie
streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index))

##Display table on page
streamlit.dataframe(my_fruit_list)





