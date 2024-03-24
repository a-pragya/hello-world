import os

apps = ["Zoom", "Slack", ,"Notion", "Google Calendar", "Gmail", "iTerm"]
message = "Hi there \U0001f44b \n\n"

for app in apps:
    message += f"Opening {app}...\n"

os.system("fortune | cowsay -f moose")
print(message)
os.system("open -a Zoom.us")
os.system("open -a Slack")
os.system("open -a Notion")
os.system("open -a 'Google Chrome' https://calendar.google.com")
os.system("open -a 'Google Chrome' https://mail.google.com")
os.system("open -a 'iTerm 2")

#common tasks that can be done with hello-world command
#open vscode
#open intellij

