# Snickerstream Flatpak Installation Guide

Snickerstream is now available as a Flatpak application optimized for Fedora Atomic, Bazzite, and other Linux distributions. This provides a seamless, one-click installation experience without requiring system package management.

## Quick Installation

### Prerequisites

First, ensure you have the Wine runtime installed:

```bash
flatpak install org.winehq.Platform//9 org.winehq.Platform.Compat.i386//9
```

### Install from Release

1. **Download the latest release bundle:**
   - Go to the [Releases page](https://github.com/Arisaya1/Snickerstream/releases)
   - Download `Snickerstream.flatpak`

2. **Install the bundle:**
   ```bash
   flatpak install --user Snickerstream.flatpak
   ```

3. **Run Snickerstream:**
   ```bash
   flatpak run io.github.Snickerstream
   ```

   Or find it in your application menu under "Games".

### Install from FlatHub (Future)

Once published to FlatHub:
```bash
flatpak install flathub io.github.Snickerstream
```

## Why Flatpak?

- **Perfect for Bazzite/Fedora Atomic**: No need for `rpm-ostree` or `dnf` commands
- **Sandboxed and secure**: Runs in an isolated environment
- **Easy updates**: `flatpak update io.github.Snickerstream`
- **Clean uninstall**: `flatpak uninstall io.github.Snickerstream`
- **No system dependencies**: Everything needed is bundled

## Features

The Flatpak version includes all the features of the original Snickerstream:

- Support for both NTR CFW and HzMod streaming protocols
- Real-time screen scaling with multiple interpolation modes
- Various screen layouts (vertical, horizontal, fullscreen, separate windows)
- Built-in screenshot functionality (press 'S' while streaming)
- Customizable quality settings and hotkeys
- Multiple 3DS console support
- First-run setup wizard for easy configuration

## Troubleshooting

### Wine Setup Issues

If you encounter Wine-related issues:

1. **Reset Wine prefix:**
   ```bash
   flatpak run --command=bash io.github.Snickerstream
   rm -rf ~/.var/app/io.github.Snickerstream/data/wine
   ```

2. **Check Wine components:**
   The Flatpak automatically installs required Windows components, but if issues persist, you can manually install additional components using `winetricks` inside the sandbox.

### Network Issues

Ensure your 3DS and computer are on the same network and that firewall settings allow the connection.

### Performance Issues

- Try different interpolation modes in the settings
- Adjust quality settings based on your network speed
- Use wired ethernet instead of WiFi if possible

## Building from Source

To build the Flatpak yourself:

```bash
# Install flatpak-builder
sudo dnf install flatpak-builder

# Clone the repository
git clone https://github.com/Arisaya1/Snickerstream.git
cd Snickerstream

# Build and install
flatpak-builder --user --install build-dir flatpak/io.github.Snickerstream.yml
```

## Support

- **Wiki**: [Snickerstream Wiki](https://github.com/RattletraPM/Snickerstream/wiki)
- **Issues**: [Report bugs](https://github.com/RattletraPM/Snickerstream/issues)
- **Discussions**: [Community support](https://github.com/RattletraPM/Snickerstream/discussions)

---

*This Flatpak port maintains full compatibility with the original Windows version while providing a modern Linux installation experience.*