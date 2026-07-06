import webbrowser
import os
import datetime
import urllib.parse


def execute_command(command):
    command = command.lower().strip()

    if not command:
        return "Please enter a command"

    # Exit
    if any(word in command for word in ["exit", "quit", "close assistant", "stop assistant"]):
        return "EXIT"

    # Google Search
    if command.startswith("search ") or "search google for" in command:
        query = command.replace("search google for", "").replace("search", "").strip()
        if query:
            webbrowser.open(f"https://www.google.com/search?q={urllib.parse.quote(query)}")
            return f"Searching Google for {query}"
        return "Please tell me what to search"

    # YouTube Search
    # YouTube Search
    if "youtube" in command and any(word in command for word in ["search", "find", "play", "tutorial", "video", "videos"]):
        query = command

        remove_words = [
            "search youtube for", "search on youtube", "search youtube",
            "find youtube", "find on youtube",
            "play", "on youtube", "youtube",
            "video", "videos"
        ]

        for word in remove_words:
            query = query.replace(word, "")

        query = query.strip()

        if query:
            webbrowser.open(f"https://www.youtube.com/results?search_query={urllib.parse.quote(query)}")
            return f"Searching YouTube for {query}"            

    # Open websites
    websites = {
        "google": "https://www.google.com",
        "youtube": "https://www.youtube.com",
        "gmail": "https://mail.google.com",
        "linkedin": "https://www.linkedin.com",
        "github": "https://github.com",
        "chatgpt": "https://chatgpt.com",
        "spotify": "https://open.spotify.com",
        "amazon": "https://www.amazon.in",
        "flipkart": "https://www.flipkart.com",
    }

    for site, url in websites.items():
        if site in command:
            webbrowser.open(url)
            return f"Opening {site.capitalize()}"

    # Windows apps
    if any(word in command for word in ["calculator", "calc", "calculate"]):
        os.system("calc")
        return "Opening Calculator"

    if any(word in command for word in ["notepad", "notes", "text editor"]):
        os.system("notepad")
        return "Opening Notepad"

    if "paint" in command or "mspaint" in command:
        os.system("mspaint")
        return "Opening Paint"

    if "command prompt" in command or "cmd" in command:
        os.system("start cmd")
        return "Opening Command Prompt"

    if "vs code" in command or "visual studio code" in command or "vscode" in command:
        os.system("code")
        return "Opening VS Code"

    # Date and time
    if "time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        return f"The current time is {now}"

    if "date" in command:
        today = datetime.datetime.now().strftime("%d %B %Y")
        return f"Today's date is {today}"

    if "day" in command:
        day = datetime.datetime.now().strftime("%A")
        return f"Today is {day}"

    # Help
    if "help" in command or "what can you do" in command:
        return (
            "I can open websites, search Google or YouTube, open apps like Calculator, "
            "Notepad, Paint, CMD, VS Code, and tell time, date, or day."
        )

    return "Sorry, I don't know that command yet"