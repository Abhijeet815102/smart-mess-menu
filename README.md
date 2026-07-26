# 🍽️ Smart Mess Menu

A web app that shows what's being served in the hostel mess right now, with special item highlighting and weekly menu browsing.

🔗 **Live App:** https://smart-mess-menu-bfixets4tyap9hzwyxjmgn.streamlit.app

## 🎯 Problem

Checking the hostel mess menu every day is inconvenient. Students usually want to know only one thing:

> **"What meal is available right now?"**

And sometimes they want to know specific items they love (like Ice Cream on Thursday dinner) or avoid (like Brinjal on Monday lunch).

## ✨ Features

- **Current Meal Detection** — Automatically shows what's being served right now based on time
- **Timezone-Aware** — Uses IST (Indian Standard Time) by default
- **Day Selector** — Browse any day of the week
- **Meal Selector** — Switch between Breakfast, Lunch, Snacks, Dinner
- **Special Item Highlighting** — Items you love get marked with ✨
- **Avoided Item Marking** — Items you don't like get marked with 🤮
- **Complete Weekly Menu** — Expandable view of all 7 days
- **Mobile-Friendly** — Works on any device with a browser
- **No Installation Required** — Just open the link

## 🕐 Meal Timings

| Meal | Time |
|------|------|
| Breakfast | 7:30 AM - 8:30 AM |
| Lunch | 12:00 PM - 1:00 PM |
| Snacks | 4:30 PM - 5:30 PM |
| Dinner | 7:30 PM - 8:30 PM |

*After 8:30 PM, the app shows tomorrow's breakfast*

## 🛠️ Tech Stack

- **Python** — Core logic
- **Streamlit** — Web framework
- **datetime** — Time-based meal detection

## 🚀 Running Locally

### Prerequisites
- Python 3.8 or higher
- pip

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Abhijeet815102/smart-mess-menu.git
cd smart-mess-menu

2. Install dependencies:
pip install -r requirements.txt

3. Run the app:
streamlit run streamlit_app.py

4. Open your browser at http://localhost:8501


🎨 Item Classification
The app automatically classifies items based on keywords:

Loved items (✨):

Ice Cream
Egg, Omelet, Omelette
Sweet
Avoided items (🤮):

Brinjal, Eggplant
📱 Screenshots
Coming soon

🤝 Contributing
This is a personal project, but suggestions are welcome! Open an issue or submit a pull request.

📝 License
MIT License — feel free to use this code for your own projects.

👤 Author
Abhijeet

GitHub: @Abhijeet815102
Project: 100 Problems Before 100 Projects
🙏 Acknowledgments
Built as part of the "100 Problems Before 100 Projects" challenge — solving real problems one project at a time.