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

if __name__ == '__main__':
    names = load_company_names('/Users/salonitilekar/efficient-search/company_names_100k.csv')
    trie = build_trie(names)
    prefix = input('Enter prefix to search: ')
    results = search_companies(trie, prefix)
    print(f'Found {len(results)} matches:')
    for name in results[:20]:  # Show only first 20 matches
        print(name) 