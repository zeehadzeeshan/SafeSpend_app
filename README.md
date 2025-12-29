# Smart Budget Manager - Mobile App

## ✅ APK Successfully Built!

**Location:** `android/app/build/outputs/apk/release/app-release-unsigned.apk`  
**Size:** 2.75 MB

---

## 📱 Installation Instructions

### Option 1: Install Unsigned APK (For Testing)

1. Transfer the APK to your Android device
2. Enable "Install from Unknown Sources" in Settings
3. Open the APK file and install

### Option 2: Sign the APK (Recommended for Distribution)

To create a signed APK for the Play Store or wider distribution:

```bash
# Generate a keystore (one-time setup)
keytool -genkey -v -keystore my-release-key.keystore -alias my-key-alias -keyalg RSA -keysize 2048 -validity 10000

# Sign the APK
jarsigner -verbose -sigalg SHA256withRSA -digestalg SHA-256 -keystore my-release-key.keystore android/app/build/outputs/apk/release/app-release-unsigned.apk my-key-alias

# Align the APK (optional but recommended)
zipalign -v 4 android/app/build/outputs/apk/release/app-release-unsigned.apk SmartBudget-signed.apk
```

---

## 🛠️ Rebuilding the APK

To rebuild after making changes to the web app:

```bash
# Run the build script
build_apk.bat
```

Or manually:

```bash
npm install
npx cap sync
cd android
gradlew.bat assembleRelease
```

---

## 📋 Features Implemented

✅ **Budget Initialization** - Set total budget and days  
✅ **Smart Budget Splitting** - 20/40/40 rule (Breakfast/Lunch/Dinner)  
✅ **Minimum Thresholds** - Ensures realistic meal budgets  
✅ **Menu Manager** - Add/remove custom menu items  
✅ **AI Meal Suggestions** - Local algorithm picks best items from your menu  
✅ **Daily Spending Log** - Track expenses and update budget  
✅ **Data Persistence** - Uses LocalStorage (survives app restarts)  
✅ **Premium Dark UI** - Slate/Sky color scheme matching Desktop app

---

## 🔧 Technical Stack

- **Framework:** Capacitor 5 (Web-to-Native)
- **Frontend:** Vanilla HTML/CSS/JavaScript
- **Storage:** LocalStorage API
- **Build:** Gradle 8.7 + Android SDK 33
- **Min Android:** API 22 (Android 5.1+)

---

## 📝 Notes

- The APK is **unsigned** by default - suitable for personal testing
- For production, sign the APK with your own keystore
- The app works 100% offline (no internet required after installation)
- All budget calculations match the Desktop Python app exactly
