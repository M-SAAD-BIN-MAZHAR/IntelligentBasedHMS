import streamlit as st
from components import show_header, show_footer, navigate_to_page
from assets.lottie_helper import load_lottie_animation
import streamlit_lottie as st_lottie

st.set_page_config(page_title="Smart HealthCare System", page_icon="🩺", layout="wide")

# 🌸 Custom CSS for animated layout, font, and buttons
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');
    html, body, [class*="css"]  {
        font-family: 'Poppins', sans-serif;
    }

    .main {
        text-align: center;
        transition: all 0.3s ease-in-out;
    }

    /* 🌈 Animated gradient buttons */
    .animated-btn {
        background: linear-gradient(90deg, #00C9FF, #92FE9D);
        border: none;
        color: white;
        padding: 15px 50px;
        border-radius: 40px;
        font-size: 18px;
        font-weight: 600;
        transition: all 0.4s ease-in-out;
        cursor: pointer;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        margin: 10px;
    }
    .animated-btn:hover {
        background: linear-gradient(90deg, #92FE9D, #00C9FF);
        transform: scale(1.07);
        box-shadow: 0 6px 20px rgba(0,0,0,0.25);
    }

    /* 🌸 Falling flower animation */
    .flower {
        position: fixed;
        top: -10px;
        animation: fall linear infinite;
        opacity: 0.9;
        z-index: 9999;
        font-size: 24px;
    }

    @keyframes fall {
        0% { transform: translateY(0) rotate(0deg); opacity: 1; }
        100% { transform: translateY(100vh) rotate(360deg); opacity: 0; }
    }

    /* Center container */
    .button-container {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 50px;
        margin-top: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# Header
show_header()

st.markdown("<h2 style='text-align:center;'>👋 Welcome to the Smart Healthcare System</h2>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center;'>Please select your role below:</h4>", unsafe_allow_html=True)

# ✅ Both buttons styled with HTML (not Streamlit's default)
st.markdown("""
<div class="button-container">
    <button class="animated-btn" id="patient-btn" onclick="triggerFlowers('🌸'); fetch('/patient')">I'm a Patient</button>
    <button class="animated-btn" id="doctor-btn" onclick="triggerFlowers('🌼'); fetch('/doctor')">I'm a Doctor</button>
</div>

<script>
function triggerFlowers(symbol) {
    for (let i = 0; i < 20; i++) {
        let flower = document.createElement('div');
        flower.innerHTML = symbol;
        flower.classList.add('flower');
        flower.style.left = Math.random() * window.innerWidth + 'px';
        flower.style.animationDuration = (5 + Math.random() * 5) + 's';
        document.body.appendChild(flower);
        setTimeout(() => flower.remove(), 10000);
    }
}
</script>
""", unsafe_allow_html=True)

# 🚀 Detect which role user picked using Streamlit’s form buttons
col1, col2 = st.columns(2)
with col1:
    if st.button("Launch Patient Dashboard", use_container_width=True):
        navigate_to_page("pages/patient_dashboard.py")
with col2:
    if st.button("Launch Doctor Dashboard", use_container_width=True):
        navigate_to_page("pages/doctor_dashboard.py")

# 🌿 Lottie animation at bottom
lottie_health = load_lottie_animation("https://assets4.lottiefiles.com/packages/lf20_w51pcehl.json")
st_lottie.st_lottie(lottie_health, height=320, key="lottie_health")

show_footer()
