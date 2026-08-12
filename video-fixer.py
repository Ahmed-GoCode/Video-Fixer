#!/usr/bin/env python3
# Video Fixer by Ahmed-GoCode
# Fixes unseekable videos, broken seekbars, and corrupted frames.

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path

VIDEO_EXTS = {'.mp4', '.mkv', '.avi', '.mov', '.flv', '.wmv', '.webm', '.ts', '.3gp', '.m4v'}

def fix_file(src, dst=None, deep_mode=False):
    src_path = Path(src).resolve()
    if not src_path.exists():
        print(f"❌ File not found: {src}")
        return False

    # Default output file name if not provided
    if not dst:
        out_path = src_path.parent / f"fixed_{src_path.name}"
    else:
        out_path = Path(dst).resolve()
        if out_path.is_dir():
            out_path = out_path / f"fixed_{src_path.name}"

    out_path.parent.mkdir(parents=True, exist_ok=True)

    print(f"\n🎬 Fixing: {src_path.name}")
    print(f"🔧 Mode: {'Deep Re-encode (for bad frames)' if deep_mode else 'Fast Fix (rebuild seek index)'}")

    # FFmpeg parameters to salvage corrupt streams & rebuild timestamps
    cmd = [
        "ffmpeg", "-y",
        "-err_detect", "ignore_err",
        "-fflags", "+genpts+discardcorrupt",
        "-i", str(src_path)
    ]

    if deep_mode:
        # Full re-encode to clean corrupt frames
        cmd += ["-c:v", "libx264", "-preset", "fast", "-crf", "22", "-c:a", "aac", "-b:a", "128k"]
    else:
        # Fast copy to fix broken seek tables instantly
        cmd += ["-c", "copy"]

    cmd += ["-avoid_negative_ts", "make_zero", str(out_path)]

    try:
        proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if proc.returncode == 0 and out_path.exists() and out_path.stat().st_size > 0:
            print(f"✅ Saved fixed video to: {out_path}")
            return True
        else:
            print(f"❌ Failed to fix {src_path.name}. Try running with --deep mode.")
            return False
    except Exception as err:
        print(f"⚠️ Error running FFmpeg: {err}")
        return False

def main():
    if not shutil.which("ffmpeg"):
        print("❌ FFmpeg is missing from your system!")
        print("Please install FFmpeg to use this script:")
        print("  - Windows: winget install ffmpeg")
        print("  - Mac: brew install ffmpeg")
        print("  - Linux / Termux: apt install ffmpeg")
        sys.exit(1)

    parser = argparse.ArgumentParser(description="Rescue broken or unseekable video files.")
    parser.add_argument("target", nargs="?", help="Video file or folder path")
    parser.add_argument("-o", "--output", help="Output file or folder destination")
    parser.add_argument("--deep", action="store_true", help="Deep repair mode (re-encodes video to fix bad frames)")
    args = parser.parse_args()

    target = args.target
    if not target:
        print("🎥 Video Fixer by Ahmed-GoCode")
        target = input("Paste video file or folder path here: ").strip().strip('"\'')

    if not target:
        print("No target specified. Exiting.")
        sys.exit(0)

    target_path = Path(target).resolve()

    if target_path.is_file():
        fix_file(target_path, args.output, args.deep)
    elif target_path.is_dir():
        videos = [f for f in target_path.rglob("*") if f.suffix.lower() in VIDEO_EXTS and not f.name.startswith("fixed_")]
        if not videos:
            print("No supported video files found in folder.")
            return
        
        print(f"Found {len(videos)} video(s) to process...")
        for vid in videos:
            fix_file(vid, args.output, args.deep)
        print("\n🎉 All done!")
    else:
        print(f"❌ Invalid path: {target}")

if __name__ == "__main__":
    main()
