#!/usr/bin/env python3
"""
Snickerstream UI Mockup - Shows the enhanced interface changes
"""

import tkinter as tk
from tkinter import ttk, messagebox
import sys

class SnickerStreamMockup:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Snickerstream v1.10 - Enhanced UI Mockup")
        self.root.geometry("600x500")
        
        # Create a notebook to show different UI states
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)
        
        # First-run wizard mockup
        self.create_wizard_mockup()
        
        # Enhanced main GUI mockup
        self.create_main_gui_mockup()
        
        # Settings dialog mockup
        self.create_settings_mockup()
        
    def create_wizard_mockup(self):
        wizard_frame = ttk.Frame(self.notebook)
        self.notebook.add(wizard_frame, text="First-Run Wizard")
        
        # Title
        title = ttk.Label(wizard_frame, text="Step 2 of 3: Choose streaming method", font=("Arial", 12, "bold"))
        title.pack(pady=20)
        
        # Method selection
        method_frame = ttk.LabelFrame(wizard_frame, text="Streaming Method", padding=20)
        method_frame.pack(pady=10, padx=20, fill="x")
        
        self.method_var = tk.StringVar(value="ntr")
        ntr_radio = ttk.Radiobutton(method_frame, text="NTR CFW (Recommended for most users)", 
                                   variable=self.method_var, value="ntr")
        ntr_radio.pack(anchor="w", pady=5)
        
        hzmod_radio = ttk.Radiobutton(method_frame, text="HzMod (Newer, experimental)", 
                                     variable=self.method_var, value="hzmod")
        hzmod_radio.pack(anchor="w", pady=5)
        
        # Info text
        info_text = tk.Text(wizard_frame, height=6, wrap="word")
        info_text.pack(pady=20, padx=20, fill="x")
        info_text.insert("1.0", """Next steps:
• Enter your 3DS IP address
• Choose a quality preset (Low/Medium/High)
• Test connection
• Start streaming!

The wizard will save your settings and remember your preferences for future use.""")
        info_text.config(state="disabled")
        
        # Buttons
        button_frame = ttk.Frame(wizard_frame)
        button_frame.pack(side="bottom", pady=20)
        
        ttk.Button(button_frame, text="< Back").pack(side="left", padx=5)
        ttk.Button(button_frame, text="Next >").pack(side="left", padx=5)
        
    def create_main_gui_mockup(self):
        main_frame = ttk.Frame(self.notebook)
        self.notebook.add(main_frame, text="Enhanced Main GUI")
        
        # Title
        title = ttk.Label(main_frame, text="Snickerstream v1.10 - Enhanced Interface", 
                         font=("Arial", 12, "bold"))
        title.pack(pady=10)
        
        # Main content in two columns
        content_frame = ttk.Frame(main_frame)
        content_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Left column - Connection settings
        left_frame = ttk.LabelFrame(content_frame, text="Connection & Quality", padding=10)
        left_frame.pack(side="left", fill="both", expand=True, padx=(0, 10))
        
        # IP with recent IPs dropdown
        ip_frame = ttk.Frame(left_frame)
        ip_frame.pack(fill="x", pady=5)
        ttk.Label(ip_frame, text="3DS IP:").pack(side="left")
        ip_combo = ttk.Combobox(ip_frame, values=["192.168.1.100", "192.168.1.105", "192.168.0.150"])
        ip_combo.pack(side="right", fill="x", expand=True, padx=(10, 0))
        ip_combo.set("192.168.1.100")
        
        # Quality preset
        quality_frame = ttk.Frame(left_frame)
        quality_frame.pack(fill="x", pady=5)
        ttk.Label(quality_frame, text="Quality:").pack(side="left")
        quality_combo = ttk.Combobox(quality_frame, values=["Low (Safe)", "Medium (Balanced)", "High (Best)"])
        quality_combo.pack(side="right", fill="x", expand=True, padx=(10, 0))
        quality_combo.set("Medium (Balanced)")
        
        # Streaming method
        method_frame = ttk.Frame(left_frame)
        method_frame.pack(fill="x", pady=5)
        ttk.Label(method_frame, text="Method:").pack(side="left")
        method_combo = ttk.Combobox(method_frame, values=["NTR CFW", "HzMod"])
        method_combo.pack(side="right", fill="x", expand=True, padx=(10, 0))
        method_combo.set("NTR CFW")
        
        # Status indicator
        status_label = ttk.Label(left_frame, text="Status: Ready to connect", foreground="green")
        status_label.pack(pady=10)
        
        # Right column - Actions
        right_frame = ttk.LabelFrame(content_frame, text="Actions", padding=10)
        right_frame.pack(side="right", fill="y")
        
        ttk.Button(right_frame, text="Connect!", width=15).pack(pady=5)
        ttk.Button(right_frame, text="Test Connection", width=15).pack(pady=5)
        ttk.Button(right_frame, text="Settings", width=15).pack(pady=5)
        ttk.Button(right_frame, text="About", width=15).pack(pady=5)
        
        # Recent connections
        recent_frame = ttk.LabelFrame(main_frame, text="Recent Connections", padding=10)
        recent_frame.pack(fill="x", padx=20, pady=10)
        
        recent_text = "Recent IPs: 192.168.1.100 (last used), 192.168.1.105, 192.168.0.150"
        ttk.Label(recent_frame, text=recent_text, foreground="gray").pack()
        
    def create_settings_mockup(self):
        settings_frame = ttk.Frame(self.notebook)
        self.notebook.add(settings_frame, text="Settings Dialog")
        
        # Title
        title = ttk.Label(settings_frame, text="Snickerstream Settings", font=("Arial", 12, "bold"))
        title.pack(pady=10)
        
        # Settings tabs
        settings_nb = ttk.Notebook(settings_frame)
        settings_nb.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Basic tab
        basic_frame = ttk.Frame(settings_nb)
        settings_nb.add(basic_frame, text="Basic")
        
        # Method selection
        method_group = ttk.LabelFrame(basic_frame, text="Streaming Method", padding=10)
        method_group.pack(fill="x", pady=5)
        
        method_var = tk.StringVar(value="ntr")
        ttk.Radiobutton(method_group, text="NTR CFW", variable=method_var, value="ntr").pack(anchor="w")
        ttk.Radiobutton(method_group, text="HzMod", variable=method_var, value="hzmod").pack(anchor="w")
        
        # Connection settings
        conn_group = ttk.LabelFrame(basic_frame, text="Connection", padding=10)
        conn_group.pack(fill="x", pady=5)
        
        ip_frame = ttk.Frame(conn_group)
        ip_frame.pack(fill="x")
        ttk.Label(ip_frame, text="3DS IP Address:").pack(side="left")
        ip_entry = ttk.Entry(ip_frame)
        ip_entry.pack(side="right", fill="x", expand=True, padx=(10, 0))
        ip_entry.insert(0, "192.168.1.100")
        
        ttk.Button(conn_group, text="Test Connection").pack(pady=5)
        
        # Quality presets
        quality_group = ttk.LabelFrame(basic_frame, text="Quality Preset", padding=10)
        quality_group.pack(fill="x", pady=5)
        
        quality_var = tk.StringVar(value="medium")
        ttk.Radiobutton(quality_group, text="Low (Safe) - Good for slow networks", 
                       variable=quality_var, value="low").pack(anchor="w")
        ttk.Radiobutton(quality_group, text="Medium (Balanced) - Recommended", 
                       variable=quality_var, value="medium").pack(anchor="w")
        ttk.Radiobutton(quality_group, text="High (Best) - Requires good network", 
                       variable=quality_var, value="high").pack(anchor="w")
        
        # Auto-connect
        auto_var = tk.BooleanVar()
        ttk.Checkbutton(basic_frame, text="Auto-connect on startup", variable=auto_var).pack(pady=10)
        
        # Advanced tab
        advanced_frame = ttk.Frame(settings_nb)
        settings_nb.add(advanced_frame, text="Advanced")
        
        adv_group = ttk.LabelFrame(advanced_frame, text="Advanced Parameters", padding=10)
        adv_group.pack(fill="x", pady=5)
        
        # Some advanced settings
        for i, (label, value) in enumerate([("Priority Factor:", "5"), ("Image Quality:", "70"), ("QoS Value:", "20")]):
            param_frame = ttk.Frame(adv_group)
            param_frame.pack(fill="x", pady=2)
            ttk.Label(param_frame, text=label).pack(side="left")
            entry = ttk.Entry(param_frame, width=10)
            entry.pack(side="right")
            entry.insert(0, value)
        
        # Buttons
        button_frame = ttk.Frame(settings_frame)
        button_frame.pack(side="bottom", pady=10)
        
        ttk.Button(button_frame, text="Import").pack(side="left", padx=5)
        ttk.Button(button_frame, text="Export").pack(side="left", padx=5)
        ttk.Button(button_frame, text="Reset to Defaults").pack(side="left", padx=5)
        ttk.Button(button_frame, text="Cancel").pack(side="left", padx=20)
        ttk.Button(button_frame, text="OK").pack(side="left", padx=5)
        
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = SnickerStreamMockup()
    app.run()