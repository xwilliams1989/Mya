import streamlit as st

# Page config
st.set_page_config(page_title="Mya – The Quote Brain", page_icon="🧠", layout="centered")

# Header
st.title("🧠 Mya – The Quote Brain")
st.subheader("Internal Agent Profile (Not Seen by Customers)")

# Agent Overview
st.markdown("### 🤖 Agent Name: **Mya**")
st.markdown("**Role:** 🧠 Quote Brain  \n**Visibility:** Internal Only (Never seen by customers)")

# Function
st.markdown("### 💼 Primary Function")
st.write("""
Mya handles **all pricing and quote calculations** for the company across every service:
- Local moves
- Long-distance
- Packing
- Junk removal
- Storage
She powers the backend quote engine with accurate, rules-based logic.
""")

# Responsibilities
st.markdown("### 🛠️ Responsibilities")
st.markdown("""
- Calculate instant quotes using zip-to-zip mileage  
- Determine service type: Local vs Long Distance  
- Apply fees (labor, truck, stairs, elevator, rush)  
- Pull accurate hourly rates based on mover count  
- Generate full quote breakdowns for automation  
- Return data for use in GHL, SMS, or internal flows  
""")

# How She's Used
st.markdown("### 🔄 Used By Other Agents")
st.write("""
Mya is called by other agents (like **Aven**, **Gigi**, or **Echo**) when a quote is needed.
""")
st.code("""
Example:
Aven captures a lead → passes move details to Mya  
→ Mya returns quote breakdown → Gigi sends it to client via GHL/SMS
""", language='markdown')

# Footer
st.markdown("---")
st.markdown("This logic agent powers all quote intelligence across the company. Mya is never customer-facing.")

