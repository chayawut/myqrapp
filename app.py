import streamlit as st
import qrcode
from datetime import datetime

st.title("QR Code Generator")


# Initilize session state
if 'clear_input' not in st.session_state:
    st.session_state.clear_input = False
if 'qr_generated' not in st.session_state:
    st.session_state.qr_generated = False

# Input field for QR code data
input_key = "input_data_clear" if st.session_state.clear_input else "input_data"
data = st.text_input("Enter data to generate QR code", key=input_key)

# Button to generate QR code
if st.button("Generate QR Code"):
    if data:
        img = qrcode.make(data)
        img_path = f"qrcodeimg/qrcode_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        img.save(img_path)

# Display the generated QR code
        st.image(img_path, caption="Generated QR Code", width=300)
        st.success("QR Code generated successfully!")

        # clear the input field after generation
        st.session_state.clear_input = True
        st.session_state.qr_generated = True
    else:
        st.error("Please enter some data to generate a QR code.")

# Set focus back to the input field
if st.session_state.clear_input:
    st.write(f"""<script>document.querySelector('input').focus();</script>""",
             unsafe_allow_html=True)
    st.session_state.clear_input = False
