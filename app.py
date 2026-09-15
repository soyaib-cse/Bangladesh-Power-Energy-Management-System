import streamlit as st

st.set_page_config(
    page_title="Bangladesh Power Energy Management",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ Bangladesh Power Energy Management System")
st.write("AI-Driven Predictive Analytics & Digital Twin")

st.divider()

st.subheader("Power System Input")

col1, col2, col3, col4 = st.columns(4)

with col1:
    demand = st.number_input("Current Demand (MW)", min_value=0.0)

with col2:
    solar = st.number_input("Solar Generation (MW)", min_value=0.0)

with col3:
    gas = st.number_input("Gas Generation (MW)", min_value=0.0)

with col4:
    coal = st.number_input("Coal Generation (MW)", min_value=0.0)

st.divider()

if st.button("Calculate Total Generation"):
    total = solar + gas + coal

    st.subheader("Result")
    st.metric("Total Generation", f"{total:.2f} MW")

    if total >= demand:
        st.success("Power Supply is Sufficient ✅")
    else:
        shortage = demand - total
        st.error(f"Power Shortage: {shortage:.2f} MW ⚠️")
