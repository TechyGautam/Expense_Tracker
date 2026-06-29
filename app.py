import database
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
st.title(":blue[Expense] :red[Tracker] 📅",text_alignment="center")

def add_expense():

    print("Add Your Today Expense")
    amount = float(input("Enter the amount: "))
    category = input("Enter the category: ")
    date = input("Enter the date (YYYY-MM-DD): ")
    description = input("Enter a description (optional): ")

    db = database.DB()
    db.add_data(amount, category, date, description)
    database.conn.commit()

def view_expenses():
    db = database.DB()
    expenses = db.get_data() #this give data in rows
    print(expenses)



# def menu():
#     while True:
#         print("Enter 1 for Adding Expenses.")
#         print("Enter 2 for View Expenses.")
#         print("Enter space for exit")
#         user = input("Enter Your Choice: ")
#         if user == "1":
#             add_expense()
#         elif user == "2":
#             view_expenses()
#         else:
#             break

# menu()

opt = st.sidebar.selectbox("Made By TEES",["Add Expenses","View Expenses","Delete Expenses","View Analytic","Upload File"])
if opt == "Add Expenses":
    categories = [
    "Food",
    "Transport",
    "Shopping",
    "Entertainment",
    "Education",
    "Health",
    "Other"
]   
    st.logo("💾")
    st.title("Add Your Today Expenses")
    amt = st.number_input("Enter the amount:",value=None,placeholder="XXX..")
    category = st.selectbox("Category", categories)
    date = st.text_input("Enter the date (YYYY-MM-DD): ")
    description = st.text_input("Enter a description (optional): ")
    if st.button("Add My Expense"):
            db = database.DB()
            db.add_data(amt, category, date, description)
            st.success("Your Expenses Is Add Sucessfully..")
            # st.session_state.clear()
            # st.rerun()
            # database.conn.commit()


elif opt == "View Expenses":
    st.title("This is Your all Expenses")
    db = database.DB()
    expense = db.get_data()
    st.dataframe(expense)
elif opt == "Delete Expenses":
    st.title("Delete Your Expenses here")
    delete_id = st.number_input("Enter ID Number for Delete Expense",value=None,placeholder="ID Number")
    db = database.DB()
    if st.button("Delete"):
        db.delete_data(delete_id)
        st.success(f"Delete ID Number {delete_id} successfully ☠")

elif opt == "View Analytic":
    st.title("Analytic's")
    db = database.DB()
    d = db.category_total() #return data frame
    st.bar_chart(data=d.set_index("Category"))
    fig, ax = plt.subplots()

    ax.pie(
        d["Total Amount"],
        labels=d["Category"],
        autopct="%1.1f%%"
    )

    ax.set_title("Expense Distribution")

    st.pyplot(fig)

elif opt == "Upload File":
    st.title("Upload Your File here")
    st.write("Get all info related to your file")
    uploaded_file = st.file_uploader("Upload CSV File",type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df)

