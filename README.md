# flatpak-installer


This repository contains a Python script that allows you to install multiple Flatpaks at once. The script makes use of a function install_flatpaks that takes a list of Flatpaks as its parameter. The function adds the Flathub repository, and then installs each Flatpak from the list. The function also uses a try-except block to catch any error that might occur during the installation process, and print the error message accordingly.

Usage
Clone the repository:

git clone https://github.com/yourusername/flatpak-installer.git
Change the current directory to the repository:

cd flatpak-installer
Install the flatpaks by running the script:

python install_flatpaks.py
Customizing the script
To customize the script, edit the list of flatpaks in the script before running it, you can add or remove flatpaks as per your need.


flatpaks = [
    "org.gimp.GIMP",
    "org.libreoffice.LibreOffice",
    "com.spotify.Client",
    "org.videolan.VLC",
    "org.audacityteam.Audacity",
    "fr.handbrake.ghb",
    "com.google.Chrome",
    "org.lutris.Lutris",
    "com.valvesoftware.Steam",
    "com.github.dawidd6.pdfarranger",
    "com.brave.Browser",
    "org.kde.kdenlive",
    "com.obsproject.Studio",
    "org.kde.okular",
    "org.winehq.Wine"
]


Please make sure you have flatpak installed on your system before running the script.

Contributing
Fork the repository
Create a new branch (git checkout -b new-feature)
Commit your changes (git commit -am 'Add new feature')
Push to the branch (git push origin new-feature)
Create a new pull request

License
This project is licensed under the MIT License.

Authors
Giift24
