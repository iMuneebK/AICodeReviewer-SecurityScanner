import streamlit as st
from ast_parser import analyze_code_ast
from security_scanner import scan_vulnerabilities

st.set_page_config(page_title="AI Code Reviewer", layout="wide")
st.title("🛡️ Autonomous AI Code Reviewer & Security Scanner")

code = st.text_area("Paste Python Code for Inspection:", height=250)
if st.button("Run Security & Quality Review"):
    ast_res = analyze_code_ast(code)
    sec_res = scan_vulnerabilities(code)
    
    st.subheader("Analysis Summary")
    st.json(ast_res)
    
    if sec_res:
        for item in sec_res:
            st.error(item)
    else:
        st.success("No critical security vulnerabilities found!")
