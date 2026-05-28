# ⚡ Vibe Coding Cache Cleaner

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12+-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python Version" />
  <img src="https://img.shields.io/badge/GUI-CustomTkinter-indigo?style=for-the-badge&logo=kinetic" alt="GUI Framework" />
  <img src="https://img.shields.io/badge/OS-Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white" alt="OS Windows" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License" />
</p>

---

## 📝 Deskripsi Singkat GitHub (Untuk Kolom About GitHub)
> **"Aplikasi GUI desktop Windows modern & cerdas berbasis Python untuk menutup paksa proses AI Coding Agent (Cursor, Windsurf, Antigravity, Kiro, Codex, OpenCode) dan membersihkan file cache pengunci chat history secara aman dengan sekali klik."**

---

## 🌟 Tentang Proyek
**Vibe Coding Cache Cleaner** adalah aplikasi utilitas desktop Windows premium yang dirancang khusus untuk memulihkan, menyegarkan, dan mengoptimalkan lingkungan kerja para developer (*Vibe Coders*). 

Ketika bekerja secara intensif menggunakan AI Coding Agents (seperti Cursor AI, Windsurf, Kiro, dsb.), file cache riwayat obrolan sering kali menumpuk, mengonsumsi ruang disk, atau bahkan "mengunci" proses editor Anda sehingga menyebabkan hang/error. Utilitas ini menyelesaikan masalah tersebut dengan melakukan pemberhentian paksa proses latar belakang dan melakukan pembersihan cache secara menyeluruh hanya dengan satu kali klik.

---

## 🛠️ Fitur Utama & Keunggulan

*   🖥️ **Premium Dashboard UI:** Antarmuka modern bernuansa *Dark Slate* minimalis bergaya SaaS kustom, lengkap dengan konsol status terminal real-time berwarna hijau matriks (`Consolas`).
*   🔍 **Sistem Auto-Detect Cerdas:** Aplikasi secara otomatis memindai sistem lokal Anda untuk mendeteksi AI Agent mana saja yang terinstal dan langsung menandainya dengan tag **`(Terdeteksi)`** serta mengaktifkan centang secara otomatis.
*   ⚡ **Asynchronous Pembersihan (Multithreading):** Proses pembersihan berjalan di latar belakang (*background thread*), memastikan GUI aplikasi tetap responsif, lancar, dan tidak mengalami *freeze* / *Not Responding*.
*   🤖 **Dukungan AI Agent Sangat Luas (IDE & CLI):**
    *   **Cursor AI** (`Cursor.exe` & default Cache)
    *   **Windsurf** (`Windsurf.exe` & default Cache)
    *   **VS Code (General AI Extensions)** (`Code.exe` & CachedData)
    *   **Antigravity IDE & CLI** (`antigravity-ide.exe`, `antigravity-cli.exe` & `.gemini` Cache)
    *   **Kiro IDE & CLI** (`kiro.exe`, `kiro-cli.exe` & `.kiro` Cache)
    *   **Codex IDE & CLI** (`codex.exe`, `codex-cli.exe` & `.codex` Cache)
    *   **OpenCode Go GUI & CLI** (`opencode.exe`, `opencode-cli.exe` & `.cache/opencode` / `.opencode-suites` Cache)

---

## 📐 Layout Antarmuka (Dashboard)
Aplikasi didesain menggunakan skema 2 kolom yang efisien:
```
+-------------------------------------------------------------------------+
|                        VIBE CODING CACHE CLEANER                        |
|   Tutup paksa proses AI Agent & bersihkan file cache secara aman        |
+--------------------------------------------------+----------------------+
| 1. PILIH AI AGENT TARGET                         | 2. KONSOL STATUS     |
| [x] Cursor AI (Terdeteksi)                       | > Sistem Siap...     |
| [x] Windsurf (Terdeteksi)                        | > Sukses delete...   |
| [ ] Antigravity IDE                              | > Selesai.           |
| [x] OpenCode Go CLI (Terdeteksi)                 +----------------------+
| [ ] ...                                          |  MULAI PEMBERSIHAN   |
+--------------------------------------------------+----------------------+
```

---

## 🚀 Memulai (Panduan Instalasi & Penggunaan)

### 📌 Persyaratan Sistem
*   Windows OS
*   Python 3.10 ke atas (jika menjalankan dari source code)

### 📥 Menjalankan dari Source Code
1. Clone repositori ini ke komputer lokal Anda.
2. Pastikan Anda menginstal *library* yang dibutuhkan terlebih dahulu:
   ```bash
   pip install customtkinter psutil
   ```
3. Jalankan aplikasi utama:
   ```bash
   python app.py
   ```

### 📦 Mengubah Menjadi Aplikasi `.exe` Mandiri (Standalone)
Jika Anda ingin mendistribusikan aplikasi ini sebagai file `.exe` yang bisa dijalankan dengan sekali klik di Windows manapun tanpa perlu instalasi Python:
1. Instal PyInstaller:
   ```bash
   pip install pyinstaller
   ```
2. Jalankan perintah kompilasi:
   ```bash
   pyinstaller --noconsole --onefile app.py
   ```
3. File executable hasil kompilasi siap digunakan di folder `dist/app.exe`.

---

## 🤝 Kontribusi
Aplikasi ini bersifat open-source dan kami sangat terbuka terhadap kontribusi dari komunitas! 

Jika Anda ingin berkontribusi:
1. **Fork** repositori ini.
2. Buat branch fitur baru Anda (`git checkout -b fitur/AgenBaru`).
3. Commit perubahan Anda (`git commit -m 'Menambahkan deteksi agen XYZ'`).
4. **Push** ke branch tersebut (`git push origin fitur/AgenBaru`).
5. Silakan kirimkan **Pull Request (PR)** Anda, dan kami akan dengan senang hati meninjau kontribusi Anda! 🚀

---

## 📜 Lisensi
Proyek ini dilisensikan di bawah **MIT License** - lihat file [LICENSE](LICENSE) untuk detailnya.

---

<p align="center">
  Dibuat dengan 💻 dan ☕ untuk komunitas Vibe Coding dunia.
</p>
