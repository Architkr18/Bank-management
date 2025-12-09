import streamlit as st
from hello import Bank

st.set_page_config(page_title="Simple Bank App", layout="centered")
st.title("🏦 Welcome to Streamlit Bank")

menu = st.sidebar.selectbox("Choose Action", ["Create Account", "Deposit", "Withdraw", "Show Details", "Update Info", "Delete Account"])

if menu == "Create Account":
    st.subheader("Create New Account")
    name = st.text_input("Your Name")
    age = st.number_input("Your Age", min_value=0, step=1, value=0)
    email = st.text_input("Your Email")
    pin = st.text_input("4-digit PIN", type="password", max_chars=4)

    if st.button("Create"):
        if name and email and pin and age > 0:
            try:
                user, msg = Bank.create_account(name, int(age), email, int(pin))
                if user:
                    st.success(msg)
                    st.info(f"Your Account Number: {user['accountNo.']}")
                else:
                    st.error(msg)
            except ValueError:
                st.error("Invalid PIN format. Please enter numbers only.")
        else:
            st.warning("Please fill all fields correctly")

elif menu == "Deposit":
    st.subheader("Deposit Money")
    acc_no = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1, value=0)

    if st.button("Deposit"):
        if acc_no and pin and amount > 0:
            try:
                success, msg = Bank.deposit(acc_no, int(pin), int(amount))
                if success:
                    st.success(msg)
                else:
                    st.error(msg)
            except ValueError:
                st.error("Invalid PIN or amount format")
        else:
            st.warning("Please fill all fields correctly")

elif menu == "Withdraw":
    st.subheader("Withdraw Money")
    acc_no = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1, value=0)

    if st.button("Withdraw"):
        if acc_no and pin and amount > 0:
            try:
                success, msg = Bank.withdraw(acc_no, int(pin), int(amount))
                if success:
                    st.success(msg)
                else:
                    st.error(msg)
            except ValueError:
                st.error("Invalid PIN or amount format")
        else:
            st.warning("Please fill all fields correctly")

elif menu == "Show Details":
    st.subheader("Account Details")
    acc_no = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Show"):
        if acc_no and pin:
            try:
                user = Bank.find_user(acc_no, int(pin))
                if user:
                    st.json(user)
                else:
                    st.error("Invalid account number or PIN")
            except ValueError:
                st.error("Invalid PIN format")
        else:
            st.warning("Please fill all fields")

elif menu == "Update Info":
    st.subheader("Update Your Info")
    acc_no = st.text_input("Account Number")
    pin = st.text_input("Current PIN", type="password")

    name = st.text_input("New Name (Leave empty to keep current)")
    email = st.text_input("New Email (Leave empty to keep current)")
    new_pin = st.text_input("New PIN (Leave empty to keep current)", type="password")

    if st.button("Update"):
        if acc_no and pin:
            try:
                # Only pass non-empty values
                success, msg = Bank.update_user(
                    acc_no, 
                    int(pin), 
                    name if name else None,
                    email if email else None,
                    new_pin if new_pin else None
                )
                if success:
                    st.success(msg)
                else:
                    st.error(msg)
            except ValueError:
                st.error("Invalid PIN format")
        else:
            st.warning("Please enter account number and PIN")

elif menu == "Delete Account":
    st.subheader("Delete Account")
    acc_no = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    
    confirm = st.checkbox("I confirm I want to delete my account")

    if st.button("Delete", type="primary"):
        if acc_no and pin and confirm:
            try:
                success, msg = Bank.delete_user(acc_no, int(pin))
                if success:
                    st.success(msg)
                else:
                    st.error(msg)
            except ValueError:
                st.error("Invalid PIN format")
        elif not confirm:
            st.warning("Please confirm you want to delete the account")
        else:
            st.warning("Please fill all fields")