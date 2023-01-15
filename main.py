import subprocess

def install_flatpaks(flatpaks: list):
    """
    function to install flatpaks
    """
    try:
        # Add the Flatpak repository
        subprocess.run(["flatpak", "remote-add", "--if-not-exists", "flathub", "https://flathub.org/repo/flathub.flatpakrepo"], check=True)
        for pak in flatpaks:
            subprocess.run(["flatpak", "install", "flathub", pak, "-y"], check=True)
        print(f"Successfully installed {len(flatpaks)} flatpaks.")
    except subprocess.CalledProcessError as error:
        print(f"An error occurred: {error}")

# List of Flatpaks to install
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

install_flatpaks(flatpaks)
