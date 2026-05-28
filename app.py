import os
import shutil
import threading
import customtkinter as ctk
import psutil

# Konfigurasi Tema GUI
ctk.set_appearance_mode("Dark")  # Force Dark Mode untuk tampilan premium
ctk.set_default_color_theme("blue")

class CacheCleanerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Vibe Coding Cache Cleaner")
        self.geometry("840x520")
        self.resizable(False, False)
        self.configure(fg_color="#0f172a")  # Slate 900 (Gelap modern)

        user_home = os.path.expanduser("~")

        # Definisi Target Agent (Bisa ditambah sesuai kebutuhan)
        # Format: "Nama Tampilan": {"process": "nama_proses.exe", "cache_path": "Path/Ke/Cache"}
        self.targets = {
            "Cursor AI": {
                "process": "Cursor.exe",
                "cache_path": os.path.join(os.getenv('APPDATA'), "Cursor", "User Data", "Default", "Cache")
            },
            "Windsurf": {
                "process": "Windsurf.exe",
                "cache_path": os.path.join(os.getenv('APPDATA'), "Windsurf", "User Data", "Default", "Cache")
            },
            "VS Code (General AI Extensions)": {
                "process": "Code.exe",
                "cache_path": os.path.join(os.getenv('APPDATA'), "Code", "CachedData")
            },
            "Antigravity IDE": {
                "process": "antigravity-ide.exe",
                "cache_path": os.path.join(user_home, ".gemini", "antigravity-ide", "brain")
            },
            "Antigravity CLI": {
                "process": "antigravity-cli.exe",
                "cache_path": os.path.join(user_home, ".gemini", "antigravity-cli", "cache")
            },
            "Kiro IDE": {
                "process": "kiro.exe",
                "cache_path": os.path.join(user_home, ".kiro", "sessions")
            },
            "Kiro CLI": {
                "process": "kiro-cli.exe",
                "cache_path": os.path.join(user_home, ".kiro", "tasks")
            },
            "Codex IDE": {
                "process": "codex.exe",
                "cache_path": os.path.join(user_home, ".codex", "cache")
            },
            "Codex CLI": {
                "process": "codex-cli.exe",
                "cache_path": os.path.join(user_home, ".codex", "tmp")
            },
            "OpenCode Go GUI": {
                "process": "opencode.exe",
                "cache_path": os.path.join(user_home, ".cache", "opencode")
            },
            "OpenCode Go CLI": {
                "process": "opencode-cli.exe",
                "cache_path": os.path.join(user_home, ".opencode-suites")
            }
        }

        self.checkbox_vars = {}
        self.setup_ui()

    def setup_ui(self):
        # --- HEADER AREA ---
        self.header_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.header_frame.pack(fill="x", padx=40, pady=(20, 15))

        self.header_label = ctk.CTkLabel(
            self.header_frame, 
            text="Vibe Coding Cache Cleaner", 
            font=ctk.CTkFont(family="Segoe UI", size=22, weight="bold"),
            text_color="#f8fafc"
        )
        self.header_label.pack(anchor="w")

        self.sub_label = ctk.CTkLabel(
            self.header_frame, 
            text="Tutup paksa proses AI Agent & bersihkan file cache pengunci chat history secara aman", 
            font=ctk.CTkFont(family="Segoe UI", size=12),
            text_color="#94a3b8"
        )
        self.sub_label.pack(anchor="w", pady=(2, 0))

        # --- MAIN BODY FRAME (Dashboard 2 Kolom) ---
        self.content_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.content_frame.pack(fill="both", expand=True, padx=40, pady=(0, 20))
        
        self.content_frame.columnconfigure(0, weight=4) # Kolom Kiri: Checkboxes (Lebih ramping)
        self.content_frame.columnconfigure(1, weight=5) # Kolom Kanan: Console (Lebih lebar)
        self.content_frame.rowconfigure(0, weight=1)

        # ================= KOLOM KIRI: PILIH TARGET =================
        self.left_frame = ctk.CTkFrame(self.content_frame, fg_color="#1e293b", corner_radius=12, border_color="#334155", border_width=1)
        self.left_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 10))

        self.left_title = ctk.CTkLabel(
            self.left_frame, 
            text="1. PILIH AI AGENT TARGET", 
            font=ctk.CTkFont(family="Segoe UI", size=13, weight="bold"),
            text_color="#38bdf8"
        )
        self.left_title.pack(anchor="w", padx=18, pady=(15, 8))

        # Scrollable Frame untuk target
        self.checkbox_frame = ctk.CTkScrollableFrame(
            self.left_frame, 
            fg_color="transparent", 
            scrollbar_button_color="#334155",
            scrollbar_button_hover_color="#475569"
        )
        self.checkbox_frame.pack(fill="both", expand=True, padx=8, pady=(0, 15))

        for name, info in self.targets.items():
            cache_exists = os.path.exists(info["cache_path"])
            
            if cache_exists:
                display_text = f"{name} (Terdeteksi)"
                var = ctk.BooleanVar(value=True)
                tc = "#f8fafc"  # Bright white for detected
                bc = "#0ea5e9"  # Active border
            else:
                display_text = f"{name}"
                var = ctk.BooleanVar(value=False)
                tc = "#64748b"  # Muted slate for missing
                bc = "#334155"  # Muted border
                
            self.checkbox_vars[name] = var
            cb = ctk.CTkCheckBox(
                self.checkbox_frame, 
                text=display_text, 
                variable=var,
                text_color=tc,
                fg_color="#0ea5e9",
                hover_color="#0284c7",
                border_color=bc,
                font=ctk.CTkFont(family="Segoe UI", size=12, weight="bold" if cache_exists else "normal")
            )
            cb.pack(anchor="w", pady=6, padx=15)

        # ================= KOLOM KANAN: KONSOL & AKSI =================
        self.right_frame = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        self.right_frame.grid(row=0, column=1, sticky="nsew", padx=(10, 0))

        self.right_title = ctk.CTkLabel(
            self.right_frame, 
            text="2. KONSOL STATUS & AKSI", 
            font=ctk.CTkFont(family="Segoe UI", size=13, weight="bold"),
            text_color="#38bdf8"
        )
        self.right_title.pack(anchor="w", pady=(0, 8))

        # Log Console (Gaya Terminal Modern)
        self.log_text = ctk.CTkTextbox(
            self.right_frame, 
            fg_color="#09090b", 
            text_color="#34d399",  # Monospace green matrix style
            font=("Consolas", 11), 
            border_color="#334155",
            border_width=1,
            state="disabled"
        )
        self.log_text.pack(fill="both", expand=True, pady=(0, 15))
        self.log("Sistem Siap. Pilih target lalu klik 'Mulai Pembersihan'.")

        # Tombol Pembersihan Besar & Premium
        self.clean_btn = ctk.CTkButton(
            self.right_frame, 
            text="MULAI PEMBERSIHAN", 
            height=45,
            fg_color="#0ea5e9",
            hover_color="#0284c7",
            text_color="#ffffff",
            font=ctk.CTkFont(family="Segoe UI", size=13, weight="bold"),
            corner_radius=8,
            command=self.start_cleanup_thread
        )
        self.clean_btn.pack(fill="x")

    def log(self, message):
        """Fungsi helper untuk mencetak log ke GUI Console"""
        self.log_text.configure(state="normal")
        self.log_text.insert("end", message + "\n")
        self.log_text.see("end")
        self.log_text.configure(state="disabled")

    def start_cleanup_thread(self):
        """Menjalankan pembersihan di thread terpisah agar GUI tidak membeku (freeze)"""
        threading.Thread(target=self.execute_cleanup, daemon=True).start()

    def execute_cleanup(self):
        self.clean_btn.configure(state="disabled", text="Memproses...")
        self.log("\n--- Memulai Proses Cleanup ---")

        any_selected = False

        for name, info in self.targets.items():
            if self.checkbox_vars[name].get():
                any_selected = True
                self.log(f"\nChecking: {name}...")

                # 1. Kill Process
                self.kill_target_process(info["process"])

                # 2. Clean Cache Directory
                self.clean_target_dir(info["cache_path"])

        if not any_selected:
            self.log("Peringatan: Tidak ada target yang dipilih.")

        self.log("\n--- Semua Proses Selesai ---")
        self.clean_btn.configure(state="normal", text="Mulai Pembersihan")

    def kill_target_process(self, process_name):
        killed = False
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                if process_name.lower() in proc.info['name'].lower():
                    proc.kill()
                    self.log(f"-> Berhasil mematikan proses: {proc.info['name']} (PID: {proc.info['pid']})")
                    killed = True
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                self.log(f"-> Gagal mematikan proses terdeteksi: {process_name} (Akses Ditolak)")
        if not killed:
            self.log(f"-> Proses {process_name} tidak sedang berjalan (Aman).")

    def clean_target_dir(self, folder_path):
        if not os.path.exists(folder_path):
            self.log(f"-> Folder tidak ditemukan (Sudah bersih/belum terinstal): {folder_path}")
            return

        success_count = 0
        fail_count = 0

        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
                success_count += 1
            except Exception as e:
                fail_count += 1

        if success_count > 0 or fail_count > 0:
            self.log(f"-> Sukses menghapus {success_count} item. Gagal: {fail_count} item.")
        else:
            self.log("-> Folder cache sudah kosong.")

if __name__ == "__main__":
    app = CacheCleanerApp()
    app.mainloop()