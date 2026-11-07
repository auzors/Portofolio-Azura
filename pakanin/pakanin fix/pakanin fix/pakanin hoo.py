import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os

# Model (unchanged)
class PakanModel:
    REKOMENDASI_PAKAN = {
        'Lele': {'Pelet Udang': 0.03, 'Pelet Ikan': 0.04, 'Cacing Sutra': 0.05},
        'Nila': {'Pelet Udang': 0.02, 'Pelet Ikan': 0.03, 'Dedak': 0.04},
        'Gurame': {'Pelet Ikan': 0.025, 'Daun Talas': 0.05, 'Pepaya': 0.04},
        'Bawal': {'Pelet Ikan': 0.03, 'Cacing': 0.05, 'Eceng Gondok': 0.04},
        'Mujair': {'Pelet Ikan': 0.02, 'Cacing Anaconda': 0.03, 'Dedak': 0.04}
    }

    INFO_IKAN = {
        'Lele': """""",
        'Nila': 'Nila cocok dibudidayakan dan mudah beradaptasi.',
        'Gurame': 'Gurame lebih lambat tumbuh tapi bernilai tinggi.',
        'Bawal': 'Bawal aktif dan responsif terhadap pakan.',
        'Mujair': 'Mujair hemat pakan dan tangguh dalam lingkungan.'
    }

    def __init__(self):
        self.jenis_ikan = ""
        self.jenis_pakan = ""
        self.jumlah_ikan = 0
        self.hasil_perhitungan = 0

    def set_data(self, jenis_ikan, jenis_pakan, jumlah_ikan):
        self.jenis_ikan = jenis_ikan
        self.jenis_pakan = jenis_pakan
        self.jumlah_ikan = jumlah_ikan

    def hitung_kebutuhan_pakan(self):
        try:
            if not self.jenis_ikan or not self.jenis_pakan or self.jumlah_ikan <= 0:
                return False
            persentase = self.REKOMENDASI_PAKAN[self.jenis_ikan][self.jenis_pakan]
            self.hasil_perhitungan = self.jumlah_ikan * persentase
            return True
        except KeyError:
            return False

    def get_rekomendasi_pakan(self, jenis_ikan):
        return list(self.REKOMENDASI_PAKAN.get(jenis_ikan, {}).keys())

    def get_info_ikan(self, jenis_ikan):
        return self.INFO_IKAN.get(jenis_ikan, "Informasi tidak tersedia.")

