# 🥗 Smart Budget Manager
### *Eat Smart, Save Smarter - The AI-Powered Meal Budgeting Companion*

[![GitHub Release](https://img.shields.io/github/v/release/zeehadzeeshan/SafeSpend_app?style=flat-square)](https://github.com/zeehadzeeshan/SafeSpend_app/releases)
[![Build Status](https://img.shields.io/badge/Build-Capacitor-blue?style=flat-square)](https://capacitorjs.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square)](https://opensource.org/licenses/MIT)

Smart Budget Manager is a mobile application built with Capacitor that helps users manage their daily meal expenses without sacrificing health. In an era of rising costs, the app uses intelligent algorithms to suggest balanced, protein-rich Bangladeshi meals tailored to your specific budget.

---

## 🚀 The Problem It Solves

Maintaining a healthy diet on a strict budget is a complex balancing act. Many people struggle with:
- **Financial Overspending:** Spending too much on one meal and starving on the next.
- **Decision Fatigue:** Struggling to decide what to eat everyday.
- **Unhealthy Choices:** Often, cheap food means low protein and high carbs.

**Smart Budget Manager** solves this by automating the math. It splits your daily budget intelligently, ensures "heavy" meals (like dinner) get priority, and suggest specific, local meal options that provide the best nutritional value for your money.

---

## ✨ Key Features

### 🧠 AI-Driven Meal Suggestions
*   **Bangladeshi Context:** A built-in database of 18 culturally appropriate healthy meals.
*   **Protein-to-Price Optimization:** Suggestions priority meals with the best protein ratio.
*   **Unique Meal Logic:** Ensures you never get the same suggestion twice in a day.
*   **Dinner Priority (Vari Khabar):** Automatically allocates more resources and "heaviness" to dinner.

### 💰 Intelligent Budgeting
*   **20/40/40 Split:** Dynamic allocation across Breakfast, Lunch, and Dinner.
*   **Smart Rebalancing:** If your budget is critically low, the app automatically skips less essential meals (like breakfast) to ensure you can afford a proper lunch and dinner.
*   **Minimum Thresholds:** Prevents unrealistic suggestions that wouldn't cover the cost of a basic meal.

### 📋 Personalized Menu Management
*   **Custom Items:** Add your own favorite meals with their local prices.
*   **Persistence:** All your menu data and budgets are saved locally on your device.

---

## 🛠️ Technical Stack

- **Platform:** [Capacitor 5](https://capacitorjs.com/) (Web-to-Native framework)
- **Frontend:** Pure HTML5, Vanilla JavaScript, and CSS3
- **Logic:** Custom localized decision-making algorithms
- **Storage:** Web Storage API (LocalStorage) for offline-first performance
- **UI Design:** Premium "Slate & Sky" dark mode aesthetic

---

## 📱 Installation & Setup

### 📥 Download APK
You can download the latest **SafeSpend_Debug.apk** from the [GitHub Releases](https://github.com/zeehadzeeshan/SafeSpend_app/releases) page.

1.  Transfer the APK to your Android device.
2.  Allow "Installation from Unknown Sources" in your settings.
3.  Open and install.

### ⚙️ Development & Rebuilding
If you wish to modify the app and rebuild it:

```bash
# Install dependencies
npm install

# Sync changes to Android/iOS projects
npx cap sync

# Build Android APK (requires Android SDK)
cd android
./gradlew.bat assembleDebug
```

---

## 🔗 Project Links

- **Main Repository:** [GitHub](https://github.com/zeehadzeeshan/SafeSpend_app)
- **Issue Tracker:** [Report Bugs](https://github.com/zeehadzeeshan/SafeSpend_app/issues)

Developed with ❤️ for health-conscious budgeters.
