import argparse
import json
import sys
import os

def load_transcript(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def summarize_text(text):
    # Placeholder: simple summarization - take first 3 sentences
    sentences = text.split('. ')
    summary = '. '.join(sentences[:3]) + ('.' if len(sentences) > 3 else '')
    return summary

def insert_timestamps(summary, timestamps):
    # timestamps: dict {segment_index: timestamp_string}
    # For simplicity, we append timestamps at end of summary as footnotes
    if not timestamps:
        return summary
    footnotes = []
    for idx, ts in sorted(timestamps.items()):
        footnotes.append(f"[{idx}] {ts}")
    if footnotes:
        summary += "\n\nTimestamps:\n" + "\n".join(footnotes)
    return summary

def main():
    parser = argparse.ArgumentParser(description='Generate meeting summary with optional Read.ai timestamps')
    parser.add_argument('--transcript', required=True, help='Path to transcript text file')
    parser.add_argument('--timestamps', help='Path to JSON file containing timestamps')
    parser.add_argument('--output', required=True, help='Path to output summary file')
    args = parser.parse_args()

    transcript = load_transcript(args.transcript)
    summary = summarize_text(transcript)

    timestamps = None
    if args.timestamps:
        if not os.path.exists(args.timestamps):
            sys.exit(f"Timestamp file not found: {args.timestamps}")
        with open(args.timestamps, 'r', encoding='utf-8') as f:
            timestamps = json.load(f)

    summary_with_ts = insert_timestamps(summary, timestamps)

    with open(args.output, 'w', encoding='utf-8') as f:
        f.write(summary_with_ts)

if __name__ == '__main__':
    main()