# View (modified for responsive text and blue background)
class PakanView(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Pakanin - Kalkulator Pakan Ikan")
        self.geometry("700x550")
        self.configure(bg='#E0F7FA')  # ubah background utama
        self.minsize(700, 550)
        
        # Store font sizes for dynamic scaling
        self.font_sizes = {
            'title': 16,
            'subtitle': 14,
            'normal': 10,
            'bold': 10
        }

        try:
            icon_path = os.path.join(os.path.dirname(__file__), "logo.png")
            self.iconphoto(False, tk.PhotoImage(file=icon_path))
        except:
            pass

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.fish_images = self._load_fish_images()
        self.logo_menu = self._load_logo_menu()
        self.frames = {}
        self._setup_frames()
        self.show_frame("start")

        self.bind("<Configure>", self._on_resize)
    
    def _load_logo_menu(self):
        logos = {}
        logo_names = ['Logo_Selamat', 'Logo_Awal', 'Logo_Kenali', 'Logo_rekomendasi', 'Logo_Hitung']
        for name in logo_names:
            try:
                img_path = os.path.join(os.path.dirname(__file__), f"{name.lower()}.png")
                img = Image.open(img_path)
                img = img.resize((80, 80), Image.LANCZOS)
                logos[name] = ImageTk.PhotoImage(img)
            except:
                img = Image.new('RGB', (80, 80), color='#B2EBF2')  # Light blue placeholder
                logos[name] = ImageTk.PhotoImage(img)
        return logos

    def _load_fish_images(self):
        images = {}
        fish_types = ['Lele', 'Nila', 'Gurame', 'Bawal', 'Mujair', ]
        for fish in fish_types:
            try:
                img_path = os.path.join(os.path.dirname(__file__), f"{fish.lower()}.png")
                img = Image.open(img_path)
                img = img.resize((80, 80), Image.LANCZOS)
                images[fish] = ImageTk.PhotoImage(img)
            except:
                img = Image.new('RGB', (80, 80), color='#B2EBF2')  # Light blue placeholder
                images[fish] = ImageTk.PhotoImage(img)
        return images

    def _setup_frames(self):
        container = tk.Frame(self, bg="#E0F7FA")  # Light blue background
        container.grid(row=0, column=0, sticky="nsew")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames["start"] = self._create_start_frame(container)
        self.frames["main"] = self._create_main_frame(container)
        self.frames["rekomendasi"] = self._create_rekomendasi_frame(container)
        self.frames["kenaliikan"] = self._create_kenaliikan_frame(container)

        for frame in self.frames.values():
            frame.grid(row=0, column=0, sticky="nsew")

    def show_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()

    def _create_styled_button(self, parent, text, command, image=None):
        btn = tk.Button(parent, text=text, command=command, image=image, compound=tk.LEFT,
                      font=("Helvetica", self.font_sizes['normal']), 
                      bg="#4DD0E1", fg="black", relief=tk.RAISED,
                      activebackground="#26C6DA", activeforeground="#DDEEFF",
                      padx=10, pady=5, bd=0)
        btn.bind("<Enter>", lambda e: btn.config(bg="#26C6DA"))
        btn.bind("<Leave>", lambda e: btn.config(bg="#4DD0E1"))
        return btn

    def _create_start_frame(self, parent):
        frame = tk.Frame(parent, bg="#E0F7FA", bd=0)  # Light blue background
        
        # Header with logo and title
        header = tk.Frame(frame, bg="#E0F7FA")
        header.pack(pady=20)
        
        if self.logo_menu['Logo_Awal']:
            logo = tk.Label(header, image=self.logo_menu['Logo_Awal'], bg="#E0F7FA")
            logo.pack(side=tk.LEFT, padx=10)


        self.title_label = tk.Label(header, text="Selamat Datang di Pakanin", 
                                  font=("Helvetica", self.font_sizes['title'], "bold"), 
                                  bg="#E0F7FA", fg="#00838F")
        self.title_label.pack(side=tk.LEFT)

        # Buttons frame
        btn_frame = tk.Frame(frame, bg="#E0F7FA")
        btn_frame.pack(pady=20)

        self._create_styled_button(btn_frame, "Kenali Ikanmu", 
            lambda: self.show_frame("kenaliikan"), 
            self.logo_menu['Logo_Kenali']).pack(pady=10, ipadx=20)

        self._create_styled_button(btn_frame, "Hitung Kebutuhan Pakan", 
            lambda: self.show_frame("main"), 
            self.logo_menu['Logo_Hitung']).pack(pady=10, ipadx=20)

        self._create_styled_button(btn_frame, "Rekomendasi Pakan", 
            lambda: self.show_frame("rekomendasi"), 
        self.logo_menu['Logo_rekomendasi']).pack(pady=10, ipadx=20)


        return frame

    def _create_main_frame(self, parent):
        frame = tk.Frame(parent, bg="#E0F7FA", bd=0)  # Light blue background

        self.label_kalkulator = tk.Label(frame, text="Kalkulator Pakan Ikan", 
                                       font=("Helvetica", self.font_sizes['subtitle'], "bold"), 
                                       bg="#E0F7FA", fg="#00838F")
        self.label_kalkulator.pack(pady=20)

        form_frame = tk.Frame(frame, bg="#E0F7FA")
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Jenis Ikan:", bg="#E0F7FA", 
                font=("Helvetica", self.font_sizes['normal'])).grid(row=0, column=0, sticky="w", pady=5)
        
        self.jenis_ikan_combobox = ttk.Combobox(form_frame, 
                                              values=list(self.controller.model.REKOMENDASI_PAKAN.keys()), 
                                              width=25,
                                              font=("Helvetica", self.font_sizes['normal']))
        self.jenis_ikan_combobox.grid(row=0, column=1, pady=5, padx=5)
        self.jenis_ikan_combobox.bind("<<ComboboxSelected>>", self.controller.on_jenis_ikan_selected)

        tk.Label(form_frame, text="Jenis Pakan:", bg="#E0F7FA",
                font=("Helvetica", self.font_sizes['normal'])).grid(row=1, column=0, sticky="w", pady=5)
        
        self.jenis_pakan_combobox = ttk.Combobox(form_frame, width=25,
                                               font=("Helvetica", self.font_sizes['normal']))
        self.jenis_pakan_combobox.grid(row=1, column=1, pady=5, padx=5)

        tk.Label(form_frame, text="Jumlah Ikan:", bg="#E0F7FA",
                font=("Helvetica", self.font_sizes['normal'])).grid(row=2, column=0, sticky="w", pady=5)
        
        self.jumlah_ikan_entry = ttk.Entry(form_frame, width=27,
                                         font=("Helvetica", self.font_sizes['normal']))
        self.jumlah_ikan_entry.grid(row=2, column=1, pady=5, padx=5)

        self._create_styled_button(frame, "Hitung", self.controller.on_hitung).pack(pady=20)
        
        self.hasil_label = tk.Label(frame, text="", fg="#00695C", bg="#E0F7FA", 
                                  font=("Helvetica", self.font_sizes['normal'], "bold"))
        self.hasil_label.pack(pady=10)
        
        self._create_styled_button(frame, "Kembali", lambda: self.show_frame("start")).pack(pady=10)

        return frame

    def _create_rekomendasi_frame(self, parent):
        frame = tk.Frame(parent, bg="#E0F7FA", bd=0)  # Light blue background

        tk.Label(frame, text="Rekomendasi Pakan", 
                font=("Helvetica", self.font_sizes['subtitle'], "bold"), 
                bg="#E0F7FA", fg="#00838F").pack(pady=20)

        text_frame = tk.Frame(frame, bg="#E0F7FA")
        text_frame.pack(pady=5, expand=True, fill="both", padx=20)

        scrollbar = tk.Scrollbar(text_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.rekomendasi_text = tk.Text(text_frame, height=15, width=60, 
                                       bg="#B2EBF2", fg="#006064",  # Light blue text area
                                       yscrollcommand=scrollbar.set,
                                       font=("Helvetica", self.font_sizes['normal']),
                                       padx=10, pady=10)
        self.rekomendasi_text.pack(expand=True, fill="both")

        scrollbar.config(command=self.rekomendasi_text.yview)
        self.rekomendasi_text.config(state=tk.NORMAL)

        for ikan, pakans in self.controller.model.REKOMENDASI_PAKAN.items():
            if ikan in self.fish_images:
                self.rekomendasi_text.image_create(tk.END, image=self.fish_images[ikan])
                self.rekomendasi_text.insert(tk.END, " ")
            self.rekomendasi_text.insert(tk.END, f"{ikan}:", 'bold')
            self.rekomendasi_text.insert(tk.END, "\n")
            for pakan in pakans:
                self.rekomendasi_text.insert(tk.END, f"  • {pakan}\n")
            self.rekomendasi_text.insert(tk.END, "\n")

        self.rekomendasi_text.tag_configure('bold', 
                                          font=('Helvetica', self.font_sizes['bold'], 'bold'))
        self.rekomendasi_text.config(state=tk.DISABLED)
        
        self._create_styled_button(frame, "Kembali", lambda: self.show_frame("start")).pack(pady=20)

        return frame

    def _create_kenaliikan_frame(self, parent):
        frame = tk.Frame(parent, bg="#E0F7FA", bd=0)

        tk.Label(frame, text="Kenali Ikanmu",
                 font=("Helvetica", self.font_sizes['subtitle'], "bold"),
                 bg="#E0F7FA", fg="#00838F").pack(pady=20)

        canvas = tk.Canvas(frame, bg="#E0F7FA", highlightthickness=0, bd=0)
        scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)

        scrollable_frame = tk.Frame(canvas, bg="#E0F7FA")
        canvas_window = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

        # Buat isi scroll follow canvas lebar
        def _on_canvas_configure(event):
            canvas.itemconfig(canvas_window, width=event.width)
        canvas.bind("<Configure>", _on_canvas_configure)

        # Update scroll region saat isi berubah
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")

        canvas.bind_all("<MouseWheel>", _on_mousewheel)  # Untuk Windows


        # ISI IKAN
        for ikan, info in self.controller.model.INFO_IKAN.items():
            ikan_frame = tk.Frame(scrollable_frame, bg="#B2EBF2", pady=10)
            ikan_frame.pack(fill="x", padx=10, pady=(0, 10))

            if ikan in self.fish_images:
                img_label = tk.Label(ikan_frame, image=self.fish_images[ikan], bg="#B2EBF2")
                img_label.pack(side="left", padx=10)

            text_widget = tk.Text(ikan_frame,
                bg="#B2EBF2",
                fg="#006064",
                font=("Helvetica", self.font_sizes['normal']),
                wrap="word",
                relief="flat",
                height=10,
                padx=0,
                pady=0
            )
            text_widget.pack(side="left", fill="x", expand=True)

                        # Contoh: isian untuk ikan Lele
            if ikan == "Lele":
                text_widget.insert(tk.END, "Lele:\n", "bold")
                text_widget.insert(tk.END, "Bentuk tubuh: ", "bold")
                text_widget.insert(tk.END, "Lonjong dan ramping, dengan kulit halus.\n")
                text_widget.insert(tk.END, "Kepala: ", "bold")
                text_widget.insert(tk.END, "Keras menulang, dengan mata kecil dan mulut lebar.\n")
                text_widget.insert(tk.END, "Sungut: ", "bold")
                text_widget.insert(tk.END, "Empat pasang sungut peraba (barbels) yang berfungsi untuk mendeteksi makanan. \n")
                text_widget.insert(tk.END, "Sirip: ", "bold")
                text_widget.insert(tk.END, "Sirip punggung dan sirip anus memanjang. Sirip ekor kadang menyatu\n")
                text_widget.insert(tk.END, "Warna: ", "bold")
                text_widget.insert(tk.END, "Kulit berwarna gelap, cenderung kehitaman atau kebiruan dengan bintik-bintik kecil berwarna putih.\n")
                text_widget.insert(tk.END, "Tidak bersisik: ", "bold")
                text_widget.insert(tk.END, "Tubuh lele tidak ditutupi sisik.\n")
                text_widget.insert(tk.END, "Habitat: ", "bold")
                text_widget.insert(tk.END, "Air tawar\n")
                text_widget.insert(tk.END, "Masa Panen: ", "bold")
                text_widget.insert(tk.END, "3-4 bulan mencapai memiliki ukuran 4-7 ekor per kilogram.\n")
            
            elif ikan == "Nila":
                text_widget.insert(tk.END, "Nila:\n", "bold")
                text_widget.insert(tk.END, "Bentuk tubuh: ", "bold")
                text_widget.insert(tk.END, "Pipih, bulat, memanjang.\n")
                text_widget.insert(tk.END, "Garis sisi: ", "bold")
                text_widget.insert(tk.END, "Terdapat lateral line.\n")
                text_widget.insert(tk.END, "Sirip: ", "bold")
                text_widget.insert(tk.END, "5 jenis sirip lengkap.\n")
                text_widget.insert(tk.END, "Warna: ", "bold")
                text_widget.insert(tk.END, "Keabuan dengan garis gelap.\n")
                text_widget.insert(tk.END, "Sirip ekor: ", "bold")
                text_widget.insert(tk.END, "Bulat dengan garis tegak.\n")
                text_widget.insert(tk.END, "Mata: ", "bold")
                text_widget.insert(tk.END, "Menonjol.\n")
                text_widget.insert(tk.END, "Habitat: ", "bold")
                text_widget.insert(tk.END, "Air tawar.\n")
                text_widget.insert(tk.END, "Masa Panen: ", "bold")
                text_widget.insert(tk.END, "4–6 bulan dengan ukuran ikan yang diminati pasar yaitu 300-500 gram per ekor\n")
            
            elif ikan == "Gurame":
                text_widget.insert(tk.END, "Gurame:\n", "bold")
                text_widget.insert(tk.END, "Bentuk tubuh: ", "bold")
                text_widget.insert(tk.END, "Tertutup sisik kuat dan agak kasar.\n")
                text_widget.insert(tk.END, "Mulut: ", "bold")
                text_widget.insert(tk.END, "Kecil dan miring.\n")
                text_widget.insert(tk.END, "Warna: ", "bold")
                text_widget.insert(tk.END, "Perut keperakan, punggung sawo matang.\n")
                text_widget.insert(tk.END, "Gurat Sisi: ", "bold")
                text_widget.insert(tk.END, "30–33 sisik dari kepala hingga ekor.\n")
                text_widget.insert(tk.END, "Bibir bawah: ", "bold")
                text_widget.insert(tk.END, "Sedikit menonjol.\n")
                text_widget.insert(tk.END, "Sirip: ", "bold")
                text_widget.insert(tk.END, "Lengkap, termasuk sirip perut yang dimodifikasi menjadi alat peraba.\n")
                text_widget.insert(tk.END, "Habitat: ", "bold")
                text_widget.insert(tk.END, "Air tawar.\n")
                text_widget.insert(tk.END, "Masa Panen: ", "bold")
                text_widget.insert(tk.END, "8–12 bulan dengan berat 500 g – 1 kg.\n")
            
            elif ikan == "Bawal":
                text_widget.insert(tk.END, "Bawal:\n", "bold")
                text_widget.insert(tk.END, "Bentuk tubuh: ", "bold")
                text_widget.insert(tk.END, "Oval dan pipih.\n")
                text_widget.insert(tk.END, "Sirip: ", "bold")
                text_widget.insert(tk.END, "Berwarna merah.\n")
                text_widget.insert(tk.END, "Warna: ", "bold")
                text_widget.insert(tk.END, "Punggung abu tua, perut putih kemerahan.\n")
                text_widget.insert(tk.END, "Garis Hitam: ", "bold")
                text_widget.insert(tk.END, "Ada di sirip ekor.\n")
                text_widget.insert(tk.END, "Kepala: ", "bold")
                text_widget.insert(tk.END, "Kecil, gigi tajam, rahang pendek.\n")
                text_widget.insert(tk.END, "Habitat: ", "bold")
                text_widget.insert(tk.END, "Air tawar.\n")
                text_widget.insert(tk.END, "Masa Panen: ", "bold")
                text_widget.insert(tk.END, "8–12 bulan, berat 500 g – 1 kg.\n")
            elif ikan == "Mujair":
                text_widget.insert(tk.END, "Bawal:\n", "bold")
                text_widget.insert(tk.END, "Bentuk tubuh: ", "bold")
                text_widget.insert(tk.END, "Pipih, memanjang, dan bisa mencapai panjang sekitar 40 cm.\n")
                text_widget.insert(tk.END, "Sirip: ", "bold")
                text_widget.insert(tk.END, "Memiliki sirip punggung dan dubur yang memiliki duri dan jari-jari.\n")
                text_widget.insert(tk.END, "Warna: ", "bold")
                text_widget.insert(tk.END, "Sisik: ", "bold")
                text_widget.insert(tk.END, "Berbentuk bulat, tipis, dan transparan, dengan lingkaran pada bagian belakangnya. .\n")
                text_widget.insert(tk.END, "Kepala: ", "bold")
                text_widget.insert(tk.END, "Berbentuk seperti kerucut.\n")
                text_widget.insert(tk.END, "Habitat: ", "bold")
                text_widget.insert(tk.END, "Air tawar.\n")
                text_widget.insert(tk.END, "Masa Panen: ", "bold")
                text_widget.insert(tk.END, "3-4 bulan dengan berat 30-45 gram per ekor.\n")
            
            else:
                text_widget.insert(tk.END, f"{ikan}:\n", "bold")
                text_widget.insert(tk.END, f"{info}\n")
            
            # tag bold & disable
            text_widget.tag_configure("bold", font=("Helvetica", self.font_sizes['bold'], "bold"))
            text_widget.config(state=tk.DISABLED)
            
            


        # Tombol kembali → masuk ke scrollable_frame agar sejajar konten
        self._create_styled_button(scrollable_frame, "Kembali", lambda: self.show_frame("start")).pack(pady=20)

        return frame


    def show_error(self, message):
        messagebox.showerror("Error", message)

    def show_hasil(self, jenis_ikan, jenis_pakan, jumlah_ikan, hasil):
        self.hasil_label.config(
            text=f"Kebutuhan harian: {hasil:.2f} kg {jenis_pakan} untuk {jumlah_ikan} ekor {jenis_ikan}"
        )

    def get_input_values(self):
        return {
            'jenis_ikan': self.jenis_ikan_combobox.get(),
            'jenis_pakan': self.jenis_pakan_combobox.get(),
            'jumlah_ikan': self.jumlah_ikan_entry.get()
        }

    def _on_resize(self, event):
        # Calculate scaling factor based on window size
        width_scale = event.width / 700
        height_scale = event.height / 550
        scale_factor = min(width_scale, height_scale)
        
        # Update font sizes
        self.font_sizes = {
            'title': max(14, int(16 * scale_factor)),
            'subtitle': max(12, int(14 * scale_factor)),
            'normal': max(8, int(10 * scale_factor)),
            'bold': max(8, int(10 * scale_factor))
        }
        
        # Update fonts for all widgets
        self._update_font_sizes()

    def _update_font_sizes(self):
        # Update fonts for all frames
        if hasattr(self, 'title_label'):
            self.title_label.config(font=("Helvetica", self.font_sizes['title'], "bold"))
        
        if hasattr(self, 'label_kalkulator'):
            self.label_kalkulator.config(font=("Helvetica", self.font_sizes['subtitle'], "bold"))
        
        if hasattr(self, 'hasil_label'):
            self.hasil_label.config(font=("Helvetica", self.font_sizes['normal'], "bold"))
        
        # Update text widgets
        for frame in self.frames.values():
            for widget in frame.winfo_children():
                if isinstance(widget, (tk.Label, tk.Button)):
                    current_font = widget.cget("font")
                    if "bold" in current_font.lower():
                        widget.config(font=("Helvetica", self.font_sizes['bold'], "bold"))
                    else:
                        widget.config(font=("Helvetica", self.font_sizes['normal']))
                elif isinstance(widget, (ttk.Combobox, ttk.Entry)):
                    widget.config(font=("Helvetica", self.font_sizes['normal']))

