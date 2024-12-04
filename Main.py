import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load your real estate dataset
@st.cache
def load_data():
    # Replace 'real_estate_data.csv' with your dataset path
    data = pd.read_csv('real_estate_data.csv')
    return data

# Main dashboard function
def main():
    st.title("Interactive Real Estate Insights")
    st.sidebar.title("Filter Options")

    # Load data
    data = load_data()

    # Sidebar Filters
    location = st.sidebar.multiselect("Select Location(s)", data['Location'].unique(), default=data['Location'].unique())
    min_price, max_price = st.sidebar.slider("Price Range", int(data['Price'].min()), int(data['Price'].max()), (int(data['Price'].min()), int(data['Price'].max())))
    bedrooms = st.sidebar.multiselect("Bedrooms", sorted(data['Bedrooms'].unique()), default=sorted(data['Bedrooms'].unique()))

    # Filtered data
    filtered_data = data[(data['Location'].isin(location)) &
                         (data['Price'] >= min_price) &
                         (data['Price'] <= max_price) &
                         (data['Bedrooms'].isin(bedrooms))]

    # Display Data
    st.subheader("Filtered Data")
    st.write(filtered_data)

    # Price Distribution
    st.subheader("Price Distribution")
    fig, ax = plt.subplots()
    filtered_data['Price'].hist(bins=30, ax=ax)
    ax.set_title("Price Distribution")
    ax.set_xlabel("Price")
    ax.set_ylabel("Frequency")
    st.pyplot(fig)

    # Price vs. Area Scatter Plot
    st.subheader("Price vs. Area")
    st.write("Analyze the relationship between price and area.")
    fig, ax = plt.subplots()
    ax.scatter(filtered_data['Area'], filtered_data['Price'], alpha=0.5)
    ax.set_title("Price vs. Area")
    ax.set_xlabel("Area (sq ft)")
    ax.set_ylabel("Price")
    st.pyplot(fig)

# Run the app
if __name__ == "__main__":
    main()
