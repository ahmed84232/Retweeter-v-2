# 🔁 Twitter Retweeter Bot

A Python script that automatically detects and retweets tweets on-screen using image recognition. It uses `pyautogui` and listens to keyboard input to start or stop retweeting.

---

## 📦 Requirements

- Python 3.7+
- Windows OS
- `pyautogui`, `pyperclip`, `pynput`

Install dependencies:

```bash
pip install pyautogui pyperclip pynput
```

---

## ⚙️ Setup

Place the following image files in the same directory as the script:

- `Retweet1.png`
- `Retweet2.png`
- `Retweet3.png`

Make sure the images represent how the retweet buttons appear on your screen.

---

## 🚀 Usage

1. Open Twitter in a browser and go to the desired page.
2. Run the script:

```bash
python retweeter.py
```

3. Press the **Left Arrow key** to start retweeting.
4. Press the **Right Arrow key** to stop.

The script will scroll and retweet up to 300 tweets or until manually stopped.

---

## ⚠️ Warning

- **Use this tool responsibly.** Automating Twitter actions can result in account restrictions or suspension.
- Ensure you have the rights to automate the account being used.

---

## 📜 License

This project is open source and free for anyone to use or modify under the MIT License.
