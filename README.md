# 🩹 Video Fixer 🎬

> *Because nothing is worse than hitting the ⏩ +10s skip button and having your video player crash or freeze forever.*

Ever downloaded a video file that plays fine until you try to seek/skip ahead, only for your player (VidPlayer, VLC, MPV, Phone Gallery) to get stuck, audio to go out of sync, or green corrupt frames to ruin the movie?

**Video Fixer** is a super simple, lightweight CLI tool built to rescue broken, unseekable, and frame-corrupted videos in seconds.

---

## ⚡ How It Works

Video corruption usually happens in two ways:
1. **Broken Seekbar / Index Table**: The video file lost its index map (Moov atom / PTS timestamps). Your player doesn't know where to jump when you skip forward.
   - 🚀 **Fast Mode (Default)**: Rebuilds the index and fixes timestamps in **seconds** without re-encoding (0% quality loss).
2. **Corrupted / Bad Frames**: Actual video bytes got chopped or damaged during download/transfer.
   - 🛠️ **Deep Mode (`--deep`)**: Tells FFmpeg to discard broken packets, ignore decoding errors, and clean up the video stream.

---

## 💻 📱 Works Everywhere (PC & Phone!)

Whether you're on a desktop setup or running python on your phone, **Video Fixer** has your back:

- **Windows**: `winget install ffmpeg`
- **macOS**: `brew install ffmpeg`
- **Linux**: `sudo apt install ffmpeg`
- **Android (Termux)**: `pkg install python ffmpeg`
- **iOS (iSH App)**: `apk add python3 ffmpeg`

---

## 🚀 Quick Start

### 1️⃣ Just Drag & Drop (Interactive)
Run the script and paste or drag your file/folder right into the terminal:
```bash
python video-fixer.py
```

### 2️⃣ Fast Fix (Instant - Fixes Seekbar & Player Skipping)
```bash
python video-fixer.py "my_broken_video.mp4"
```

### 3️⃣ Deep Fix (Re-encodes Bad / Glitched Frames)
```bash
python video-fixer.py "glitched_video.mkv" --deep
```

### 4️⃣ Batch Fix a Folder Full of Videos
```bash
python video-fixer.py "C:\Users\You\Downloads\CorruptedVideos"
```

---

## 🌟 Supported Formats
Supports `.mp4`, `.mkv`, `.avi`, `.mov`, `.flv`, `.wmv`, `.webm`, `.ts`, `.3gp`, `.m4v` and more!

---

## 👤 Author

Crafted by **[Ahmed-GoCode](https://github.com/Ahmed-GoCode)**  
Feel free to ⭐ star the repo if this saved your videos!

---

## 📄 License
MIT License - use it, modify it, share it freely!
