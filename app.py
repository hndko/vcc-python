import os
import shutil
import threading
import customtkinter as ctk
import psutil

# Konfigurasi Tema GUI
ctk.set_appearance_mode("System")  # Pilihan: "System", "Dark", "Light"
ctk.set_default_color_theme("blue")

class CacheCleanerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Vibe Coding Cache Cleaner")
        self.geometry("600x550")
        self.resizable(False, False)

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
        # Header
        self.header_label = ctk.CTkLabel(self, text="AI Agent Cache Cleaner", font=ctk.CTkFont(size=20, weight="bold"))
        self.header_label.pack(pady=(20, 10))

        self.sub_label = ctk.CTkLabel(self, text="Tutup proses & bersihkan chat history yang mengunci", font=ctk.CTkFont(size=12))
        self.sub_label.pack(pady=(0, 15))

        # Frame untuk Target Checkbox (Menggunakan CTkScrollableFrame agar muat banyak)
        self.checkbox_frame = ctk.CTkScrollableFrame(self, height=150)
        self.checkbox_frame.pack(pady=10, fill="x", padx=40)

        for name, info in self.targets.items():
            # Auto-detect: Cek apakah folder cache ada di sistem
            cache_exists = os.path.exists(info["cache_path"])
            
            if cache_exists:
                display_text = f"{name} (Terdeteksi)"
                var = ctk.BooleanVar(value=True)  # Auto-check jika ditemukan
            else:
                display_text = f"{name}"
                var = ctk.BooleanVar(value=False) # Uncheck jika tidak ada
                
            self.checkbox_vars[name] = var
            cb = ctk.CTkCheckBox(self.checkbox_frame, text=display_text, variable=var)
            cb.pack(anchor="w", pady=6, padx=20)

        # Log Console
        self.log_text = ctk.CTkTextbox(self, height=150, width=520, state="disabled")
        self.log_text.pack(pady=15, padx=40)
        self.log("Sistem Siap. Pilih target dan klik 'Mulai Pembersihan'.")

        # Tombol Aksi Utama
        self.clean_btn = ctk.CTkButton(self, text="Mulai Pembersihan", command=self.start_cleanup_thread, font=ctk.CTkFont(weight="bold"))
        self.clean_btn.pack(pady=(5, 20))

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