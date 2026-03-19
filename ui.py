import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title = "AI Sales Agent",layout="wide")

st.title("AI Sales Agent")
st.write("Generate leads + personalized outreach using AI")

query = st.text_input("Enter niche (e.g. fintech startups, AI healthcare)")
if st.button("Generate Leads"):
    if not query:
        st.warning("Please enter a query")
    else:
        with st.spinner("Fetching leads and generating emails..."):
            try:
                response = requests.get(
                    "http://127.0.0.1:8000/leads",
                    params={"query": query}
                )

                data = response.json()

                if isinstance(data,dict) and "error" in data:
                    st.error(data["error"])
                else:
                    df = pd.DataFrame(data)

                    st.success("Leads generated!")
                    st.dataframe(df)

                    st.markdown("### 📧 Emails")
                    for item in data:
                        st.subheader(item["company"])
                        st.write(item["email"])
                        st.divider()

                    csv = df.to_csv(index=False).encode("utf-8")

                    st.download_button(
                        "Download CSV",
                        csv,
                        "leads.csv",
                        "text/csv"
                    )

            except Exception as e:
                st.error(f"Error: {str(e)}")