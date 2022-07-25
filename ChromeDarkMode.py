
fileDirectory = "/usr/share/applications/google-chrome.desktop"

try:
    appended_strings = 0
    with open(fileDirectory, 'r+', encoding="utf8") as chromeDesktopFile:
        lines = chromeDesktopFile.readlines()
        for i, line in enumerate(lines):
            if line.startswith('Exec=/usr/bin/google-chrome-stable') and line.find('--force-dark-mode') == -1:
                appended_strings += 1
                lines[i] = lines[i].strip() + ' --force-dark-mode\n'
        chromeDesktopFile.seek(0)
        for line in lines:
            chromeDesktopFile.write(line)
except FileNotFoundError:
    print("File missing. We are looking for " + fileDirectory)
else:
    print("Completed successfully, appended", appended_strings, "lines.")
