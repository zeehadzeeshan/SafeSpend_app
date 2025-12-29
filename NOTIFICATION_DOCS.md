# 🔔 SafeSpend: Sticky Budget Notification Documentation

The **Sticky Budget Notification** is a core feature of SafeSpend designed to keep you financially disciplined by providing real-time budget updates directly in your Android notification tray. This ensures you always know your spending limits without even opening the app.

---

## 🛠 How It Works

The notification is **"Persistent"** (Unremovable), meaning it stays pinned to your notification area. It updates automatically every time you:

1.  **Add a new expense** (Breakfast, Lunch, Dinner, etc.)
2.  **Edit your monthly budget**
3.  **Open the app** to check your status

---

## 📊 What Information Is Displayed?

The notification is divided into two key metrics:

### 1. **Day: ৳XXX Left** (The Title)

This is your **Daily spending limit**.

- **Definition**: The amount of money you have remaining _specifically for today_.
- **Logic**: It takes your "Today's Allowance" (calculated at midnight) and subtracts any expenses you've already recorded today.
- **Why it matters**: If this number goes to ৳0, it means you have reached your target limit for the day. Any further spending will eat into your future savings.

### 2. **Total Balance: ৳XXXX** (The Body)

This is your **Total Monthly Remaining Balance**.

- **Definition**: Every single Taka remaining in your monthly budget.
- **Logic**: Your `Initial Budget` minus `Total Expenses` recorded since the start of the month.
- **Why it matters**: This gives you the "Big Picture" of your financial health for the rest of the month.

---

## 🔓 Granting Permissions

To see this feature on Android 13 or newer:

1. When you first launch the app, click **"Allow"** when asked for Permission to send notifications.
2. If you missed it, go to **Settings > Apps > SafeSpend > Notifications** and ensure "All SafeSpend notifications" is turned **ON**.

---

## 🎯 Pro-Tips for Discipline

- **Don't Clear It**: On most Android versions, this notification cannot be swiped away. This is intentional! It serves as a constant subconscious reminder of your savings goal.
- **Real-Time Sync**: If you record a meal (e.g., ৳60 for Lunch), pull down your notification tray immediately—you will see your "Day Left" decrease instantly!

---

_SafeSpend — Save Today, Enjoy Tomorrow._
