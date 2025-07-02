import streamlit as st
import pandas as pd
from trie import Trie

def load_company_names(csv_path):
    df = pd.read_csv(csv_path)
    return df['name'].dropna().astype(str).tolist()

def build_trie(names):
    trie = Trie()
    for name in names:
        trie.insert(name)
    return trie

def search_companies(trie, prefix):
    return trie.starts_with(prefix)

# Load data and build trie
@st.cache_data
def load_data():
    names = load_company_names('/Users/salonitilekar/efficient-search/company_names_100k.csv')
    trie = build_trie(names)
    return trie

def main():
    st.title("Company Name Predictive Search")
    st.write("Enter a prefix to search for company names")
    
    # Load trie
    trie = load_data()
    
    # Search input
    prefix = st.text_input("Enter prefix:", "")
    
    if prefix:
        results = search_companies(trie, prefix)
        st.write(f"Found {len(results)} matches:")
        
        # Display results
        if results:
            for i, name in enumerate(results[:50]):  # Show first 50 results
                st.write(f"{i+1}. {name}")
        else:
            st.write("No matches found.")

if __name__ == "__main__":
    main() 