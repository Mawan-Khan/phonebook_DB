import streamlit as st
import mysql.connector

# Database connection
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="phonebook_db"
    )

# Save the data to the phonebook
def save():
    name = st.text_input("Enter Name:")
    contact_no = st.text_input("Enter Contact No:")
    email = st.text_input("Enter Email:")
    if st.button("Save"):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO contacts (name, contact_no, email) VALUES (%s, %s, %s)", (name, contact_no, email))
        conn.commit()
        cursor.close()
        conn.close()
        st.success("*****Data Saved Successfully*****")

# Fetch the saved data from phonebook
def retrieve():
    name = st.text_input("Enter name to find the data:")
    if st.button("Find"):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM contacts WHERE name LIKE %s", (f"%{name}%",))
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        if results:
            st.success("*****Record Found:*****")
            for row in results:
                st.write(f"Name: {row[1]}, Contact No: {row[2]}, Email: {row[3]}")
        else:
            st.error("No records found.")

# The input menu of the phonebook
def menu():
    st.title("Phonebook App")
    choice = st.selectbox("Choose an option", ["Add new Contact", "Find a Contact", "Quit"])
    if choice == "Add new Contact":
        save()
    elif choice == "Find a Contact":
        retrieve()
    elif choice == "Quit":
        st.stop()

# Call to the menu from main
if __name__ == "__main__":
    menu()
