import streamlit as st

def main():
    st.title("Find the Largest Number")
    st.write("Enter three numbers below to find the largest among them:")

    a = st.number_input("Enter the first number:")
    b = st.number_input("Enter the second number:")
    c = st.number_input("Enter the third number:")

    if st.button("Find Largest"):
        largest = max(a, b, c)
        st.success(f"The largest number is: {largest}")

if __name__ == "__main__":
    main()
