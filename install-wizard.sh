#!/bin/bash

# Snickerstream Installation Wizard for Bazzite
# A nice terminal GUI installer with first-run wizard for "dumb easy" installation

set -e

# Configuration
SCRIPT_DIR="$(dirname "$0")"
APP_NAME="Snickerstream"
APP_DESC="Nintendo 3DS streaming application"
REPO_URL="https://github.com/Arisaya1/Snickerstream"
WIKI_URL="https://github.com/Arisaya1/Snickerstream/wiki"

# Colors for fallback mode
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Check if whiptail is available for nice dialogs
if command -v whiptail &> /dev/null; then
    HAS_WHIPTAIL=true
else
    HAS_WHIPTAIL=false
fi

# Utility functions
log_info() {
    if [ "$HAS_WHIPTAIL" = true ]; then
        echo "$1"
    else
        echo -e "${BLUE}[INFO]${NC} $1"
    fi
}

log_success() {
    if [ "$HAS_WHIPTAIL" = true ]; then
        echo "$1"
    else
        echo -e "${GREEN}[SUCCESS]${NC} $1"
    fi
}

log_warning() {
    if [ "$HAS_WHIPTAIL" = true ]; then
        echo "$1"
    else
        echo -e "${YELLOW}[WARNING]${NC} $1"
    fi
}

log_error() {
    if [ "$HAS_WHIPTAIL" = true ]; then
        echo "$1"
    else
        echo -e "${RED}[ERROR]${NC} $1"
    fi
}

# Show welcome screen
show_welcome() {
    if [ "$HAS_WHIPTAIL" = true ]; then
        whiptail --title "Welcome to $APP_NAME Installer" --msgbox \
"Welcome to the $APP_NAME Installation Wizard!

$APP_DESC for Bazzite and other Linux gaming distributions.

✨ What's New in the Linux Version:
• Modern Python UI optimized for Linux
• Native Flatpak for secure, sandboxed installation  
• Cross-platform compatibility (no Wine needed)
• All original features plus Linux enhancements

This wizard will guide you through the installation process step by step.

Press OK to continue..." 18 70
    else
        clear
        echo -e "${CYAN}"
        echo "======================================================="
        echo "    Welcome to $APP_NAME Installation Wizard!"
        echo "======================================================="
        echo -e "${NC}"
        echo "$APP_DESC for Bazzite and other Linux gaming distributions."
        echo ""
        echo -e "${GREEN}✨ What's New in the Linux Version:${NC}"
        echo "• Modern Python UI optimized for Linux"
        echo "• Native Flatpak for secure, sandboxed installation"
        echo "• Cross-platform compatibility (no Wine needed)"
        echo "• All original features plus Linux enhancements"
        echo ""
        echo "This wizard will guide you through the installation process."
        echo ""
        read -p "Press Enter to continue..."
    fi
}