# Controller (unchanged)
class PakanController:
    def __init__(self):
        self.model = PakanModel()
        self.view = PakanView(self)
 
    def run(self):
        self.view.mainloop()

    def on_jenis_ikan_selected(self, event=None):
        jenis_ikan = self.view.jenis_ikan_combobox.get()
        rekomendasi = self.model.get_rekomendasi_pakan(jenis_ikan)
        self.view.jenis_pakan_combobox['values'] = rekomendasi

    def on_hitung(self):
        input_values = self.view.get_input_values()
        try:
            jenis_ikan = input_values['jenis_ikan']
            jenis_pakan = input_values['jenis_pakan']
            jumlah_ikan = int(input_values['jumlah_ikan'])

            if jumlah_ikan <= 0:
                raise ValueError("Jumlah ikan harus lebih dari 0")

            self.model.set_data(jenis_ikan, jenis_pakan, jumlah_ikan)

            if self.model.hitung_kebutuhan_pakan():
                self.view.show_hasil(jenis_ikan, jenis_pakan, jumlah_ikan, self.model.hasil_perhitungan)
            else:
                self.view.show_error("Kombinasi ikan dan pakan tidak tersedia.")
        except ValueError as e:
            self.view.show_error(f"Input tidak valid: {str(e)}")

# Main
if __name__ == "__main__":
    app = PakanController()
    app.run()