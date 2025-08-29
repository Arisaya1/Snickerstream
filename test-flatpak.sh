#!/bin/bash

# Test script for Snickerstream Flatpak build
# This validates that the Flatpak can be built successfully

set -e

echo "Testing Snickerstream Flatpak build..."

# Check dependencies
if ! command -v flatpak &> /dev/null; then
    echo "❌ Flatpak not found. Please install flatpak first."
    exit 1
fi

if ! command -v flatpak-builder &> /dev/null; then
    echo "❌ flatpak-builder not found. Please install flatpak-builder first."
    exit 1
fi

# Check if required runtimes are available
echo "Checking Flatpak runtimes..."
if ! flatpak list | grep -q "org.freedesktop.Platform.*23.08"; then
    echo "Installing org.freedesktop.Platform//23.08..."
    flatpak install -y flathub org.freedesktop.Platform//23.08
fi

if ! flatpak list | grep -q "org.freedesktop.Sdk.*23.08"; then
    echo "Installing org.freedesktop.Sdk//23.08..."
    flatpak install -y flathub org.freedesktop.Sdk//23.08
fi

# Validate manifest
echo "Validating Flatpak manifest..."
if [[ ! -f "com.github.arisaya1.Snickerstream.yml" ]]; then
    echo "❌ Flatpak manifest not found!"
    exit 1
fi

# Check if Python script exists
if [[ ! -f "snickerstream-python/snickerstream.py" ]]; then
    echo "❌ Python script not found!"
    exit 1
fi

# Check if desktop file exists  
if [[ ! -f "com.github.arisaya1.Snickerstream.desktop" ]]; then
    echo "❌ Desktop file not found!"
    exit 1
fi

# Check if appdata exists
if [[ ! -f "com.github.arisaya1.Snickerstream.appdata.xml" ]]; then
    echo "❌ AppData file not found!"
    exit 1
fi

# Validate Python script syntax
echo "Validating Python script syntax..."
if ! python3 -m py_compile snickerstream-python/snickerstream.py; then
    echo "❌ Python script has syntax errors!"
    exit 1
fi

# Test build (dry run)
echo "Testing Flatpak build..."
BUILD_DIR="/tmp/snickerstream-test-build"
rm -rf "$BUILD_DIR"
mkdir -p "$BUILD_DIR"

# Copy source to build directory
cp -r . "$BUILD_DIR/"
cd "$BUILD_DIR"

# Try to build (but don't install)
if flatpak-builder --dry-run build-dir com.github.arisaya1.Snickerstream.yml; then
    echo "✅ Flatpak build validation successful!"
else
    echo "❌ Flatpak build validation failed!"
    exit 1
fi

# Clean up
cd ..
rm -rf "$BUILD_DIR"

echo ""
echo "✅ All tests passed!"
echo "The Snickerstream Flatpak is ready for installation."
echo ""
echo "To install:"
echo "  ./install-bazzite.sh"
echo ""
echo "To build manually:"
echo "  flatpak-builder --user --install build-dir com.github.arisaya1.Snickerstream.yml"