#!/usr/bin/env python3
"""
Simple UI mockup generator for Snickerstream
Creates a mockup image of what the interface looks like
"""

import tkinter as tk
from tkinter import ttk
import os

def create_mockup():
    root = tk.Tk()
    root.title("Snickerstream - Nintendo 3DS Streaming Client")
    root.geometry("600x500")
    
    # Configure style for better appearance
    style = ttk.Style()
    
    # Main notebook
    notebook = ttk.Notebook(root)
    notebook.pack(fill="both", expand=True, padx=10, pady=10)
    
    # Connection tab
    conn_frame = ttk.Frame(notebook)
    notebook.add(conn_frame, text="Connection")
    
    # IP Address section
    ip_frame = ttk.LabelFrame(conn_frame, text="3DS Connection", padding=10)
    ip_frame.pack(fill="x", padx=10, pady=5)
    
    ttk.Label(ip_frame, text="IP Address:").grid(row=0, column=0, sticky="w", padx=5)
    ip_entry = ttk.Entry(ip_frame, width=20)
    ip_entry.insert(0, "192.168.1.100")
    ip_entry.grid(row=0, column=1, padx=5)
    
    ttk.Label(ip_frame, text="Port:").grid(row=0, column=2, sticky="w", padx=5)
    port_entry = ttk.Entry(ip_frame, width=10)
    port_entry.insert(0, "8000")
    port_entry.grid(row=0, column=3, padx=5)
    
    # Streaming app
    app_frame = ttk.LabelFrame(conn_frame, text="Streaming App", padding=10)
    app_frame.pack(fill="x", padx=10, pady=5)
    
    app_combo = ttk.Combobox(app_frame, values=["NTR CFW", "HzMod"], state="readonly")
    app_combo.set("NTR CFW")
    app_combo.pack(side="left", padx=5)
    
    # Buttons
    button_frame = ttk.Frame(conn_frame)
    button_frame.pack(fill="x", padx=10, pady=20)
    
    connect_btn = ttk.Button(button_frame, text="Connect")
    connect_btn.pack(side="left", padx=5)
    
    screenshot_btn = ttk.Button(button_frame, text="Screenshot")
    screenshot_btn.pack(side="left", padx=5)
    
    status_label = ttk.Label(button_frame, text="Ready to connect")
    status_label.pack(side="right", padx=5)
    
    # Preview area
    preview_frame = ttk.LabelFrame(conn_frame, text="Stream Preview", padding=10)
    preview_frame.pack(fill="both", expand=True, padx=10, pady=5)
    
    preview_text = tk.Text(preview_frame, height=10, bg="#f0f0f0")
    preview_text.insert("1.0", "🎮 Nintendo 3DS Stream Preview\n\n" +
                               "Connect to your 3DS to see the screens here!\n\n" +
                               "Features:\n" +
                               "• Real-time screen scaling\n" +
                               "• Multiple layout options\n" +
                               "• Screenshot capability\n" +
                               "• NTR CFW & HzMod support")
    preview_text.config(state="disabled")
    preview_text.pack(fill="both", expand=True)
    
    # Settings tab
    settings_frame = ttk.Frame(notebook)
    notebook.add(settings_frame, text="Settings")
    
    # Quality settings
    quality_frame = ttk.LabelFrame(settings_frame, text="Quality Settings", padding=10)
    quality_frame.pack(fill="x", padx=10, pady=5)
    
    ttk.Label(quality_frame, text="Quality:").grid(row=0, column=0, sticky="w")
    quality_scale = ttk.Scale(quality_frame, from_=10, to=100, orient="horizontal")
    quality_scale.set(90)
    quality_scale.grid(row=0, column=1, sticky="ew", padx=5)
    ttk.Label(quality_frame, text="90%").grid(row=0, column=2, padx=5)
    
    # Layout settings
    layout_frame = ttk.LabelFrame(settings_frame, text="Screen Layout", padding=10)
    layout_frame.pack(fill="x", padx=10, pady=5)
    
    layouts = ["Vertical", "Horizontal", "Top Only", "Bottom Only"]
    layout_var = tk.StringVar(value="Vertical")
    
    for i, layout in enumerate(layouts):
        ttk.Radiobutton(layout_frame, text=layout, variable=layout_var, 
                       value=layout).grid(row=i//2, column=i%2, sticky="w", padx=5, pady=2)
    
    # Advanced tab
    advanced_frame = ttk.Frame(notebook)
    notebook.add(advanced_frame, text="Advanced")
    
    # Hotkeys info
    hotkey_frame = ttk.LabelFrame(advanced_frame, text="Keyboard Shortcuts", padding=10)
    hotkey_frame.pack(fill="x", padx=10, pady=5)
    
    hotkeys_text = tk.Text(hotkey_frame, height=8, bg="#f8f8f8")
    hotkeys_text.insert("1.0", "ESC: Close Snickerstream\n" +
                               "UP/DOWN: Increase/Decrease scaling\n" +
                               "LEFT/RIGHT: Change interpolation\n" +
                               "S: Take screenshot\n" +
                               "ENTER: Return to connection window\n" +
                               "SPACE: Pop up other screen")
    hotkeys_text.config(state="disabled")
    hotkeys_text.pack(fill="both", expand=True)
    
    # Take screenshot after a delay
    def take_screenshot():
        try:
            root.update()
            # This would normally save a screenshot, but for the mockup we'll just print
            print("📸 Mockup screenshot would be saved here")
            print("✅ Snickerstream UI mockup ready!")
        except Exception as e:
            print(f"Screenshot error: {e}")
        finally:
            root.quit()
    
    root.after(100, take_screenshot)
    root.mainloop()

if __name__ == "__main__":
    create_mockup()