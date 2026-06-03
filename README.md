# Pokemon-Tracker

## Overview

This is a Flask web application that allows users to search for Pokémon cards by card name and set name. The app fetches data from the Pokémon TCG API and displays relevant card details, including pricing information and links to purchase listings.

---

## 🚀 Features

- Search Pokémon cards by name and set  
- Displays card name and set  
- Shows pricing data (average, low, high, market price)  
- Provides a link to the lowest listing on TCGPlayer  
- Styled frontend using CSS  

---

## 🛠️ Tech Stack

- **Language:** Python  
- **Framework:** Flask  
- **API:** Pokémon TCG API (`https://api.pokemontcg.io`)  
- **HTTP Requests:** requests  
- **Frontend:** HTML, CSS (Jinja templates)  

---

## 📂 Project Structure

```
project-root/
│── app.py
│── static/
│   │── styles.css
│── templates/
│   │── index.html
│   │── about.html
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation & Setup

1. Clone the repository:
```bash
git clone https://github.com/your-username/pokemon-card-app.git
cd pokemon-card-app
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

4. Open your browser and go to:
```
http://127.0.0.1:5000/
```

---

## ▶️ Usage

1. Enter a Pokémon card name  
2. Enter a set name  
3. Submit the form  
4. View results including:
   - Card name  
   - Set name  
   - Price data  
   - Link to lowest listing  

---

## ✅ Requirements
- Python 3.10 or higher   
---
## 📦 Dependencies
```
flask
requests
```

---

## 🎨 Styling (CSS)
The app uses a custom stylesheet located in:
```
static/styles.css
```

