import streamlit as st
import streamlit.components.v1 as components
def main():
    with open('test.html', 'r') as f:
        html_string = f.read()
    components.html(html_string, height=600)

if __name__ == '__main__':
    main()