# Check system requirements
check_system_requirements() {
    local issues=()
    local warnings=()
    
    # Check if running on Bazzite/Fedora
    if [[ ! -f /etc/fedora-release ]] && [[ ! -f /etc/bazzite-release ]]; then
        warnings+=("Not running on Bazzite/Fedora (installer is optimized for these systems)")
    fi
    
    # Check for Flatpak
    if ! command -v flatpak &> /dev/null; then
        issues+=("Flatpak is required but not installed")
    fi
    
    # Check for flatpak-builder
    if ! command -v flatpak-builder &> /dev/null; then
        warnings+=("flatpak-builder not found (will be installed automatically)")
    fi
    
    # Check network connectivity
    if ! ping -c 1 flathub.org &> /dev/null; then
        warnings+=("Cannot reach flathub.org (check internet connection)")
    fi
    
    # Show results
    if [ ${#issues[@]} -gt 0 ]; then
        local error_text="System Requirements Check Failed!\n\nCritical Issues Found:\n"
        for issue in "${issues[@]}"; do
            error_text+="• $issue\n"
        done
        error_text+="\nPlease resolve these issues before continuing."
        
        if [ "$HAS_WHIPTAIL" = true ]; then
            whiptail --title "System Requirements Check" --msgbox "$error_text" 15 70
        else
            log_error "System Requirements Check Failed!"
            echo ""
            echo "Critical Issues Found:"
            for issue in "${issues[@]}"; do
                echo "• $issue"
            done
            echo ""
            echo "Please resolve these issues before continuing."
        fi
        return 1
    fi
    
    # Show warnings if any
    if [ ${#warnings[@]} -gt 0 ]; then
        local warning_text="System Requirements Check - Warnings\n\n"
        for warning in "${warnings[@]}"; do
            warning_text+="• $warning\n"
        done
        warning_text+="\nThese issues will be handled automatically, but you may want to address them manually.\n\nContinue with installation?"
        
        if [ "$HAS_WHIPTAIL" = true ]; then
            if ! whiptail --title "System Requirements Check" --yesno "$warning_text" 15 70; then
                return 1
            fi
        else
            log_warning "System Requirements Check - Warnings"
            echo ""
            for warning in "${warnings[@]}"; do
                echo "• $warning"
            done
            echo ""
            echo "These issues will be handled automatically."
            read -p "Continue with installation? (y/N): " -n 1 -r
            echo
            if [[ ! $REPLY =~ ^[Yy]$ ]]; then
                return 1
            fi
        fi
    else
        if [ "$HAS_WHIPTAIL" = true ]; then
            whiptail --title "System Requirements Check" --msgbox \
"✅ System Requirements Check Passed!

All requirements are met:
• Flatpak is available
• Running on compatible system
• Network connectivity confirmed

Ready to proceed with installation!" 12 50
        else
            log_success "System Requirements Check Passed!"
            echo ""
            echo "All requirements are met:"
            echo "• Flatpak is available"
            echo "• Running on compatible system"
            echo "• Network connectivity confirmed"
            echo ""
            echo "Ready to proceed with installation!"
            sleep 2
        fi
    fi
    
    return 0
}

# Show installation options
show_installation_options() {
    if [ "$HAS_WHIPTAIL" = true ]; then
        if ! whiptail --title "Installation Options" --yesno \
"Choose Installation Method:

RECOMMENDED: Standard Installation
• Install Snickerstream as Flatpak
• Set up all dependencies automatically
• Add to application menu
• Full feature set enabled

Alternative: Manual setup later
• Exit wizard, install manually

Do you want to proceed with the standard installation?" 16 60; then
            return 1
        fi
    else
        echo -e "${CYAN}Installation Options:${NC}"
        echo ""
        echo "1. Standard Installation (Recommended)"
        echo "   • Install Snickerstream as Flatpak"
        echo "   • Set up all dependencies automatically"
        echo "   • Add to application menu"
        echo "   • Full feature set enabled"
        echo ""
        echo "2. Exit and install manually"
        echo ""
        read -p "Choose option (1-2): " choice
        case $choice in
            1) return 0 ;;
            2) return 1 ;;
            *) 
                log_error "Invalid choice. Please try again."
                show_installation_options
                ;;
        esac
    fi
}

# Show progress with whiptail gauge or simple progress
show_progress() {
    local message="$1"
    local percent="$2"
    
    if [ "$HAS_WHIPTAIL" = true ]; then
        echo "$percent"
        echo "XXX"
        echo "$message"
        echo "XXX"
    else
        local bar_length=40
        local filled_length=$((percent * bar_length / 100))
        local bar=""
        
        for ((i=0; i<filled_length; i++)); do
            bar+="█"
        done
        
        for ((i=filled_length; i<bar_length; i++)); do
            bar+="░"
        done
        
        printf "\r${BLUE}[${bar}]${NC} ${percent}%% - ${message}"
        
        if [ "$percent" -eq 100 ]; then
            echo ""
        fi
    fi
}

# Run the actual installation
run_installation() {
    if [ "$HAS_WHIPTAIL" = true ]; then
        # Use whiptail gauge for progress
        {
            show_progress "Setting up Flatpak repositories..." 10
            sleep 1
            
            show_progress "Adding Flathub repository..." 20
            flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo 2>/dev/null || true
            
            show_progress "Installing Python runtime dependencies..." 40
            if ! flatpak list | grep -q "org.freedesktop.Platform.*23.08"; then
                flatpak install -y flathub org.freedesktop.Platform//23.08 &>/dev/null
            fi
            
            show_progress "Installing Python SDK..." 60
            if ! flatpak list | grep -q "org.freedesktop.Sdk.*23.08"; then
                flatpak install -y flathub org.freedesktop.Sdk//23.08 &>/dev/null
            fi
            
            show_progress "Installing flatpak-builder..." 70
            if ! command -v flatpak-builder &> /dev/null; then
                if command -v dnf &> /dev/null; then
                    sudo dnf install -y flatpak-builder &>/dev/null
                elif command -v apt &> /dev/null; then
                    sudo apt update &>/dev/null && sudo apt install -y flatpak-builder &>/dev/null
                fi
            fi
            
            show_progress "Building Snickerstream Flatpak..." 80
            
            # Create build directory
            BUILD_DIR="/tmp/snickerstream-build-$$"
            mkdir -p "$BUILD_DIR"
            
            # Copy source files
            cp -r "$SCRIPT_DIR"/* "$BUILD_DIR/"
            cd "$BUILD_DIR"
            
            # Build the Flatpak
            flatpak-builder --user --install --force-clean build-dir com.github.arisaya1.Snickerstream.yml &>/dev/null
            
            show_progress "Cleaning up..." 95
            cd "$SCRIPT_DIR"
            rm -rf "$BUILD_DIR"
            
            show_progress "Installation complete!" 100
            
        } | whiptail --title "Installing Snickerstream" --gauge "Preparing installation..." 8 70 0
    else
        echo ""
        log_info "Starting installation process..."
        
        show_progress "Setting up Flatpak repositories..." 10
        sleep 1
        
        show_progress "Adding Flathub repository..." 20
        flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo 2>/dev/null || true
        
        show_progress "Installing Python runtime dependencies..." 40
        if ! flatpak list | grep -q "org.freedesktop.Platform.*23.08"; then
            flatpak install -y flathub org.freedesktop.Platform//23.08
        fi
        
        show_progress "Installing Python SDK..." 60
        if ! flatpak list | grep -q "org.freedesktop.Sdk.*23.08"; then
            flatpak install -y flathub org.freedesktop.Sdk//23.08
        fi
        
        show_progress "Installing flatpak-builder..." 70
        if ! command -v flatpak-builder &> /dev/null; then
            if command -v dnf &> /dev/null; then
                sudo dnf install -y flatpak-builder
            elif command -v apt &> /dev/null; then
                sudo apt update && sudo apt install -y flatpak-builder
            fi
        fi
        
        show_progress "Building Snickerstream Flatpak..." 80
        
        # Create build directory  
        BUILD_DIR="/tmp/snickerstream-build-$$"
        mkdir -p "$BUILD_DIR"
        
        # Copy source files
        cp -r "$SCRIPT_DIR"/* "$BUILD_DIR/"
        cd "$BUILD_DIR"
        
        # Build the Flatpak
        flatpak-builder --user --install --force-clean build-dir com.github.arisaya1.Snickerstream.yml
        
        show_progress "Cleaning up..." 95
        cd "$SCRIPT_DIR"
        rm -rf "$BUILD_DIR"
        
        show_progress "Installation complete!" 100
        echo ""
    fi
}

# Show post-installation help
show_post_installation() {
    if [ "$HAS_WHIPTAIL" = true ]; then
        whiptail --title "Installation Complete!" --msgbox \
"🎮 $APP_NAME has been successfully installed!

✅ Installation Summary:
• Flatpak application installed and ready to use
• Added to your application menu (Games category)
• All dependencies configured

🚀 How to Launch:
• From application menu: Games → Snickerstream
• From terminal: flatpak run com.github.arisaya1.Snickerstream

📖 Next Steps:
1. Set up your Nintendo 3DS with NTR CFW or HzMod
2. Connect your 3DS to the same network as your PC
3. Launch Snickerstream and enter your 3DS IP address
4. Start streaming!

🆘 Need Help?
Visit: $WIKI_URL

Press OK to finish." 22 70
    else
        clear
        echo -e "${GREEN}"
        echo "======================================================="
        echo "    🎮 $APP_NAME Installation Complete!"
        echo "======================================================="
        echo -e "${NC}"
        echo ""
        echo -e "${GREEN}✅ Installation Summary:${NC}"
        echo "• Flatpak application installed and ready to use"
        echo "• Added to your application menu (Games category)"
        echo "• All dependencies configured"
        echo ""
        echo -e "${CYAN}🚀 How to Launch:${NC}"
        echo "• From application menu: Games → Snickerstream"
        echo "• From terminal: flatpak run com.github.arisaya1.Snickerstream"
        echo ""
        echo -e "${BLUE}📖 Next Steps:${NC}"
        echo "1. Set up your Nintendo 3DS with NTR CFW or HzMod"
        echo "2. Connect your 3DS to the same network as your PC"
        echo "3. Launch Snickerstream and enter your 3DS IP address"
        echo "4. Start streaming!"
        echo ""
        echo -e "${YELLOW}🆘 Need Help?${NC}"
        echo "Visit: $WIKI_URL"
        echo ""
        read -p "Press Enter to finish..."
    fi
}

# Show quick setup guide
show_quick_setup_guide() {
    if [ "$HAS_WHIPTAIL" = true ]; then
        if whiptail --title "Quick Setup Guide" --yesno \
"Would you like to see a quick setup guide for your Nintendo 3DS?

This will show you how to:
• Install NTR CFW on your 3DS
• Configure network settings
• Connect to Snickerstream

Show setup guide?" 12 60; then
            whiptail --title "Nintendo 3DS Setup Guide" --msgbox \
"🎮 Setting up your Nintendo 3DS:

1️⃣ Install Custom Firmware:
   • Install Luma3DS CFW on your 3DS
   • Install NTR CFW or HzMod

2️⃣ Network Setup:
   • Connect your 3DS to WiFi
   • Note your 3DS IP address (System Settings → Internet)
   • Ensure PC and 3DS are on same network

3️⃣ Launch NTR:
   • Start NTR CFW on your 3DS
   • Enable streaming mode

4️⃣ Connect with Snickerstream:
   • Launch Snickerstream on your PC
   • Enter 3DS IP address
   • Click Connect and enjoy!

For detailed instructions, visit:
$WIKI_URL" 24 70
        fi
    else
        echo ""
        read -p "Would you like to see a quick setup guide for your Nintendo 3DS? (y/N): " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            echo ""
            echo -e "${CYAN}🎮 Setting up your Nintendo 3DS:${NC}"
            echo ""
            echo "1️⃣ Install Custom Firmware:"
            echo "   • Install Luma3DS CFW on your 3DS"
            echo "   • Install NTR CFW or HzMod"
            echo ""
            echo "2️⃣ Network Setup:"
            echo "   • Connect your 3DS to WiFi"
            echo "   • Note your 3DS IP address (System Settings → Internet)"
            echo "   • Ensure PC and 3DS are on same network"
            echo ""
            echo "3️⃣ Launch NTR:"
            echo "   • Start NTR CFW on your 3DS"
            echo "   • Enable streaming mode"
            echo ""
            echo "4️⃣ Connect with Snickerstream:"
            echo "   • Launch Snickerstream on your PC"
            echo "   • Enter 3DS IP address"
            echo "   • Click Connect and enjoy!"
            echo ""
            echo -e "${YELLOW}For detailed instructions, visit:${NC}"
            echo "$WIKI_URL"
            echo ""
            read -p "Press Enter to continue..."
        fi
    fi
}

# Main wizard flow
main() {
    # Check if running with --simple flag for fallback mode
    if [[ "$1" == "--simple" ]] || [[ "$HAS_WHIPTAIL" != true ]]; then
        log_info "Running in simple mode (no GUI available)"
        exec "$SCRIPT_DIR/install-bazzite.sh"
        return
    fi

    # Run the wizard steps
    show_welcome || exit 0
    
    check_system_requirements || {
        if [ "$HAS_WHIPTAIL" = true ]; then
            whiptail --title "Installation Cancelled" --msgbox "Installation was cancelled due to system requirements issues.\n\nPlease resolve the issues and run the installer again." 10 60
        else
            log_error "Installation cancelled due to system requirements issues."
        fi
        exit 1
    }
    
    show_installation_options || {
        if [ "$HAS_WHIPTAIL" = true ]; then
            whiptail --title "Installation Cancelled" --msgbox "Installation was cancelled by user.\n\nYou can run this installer again anytime or install manually using:\n./install-bazzite.sh" 10 60
        else
            log_info "Installation cancelled by user."
            echo "You can run this installer again anytime or install manually using:"
            echo "./install-bazzite.sh"
        fi
        exit 0
    }
    
    # Run installation
    if ! run_installation; then
        if [ "$HAS_WHIPTAIL" = true ]; then
            whiptail --title "Installation Failed" --msgbox "Installation failed. Please check the error messages above and try again.\n\nIf the problem persists, try manual installation:\n./install-bazzite.sh\n\nOr visit: $REPO_URL" 12 60
        else
            log_error "Installation failed."
            echo "If the problem persists, try manual installation: ./install-bazzite.sh"
            echo "Or visit: $REPO_URL"
        fi
        exit 1
    fi
    
    # Show success and next steps
    show_post_installation
    show_quick_setup_guide
    
    log_success "Installation wizard completed successfully! 🎮"
}

# Run the main function
main "$@"