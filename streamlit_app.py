import streamlit as st

canteen_menu = {
    "🍗 Biryanis": {
        "Chicken Biryani": 8,
        "Mutton Biryani": 10,
        "Veg Biryani": 6,
        "Egg Biryani": 7
    },
    "🧃 Juices & Drinks": {
        "Mango Juice": 3,
        "Orange Juice": 3,
        "Apple Juice": 4,
        "Cold Coffee": 4
    },
    "🍟 Snacks & Starters": {
        "Gobi Manchurian": 4,
        "Samosa (2pcs)": 2,
        "French Fries": 3,
        "Chicken 65": 6
    }
}

if "cart" not in st.session_state:
    st.session_state.cart = []

st.title("🏪 Smart Canteen Ordering System")
st.write("Browse categories, customize your order, and calculate your dynamic bill.")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🍔 Step 1: Select Your Food")
    category_list = list(canteen_menu.keys())
    selected_category = st.selectbox("Choose a category:", category_list)
    sub_items = canteen_menu[selected_category]
    selected_item = st.selectbox("Choose specific item:", list(sub_items.keys()))
    item_price = sub_items[selected_item]
    st.info(f"Price: ${item_price}")
    if st.button("➕ Add Item to Order"):
        st.session_state.cart.append((selected_item, item_price))
        st.success(f"Added {selected_item} to cart!")
    if st.button("🗑️ Clear Entire Order"):
        st.session_state.cart = []
        st.rerun()

with col2:
    st.subheader("🧾 Step 2: Live Invoice")
    base_total = sum(price for item, price in st.session_state.cart)
    if st.session_state.cart:
        for item, price in st.session_state.cart:
            st.write(f"• {item} — ${price}")
        st.markdown("---")
    else:
        st.write("*Your cart is empty. Please add items.*")
    status = st.selectbox("Select Student Status:", ["Guest", "Hosteler", "Day Scholar"])
    discount = 0
    if status == "Hosteler":
        discount = 4
    elif status == "Day Scholar" and base_total > 6:
        discount = 1
    final_bill = max(0, base_total - discount)
    st.metric(label="Items Subtotal", value=f"${base_total}")
    st.metric(label="Status Discount", value=f"-${discount}")
    st.header(f"Total Due: ${final_bill}")
