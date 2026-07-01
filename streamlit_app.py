 import streamlit as st

# ==========================================
# 1. THE EXPANDED NESTED DICTIONARY MENU
# ==========================================
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

# ==========================================
# 2. INITIALIZE THE SHOPPING CART MEMORY
# ==========================================
if "cart" not in st.session_state:
    st.session_state.cart = []  # Holds tuples of (item_name, price)

# ==========================================
# 3. INTERFACE LAYOUT
# ==========================================
st.title("🏪 Smart Canteen Ordering System")
st.write("Browse categories, customize your order, and calculate your dynamic bill.")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🍔 Step 1: Select Your Food")
    
    # Dropdown 1: Main Categories
    category_list = list(canteen_menu.keys())
    selected_category = st.selectbox("Choose a category:", category_list)
    
    # Dropdown 2: Automatically updates items based on Category Choice!
    sub_items = canteen_menu[selected_category]
    selected_item = st.selectbox("Choose specific item:", list(sub_items.keys()))
    
    # Fetch the exact price instantly from the dictionary
    item_price = sub_items[selected_item]
    st.info(f"Price: ${item_price}")
    
    # Add to Cart Button
    if st.button("➕ Add Item to Order"):
        st.session_state.cart.append((selected_item, item_price))
        st.success(f"Added {selected_item} to cart!")

    # Clear Cart option
    if st.button("🗑️ Clear Entire Order"):
        st.session_state.cart = []
        st.rerun()

with col2:
    st.subheader("🧾 Step 2: Live Invoice")
    
    # Calculate current base subtotal from the cart memory
    base_total = sum(price for item, price in st.session_state.cart)
    
    # Display current cart items
    if st.session_state.cart:
        for item, price in st.session_state.cart:
            st.write(f"• {item} — ${price}")
        st.markdown("---")
    else:
        st.write("*Your cart is empty. Please add items.*")
    
    # Student Profile and Discount Calculation
    status = st.selectbox("Select Student Status:", ["Guest", "Hosteler", "Day Scholar"])
    
    discount = 0
    if status == "Hosteler":
        discount = 4
    elif status == "Day Scholar" and base_total > 6:
        discount = 1

    # Final math execution
    final_bill = max(0, base_total - discount)
    
    # Visual metrics display
    st.metric(label="Items Subtotal", value=f"${base_total}")
    st.metric(label="Status Discount", value=f"-${discount}")
    st.header(f"Total Due: ${final_bill}")
