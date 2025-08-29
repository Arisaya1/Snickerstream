# Snickerstream for Bazzite - Easy Installation Guide

Snickerstream is now available as a modern Flatpak application optimized for Bazzite and other Linux gaming distributions!

## ✨ What's New in the Linux Version

- **Modern Python UI**: Clean, responsive interface designed for Linux
- **Native Flatpak**: Sandboxed, secure installation through Flatpak
- **Cross-platform compatibility**: No more Wine dependencies
- **Enhanced features**: All the power of the original with Linux optimizations

## 🚀 One-Click Installation

### Quick Install (Recommended)

```bash
# Download and run the installer
curl -fsSL https://raw.githubusercontent.com/Arisaya1/Snickerstream/master/install-bazzite.sh | bash
```

### Manual Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Arisaya1/Snickerstream.git
   cd Snickerstream
   ```

2. **Run the installer:**
   ```bash
   ./install-bazzite.sh
   ```

3. **Launch Snickerstream:**
   - Find it in your application menu under "Games"
   - Or run: `flatpak run com.github.arisaya1.Snickerstream`

## 🎮 Features

### Core Streaming Features
- ✅ **NTR CFW Support**: Stream from any 3DS with NTR CFW
- ✅ **HzMod Support**: Alternative streaming with enhanced stability
- ✅ **Real-time Quality Control**: Adjust streaming quality on the fly
- ✅ **Multiple Console Support**: Stream from several 3DS systems simultaneously

### Display & Layout Options
- ✅ **Screen Layouts**: Vertical, Horizontal, Top-only, Bottom-only, Fullscreen
- ✅ **Real-time Scaling**: Zoom in/out while streaming
- ✅ **Interpolation Modes**: Nearest, Linear, Cubic, Lanczos for better image quality
- ✅ **Separate Windows**: Independent windows for each screen

### User Experience
- ✅ **Modern UI**: Clean tabbed interface with intuitive controls
- ✅ **Configuration Management**: Save/load settings, multiple profiles
- ✅ **Keyboard Shortcuts**: Customizable hotkeys for common actions
- ✅ **Screenshot Function**: Capture moments from your 3DS gameplay
- ✅ **Auto-connect**: Automatically connect to your 3DS on startup

## ⌨️ Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `ESC` | Close Snickerstream |
| `UP/DOWN` | Increase/Decrease scaling |
| `LEFT/RIGHT` | Change interpolation settings |
| `S` | Take screenshot |
| `ENTER` | Return to connection window |
| `SPACE` | Pop up other screen (fullscreen modes) |

## 🔧 Setup Guide

### 1. Prepare Your 3DS

**For NTR CFW:**
1. Install NTR CFW on your 3DS
2. Enable wireless streaming in NTR settings
3. Note your 3DS IP address (System Settings → Internet)

**For HzMod:**
1. Install HzMod homebrew application
2. Launch HzMod and enable streaming
3. Note the IP address displayed

### 2. Configure Snickerstream

1. **Launch Snickerstream** from the applications menu
2. **Connection Tab:**
   - Enter your 3DS IP address
   - Set port (usually 8000 for NTR, varies for HzMod)
   - Select streaming app (NTR CFW or HzMod)
3. **Settings Tab:**
   - Adjust quality (10-100%)
   - Choose screen layout
   - Select interpolation method
4. **Advanced Tab:**
   - Configure hotkeys
   - Set auto-connect preferences
   - Manage configuration profiles

### 3. Start Streaming

1. Click **"Connect"** in the Connection tab
2. Your 3DS screens should appear in the preview area
3. Use hotkeys or UI controls to adjust the stream
4. Click **"Disconnect"** when finished

## 🛠️ Troubleshooting

### Connection Issues
- **Can't connect**: Verify 3DS and PC are on the same network
- **Wrong IP**: Check 3DS network settings for correct IP address
- **Firewall**: Ensure ports 8000-8001 are open on your PC

### Performance Issues
- **Slow streaming**: Reduce quality setting or change interpolation
- **Choppy video**: Check network stability, try different layout modes
- **High CPU usage**: Lower quality settings, disable unnecessary effects

### Installation Issues
- **Flatpak errors**: Ensure Flatpak is properly installed: `sudo dnf install flatpak`
- **Permission denied**: Make sure installer script is executable: `chmod +x install-bazzite.sh`
- **Missing dependencies**: Run: `flatpak install flathub org.freedesktop.Platform//23.08`

## 📋 System Requirements

### Minimum Requirements
- **OS**: Bazzite, Fedora 38+, or any Linux distribution with Flatpak
- **RAM**: 2GB available
- **Network**: WiFi connection shared with 3DS
- **Display**: 1024x768 resolution

### Recommended Requirements
- **OS**: Bazzite (latest version)
- **RAM**: 4GB+ available
- **Network**: 5GHz WiFi or wired connection
- **Display**: 1920x1080+ resolution
- **GPU**: Hardware acceleration support for better performance

## 🔄 Updating

To update Snickerstream:

```bash
flatpak update com.github.arisaya1.Snickerstream
```

## 🗑️ Uninstalling

To remove Snickerstream:

```bash
flatpak uninstall com.github.arisaya1.Snickerstream
```

## 💡 Tips for Bazzite Users

1. **Gaming Mode**: Snickerstream works in both Desktop and Gaming modes
2. **Controller Support**: While primarily mouse/keyboard focused, basic controller navigation is supported
3. **Performance**: For best results, close unnecessary applications while streaming
4. **Network**: Use wired connection for PC when possible for stable streaming
5. **Steam Integration**: You can add the Flatpak to Steam as a non-Steam game

## 🆘 Getting Help

- **Documentation**: [GitHub Wiki](https://github.com/RattletraPM/Snickerstream/wiki)
- **Issues**: [GitHub Issues](https://github.com/RattletraPM/Snickerstream/issues)
- **Community**: Join gaming communities on Discord for 3DS streaming help

## 📝 License

Snickerstream is licensed under GPL-3.0. The original Windows version was created by RattletraPM, and this Linux/Flatpak port maintains compatibility while adding modern cross-platform support.

---

**Enjoy streaming your Nintendo 3DS games on Bazzite! 🎮**