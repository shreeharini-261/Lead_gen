# LinkedIn Profile Finder 🔍

A Streamlit web application that helps you find LinkedIn profiles based on domain/role/skill and country using Google Custom Search API.

![Demo Screenshot](https://via.placeholder.com/800x500?text=LinkedIn+Profile+Finder+Demo) 
*(Replace with actual screenshot)*

## Features ✨

- Search LinkedIn profiles by domain/role/skill (e.g., "Data Scientist")
- Filter profiles by country (e.g., "India")
- Clean, user-friendly interface with responsive design
- Displays profile title, link, and snippet from search results
- Built with Python and Streamlit for easy deployment

## Live Demo 🌐

The application is deployed on Streamlit Cloud:  
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://leadgen-kzpsjxwjbahf3vwmkbtdn4.streamlit.app/)

## How It Works ⚙️

1. User enters a domain/role/skill and country
2. The app constructs a custom Google search query targeting LinkedIn profiles
3. Uses Google Custom Search JSON API to fetch results
4. Displays the profiles with clickable links

## Setup & Installation 🛠️

### Prerequisites

- Python 3.7+
- Google Custom Search JSON API key
- Google Custom Search Engine ID

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/linkedin-profile-finder.git
   cd linkedin-profile-finder
