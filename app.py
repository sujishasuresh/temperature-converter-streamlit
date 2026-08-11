import streamlit as st

def main():
    st.title("Temperature Converter")
    # To add more vertical space between your widgets
    st.write("")
    # container acts like a reference to a section of your Streamlit page
    container=st.container()
    unit=container.radio("Is this temperature in Celsius or Fahrenheit?",["Celsius","Fahrenheit"])
    st.write("")  
    temperature=container.number_input("Enter your temperature")
    st.write("")  
    btn=container.button("Submit",use_container_width=True)
    st.write("")  
    if btn:    
        if unit=="Celsius":
            # Converting the temperature to Fahrenheit using the formula
            f = (temperature * 1.8) + 32
            st.write("")  
            container.write(f"Fahrenheit: {f}")
        elif unit=="Fahrenheit":
            # Converting the temperature to Celsius
            c = (temperature - 32) / 1.8
            st.write("")  
            container.write(f"Celsius: {c}")

main()