import streamlit as st
import requests

def google_linkedin_search(domain, country, api_key, cse_id, num_results=10):
    query = f'"{domain}" "{country}" site:linkedin.com/in'
    url = "https://www.googleapis.com/customsearch/v1"

    params = {
        "key": api_key,
        "cx": cse_id,
        "q": query,
        "num": num_results
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        results = response.json().get("items", [])

        profiles = []
        for item in results:
            profiles.append({
                "title": item.get("title"),
                "link": item.get("link"),
                "snippet": item.get("snippet")
            })

        return profiles

    except requests.exceptions.RequestException as e:
        st.error(f"Error: {e}")
        return []

# Streamlit UI
st.set_page_config(page_title="LinkedIn Profile Finder", page_icon="🔍", layout="centered")

st.title("🔍 LinkedIn Profile Search")
st.markdown("Search for top LinkedIn profiles based on a **domain** and **country** using Google Custom Search API.")

with st.form("search_form"):
    domain_input = st.text_input("Enter domain/role/skill (e.g., 'Data Scientist')", "")
    country_input = st.text_input("Enter country (e.g., 'India')", "")
    submitted = st.form_submit_button("Search")

if submitted:
    if not domain_input or not country_input:
        st.warning("Please fill in both fields.")
    else:
        with st.spinner("Searching..."):
            # TODO: Replace with your actual credentials
            GOOGLE_API_KEY = "AIzaSy"+"BM0k6Dyke8Lyan"+"ZuTVxRyfLd1zSh8YO1c"
            GOOGLE_CSE_ID = "f0d8"+"60f6e"+"2d214bb0"

            results = google_linkedin_search(domain_input, country_input, GOOGLE_API_KEY, GOOGLE_CSE_ID)

        if results:
            st.success(f"Found {len(results)} profiles:")
            for idx, profile in enumerate(results, start=1):
                st.markdown(f"**{idx}. [{profile['title']}]({profile['link']})**")
                st.caption(profile['snippet'])
        else:
            st.warning("No profiles found.")