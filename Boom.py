import streamlit as st

# ตั้งค่าหน้าตาเบราว์เซอร์
st.set_page_config(page_title=" บูมรักแพนนี่ ", page_icon="💖")

# ตกแต่งสไตล์น่ารักๆ หวานๆ ด้วย CSS
st.markdown("""
    <style>
    .stApp {
        background-color: #FFF0F5;
    }
    h1 {
        color: #FF69B4;
        text-align: center;
    }
    .stButton>button {
        background-color: #FFB6C1;
        color: white;
        border-radius: 20px;
        border: none;
        padding: 10px 24px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #FF69B4;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# ส่วนแสดงผล UI
st.title(" ให้แพนนี่ดูได้คนเดียวนะ ")
st.write(" กรอกรหัสผ่านหน้าจอของไอบูมมาาา")

# ช่องกรอกรหัสผ่าน
n = st.text_input("รหัสผ่าน:", type="password", placeholder="เช่น 551489")

# ปุ่มกดส่งรหัสผ่าน
if st.button(" ปลดล็อกกก "):
    if n == "248024":
        st.balloons()  # เอฟเฟกต์ลูกโป่งลอย
        st.success(" ถูกต้องจ้าาาา")
        st.markdown(" สุขสันต์วันครบรอบย้อนหลังนะแพนนี่ เค้ารักเธอม้ากกกก ช่วงนี้สู้ๆนะะะ ใกล้สอบแล้วว รักเธอที่สุดดด คนเก่งงงง ❤")
    else:
        st.error(" ไม่ถูก กดใหม่เลย งอนด้วย หึ")