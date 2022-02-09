import streamlit as st
from PIL import Image

st.title("MEL BEAUTY")

img = Image.open("mel_beauty.png")
st.image(img, width=300)


st.header("Melanin Popping Beauty Space")
st.subheader("Book us for your day")

st.text("Enter the makeup service that you want")
st.success("Brown Skin Beauties")

if st.checkbox("Select/Unselect"):
    st.text("Selected")

service_type = st.radio("Select service type: ", ("Home service", "Physical service"))
if (service_type == "Home service"):
    st.success("Home service")
else:
    st.success("Physical service")
    
st.text("Select the look that you want for your occasion")
look = st.selectbox("Select look: ", 
                    ["None", "Simple look", "Bridal look", "Skin-like look", "Trad look"])
st.write("Confirmed, you have selected: ", look)

name = st.text_input("Enter your name", "Type your name ...")
if(st.button("Submit")):
    result = name.title()
    st.success(result)
    
st.write("Select the appointment date for your big day")
appointment_date = st.date_input("pick a date")
st.time_input("pick a time")

email_address = st.text_input("Enter your email address", "Type it here ...")

if(st.checkbox("Done")):
    st.info("You have succesfully entered your details, we will send you an email containing the price and other details for your big day")


referral_level = st.slider("Would you refer us to your friends on a scale of 10?", 1, 10)
st.text("Selected: {}".format(referral_level))
    
