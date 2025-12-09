import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import streamlit as st
import pandas as pd

st.title("CSV File Uploader")

# Use st.file_uploader to allow users to upload a CSV file
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the uploaded CSV file into a pandas DataFrame
    df = pd.read_csv(uploaded_file)

    # Display the DataFrame
    st.write("Data Preview:")
    st.dataframe(df)
else:
    st.info("Please upload a CSV file to see the data.")
