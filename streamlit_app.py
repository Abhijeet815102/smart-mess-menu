import streamlit as st
from datetime import datetime, time
from menu import mess_menu

st.set_page_config(
    page_title="Smart Mess Menu",
    page_icon="🍽️",
    layout="centered"
)

st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #0F172A 0%, #1E293B 50%, #0F172A 100%);
        color: white;
    }
    .stMarkdown, .stText, p, h1, h2, h3, label {
        color: white !important;
    }
    .stButton button {
        background-color: #60A5FA;
        color: white;
    }
    .special-item {
        background-color: rgba(96, 165, 250, 0.15);
        padding: 8px 12px;
        border-radius: 8px;
        color: #60A5FA;
        font-weight: bold;
    }
    .avoided-item {
        color: #6B7280;
        font-size: 14px;
    }
</style>
""", unsafe_allow_html=True)

st.title("🍽️ Smart Mess Menu")
st.markdown("---")

# Time-based meal detection
meal_times = {
    "Breakfast": (time(7, 30), time(8, 30)),
    "Lunch": (time(12, 0), time(13, 0)),
    "Snacks": (time(16, 30), time(17, 30)),
    "Dinner": (time(19, 30), time(20, 30))
}

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
current_time = datetime.now().time()
day_index = datetime.now().weekday()
day_to_show = days[day_index]

meal_to_show = "Breakfast"
for meal, (start, end) in meal_times.items():
    if current_time < start:
        meal_to_show = meal
        break
    elif start <= current_time <= end:
        meal_to_show = meal
        break
else:
    day_to_show = days[(day_index + 1) % 7]

def get_special_items(day, meal):
    items = mess_menu[day][meal]
    loved_keywords = ["ice cream", "egg", "omelet", "omelette", "sweet"]
    avoided_keywords = ["brinjal", "eggplant"]
    
    loved = []
    avoided = []
    
    for item in items:
        lower_item = item.lower()
        if any(keyword in lower_item for keyword in avoided_keywords):
            avoided.append(item)
        elif any(keyword in lower_item for keyword in loved_keywords):
            loved.append(item)
    
    return loved, avoided

st.sidebar.header("Browse Menu")
selected_day = st.sidebar.selectbox("Day", days, index=days.index(day_to_show))
selected_meal = st.sidebar.selectbox(
    "Meal", 
    ["Breakfast", "Lunch", "Snacks", "Dinner"],
    index=["Breakfast", "Lunch", "Snacks", "Dinner"].index(meal_to_show)
)

st.markdown(f"### 📅 Showing {selected_day} - {selected_meal}")
st.markdown("---")

items = mess_menu[selected_day][selected_meal]
loved_items, avoided_items = get_special_items(selected_day, selected_meal)

for item in items:
    if item in loved_items:
        st.markdown(f'<div class="special-item">✨ {item}</div>', unsafe_allow_html=True)
    elif item in avoided_items:
        st.markdown(f'<div class="avoided-item">🤮 {item}</div>', unsafe_allow_html=True)
    else:
        st.write(f"• {item}")

st.markdown("---")
with st.expander("📋 Show Complete Menu for Week"):
    for day in days:
        st.markdown(f"### {day}")
        for meal in ["Breakfast", "Lunch", "Snacks", "Dinner"]:
            st.markdown(f"**{meal}:**")
            meal_items = mess_menu[day][meal]
            loved, avoided = get_special_items(day, meal)
            for item in meal_items:
                if item in loved:
                    st.markdown(f'<div class="special-item">✨ {item}</div>', unsafe_allow_html=True)
                elif item in avoided:
                    st.markdown(f'<div class="avoided-item">🤮 {item}</div>', unsafe_allow_html=True)
                else:
                    st.write(f"• {item}")

st.markdown("---")
st.markdown("Made with ❤️ for hostel students")
