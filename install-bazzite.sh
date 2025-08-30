#!/bin/bash

# Snickerstream Easy Install Script for Bazzite
# This script sets up Snickerstream as a Flatpak for easy installation

set -e

echo "=================================="
echo "Snickerstream Flatpak Installer"
echo "=================================="
echo "Installing Snickerstream for Nintendo 3DS streaming on Bazzite"
echo ""

# Check if running on Bazzite/Fedora
if [[ ! -f /etc/fedora-release ]] && [[ ! -f /etc/bazzite-release ]]; then
    echo "Warning: This installer is optimized for Bazzite/Fedora systems"
    read -p "Continue anyway? (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

# Check if Flatpak is available
if ! command -v flatpak &> /dev/null; then
    echo "Error: Flatpak is required but not installed"
    echo "Please install Flatpak first:"
    echo "  sudo dnf install flatpak"
    exit 1
fi

# Add Flathub if not already added
echo "Setting up Flatpak repositories..."
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo

# Install dependencies
echo "Installing Python dependencies..."
if ! flatpak list | grep -q org.freedesktop.Platform; then
    flatpak install -y flathub org.freedesktop.Platform//23.08
fi

if ! flatpak list | grep -q org.freedesktop.Sdk; then
    flatpak install -y flathub org.freedesktop.Sdk//23.08
fi

# Build and install Snickerstream
echo "Building Snickerstream Flatpak..."

# Check if we have flatpak-builder
if ! command -v flatpak-builder &> /dev/null; then
    echo "Installing flatpak-builder..."
    sudo dnf install -y flatpak-builder
fi

# Create build directory
BUILD_DIR="/tmp/snickerstream-build"
rm -rf "$BUILD_DIR"
mkdir -p "$BUILD_DIR"

# Copy source files
cp -r "$(dirname "$0")"/* "$BUILD_DIR/"
cd "$BUILD_DIR"

# Build the Flatpak
echo "Building Flatpak package..."
flatpak-builder --user --install --force-clean build-dir com.github.arisaya1.Snickerstream.yml

echo ""
echo "✅ Installation complete!"
echo ""
echo "Snickerstream has been installed as a Flatpak application."
echo ""
echo "To run Snickerstream:"
echo "  - Use the application menu (Games category)"
echo "  - Or run: flatpak run com.github.arisaya1.Snickerstream"
echo ""
echo "Features:"
echo "  ✓ Modern Python-based UI optimized for Linux"
echo "  ✓ Support for NTR CFW and HzMod streaming"
echo "  ✓ Real-time screen scaling and interpolation"
echo "  ✓ Multiple screen layouts"
echo "  ✓ Configurable hotkeys"
echo "  ✓ Screenshot functionality"
echo ""
echo "For help and troubleshooting, visit:"
echo "https://github.com/Arisaya1/Snickerstream/wiki"
echo ""

# Clean up
cd ..
rm -rf "$BUILD_DIR"

echo "Installation completed successfully! 🎮"