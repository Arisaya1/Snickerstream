#!/bin/bash

# Easy installer launcher for Snickerstream on Bazzite
# This script provides the best installation experience based on available tools

SCRIPT_DIR="$(dirname "$0")"

echo "🎮 Snickerstream Easy Installer for Bazzite"
echo ""

# Check what's available and use the best option
if [ -f "$SCRIPT_DIR/install-wizard.sh" ] && command -v whiptail &> /dev/null; then
    echo "✨ Starting graphical installation wizard..."
    echo ""
    exec "$SCRIPT_DIR/install-wizard.sh"
elif [ -f "$SCRIPT_DIR/install-wizard.sh" ]; then
    echo "📋 Starting installation wizard (text mode)..."
    echo ""
    exec "$SCRIPT_DIR/install-wizard.sh"
elif [ -f "$SCRIPT_DIR/install-bazzite.sh" ]; then
    echo "🔧 Starting basic installer..."
    echo ""
    exec "$SCRIPT_DIR/install-bazzite.sh"
else
    echo "❌ Error: No installer scripts found!"
    echo ""
    echo "Please ensure you have downloaded the complete Snickerstream package."
    echo "Visit: https://github.com/Arisaya1/Snickerstream"
    exit 1
fi