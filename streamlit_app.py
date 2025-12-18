import streamlit as st 

if not st.user.is_logged_in:
    st.header("This app is private.")
    st.subheader("Please log in.")
    st.button("Log in with Google", on_click=st.login)
else:
    st.write("Secret Content")
    st.write(st.user)
    if st.checkbox("Show tokens (not safe!)"):
        st.write(st.user.tokens.access)

    st.button("Logout", on_click=st.logout)

