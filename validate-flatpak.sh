#!/bin/bash

# Simple validation test for the Flatpak manifest
echo "Testing Snickerstream Flatpak manifest..."

# Check if required files exist
echo "Checking required files..."

required_files=(
    "flatpak/io.github.Snickerstream.yml"
    "flatpak/snickerstream-wrapper"
    "flatpak/io.github.Snickerstream.desktop"
    "flatpak/io.github.Snickerstream.metainfo.xml"
    "flatpak/icons/io.github.Snickerstream.png"
    "docs/FLATPAK.md"
    ".github/workflows/flatpak.yml"
)

missing_files=0
for file in "${required_files[@]}"; do
    if [[ -f "$file" ]]; then
        echo "✓ $file"
    else
        echo "✗ $file (missing)"
        missing_files=$((missing_files + 1))
    fi
done

# Basic manifest validation
echo ""
echo "Validating manifest content..."

if [[ -f "flatpak/io.github.Snickerstream.yml" ]]; then
    # Check for required fields
    if grep -q "app-id: io.github.Snickerstream" flatpak/io.github.Snickerstream.yml; then
        echo "✓ Correct app-id"
    else
        echo "✗ Invalid or missing app-id"
        missing_files=$((missing_files + 1))
    fi
    
    if grep -q "runtime: org.winehq.Platform" flatpak/io.github.Snickerstream.yml; then
        echo "✓ Wine runtime specified"
    else
        echo "✗ Wine runtime not specified"
        missing_files=$((missing_files + 1))
    fi
    
    if grep -q "command: snickerstream" flatpak/io.github.Snickerstream.yml; then
        echo "✓ Command specified"
    else
        echo "✗ Command not specified"
        missing_files=$((missing_files + 1))
    fi
fi

# Check wrapper script permissions
if [[ -f "flatpak/snickerstream-wrapper" ]]; then
    if [[ -x "flatpak/snickerstream-wrapper" ]]; then
        echo "✓ Wrapper script is executable"
    else
        echo "✗ Wrapper script is not executable"
        chmod +x flatpak/snickerstream-wrapper
        echo "  → Fixed: Made wrapper script executable"
    fi
fi

echo ""
if [[ $missing_files -eq 0 ]]; then
    echo "✅ All validation checks passed!"
    echo "The Flatpak is ready for building."
else
    echo "❌ $missing_files validation errors found."
    exit 1
fi

# Test AutoIt script syntax if possible
echo ""
echo "Checking AutoIt script..."
if [[ -f "Snickerstream.au3" ]]; then
    # Basic syntax check - look for balanced Func/EndFunc
    func_count=$(grep -c "^Func " Snickerstream.au3)
    endfunc_count=$(grep -c "EndFunc" Snickerstream.au3)
    
    if [[ $func_count -eq $endfunc_count ]]; then
        echo "✓ AutoIt script has balanced Func/EndFunc statements ($func_count functions)"
    else
        echo "⚠ AutoIt script may have syntax issues (Func: $func_count, EndFunc: $endfunc_count)"
    fi
    
    # Check for our new functions
    if grep -q "ShowFirstRunWizard" Snickerstream.au3; then
        echo "✓ First-run wizard function found"
    else
        echo "✗ First-run wizard function missing"
    fi
    
    if grep -q "ShowSettingsDialog" Snickerstream.au3; then
        echo "✓ Settings dialog function found"
    else
        echo "✗ Settings dialog function missing"
    fi
fi

echo ""
echo "Validation complete!"