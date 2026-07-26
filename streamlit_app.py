import streamlit as st
from datetime import datetime, time, timezone, timedelta
from menu import mess_menu

st.cache_data.clear()
st.cache_resource.clear()

st.set_page_config(
    page_title="Smart Mess Menu",
    page_icon="🍽️",
    layout="centered"
)

# Use IST (UTC+5:30) - change this if you target other countries
TIMEZONE_OFFSET = 5.5  # hours
TZ = timezone(timedelta(hours=TIMEZONE_OFFSET))

# Time-based meal detection
meal_times = {
    "Breakfast": (time(7, 30), time(8, 30)),
    "Lunch": (time(12, 0), time(13, 0)),
    "Snacks": (time(16, 30), time(17, 30)),
    "Dinner": (time(19, 30), time(20, 30))
}

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Get current time in IST
current_datetime = datetime.now(TZ)
current_time = current_datetime.time()
day_index = current_datetime.weekday()
day_to_show = days[day_index]

# DEBUG: Show current time info
st.write(f"🕐 Server time (IST): {current_time}")
st.write(f"📅 Day index: {day_index} ({days[day_index]})")
# Determine current meal
meal_to_show = "Breakfast"
for meal, (start, end) in meal_times.items():
    if current_time < start:
        meal_to_show = meal
        break
    elif start <= current_time <= end:
        meal_to_show = meal
        break
else:
    # After dinner - show tomorrow's breakfast
    day_to_show = days[(day_index + 1) % 7]

# ... rest of your code


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
