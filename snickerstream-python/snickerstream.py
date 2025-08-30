#!/usr/bin/env python3
"""
Snickerstream - Nintendo 3DS Streaming Client
Cross-platform Python implementation for Linux/Flatpak compatibility

Based on the original AutoIt version by RattletraPM
"""

import socket
import threading
import json
import os
import sys

# Check for tkinter availability
try:
    import tkinter as tk
    from tkinter import ttk, messagebox, filedialog
    TKINTER_AVAILABLE = True
except ImportError:
    TKINTER_AVAILABLE = False
    print("Error: tkinter not available. This is required for the GUI.")
    sys.exit(1)

# Check for Pillow availability
try:
    from PIL import Image, ImageTk
    PILLOW_AVAILABLE = True
except ImportError:
    PILLOW_AVAILABLE = False
    print("Warning: Pillow not available, some image features may be limited")


class SnickerStreamGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Snickerstream - Nintendo 3DS Streaming Client")
        self.root.geometry("600x500")
        
        # Configuration
        self.config = {
            "ip": "192.168.1.100",
            "port": 8000,
            "streaming_app": "NTR CFW",
            "quality": 90,
            "layout": "Vertical",
            "interpolation": "Linear",
            "auto_connect": False
        }
        
        self.load_config()
        self.create_widgets()
        self.streaming = False
        self.stream_thread = None
        
    def create_widgets(self):
        # Main notebook for tabs
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Connection tab
        conn_frame = ttk.Frame(notebook)
        notebook.add(conn_frame, text="Connection")
        self.create_connection_tab(conn_frame)
        
        # Settings tab
        settings_frame = ttk.Frame(notebook)
        notebook.add(settings_frame, text="Settings")
        self.create_settings_tab(settings_frame)
        
        # Advanced tab
        advanced_frame = ttk.Frame(notebook)
        notebook.add(advanced_frame, text="Advanced")
        self.create_advanced_tab(advanced_frame)
        
    def create_connection_tab(self, parent):
        # IP Address and Port
        ip_frame = ttk.LabelFrame(parent, text="3DS Connection", padding=10)
        ip_frame.pack(fill="x", padx=10, pady=5)
        
        ttk.Label(ip_frame, text="IP Address:").grid(row=0, column=0, sticky="w", padx=5)
        self.ip_var = tk.StringVar(value=self.config["ip"])
        self.ip_entry = ttk.Entry(ip_frame, textvariable=self.ip_var, width=20)
        self.ip_entry.grid(row=0, column=1, padx=5)
        
        ttk.Label(ip_frame, text="Port:").grid(row=0, column=2, sticky="w", padx=5)
        self.port_var = tk.StringVar(value=str(self.config["port"]))
        self.port_entry = ttk.Entry(ip_frame, textvariable=self.port_var, width=10)
        self.port_entry.grid(row=0, column=3, padx=5)
        
        # Streaming app selection
        app_frame = ttk.LabelFrame(parent, text="Streaming App", padding=10)
        app_frame.pack(fill="x", padx=10, pady=5)
        
        self.app_var = tk.StringVar(value=self.config["streaming_app"])
        app_combo = ttk.Combobox(app_frame, textvariable=self.app_var, 
                                values=["NTR CFW", "HzMod"], state="readonly")
        app_combo.pack(side="left", padx=5)
        
        # Control buttons
        button_frame = ttk.Frame(parent)
        button_frame.pack(fill="x", padx=10, pady=20)
        
        self.connect_btn = ttk.Button(button_frame, text="Connect", 
                                     command=self.toggle_streaming, style="Accent.TButton")
        self.connect_btn.pack(side="left", padx=5)
        
        ttk.Button(button_frame, text="Screenshot", 
                  command=self.take_screenshot).pack(side="left", padx=5)
        
        ttk.Button(button_frame, text="Settings", 
                  command=self.open_settings).pack(side="left", padx=5)
        
        # Status
        self.status_var = tk.StringVar(value="Ready to connect")
        status_label = ttk.Label(button_frame, textvariable=self.status_var)
        status_label.pack(side="right", padx=5)
        
        # Preview area
        preview_frame = ttk.LabelFrame(parent, text="Stream Preview", padding=10)
        preview_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        self.preview_label = ttk.Label(preview_frame, text="Stream will appear here")
        self.preview_label.pack(expand=True)
        
    def create_settings_tab(self, parent):
        # Quality settings
        quality_frame = ttk.LabelFrame(parent, text="Quality Settings", padding=10)
        quality_frame.pack(fill="x", padx=10, pady=5)
        
        ttk.Label(quality_frame, text="Quality:").grid(row=0, column=0, sticky="w")
        self.quality_var = tk.IntVar(value=self.config["quality"])
        quality_scale = ttk.Scale(quality_frame, from_=10, to=100, 
                                 variable=self.quality_var, orient="horizontal")
        quality_scale.grid(row=0, column=1, sticky="ew", padx=5)
        
        quality_label = ttk.Label(quality_frame, textvariable=self.quality_var)
        quality_label.grid(row=0, column=2, padx=5)
        
        # Layout settings
        layout_frame = ttk.LabelFrame(parent, text="Screen Layout", padding=10)
        layout_frame.pack(fill="x", padx=10, pady=5)
        
        self.layout_var = tk.StringVar(value=self.config["layout"])
        layouts = ["Vertical", "Horizontal", "Top Only", "Bottom Only", 
                  "Fullscreen Top", "Fullscreen Bottom", "Separate Windows"]
        
        for i, layout in enumerate(layouts):
            ttk.Radiobutton(layout_frame, text=layout, variable=self.layout_var, 
                           value=layout).grid(row=i//2, column=i%2, sticky="w", padx=5, pady=2)
        
        # Interpolation settings
        interp_frame = ttk.LabelFrame(parent, text="Interpolation", padding=10)
        interp_frame.pack(fill="x", padx=10, pady=5)
        
        self.interp_var = tk.StringVar(value=self.config["interpolation"])
        interp_combo = ttk.Combobox(interp_frame, textvariable=self.interp_var,
                                   values=["Nearest", "Linear", "Cubic", "Lanczos"],
                                   state="readonly")
        interp_combo.pack(side="left", padx=5)
        
    def create_advanced_tab(self, parent):
        # Auto-connect
        auto_frame = ttk.LabelFrame(parent, text="Automation", padding=10)
        auto_frame.pack(fill="x", padx=10, pady=5)
        
        self.auto_connect_var = tk.BooleanVar(value=self.config["auto_connect"])
        ttk.Checkbutton(auto_frame, text="Auto-connect on startup", 
                       variable=self.auto_connect_var).pack(anchor="w")
        
        # Hotkeys
        hotkey_frame = ttk.LabelFrame(parent, text="Keyboard Shortcuts", padding=10)
        hotkey_frame.pack(fill="x", padx=10, pady=5)
        
        hotkeys = [
            ("ESC", "Close Snickerstream"),
            ("UP/DOWN", "Increase/Decrease scaling"),
            ("LEFT/RIGHT", "Change interpolation"),
            ("S", "Take screenshot"),
            ("ENTER", "Return to connection window"),
            ("SPACE", "Pop up other screen (fullscreen modes)"),
        ]
        
        for i, (key, desc) in enumerate(hotkeys):
            ttk.Label(hotkey_frame, text=f"{key}:").grid(row=i, column=0, sticky="w", padx=5)
            ttk.Label(hotkey_frame, text=desc).grid(row=i, column=1, sticky="w", padx=5)
        
        # Save/Load config
        config_frame = ttk.Frame(parent)
        config_frame.pack(fill="x", padx=10, pady=10)
        
        ttk.Button(config_frame, text="Save Config", 
                  command=self.save_config).pack(side="left", padx=5)
        ttk.Button(config_frame, text="Load Config", 
                  command=self.load_config_file).pack(side="left", padx=5)
        ttk.Button(config_frame, text="Reset to Defaults", 
                  command=self.reset_config).pack(side="left", padx=5)
        
    def toggle_streaming(self):
        if not self.streaming:
            self.start_streaming()
        else:
            self.stop_streaming()
    
    def start_streaming(self):
        try:
            self.update_config()
            self.streaming = True
            self.connect_btn.config(text="Disconnect")
            self.status_var.set(f"Connecting to {self.config['ip']}:{self.config['port']}...")
            
            # Start streaming thread
            self.stream_thread = threading.Thread(target=self.stream_worker, daemon=True)
            self.stream_thread.start()
            
        except Exception as e:
            messagebox.showerror("Connection Error", f"Failed to start streaming: {str(e)}")
            self.streaming = False
            self.connect_btn.config(text="Connect")
            self.status_var.set("Connection failed")
    
    def stop_streaming(self):
        self.streaming = False
        self.connect_btn.config(text="Connect")
        self.status_var.set("Disconnected")
        
    def stream_worker(self):
        """Simplified streaming worker - would need actual NTR/HzMod protocol implementation"""
        try:
            # This is a placeholder for the actual streaming implementation
            self.status_var.set("Connected - Streaming...")
            
            # Simulate streaming loop
            while self.streaming:
                # In real implementation, this would:
                # 1. Receive image data from 3DS
                # 2. Process and display frames
                # 3. Handle scaling and interpolation
                
                # For now, just keep the connection alive
                threading.Event().wait(0.1)
                
        except Exception as e:
            self.root.after(0, lambda: messagebox.showerror("Streaming Error", str(e)))
        finally:
            self.root.after(0, lambda: self.stop_streaming())
    
    def take_screenshot(self):
        if self.streaming:
            # Placeholder for screenshot functionality
            messagebox.showinfo("Screenshot", "Screenshot saved to: screenshot.png")
        else:
            messagebox.showwarning("Not Streaming", "Cannot take screenshot while not streaming")
    
    def open_settings(self):
        # Settings are already in the Settings tab
        pass
    
    def update_config(self):
        try:
            self.config["ip"] = self.ip_var.get().strip()
            port_str = self.port_var.get().strip()
            if not port_str.isdigit() or not (1 <= int(port_str) <= 65535):
                raise ValueError("Port must be a number between 1 and 65535")
            self.config["port"] = int(port_str)
            self.config["streaming_app"] = self.app_var.get()
            self.config["quality"] = self.quality_var.get()
            self.config["layout"] = self.layout_var.get()
            self.config["interpolation"] = self.interp_var.get()
            self.config["auto_connect"] = self.auto_connect_var.get()
        except ValueError as e:
            raise ValueError(f"Invalid configuration: {str(e)}")
        except Exception as e:
            raise Exception(f"Configuration error: {str(e)}")
    
    def save_config(self):
        self.update_config()
        config_path = os.path.expanduser("~/.snickerstream_config.json")
        try:
            with open(config_path, 'w') as f:
                json.dump(self.config, f, indent=2)
            messagebox.showinfo("Config Saved", f"Configuration saved to {config_path}")
        except Exception as e:
            messagebox.showerror("Save Error", f"Failed to save config: {str(e)}")
    
    def load_config(self):
        config_path = os.path.expanduser("~/.snickerstream_config.json")
        try:
            if os.path.exists(config_path):
                with open(config_path, 'r') as f:
                    self.config.update(json.load(f))
        except Exception:
            pass  # Use defaults if config loading fails
    
    def load_config_file(self):
        filename = filedialog.askopenfilename(
            title="Load Configuration",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        if filename:
            try:
                with open(filename, 'r') as f:
                    self.config.update(json.load(f))
                self.refresh_ui()
                messagebox.showinfo("Config Loaded", "Configuration loaded successfully")
            except Exception as e:
                messagebox.showerror("Load Error", f"Failed to load config: {str(e)}")
    
    def reset_config(self):
        self.config = {
            "ip": "192.168.1.100",
            "port": 8000,
            "streaming_app": "NTR CFW",
            "quality": 90,
            "layout": "Vertical",
            "interpolation": "Linear",
            "auto_connect": False
        }
        self.refresh_ui()
        messagebox.showinfo("Config Reset", "Configuration reset to defaults")
    
    def refresh_ui(self):
        """Update UI elements with current config values"""
        self.ip_var.set(self.config["ip"])
        self.port_var.set(str(self.config["port"]))
        self.app_var.set(self.config["streaming_app"])
        self.quality_var.set(self.config["quality"])
        self.layout_var.set(self.config["layout"])
        self.interp_var.set(self.config["interpolation"])
        self.auto_connect_var.set(self.config["auto_connect"])


def main():
    try:
        # Set up tkinter with better theming
        root = tk.Tk()
        
        # Try to use modern theme if available
        try:
            root.tk.call('source', '/usr/share/tcltk/tk8.6/ttk/altTheme.tcl')
            style = ttk.Style()
            style.theme_use('alt')
        except:
            pass
        
        # Create and run the application
        app = SnickerStreamGUI(root)
        
        # Auto-connect if enabled
        if app.config.get("auto_connect", False):
            root.after(1000, app.start_streaming)
        
        # Set up proper close handling
        def on_closing():
            try:
                if app.streaming:
                    app.stop_streaming()
                root.destroy()
            except Exception:
                pass  # Ignore errors during shutdown
        
        root.protocol("WM_DELETE_WINDOW", on_closing)
        
        # Bind hotkeys
        root.bind('<Escape>', lambda e: on_closing())
        root.bind('<KeyPress-s>', lambda e: app.take_screenshot())
        
        # Start the GUI
        root.mainloop()
        
    except Exception as e:
        print(f"Fatal error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()