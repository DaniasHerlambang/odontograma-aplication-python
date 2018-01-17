from Tkinter import *
import MySQLdb
from tkMessageBox  import*
import tkMessageBox as pesan
import ttk
import Tkinter as tk
import sys
from PIL import Image
import base64
import cStringIO
import PIL.Image
from PIL import ImageTk, Image

#####****************************************** TK UNTUK LOADING ********************************************************************************
#####*** loading akan beraksi , dan akan menutup window setelah sekian detik .. lalu TK data utama akan otomatis dijalankan oleh python *********
### ##from winsound import *
##
##window = Tk()
##window.iconbitmap(default='./gambar/logo.ico')
##window.overrideredirect(True) #menghapus kulit window
##window.after(6000, window.destroy)
##s = ttk.Style() 
##s.theme_use('classic')
##s.configure("#DCE9F1.Horizontal.TProgressbar", foreground='#DCE9F1', background='#CA1126')
##pb_hd = ttk.Progressbar(window, style="#DCE9F1.Horizontal.TProgressbar" , orient = 'horizontal', mode='determinate')
##pb_hd.pack(expand = True, fill = BOTH, side = BOTTOM)
##pb_hd.start(2)
##lebar = 700
##tinggi = 300
### ************************* penggunaan fungsi winfo_screenwidth()
##setTengahX = (window.winfo_screenwidth() - lebar)//2
### ************************* penggunaan fungsi winfo_screenheight()
##setTengahY = (window.winfo_screenheight() - tinggi)//2
##
##window.geometry("%ix%i+%i+%i" %(lebar, tinggi, setTengahX, setTengahY))
##s = ttk.Style()
##s.configure('TButton', relief=RIDGE, background ='#DCE9F1',fontground="#DCE9F1",foreground="maroon", fieldbackground="#DCE9F1")
##s.theme_use('clam')
##
##try:
## asd=PhotoImage(file = './gambar/loading.gif')
## canvas = Canvas(window, width = 700, height = 350, bg = '#F8CF7F')
## canvas.pack(side = TOP)
## x0 = 60
## y0 = 140
## x1 = 560
## y1 = 300
## i = 0
## deltax = 2
## deltay = 3
## which = canvas.create_image(350,142, image = asd, tag='#DCE9F1Ball')
##
## canvas.create_text(180,230, text = 'ondotogram', font = ('Papyrus', 35), fill = '#CA1126')
## canvas.create_text(80,130, text = 'APLIKASI', font = ('Papyrus', 14), fill = '#CA1126')
##
##except:
## pass
##
##window.mainloop()


#______________________________________________________________________________________________________________________________________________________________________
#______________________________________________________________________________________________________________________________________________________________________


class Data(Frame):
    
    def __init__(self,parent):
        Frame.__init__(self, parent)
        self.induk = parent
        self.induk.iconbitmap(default='./gambar/logo.ico')
##        self.induk.resizable(False, False)
        self.initUI()
##        self.trvTabel_c.bind("<<TreeviewSelect>>", self.tampil_data_lama_ke_rekam)
##        self.box_kelamin.bind("<<ComboboxSelected>>", self.pilihan_kelamin)
##        self.box_ttl_tanggal.bind("<<ComboboxSelected>>", self.pilihan_ttl_tanggal)
##        self.box_ttl_bulan.bind("<<ComboboxSelected>>", self.pilihan_ttl_bulan)
##        self.box_ttl_tahun.bind("<<ComboboxSelected>>", self.pilihan_ttl_tahun)
##
    def initUI(self):
        #D2D7FD
        #EAEBFF
        self.induk.title("APLIKASI ONDOTOGRAM")
        # atur ukuran window
        # menempatkan window di tengah layar PC/Laptop
        lebar =900
        tinggi = 650
 
        # ************************* penggunaan fungsi winfo_screenwidth()
        setTengahX = (self.induk.winfo_screenwidth()-lebar)//2
        # ************************* penggunaan fungsi winfo_screenheight()
        setTengahY = (self.induk.winfo_screenheight()-tinggi)//2
 
        self.induk.geometry("%ix%i+%i+%i" %(lebar, tinggi, setTengahX, setTengahY))
        # **************************************************************** 
        
        mainFrame = Frame(self.induk,bg='#DCE9F1' )
        mainFrame.pack(fill=BOTH, expand=YES)
        self.main = mainFrame
        
        photobg = PhotoImage(file = "./gambar/bg_cc.gif")
        self.x = Label (self.main, image = photobg, fg = 'white', bg = '#DCE9F1')
        self.x.photo = photobg
        self.x.pack(side = 'top', fill = 'both', expand = 'yes')


##        fm = tk.Frame(self.x, width=200, height=200, background="#DCE9F1")
        f1 = tk.Frame(self.x, width=100, height=100, background="black")
        f2 = tk.Frame(self.x, width=100, height=100, background="#DCE9F1")
        f3 = tk.Frame(self.x, width=100, height=100, background="#DCE9F1")
        f4 = tk.Frame(self.x, width=100, height=100, background="#DCE9F1")
##        fm.pack(fill="both", expand=True, padx=150, pady=150)
        f1.place(in_=self.x, anchor="nw", relx=.6, rely=.6)
        f2.place(in_=self.x, anchor="ne", relx=.5, rely=.5)
        f3.place(in_=self.x, anchor="sw", relx=.5, rely=.5)
        f4.place(in_=self.x, anchor="se", relx=.4, rely=.4)

        photo1 = PhotoImage(file = "./gambar/cari.gif")
        self.Tombol_cari = ttk.Button (f4 , style='Kim.TButton'
                                       ,compound="top", text='CARI DATA PASIEN',command=self.Pencarian, image = photo1)
        self.Tombol_cari.photo = photo1
        self.Tombol_cari.photo = photo1
        self.Tombol_cari.pack( side=LEFT)

        photo2 = PhotoImage(file = "./gambar/rekam.gif")
        self.Tombol_rekam_medis = ttk.Button (f3 , image = photo2,compound="top", text='REKAM MEDIS', command=self.rekam_medis)
        self.Tombol_rekam_medis.photo = photo2
        self.Tombol_rekam_medis.pack( side=LEFT)

        photo3 = PhotoImage(file = "./gambar/master_obat.gif")
        self.Tombol_master_obat = ttk.Button (f2 , style='Kim.TButton',compound="top", text='MASTER OBAT',command=self.Pencarian, image = photo3)
        self.Tombol_master_obat.photo = photo3
        self.Tombol_master_obat.pack( side=LEFT)

        photo4 = PhotoImage(file = "./gambar/data_pasien.gif")
        self.Tombol_data_pasien = ttk.Button (f1 , image = photo4,compound="top", text='DATA PASIEN', command=self.rekam_medis)
        self.Tombol_data_pasien.photo = photo4
        self.Tombol_data_pasien.pack( side=LEFT)
        
        s = ttk.Style()
        s.theme_use('clam')
        s.configure('TButton', foreground='maroon')
        
        
    def rekam_medis(self):
        self.rekam_medis_window = Toplevel(self)
        self.rekam_medis_window.wm_title('Rekam Medis')
        # atur ukuran window
        # menempatkan window di tengah layar PC/Laptop
        lebar =1400
        tinggi = 800
 
        # ************************* penggunaan fungsi winfo_screenwidth()
        setTengahX = (self.rekam_medis_window.winfo_screenwidth()-lebar)//3
        # ************************* penggunaan fungsi winfo_screenheight()
        setTengahY = (self.rekam_medis_window.winfo_screenheight()-tinggi)//4
 
        self.rekam_medis_window.geometry("%ix%i+%i+%i" %(lebar, tinggi, setTengahX, setTengahY))
        # **************************************************************** 
        self.induk.withdraw()
        
        photorekam = PhotoImage(file = "./gambar/bg_rekam.gif")
        mainFrame = Label(self.rekam_medis_window , image = photorekam  ,bg='#DCE9F1' )
        mainFrame.photo = photorekam
        mainFrame.pack(fill=BOTH, expand=YES)
        self.pusat_rekam = mainFrame

        photorekam = PhotoImage(file = "./gambar/bg_rekam.gif")
        kiri = Label(self.pusat_rekam  ,bg='#DCE9F1' ,image=photorekam)
        kiri.photo = photorekam
        kiri.pack( side= LEFT, expand=YES)
        self.main_rekam = kiri

        # ********************* INPUT **********************************************
        self.L_F_atas = LabelFrame (self.main_rekam , bg ='#DCE9F1' ,text=' '*100+'DATA PASIEN', relief = FLAT , bd=3)
        self.L_F_atas.pack(side=TOP)
        
        self.F_atas = Frame (self.L_F_atas , bg ='#DCE9F1' , relief = FLAT , bd=3)
        self.F_atas.pack(fill=BOTH,side=TOP)
        self.F_atas_kiri = Frame (self.F_atas , bg ='#DCE9F1' , relief = RIDGE , bd=3)
        self.F_atas_kiri.pack(fill=BOTH,side=LEFT)

        #________nama____________
        self.F_nama = Frame (self.F_atas_kiri , bg ='#D2D7FD' , relief = FLAT , bd=3)
        self.F_nama.pack(fill=BOTH,side=TOP)
        self.Label_nama = Label (self.F_nama , text='Nama'+' '*38+':', bg ='#D2D7FD')#DCE9F1
        self.Label_nama.pack( side=LEFT)
        self.Entry_nama = Entry (self.F_nama , width=75, relief = GROOVE , bd=2)
        self.Entry_nama.pack(fill=BOTH, side=LEFT)

        #________kelamin____________
        self.F_kelamin = Frame (self.F_atas_kiri , bg ='#DCE9F1' , relief = FLAT , bd=3)
        self.F_kelamin.pack(fill=BOTH,side=TOP)
        self.Label_kelamin = Label (self.F_kelamin , text='Kelamin'+' '*34+':', bg ='#DCE9F1')
        self.Label_kelamin.pack( side=LEFT)
        
        self.kelamin_value = StringVar()
        self.box_kelamin = ttk.Combobox(self.F_kelamin, textvariable=self.kelamin_value)
        self.box_kelamin['values'] = ('LAKI-LAKI', 'PEREMPUAN')
        self.box_kelamin.pack(side=LEFT)

        #________Tempat_Tanggal_Lahir____________
        self.F_ttl = Frame (self.F_atas_kiri , bg ='#D2D7FD', relief = FLAT , bd=3)
        self.F_ttl.pack(fill=BOTH,side=TOP)
        self.Label_ttl = Label (self.F_ttl , text='Tempat,Tanggal Lahir'+' '*10+':', bg ='#D2D7FD')
        self.Label_ttl.pack( side=LEFT)

        self.Entry_ttl = Entry (self.F_ttl , width=30, relief = GROOVE , bd=2)
        self.Entry_ttl.pack(side=LEFT)
        
        self.ttl_tanggal_value = IntVar()
        self.box_ttl_tanggal = ttk.Combobox(self.F_ttl, textvariable=self.ttl_tanggal_value ,width=5)
        self.box_ttl_tanggal['values'] = ( range(1,32))
        self.box_ttl_tanggal.pack(side=LEFT,padx=3)

        self.ttl_bulan_value = StringVar()
        self.box_ttl_bulan = ttk.Combobox(self.F_ttl, textvariable=self.ttl_bulan_value ,width=13)
        self.box_ttl_bulan['values'] = ('JANUARI', 'FEBUARI' , 'MARET' ,'APRIL', 'MEI', 'JUNI', 'JULI', 'AGUSTUS', 'SEPTEMBER', 'OKTOBER', 'NOVEMBER',
                                        'DESEMBER')
        self.box_ttl_bulan.pack(side=LEFT,padx=3)

        self.ttl_tahun_value = IntVar()
        self.box_ttl_tahun = ttk.Combobox(self.F_ttl, textvariable=self.ttl_tahun_value ,width=5)
        self.box_ttl_tahun['values'] = ( range(1901,2018))
        self.box_ttl_tahun.pack(side=LEFT,padx=3)

        #________Alamat____________
        self.F_alamat = Frame (self.F_atas_kiri , bg ='#DCE9F1',relief = FLAT , bd=3)
        self.F_alamat.pack(fill=BOTH,side=TOP)

        self.Label_alamat = Label (self.F_alamat , text='Alamat'+' '*36+':', bg ='#DCE9F1')
        self.Label_alamat.pack( side=LEFT)

        self.Entry_alamat = Entry (self.F_alamat , width=30, relief = GROOVE , bd=2)
        self.Entry_alamat.pack(side=LEFT)

        #________Pekerjaan____________
        self.F_pekerjaan = Frame (self.F_atas_kiri , bg ='#D2D7FD', relief = FLAT , bd=3)
        self.F_pekerjaan.pack(fill=BOTH,side=TOP)

        self.Label_pekerjaan = Label (self.F_pekerjaan , text='Pekerjaan'+' '*32+':', bg ='#D2D7FD')
        self.Label_pekerjaan.pack( side=LEFT)

        self.Entry_pekerjaan = Entry (self.F_pekerjaan , width=30, relief = GROOVE , bd=2)
        self.Entry_pekerjaan.pack(side=LEFT)


        # ********************* MEDIK ONDO  **********************************************
        # ********************* MEDIK   **********************************************
        self.F_tengah = Frame (self.main_rekam , bg ='#DCE9F1' , relief = FLAT , bd=3)
        self.F_tengah.pack(fill=BOTH,side=TOP)
        
        self.F_tengah_x = Frame (self.F_tengah , bg ='#DCE9F1' , relief = FLAT , bd=3)
        self.F_tengah_x.pack(fill=BOTH,side=TOP)
        
        self.L_F_tengah_kiri = LabelFrame (self.F_tengah_x  ,text=' '*26+'DATA MEDIK YANG DIPERLUKAN' , bg ='#DCE9F1' , relief = FLAT , bd=3)
        self.L_F_tengah_kiri.pack(fill=BOTH,side=LEFT)
        self.F_tengah_kiri = Frame (self.L_F_tengah_kiri , bg ='#DCE9F1' , relief = RIDGE , bd=3)
        self.F_tengah_kiri.pack(fill=BOTH,side=LEFT)

        self.L_F_tengah_kanan = LabelFrame (self.F_tengah_x  ,text=' '*28+'DATA ONDOTOGRAM' , bg ='#DCE9F1' , relief = FLAT , bd=3)
        self.L_F_tengah_kanan.pack(fill=BOTH,side=LEFT)
        self.F_tengah_kanan = Frame (self.L_F_tengah_kanan , bg ='#D2D7FD' , relief = RIDGE , bd=3)
        self.F_tengah_kanan.pack(fill=BOTH,side=LEFT)

        self.F_tengah_xx = Frame (self.F_tengah , bg ='#DCE9F1' , relief = FLAT , bd=3)
        self.F_tengah_xx.pack(fill=BOTH,side=TOP)
        #________Tombol_Oke_Cancel_identitas____________

        self.F_tombol_home = Frame (self.F_tengah_xx , bg ='#DCE9F1', relief = FLAT , bd=3)
        self.F_tombol_home.pack(fill=BOTH,side=LEFT)
        
        self.F_tombol_oke_cancel_identitas = Frame (self.F_tengah_xx , bg ='#DCE9F1', relief = FLAT , bd=3)
        self.F_tombol_oke_cancel_identitas.pack(fill=BOTH,side=LEFT)
        
        self.gmbrhome = PhotoImage(file='./gambar/Home.gif')
        self.Tombol_cari = ttk.Button (self.F_tombol_home ,text="HOME",command=self.kembali, image=self.gmbrhome, compound="top")
        self.Tombol_cari.pack( side=LEFT)

        self.gmbr1 = PhotoImage(file='./gambar/cancel.gif')
        self.Tombol_tombol_cancel = ttk.Button (self.F_tombol_oke_cancel_identitas,compound='top',image= self.gmbr1,
                                         text='CANCEL' ,command=self.input_identitas_kosongan)
        self.Tombol_tombol_cancel.pack( side=LEFT,padx=8)

        self.ru = PhotoImage(file='./gambar/tambah_c.gif')
        self.Tombol_tombol_tambah = ttk.Button (self.F_tombol_oke_cancel_identitas ,compound='top',image= self.ru,
                                         text='BARU',command=self.baru_data)
        self.Tombol_tombol_tambah.pack( side=LEFT,pady=8,padx=9)

        self.gmbr2 = PhotoImage(file='./gambar/+.gif')
        self.Tombol_tombol_odontogram = ttk.Button (self.F_tombol_oke_cancel_identitas,compound='top',image= self.gmbr2,
                                         text='ODONTOGRAM' ,command=self.tampil_data_ke_odontogram)
        self.Tombol_tombol_odontogram.pack( side=LEFT,pady=8)
        
        s = ttk.Style()
        s.configure('TButton', relief=RIDGE, background ='#DCE9F1',fontground="#DCE9F1",foreground="maroon", fieldbackground="#DCE9F1")
        s.theme_use('clam')
        
        #________golongan_darah____________
        self.F_golongan_darah = Frame (self.F_tengah_kiri , bg ='#D2D7FD' , relief = FLAT , bd=3)
        self.F_golongan_darah.pack(fill=BOTH,side=TOP)
        self.Label_golongan_darah = Label (self.F_golongan_darah , text='Golongan Darah'+' '*25+':', bg ='#D2D7FD')
        self.Label_golongan_darah.pack( side=LEFT)
        
        self.golongan_darah_value = StringVar()
        self.box_golongan_darah = ttk.Combobox(self.F_golongan_darah, textvariable=self.golongan_darah_value)
        self.box_golongan_darah['values'] = ('A', 'B','AB', 'O')
        self.box_golongan_darah.pack(side=LEFT,pady=5)

        #________tekanan_darah_normal____________
        self.F_tekanan_darah_normal = Frame (self.F_tengah_kiri , bg ='#DCE9F1' , relief = FLAT , bd=3)
        self.F_tekanan_darah_normal.pack(fill=BOTH,side=TOP)
        self.Label_tekanan_darah_normal = Label (self.F_tekanan_darah_normal , text='Tekanan Darah Normal'+' '*13+':', bg ='#DCE9F1')
        self.Label_tekanan_darah_normal.pack( side=LEFT)
        
        self.tekanan_darah_normal_value = StringVar()
        self.box_tekanan_darah_normal = ttk.Combobox(self.F_tekanan_darah_normal, textvariable=self.tekanan_darah_normal_value)
        self.box_tekanan_darah_normal['values'] = ('Hypertensi', 'Hypotensi','Normal')
        self.box_tekanan_darah_normal.pack(side=LEFT,pady=5)

        #________penyakit_jantung____________
        self.F_penyakit_jantung = Frame (self.F_tengah_kiri , bg ='#D2D7FD' , relief = FLAT , bd=3)
        self.F_penyakit_jantung.pack(fill=BOTH,side=TOP)
        self.Label_penyakit_jantung = Label (self.F_penyakit_jantung , text='Penyakit Jantung'+' '*24+':', bg ='#D2D7FD')
        self.Label_penyakit_jantung.pack( side=LEFT)
        
        self.penyakit_jantung_value = StringVar()
        self.box_penyakit_jantung = ttk.Combobox(self.F_penyakit_jantung, textvariable=self.penyakit_jantung_value)
        self.box_penyakit_jantung['values'] = ('Tidak Ada', 'Ada')
        self.box_penyakit_jantung.pack(side=LEFT,pady=5)

        #________diabetes____________
        self.F_diabetes = Frame (self.F_tengah_kiri , bg ='#DCE9F1' , relief = FLAT , bd=3)
        self.F_diabetes.pack(fill=BOTH,side=TOP)
        self.Label_diabetes = Label (self.F_diabetes , text='Diabetes'+' '*39+':', bg ='#DCE9F1')
        self.Label_diabetes.pack( side=LEFT)
        
        self.diabetes_value = StringVar()
        self.box_diabetes = ttk.Combobox(self.F_diabetes, textvariable=self.diabetes_value)
        self.box_diabetes['values'] = ('Tidak Ada', 'Ada')
        self.box_diabetes.pack(side=LEFT,pady=5)

        #________haemophilia____________
        self.F_haemophilia = Frame (self.F_tengah_kiri , bg ='#D2D7FD' , relief = FLAT , bd=3)
        self.F_haemophilia.pack(fill=BOTH,side=TOP)
        self.Label_haemophilia = Label (self.F_haemophilia , text='Haemophilia'+' '*31+':', bg ='#D2D7FD')
        self.Label_haemophilia.pack( side=LEFT)
        
        self.haemophilia_value = StringVar()
        self.box_haemophilia = ttk.Combobox(self.F_haemophilia, textvariable=self.haemophilia_value)
        self.box_haemophilia['values'] = ('Tidak Ada', 'Ada')
        self.box_haemophilia.pack(side=LEFT,pady=5)

        #________hepatitis____________
        self.F_hepatitis = Frame (self.F_tengah_kiri , bg ='#DCE9F1' , relief = FLAT , bd=3)
        self.F_hepatitis.pack(fill=BOTH,side=TOP)
        self.Label_hepatitis = Label (self.F_hepatitis , text='Hepatitis'+' '*38+':', bg ='#DCE9F1')
        self.Label_hepatitis.pack( side=LEFT)
        
        self.hepatitis_value = StringVar()
        self.box_hepatitis = ttk.Combobox(self.F_hepatitis, textvariable=self.hepatitis_value)
        self.box_hepatitis['values'] = ('Tidak Ada', 'Ada')
        self.box_hepatitis.pack(side=LEFT,pady=5)

        #________penyakit_lainya____________
        self.F_penyakit_lainya = Frame (self.F_tengah_kiri , bg ='#D2D7FD' , relief = FLAT , bd=3)
        self.F_penyakit_lainya.pack(fill=BOTH,side=TOP)
        self.Label_penyakit_lainya = Label (self.F_penyakit_lainya , text='Penyakit Lainya'+' '*26+':', bg ='#D2D7FD')
        self.Label_penyakit_lainya.pack( side=LEFT)
        
        self.penyakit_lainya_value = StringVar()
        self.box_penyakit_lainya = ttk.Combobox(self.F_penyakit_lainya, textvariable=self.penyakit_lainya_value)
        self.box_penyakit_lainya['values'] = ('Tidak Ada', 'Ada')
        self.box_penyakit_lainya.pack(side=LEFT,pady=5)

        #________alergi_thd_obat_obatan____________
        self.F_alergi_thd_obat_obatan = Frame (self.F_tengah_kiri , bg ='#DCE9F1' , relief = FLAT , bd=3)
        self.F_alergi_thd_obat_obatan.pack(fill=BOTH,side=TOP)
        self.Label_alergi_thd_obat_obatan = Label (self.F_alergi_thd_obat_obatan , text='Alergi terhadap obat-obatan'+' '*3+':', bg ='#DCE9F1')
        self.Label_alergi_thd_obat_obatan.pack( side=LEFT)
        
        self.alergi_thd_obat_obatan_value = StringVar()
        self.box_alergi_thd_obat_obatan = ttk.Combobox(self.F_alergi_thd_obat_obatan, textvariable=self.alergi_thd_obat_obatan_value)
        self.box_alergi_thd_obat_obatan['values'] = ('Tidak Ada', 'Ada')
        self.box_alergi_thd_obat_obatan.pack(side=LEFT,pady=5)


         #________alergi_thd_makanan____________
        self.F_alergi_thd_makanan = Frame (self.F_tengah_kiri , bg ='#D2D7FD' , relief = FLAT , bd=3)
        self.F_alergi_thd_makanan.pack(fill=BOTH,side=TOP)
        self.Label_alergi_thd_makanan = Label (self.F_alergi_thd_makanan , text='Alergi terhadap makanan'+' '*9+':', bg ='#D2D7FD')
        self.Label_alergi_thd_makanan.pack( side=LEFT)
        
        self.alergi_thd_makanan_value = StringVar()
        self.box_alergi_thd_makanan = ttk.Combobox(self.F_alergi_thd_makanan, textvariable=self.alergi_thd_makanan_value)
        self.box_alergi_thd_makanan['values'] = ('Tidak Ada', 'Ada')
        self.box_alergi_thd_makanan.pack(side=LEFT,pady=5)

        
        # ********************* MEDIK ONDO  **********************************************
        # *********************  ONDO  **********************************************
        #________occulusi____________
        self.F_occulusi = Frame (self.F_tengah_kanan , bg ='#D2D7FD' , relief = FLAT , bd=3)
        self.F_occulusi.pack(fill=BOTH,side=TOP)
        self.Label_occulusi = Label (self.F_occulusi , text='Occulusi'+' '*27+':', bg ='#D2D7FD')
        self.Label_occulusi.pack( side=LEFT)
        
        self.occulusi_value = StringVar()
        self.box_occulusi = ttk.Combobox(self.F_occulusi, textvariable=self.occulusi_value)
        self.box_occulusi['values'] = ('Normal Bite', 'Cross Bite','Strike Bite')
        self.box_occulusi.pack(side=LEFT,pady=5)

        #________torus_palantinus____________
        self.F_torus_palantinus = Frame (self.F_tengah_kanan , bg ='#EAEBFF' , relief = FLAT , bd=3)
        self.F_torus_palantinus.pack(fill=BOTH,side=TOP)
        self.Label_torus_palantinus = Label (self.F_torus_palantinus , text='Torus Palantinus'+' '*13+':', bg ='#EAEBFF')
        self.Label_torus_palantinus.pack( side=LEFT)
        
        self.torus_palantinus_value = StringVar()
        self.box_torus_palantinus = ttk.Combobox(self.F_torus_palantinus, textvariable=self.torus_palantinus_value)
        self.box_torus_palantinus['values'] = ('Tidak Ada', 'Kecil','Sedang', 'Besar','Multiple')
        self.box_torus_palantinus.pack(side=LEFT,pady=5)
        
        #________torus_mandibularis____________
        self.F_torus_mandibularis = Frame (self.F_tengah_kanan , bg ='#D2D7FD' , relief = FLAT , bd=3)
        self.F_torus_mandibularis.pack(fill=BOTH,side=TOP)
        self.Label_torus_mandibularis = Label (self.F_torus_mandibularis , text='Torus Mandibularis'+' '*8+':', bg ='#D2D7FD')
        self.Label_torus_mandibularis.pack( side=LEFT)
        
        self.torus_mandibularis_value = StringVar()
        self.box_torus_mandibularis = ttk.Combobox(self.F_torus_mandibularis, textvariable=self.torus_mandibularis_value)
        self.box_torus_mandibularis['values'] = ('Tidak Ada', 'Sisi Kiri', 'Sisi Kanan', 'Kedua Sisi')
        self.box_torus_mandibularis.pack(side=LEFT,pady=5)

        #________palatum____________
        self.F_palatum = Frame (self.F_tengah_kanan , bg ='#EAEBFF' , relief = FLAT , bd=3)
        self.F_palatum.pack(fill=BOTH,side=TOP)
        self.Label_palatum = Label (self.F_palatum , text='Palatum'+' '*27+':', bg ='#EAEBFF')
        self.Label_palatum.pack( side=LEFT)
        
        self.palatum_value = StringVar()
        self.box_palatum = ttk.Combobox(self.F_palatum, textvariable=self.palatum_value)
        self.box_palatum['values'] = ('Dalam', 'Sedang', 'Rendah')
        self.box_palatum.pack(side=LEFT,pady=5)

        #________supernumerary_teeth____________
        self.F_supernumerary_teeth = Frame (self.F_tengah_kanan , bg ='#D2D7FD' , relief = FLAT , bd=3)
        self.F_supernumerary_teeth.pack(fill=BOTH,side=TOP)
        self.Label_supernumerary_teeth = Label (self.F_supernumerary_teeth , text='Supernumerary Teeth'+' '*4+':', bg ='#D2D7FD')
        self.Label_supernumerary_teeth.pack( side=LEFT) 
        
        self.supernumerary_teeth_value = StringVar()
        self.box_supernumerary_teeth = ttk.Combobox(self.F_supernumerary_teeth, textvariable=self.supernumerary_teeth_value)
        self.box_supernumerary_teeth['values'] = ('Tidak Ada', 'Ada')
        self.box_supernumerary_teeth.pack(side=LEFT,pady=5)

        #________diasterna____________
        self.F_diasterna = Frame (self.F_tengah_kanan , bg ='#EAEBFF' , relief = FLAT , bd=3)
        self.F_diasterna.pack(fill=BOTH,side=TOP)
        self.Label_diasterna = Label (self.F_diasterna , text='Diasterna'+' '*25+':', bg ='#EAEBFF')
        self.Label_diasterna.pack( side=LEFT)
        
        self.diasterna_value = StringVar()
        self.box_diasterna = ttk.Combobox(self.F_diasterna, textvariable=self.diasterna_value)
        self.box_diasterna['values'] = ('Tidak Ada', 'Ada')
        self.box_diasterna.pack(side=LEFT,pady=5)

        #________gigi_anomali____________
        self.F_gigi_anomali = Frame (self.F_tengah_kanan , bg ='#D2D7FD' , relief = FLAT , bd=3)
        self.F_gigi_anomali.pack(fill=BOTH,side=TOP)
        self.Label_gigi_anomali = Label (self.F_gigi_anomali , text='Gigi Anomaly'+' '*18+':', bg ='#D2D7FD')
        self.Label_gigi_anomali.pack( side=LEFT)
        
        self.gigi_anomali_value = StringVar()
        self.box_gigi_anomali = ttk.Combobox(self.F_gigi_anomali, textvariable=self.gigi_anomali_value)
        self.box_gigi_anomali['values'] = ('Tidak Ada', 'Ada')
        self.box_gigi_anomali.pack(side=LEFT,pady=5)
        
        #________lain_lain____________
        self.F_lain_lain = Frame (self.F_tengah_kanan , bg ='#EAEBFF' , relief = FLAT , bd=3)
        self.F_lain_lain.pack(fill=BOTH,side=TOP)
        self.Label_lain_lain = Label (self.F_lain_lain , text='Lain-Lain'+' '*25+':', bg ='#EAEBFF')
        self.Label_lain_lain.pack( side=LEFT)
        
        self.lain_lain_value = StringVar()
        self.box_lain_lain = ttk.Combobox(self.F_lain_lain, textvariable=self.lain_lain_value)
        self.box_lain_lain['values'] = ('Tidak Ada', 'Ada')
        self.box_lain_lain.pack(side=LEFT,pady=5)

        ##___________ODONTOGRAM_______________##___________ODONTOGRAM_______________##___________ODONTOGRAM_______________##___________ODONTOGRAM_______________
        ##___________ODONTOGRAM_______________##___________ODONTOGRAM_______________##___________ODONTOGRAM_______________##___________ODONTOGRAM_______________
        ##___________ODONTOGRAM_______________##___________ODONTOGRAM_______________##___________ODONTOGRAM_______________##___________ODONTOGRAM_______________

    def odontogram(self):
        self.odontogram_window = Toplevel(self)
        self.odontogram_window.wm_title('ODONTOGRAM')
        # atur ukuran window
        # menempatkan window di tengah layar PC/Laptop
        lebar =1400
        tinggi = 800
 
        # ************************* penggunaan fungsi winfo_screenwidth()
        setTengahX = (self.odontogram_window.winfo_screenwidth()-lebar)//3
        # ************************* penggunaan fungsi winfo_screenheight()
        setTengahY = (self.odontogram_window.winfo_screenheight()-tinggi)//4
 
        self.odontogram_window.geometry("%ix%i+%i+%i" %(lebar, tinggi, setTengahX, setTengahY))
        # **************************************************************** 
        self.induk.withdraw()

        #***********MENU BAR****************************************
        self.menubar = Menu(self.odontogram_window)
        self.odontogram_window.config(menu = self.menubar)
        
        self.home = PhotoImage(file='./gambar/home.gif')
        self.gambar_RM = PhotoImage(file='./gambar/plus.gif')
        self.garis = PhotoImage(file='./gambar/garis.gif')
        
        fileMenu = Menu(self.menubar, tearoff=0)
        fileMenu.add_separator()
        self.menubar.add_cascade(label = 'KEMBALI',menu = fileMenu)
        fileMenu.add_command( image=self.garis)
        fileMenu.add_command( label = 'HOME',image=self.home, compound='left',command=self.odontogram_ke_home)
        fileMenu.add_command( image=self.garis)
        fileMenu.add_command( label = 'REKAM MEDIS',image=self.gambar_RM, compound='left', command=self.odontogram_ke_rekam_medis)
        fileMenu.add_command( image=self.garis)
        fileMenu.add_separator()

        self.data = PhotoImage(file='./gambar/data.gif')
        
        fileMenu = Menu(self.menubar, tearoff=0)
        fileMenu.add_separator()
        self.menubar.add_cascade(label = 'CETAK',menu = fileMenu)
        fileMenu.add_command( image=self.garis)
        fileMenu.add_command( label = 'SURAT RUJUKAN',image=self.data, compound='left',command=self.cetak_gambar)
        fileMenu.add_command( image=self.garis)
        fileMenu.add_command( label = 'SURAT KETERANGAN SAKIT',image=self.data, compound='left')
        fileMenu.add_command( image=self.garis)
        fileMenu.add_separator()
        
        #***********************************************************
        
        photorekam = PhotoImage(file = "./gambar/bg_rekam.gif")
        mainFrame = Label(self.odontogram_window , image = photorekam  ,bg='#78C9E4' )
        mainFrame.photo = photorekam
        mainFrame.pack(fill=BOTH, expand=YES)
        self.pusat_odontogram = mainFrame

        self.pusat_odontogram = Label(self.pusat_odontogram  ,bg='#78C9E4' )
        self.pusat_odontogram.pack( side= LEFT,fill=BOTH)

        photorekam = PhotoImage(file = "./gambar/bg_rekamm.gif")
        self.pusat_odontogram2= Label(mainFrame  ,bg='#78C9E4' , image = photorekam )
        self.pusat_odontogram2.photo = photorekam
        self.pusat_odontogram2.pack(  fill=BOTH,side= RIGHT)

        atas = Label(self.pusat_odontogram  ,bg='#DCE9F1' )
        atas.pack( side= TOP,pady=10)

        atas1 = Label(atas  ,bg='#78C9E4' )
        atas1.pack( fill=BOTH,side= LEFT)

        atas2 = Label(atas  ,bg='#78C9E4' )
        atas2.pack( fill=BOTH,side= LEFT)

        #________nama_odontogram____________
        self.F_nama_odontogram = Frame (atas1 , bg ='#78C9E4' , relief = FLAT , bd=3)
        self.F_nama_odontogram.pack(fill=BOTH,side=TOP)
        self.Label_nama_odontogram = Label (self.F_nama_odontogram , text='Nama'+' '*30+':', bg ='#78C9E4')#DCE9F1
        self.Label_nama_odontogram.pack( side=LEFT)
        self.Entry_nama_odontogram = Entry (self.F_nama_odontogram , width=66, relief = GROOVE , bd=2)
        self.Entry_nama_odontogram.pack( side=LEFT)

        #________kelamin_odontogram____________
        self.F_kelamin_odontogram = Frame (atas2 , bg ='#78C9E4' , relief = FLAT , bd=3)
        self.F_kelamin_odontogram.pack(fill=BOTH,side=TOP)
        self.Label_kelamin_odontogram = Label (self.F_kelamin_odontogram , text='Kelamin'+' '*5+':', bg ='#78C9E4')
        self.Label_kelamin_odontogram.pack( side=LEFT)
        
        self.kelamin_odontogram_value = StringVar()
        self.box_kelamin_odontogram = ttk.Combobox(self.F_kelamin_odontogram, textvariable=self.kelamin_odontogram_value)
        self.box_kelamin_odontogram['values'] = ('LAKI-LAKI', 'PEREMPUAN')
        self.box_kelamin_odontogram.pack(side=LEFT)
        
        #________Alamat__odontogram___________
        self.F_alamat_odontogram = Frame (atas2 , bg ='#78C9E4',relief = FLAT , bd=3)
        self.F_alamat_odontogram.pack(fill=BOTH,side=TOP)

        self.Label_alamat_odontogram = Label (self.F_alamat_odontogram , text='Alamat'+' '*6+':', bg ='#78C9E4')
        self.Label_alamat_odontogram.pack( side=LEFT)

        self.Entry_alamat_odontogram = Entry (self.F_alamat_odontogram , width=23, relief = GROOVE , bd=2)
        self.Entry_alamat_odontogram.pack(side=LEFT)


        #________Tempat_Tanggal_Lahir__odontogram___________
        self.F_ttl_odontogram = Frame (atas1 , bg ='#78C9E4', relief = FLAT , bd=3)
        self.F_ttl_odontogram.pack(fill=BOTH,side=TOP)
        self.Label_ttl_odontogram = Label (self.F_ttl_odontogram , text='Tempat,Tanggal Lahir'+' '*2+':', bg ='#78C9E4')
        self.Label_ttl_odontogram.pack( side=LEFT)

        self.Entry_ttl_odontogram = Entry (self.F_ttl_odontogram , width=30, relief = GROOVE , bd=2)
        self.Entry_ttl_odontogram.pack(side=LEFT)
        
        self.ttl_tanggal_odontogram_value = IntVar()
        self.box_ttl_tanggal_odontogram = ttk.Combobox(self.F_ttl_odontogram, textvariable=self.ttl_tanggal_odontogram_value ,width=5)
        self.box_ttl_tanggal_odontogram['values'] = ( range(1,32))
        self.box_ttl_tanggal_odontogram.pack(side=LEFT,padx=3)

        self.ttl_bulan_odontogram_value = StringVar()
        self.box_ttl_bulan_odontogram = ttk.Combobox(self.F_ttl_odontogram, textvariable=self.ttl_bulan_odontogram_value ,width=13)
        self.box_ttl_bulan_odontogram['values'] = ('JANUARI', 'FEBUARI' , 'MARET' ,'APRIL', 'MEI', 'JUNI', 'JULI', 'AGUSTUS', 'SEPTEMBER', 'OKTOBER', 'NOVEMBER',
                                        'DESEMBER')
        self.box_ttl_bulan_odontogram.pack(side=LEFT,padx=3)

        self.ttl_tahun_odontogram_value = IntVar()
        self.box_ttl_tahun_odontogram = ttk.Combobox(self.F_ttl_odontogram, textvariable=self.ttl_tahun_odontogram_value ,width=5)
        self.box_ttl_tahun_odontogram['values'] = ( range(1901,2018))
        self.box_ttl_tahun_odontogram.pack(side=LEFT,padx=3)

        
        # **************************************************************** 
        tengah = Frame(self.pusat_odontogram,bg='#78C9E4' )
        tengah.pack( side= TOP)

        tengah_atas = Frame(tengah,bg='#DCE9F1' )
        tengah_atas.pack(side= TOP)
        
        tengah_atas_kiri = Frame(tengah_atas,bg='#DCE9F1' ,relief=RIDGE,bd=4)
        tengah_atas_kiri.pack( side= LEFT)
        
        tengah_atas_kanan = Frame(tengah_atas,bg='#DCE9F1' ,relief=RIDGE,bd=4)
        tengah_atas_kanan.pack( side= LEFT)

        tengah_bawah = Frame(tengah,bg='#DCE9F1' )
        tengah_bawah.pack(side= TOP)
        
        tengah_bawah_kiri = Frame(tengah_bawah,bg='#DCE9F1' ,relief=RIDGE,bd=4)
        tengah_bawah_kiri.pack( side= LEFT)
        
        tengah_bawah_kanan = Frame(tengah_bawah,bg='#DCE9F1' ,relief=RIDGE,bd=4)
        tengah_bawah_kanan.pack( side= LEFT)

        tengah_atas2 = Frame(tengah,bg='#DCE9F1' )
        tengah_atas2.pack(side= TOP)
        
        tengah_atas2_kiri = Frame(tengah_atas2,bg='#DCE9F1' ,relief=RIDGE,bd=4)
        tengah_atas2_kiri.pack( side= LEFT)
        
        tengah_atas2_kanan = Frame(tengah_atas2,bg='#DCE9F1' ,relief=RIDGE,bd=4)
        tengah_atas2_kanan.pack( side= LEFT)

        tengah_bawah2 = Frame(tengah,bg='#DCE9F1' )
        tengah_bawah2.pack(side= TOP)
        
        tengah_bawah2_kiri = Frame(tengah_bawah2,bg='#DCE9F1' ,relief=RIDGE,bd=4)
        tengah_bawah2_kiri.pack( side= LEFT)
        
        tengah_bawah2_kanan = Frame(tengah_bawah2,bg='#DCE9F1' ,relief=RIDGE,bd=4)
        tengah_bawah2_kanan.pack( side= LEFT)
        
        #_________AAA_____________
        #_________a18_____________
        
        F_a18 = Frame(tengah_atas_kiri,bg='#DCE9F1' )
        F_a18.pack( side= LEFT)

        L_a18 = Label(F_a18  ,bg='#DCE9F1', text="18")
        L_a18.pack( side= TOP)
        
        photobg = PhotoImage(file = "./gambar/odon/gigi.gif")
        self.a18 = Button (F_a18, image = photobg, fg = 'white', bg = '#DCE9F1', command= self.ganti_gambar_a18)
        self.a18.photo = photobg
        self.a18.pack(side = 'top')
        
        #_________a17_____________
                
        F_a17 = Frame(tengah_atas_kiri,bg='#DCE9F1' )
        F_a17.pack(side= LEFT)

        L_a17 = Label(F_a17  ,bg='#DCE9F1', text="17")
        L_a17.pack( side= TOP)
        
        photobg = PhotoImage(file = "./gambar/odon/gigi.gif")
        self.a17 = Button (F_a17, image = photobg, fg = 'white', bg = '#DCE9F1', command= self.ganti_gambar_a17)
        self.a17.photo = photobg
        self.a17.pack(side = 'top')

        #_________a16_____________
                
        F_a16 = Frame(tengah_atas_kiri,bg='#DCE9F1')
        F_a16.pack( side= LEFT)

        L_a16 = Label(F_a16  ,bg='#DCE9F1', text="16")
        L_a16.pack( side= TOP)
        
        photobg = PhotoImage(file = "./gambar/odon/gigi.gif")
        self.a16 = Button (F_a16, image = photobg, fg = 'white', bg = '#DCE9F1', command= self.ganti_gambar_a16)
        self.a16.photo = photobg
        self.a16.pack(side = 'top')

        #_________a15_____________
                
        F_a15 = Frame(tengah_atas_kiri,bg='#DCE9F1')
        F_a15.pack(side= LEFT)

        L_a15 = Label(F_a15  ,bg='#DCE9F1', text="15")
        L_a15.pack( side= TOP)
        
        photobg = PhotoImage(file = "./gambar/odon/gigi.gif")
        self.a15 = Button (F_a15, image = photobg, fg = 'white', bg = '#DCE9F1', command= self.ganti_gambar_a15)
        self.a15.photo = photobg
        self.a15.pack(side = 'top')

        #_________a14_____________
                
        F_a14 = Frame(tengah_atas_kiri,bg='#DCE9F1' )
        F_a14.pack(side= LEFT)

        L_a14 = Label(F_a14  ,bg='#DCE9F1', text="14")
        L_a14.pack( side= TOP)
        
        photobg = PhotoImage(file = "./gambar/odon/gigi.gif")
        self.a14 = Button (F_a14, image = photobg, fg = 'white', bg = '#DCE9F1', command= self.ganti_gambar_a14)
        self.a14.photo = photobg
        self.a14.pack(side = 'top')

        #_________a13_____________
                
        F_a13 = Frame(tengah_atas_kiri,bg='#DCE9F1' )
        F_a13.pack(side= LEFT)

        L_a13 = Label(F_a13  ,bg='#DCE9F1', text="13")
        L_a13.pack( side= TOP)
        
        photobg = PhotoImage(file = "./gambar/odon/gigisusu.gif")
        self.a13 = Button (F_a13, image = photobg, fg = 'white', bg = '#DCE9F1', command= self.ganti_gambar_a13)
        self.a13.photo = photobg
        self.a13.pack(side = 'top')


        #_________a12_____________
                
        F_a12 = Frame(tengah_atas_kiri,bg='#DCE9F1' )
        F_a12.pack(side= LEFT)

        L_a12 = Label(F_a12  ,bg='#DCE9F1', text="12")
        L_a12.pack( side= TOP)
        
        photobg = PhotoImage(file = "./gambar/odon/gigisusu.gif")
        self.a12 = Button (F_a12, image = photobg, fg = 'white', bg = '#DCE9F1', command= self.ganti_gambar_a12)
        self.a12.photo = photobg
        self.a12.pack(side = 'top')


        #_________a11_____________
                
        F_a11 = Frame(tengah_atas_kiri,bg='#DCE9F1' )
        F_a11.pack(side= LEFT)

        L_a11 = Label(F_a11  ,bg='#DCE9F1', text="11")
        L_a11.pack( side= TOP)
        
        photobg = PhotoImage(file = "./gambar/odon/gigisusu.gif")
        self.a11 = Button (F_a11, image = photobg, fg = 'white', bg = '#DCE9F1', command= self.ganti_gambar_a11)
        self.a11.photo = photobg
        self.a11.pack(side = 'top')


        #_________BBB_____________
        #_________b21_____________
        
        F_b21 = Frame(tengah_atas_kanan,bg='#DCE9F1' )
        F_b21.pack( side= LEFT)

        L_b21 = Label(F_b21  ,bg='#DCE9F1', text="21")
        L_b21.pack( side= TOP)
        
        photobg = PhotoImage(file = "./gambar/odon/gigisusu.gif")
        self.b21 = Button (F_b21, image = photobg, fg = 'white', bg = '#DCE9F1', command= self.ganti_gambar_b21)
        self.b21.photo = photobg
        self.b21.pack(side = 'top')

        #_________b22_____________
        
        F_b22 = Frame(tengah_atas_kanan,bg='#DCE9F1' )
        F_b22.pack( side= LEFT)

        L_b22 = Label(F_b22  ,bg='#DCE9F1', text="22")
        L_b22.pack( side= TOP)
        
        photobg = PhotoImage(file = "./gambar/odon/gigisusu.gif")
        self.b22 = Button (F_b22, image = photobg, fg = 'white', bg = '#DCE9F1', command= self.ganti_gambar_b22)
        self.b22.photo = photobg
        self.b22.pack(side = 'top')

        #_________b23_____________
        
        F_b23 = Frame(tengah_atas_kanan,bg='#DCE9F1' )
        F_b23.pack( side= LEFT)

        L_b23 = Label(F_b23  ,bg='#DCE9F1', text="23")
        L_b23.pack( side= TOP)
        
        photobg = PhotoImage(file = "./gambar/odon/gigisusu.gif")
        self.b23 = Button (F_b23, image = photobg, fg = 'white', bg = '#DCE9F1', command= self.ganti_gambar_b23)
        self.b23.photo = photobg
        self.b23.pack(side = 'top')

        #_________b24_____________
        
        F_b24 = Frame(tengah_atas_kanan,bg='#DCE9F1' )
        F_b24.pack( side= LEFT)

        L_b24 = Label(F_b24  ,bg='#DCE9F1', text="24")
        L_b24.pack( side= TOP)
        
        photobg = PhotoImage(file = "./gambar/odon/gigi.gif")
        self.b24 = Button (F_b24, image = photobg, fg = 'white', bg = '#DCE9F1', command= self.ganti_gambar_b24)
        self.b24.photo = photobg
        self.b24.pack(side = 'top')
        #_________b25_____________
        
        F_b25 = Frame(tengah_atas_kanan,bg='#DCE9F1')
        F_b25.pack( side= LEFT)

        L_b25 = Label(F_b25  ,bg='#DCE9F1', text="25")
        L_b25.pack( side= TOP)
        
        photobg = PhotoImage(file = "./gambar/odon/gigi.gif")
        self.b25 = Button (F_b25, image = photobg, fg = 'white', bg = '#DCE9F1', command= self.ganti_gambar_b25)
        self.b25.photo = photobg
        self.b25.pack(side = 'top')
        #_________b26_____________
        
        F_b26 = Frame(tengah_atas_kanan,bg='#DCE9F1')
        F_b26.pack( side= LEFT)

        L_b26 = Label(F_b26  ,bg='#DCE9F1', text="26")
        L_b26.pack( side= TOP)
        
        photobg = PhotoImage(file = "./gambar/odon/gigi.gif")
        self.b26 = Button (F_b26, image = photobg, fg = 'white', bg = '#DCE9F1', command= self.ganti_gambar_b26)
        self.b26.photo = photobg
        self.b26.pack(side = 'top')
        #_________b27_____________
        
        F_b27 = Frame(tengah_atas_kanan,bg='#DCE9F1')
        F_b27.pack( side= LEFT)

        L_b27 = Label(F_b27  ,bg='#DCE9F1', text="27")
        L_b27.pack( side= TOP)
        
        photobg = PhotoImage(file = "./gambar/odon/gigi.gif")
        self.b27 = Button (F_b27, image = photobg, fg = 'white', bg = '#DCE9F1', command= self.ganti_gambar_b27)
        self.b27.photo = photobg
        self.b27.pack(side = 'top')
        #_________b28_____________
        
        F_b28 = Frame(tengah_atas_kanan,bg='#DCE9F1')
        F_b28.pack( side= LEFT)

        L_b28 = Label(F_b28  ,bg='#DCE9F1', text="28")
        L_b28.pack( side= TOP)
        
        photobg = PhotoImage(file = "./gambar/odon/gigi.gif")
        self.b28 = Button (F_b28, image = photobg, fg = 'white', bg = '#DCE9F1', command= self.ganti_gambar_b28)
        self.b28.photo = photobg
        self.b28.pack(side = 'top')

        #_________AAA___222_____________
        #_________aa55_____________
        
        F_aa55 = Frame(tengah_bawah_kiri,bg='#DCE9F1' )
        F_aa55.pack( side= LEFT)

        L_aa55 = Label(F_aa55  ,bg='#DCE9F1', text="55")
        L_aa55.pack( side= TOP)
        
        photobg = PhotoImage(file = "./gambar/odon/gigi.gif")
        self.aa55 = Button (F_aa55, image = photobg, fg = 'white', bg = '#DCE9F1', command= self.ganti_gambar_aa55)
        self.aa55.photo = photobg
        self.aa55.pack(side = 'top')       

        #_________aa54_____________
        
        F_aa54 = Frame(tengah_bawah_kiri,bg='#DCE9F1' )
        F_aa54.pack( side= LEFT)

        L_aa54 = Label(F_aa54  ,bg='#DCE9F1', text="54")
        L_aa54.pack( side= TOP)
        
        photobg = PhotoImage(file = "./gambar/odon/gigi.gif")
        self.aa54 = Button (F_aa54, image = photobg, fg = 'white', bg = '#DCE9F1', command= self.ganti_gambar_aa54)
        self.aa54.photo = photobg
        self.aa54.pack(side = 'top')

        #_________aa53_____________
        
        F_aa53 = Frame(tengah_bawah_kiri,bg='#DCE9F1' )
        F_aa53.pack( side= LEFT)

        L_aa53 = Label(F_aa53  ,bg='#DCE9F1', text="53")
        L_aa53.pack( side= TOP)
        
        photobg = PhotoImage(file = "./gambar/odon/gigisusu.gif")
        self.aa53 = Button (F_aa53, image = photobg, fg = 'white', bg = '#DCE9F1', command= self.ganti_gambar_aa53)
        self.aa53.photo = photobg
        self.aa53.pack(side = 'top')
        
        #_________aa52_____________
        
        F_aa52 = Frame(tengah_bawah_kiri,bg='#DCE9F1' )
        F_aa52.pack( side= LEFT)

        L_aa52 = Label(F_aa52  ,bg='#DCE9F1', text="52")
        L_aa52.pack( side= TOP)
        
        photobg = PhotoImage(file = "./gambar/odon/gigisusu.gif")
        self.aa52 = Button (F_aa52, image = photobg, fg = 'white', bg = '#DCE9F1', command= self.ganti_gambar_aa52)
        self.aa52.photo = photobg
        self.aa52.pack(side = 'top')

        #_________aa51_____________
        
        F_aa51 = Frame(tengah_bawah_kiri,bg='#DCE9F1' )
        F_aa51.pack( side= LEFT)

        L_aa51 = Label(F_aa51  ,bg='#DCE9F1', text="51")
        L_aa51.pack( side= TOP)
        
        photobg = PhotoImage(file = "./gambar/odon/gigisusu.gif")
        self.aa51 = Button (F_aa51, image = photobg, fg = 'white', bg = '#DCE9F1', command= self.ganti_gambar_aa51)
        self.aa51.photo = photobg
        self.aa51.pack(side = 'top')

        #_________BBB___222_____________
        #_________bb61_____________
        
        F_bb61 = Frame(tengah_bawah_kanan,bg='#DCE9F1' )
        F_bb61.pack( side= LEFT)

        L_bb61 = Label(F_bb61  ,bg='#DCE9F1', text="61")
        L_bb61.pack( side= TOP)
        
        photobg = PhotoImage(file = "./gambar/odon/gigisusu.gif")
        self.bb61 = Button (F_bb61, image = photobg, fg = 'white', bg = '#DCE9F1', command= self.ganti_gambar_bb61)
        self.bb61.photo = photobg
        self.bb61.pack(side = 'top')       

        #_________bb62_____________
        
        F_bb62 = Frame(tengah_bawah_kanan,bg='#DCE9F1' )
        F_bb62.pack( side= LEFT)

        L_bb62 = Label(F_bb62  ,bg='#DCE9F1', text="62")
        L_bb62.pack( side= TOP)
        
        photobg = PhotoImage(file = "./gambar/odon/gigisusu.gif")
        self.bb62 = Button (F_bb62, image = photobg, fg = 'white', bg = '#DCE9F1', command= self.ganti_gambar_bb62)
        self.bb62.photo = photobg
        self.bb62.pack(side = 'top')

        #_________bb63_____________
        
        F_bb63 = Frame(tengah_bawah_kanan,bg='#DCE9F1' )
        F_bb63.pack( side= LEFT)

        L_bb63 = Label(F_bb63  ,bg='#DCE9F1', text="63")
        L_bb63.pack( side= TOP)
        
        photobg = PhotoImage(file = "./gambar/odon/gigisusu.gif")
        self.bb63 = Button (F_bb63, image = photobg, fg = 'white', bg = '#DCE9F1', command= self.ganti_gambar_bb63)
        self.bb63.photo = photobg
        self.bb63.pack(side = 'top')

        #_________bb64_____________
        
        F_bb64 = Frame(tengah_bawah_kanan,bg='#DCE9F1' )
        F_bb64.pack( side= LEFT)

        L_bb64 = Label(F_bb64  ,bg='#DCE9F1', text="64")
        L_bb64.pack( side= TOP)
        
        photobg = PhotoImage(file = "./gambar/odon/gigi.gif")
        self.bb64 = Button (F_bb64, image = photobg, fg = 'white', bg = '#DCE9F1', command= self.ganti_gambar_bb64)
        self.bb64.photo = photobg
        self.bb64.pack(side = 'top')

        #_________bb65_____________
        
        F_bb65 = Frame(tengah_bawah_kanan,bg='#DCE9F1' )
        F_bb65.pack( side= LEFT)

        L_bb65 = Label(F_bb65  ,bg='#DCE9F1', text="65")
        L_bb65.pack( side= TOP)
        
        photobg = PhotoImage(file = "./gambar/odon/gigi.gif")
        self.bb65 = Button (F_bb65, image = photobg, fg = 'white', bg = '#DCE9F1', command= self.ganti_gambar_bb65)
        self.bb65.photo = photobg
        self.bb65.pack(side = 'top')

        #_________CCC___222_____________
        #_________cc85_____________
        
        F_cc85 = Frame(tengah_atas2_kiri,bg='#DCE9F1' )
        F_cc85.pack( side= LEFT)

        L_cc85 = Label(F_cc85  ,bg='#DCE9F1', text="85")
        L_cc85.pack( side= TOP)
        
        photobg = PhotoImage(file = "./gambar/odon/gigi.gif")
        self.cc85 = Button (F_cc85, image = photobg, fg = 'white', bg = '#DCE9F1', command= self.ganti_gambar_cc85)
        self.cc85.photo = photobg
        self.cc85.pack(side = 'top')       

        #_________cc84_____________
        
        F_cc84 = Frame(tengah_atas2_kiri,bg='#DCE9F1' )
        F_cc84.pack( side= LEFT)

        L_cc84 = Label(F_cc84  ,bg='#DCE9F1', text="84")
        L_cc84.pack( side= TOP)
        
        photobg = PhotoImage(file = "./gambar/odon/gigi.gif")
        self.cc84 = Button (F_cc84, image = photobg, fg = 'white', bg = '#DCE9F1', command= self.ganti_gambar_cc84)
        self.cc84.photo = photobg
        self.cc84.pack(side = 'top')

        #_________cc83_____________
        
        F_cc83 = Frame(tengah_atas2_kiri,bg='#DCE9F1' )
        F_cc83.pack( side= LEFT)

        L_cc83 = Label(F_cc83  ,bg='#DCE9F1', text="83")
        L_cc83.pack( side= TOP)
        
        photobg = PhotoImage(file = "./gambar/odon/gigisusu.gif")
        self.cc83 = Button (F_cc83, image = photobg, fg = 'white', bg = '#DCE9F1', command= self.ganti_gambar_cc83)
        self.cc83.photo = photobg
        self.cc83.pack(side = 'top')

        #_________cc82_____________
        
        F_cc82 = Frame(tengah_atas2_kiri,bg='#DCE9F1' )
        F_cc82.pack( side= LEFT)

        L_cc82 = Label(F_cc82  ,bg='#DCE9F1', text="82")
        L_cc82.pack( side= TOP)
        
        photobg = PhotoImage(file = "./gambar/odon/gigisusu.gif")
        self.cc82 = Button (F_cc82, image = photobg, fg = 'white', bg = '#DCE9F1', command= self.ganti_gambar_cc82)
        self.cc82.photo = photobg
        self.cc82.pack(side = 'top')

        #_________cc81_____________
        
        F_cc81 = Frame(tengah_atas2_kiri,bg='#DCE9F1' )
        F_cc81.pack( side= LEFT)

        L_cc81 = Label(F_cc81  ,bg='#DCE9F1', text="81")
        L_cc81.pack( side= TOP)
        
        photobg = PhotoImage(file = "./gambar/odon/gigisusu.gif")
        self.cc81 = Button (F_cc81, image = photobg, fg = 'white', bg = '#DCE9F1', command= self.ganti_gambar_cc81)
        self.cc81.photo = photobg
        self.cc81.pack(side = 'top')

        #_________DDD___222_____________
        #_________dd71_____________
        
        F_dd71 = Frame(tengah_atas2_kanan,bg='#DCE9F1' )
        F_dd71.pack( side= LEFT)

        L_dd71 = Label(F_dd71  ,bg='#DCE9F1', text="71")
        L_dd71.pack( side= TOP)
        
        photobg = PhotoImage(file = "./gambar/odon/gigisusu.gif")
        self.dd71 = Button (F_dd71, image = photobg, fg = 'white', bg = '#DCE9F1', command= self.ganti_gambar_dd71)
        self.dd71.photo = photobg
        self.dd71.pack(side = 'top')

        #_________dd72_____________
        
        F_dd72 = Frame(tengah_atas2_kanan,bg='#DCE9F1' )
        F_dd72.pack( side= LEFT)

        L_dd72 = Label(F_dd72  ,bg='#DCE9F1', text="72")
        L_dd72.pack( side= TOP)
        
        photobg = PhotoImage(file = "./gambar/odon/gigisusu.gif")
        self.dd72 = Button (F_dd72, image = photobg, fg = 'white', bg = '#DCE9F1', command= self.ganti_gambar_dd72)
        self.dd72.photo = photobg
        self.dd72.pack(side = 'top')

        #_________dd73_____________
        
        F_dd73 = Frame(tengah_atas2_kanan,bg='#DCE9F1' )
        F_dd73.pack( side= LEFT)

        L_dd73 = Label(F_dd73  ,bg='#DCE9F1', text="73")
        L_dd73.pack( side= TOP)
        
        photobg = PhotoImage(file = "./gambar/odon/gigisusu.gif")
        self.dd73 = Button (F_dd73, image = photobg, fg = 'white', bg = '#DCE9F1', command= self.ganti_gambar_dd73)
        self.dd73.photo = photobg
        self.dd73.pack(side = 'top')


        #_________dd74_____________
        
        F_dd74 = Frame(tengah_atas2_kanan,bg='#DCE9F1' )
        F_dd74.pack( side= LEFT)

        L_dd74 = Label(F_dd74  ,bg='#DCE9F1', text="74")
        L_dd74.pack( side= TOP)
        
        photobg = PhotoImage(file = "./gambar/odon/gigi.gif")
        self.dd74 = Button (F_dd74, image = photobg, fg = 'white', bg = '#DCE9F1', command= self.ganti_gambar_dd74)
        self.dd74.photo = photobg
        self.dd74.pack(side = 'top')


        #_________dd75_____________
        
        F_dd75 = Frame(tengah_atas2_kanan,bg='#DCE9F1' )
        F_dd75.pack( side= LEFT)

        L_dd75 = Label(F_dd75  ,bg='#DCE9F1', text="75")
        L_dd75.pack( side= TOP)
        
        photobg = PhotoImage(file = "./gambar/odon/gigi.gif")
        self.dd75 = Button (F_dd75, image = photobg, fg = 'white', bg = '#DCE9F1', command= self.ganti_gambar_dd75)
        self.dd75.photo = photobg
        self.dd75.pack(side = 'top')


        #_________CCC_____________
        #_________c48_____________
        
        F_c48 = Frame(tengah_bawah2_kiri,bg='#DCE9F1' )
        F_c48.pack( side= LEFT)

        L_c48 = Label(F_c48  ,bg='#DCE9F1', text="48")
        L_c48.pack( side= TOP)
        
        photobg = PhotoImage(file = "./gambar/odon/gigi.gif")
        self.c48 = Button (F_c48, image = photobg, fg = 'white', bg = '#DCE9F1', command= self.ganti_gambar_c48)
        self.c48.photo = photobg
        self.c48.pack(side = 'top')

        #_________c47_____________
        
        F_c47 = Frame(tengah_bawah2_kiri,bg='#DCE9F1' )
        F_c47.pack( side= LEFT)

        L_c47 = Label(F_c47  ,bg='#DCE9F1', text="47")
        L_c47.pack( side= TOP)
        
        photobg = PhotoImage(file = "./gambar/odon/gigi.gif")
        self.c47 = Button (F_c47, image = photobg, fg = 'white', bg = '#DCE9F1', command= self.ganti_gambar_c47)
        self.c47.photo = photobg
        self.c47.pack(side = 'top')


        #_________c46_____________
        
        F_c46 = Frame(tengah_bawah2_kiri,bg='#DCE9F1' )
        F_c46.pack( side= LEFT)

        L_c46 = Label(F_c46  ,bg='#DCE9F1', text="46")
        L_c46.pack( side= TOP)
        
        photobg = PhotoImage(file = "./gambar/odon/gigi.gif")
        self.c46 = Button (F_c46, image = photobg, fg = 'white', bg = '#DCE9F1', command= self.ganti_gambar_c46)
        self.c46.photo = photobg
        self.c46.pack(side = 'top')

        #_________c45_____________
        
        F_c45 = Frame(tengah_bawah2_kiri,bg='#DCE9F1' )
        F_c45.pack( side= LEFT)

        L_c45 = Label(F_c45  ,bg='#DCE9F1', text="45")
        L_c45.pack( side= TOP)
        
        photobg = PhotoImage(file = "./gambar/odon/gigi.gif")
        self.c45 = Button (F_c45, image = photobg, fg = 'white', bg = '#DCE9F1', command= self.ganti_gambar_c45)
        self.c45.photo = photobg
        self.c45.pack(side = 'top')


        #_________c44_____________
        
        F_c44 = Frame(tengah_bawah2_kiri,bg='#DCE9F1' )
        F_c44.pack( side= LEFT)

        L_c44 = Label(F_c44  ,bg='#DCE9F1', text="44")
        L_c44.pack( side= TOP)
        
        photobg = PhotoImage(file = "./gambar/odon/gigi.gif")
        self.c44 = Button (F_c44, image = photobg, fg = 'white', bg = '#DCE9F1', command= self.ganti_gambar_c44)
        self.c44.photo = photobg
        self.c44.pack(side = 'top')

        #_________c43_____________
        
        F_c43 = Frame(tengah_bawah2_kiri,bg='#DCE9F1' )
        F_c43.pack( side= LEFT)

        L_c43 = Label(F_c43  ,bg='#DCE9F1', text="43")
        L_c43.pack( side= TOP)
        
        photobg = PhotoImage(file = "./gambar/odon/gigisusu.gif")
        self.c43 = Button (F_c43, image = photobg, fg = 'white', bg = '#DCE9F1', command= self.ganti_gambar_c43)
        self.c43.photo = photobg
        self.c43.pack(side = 'top')


        #_________c42_____________
        
        F_c42 = Frame(tengah_bawah2_kiri,bg='#DCE9F1' )
        F_c42.pack( side= LEFT)

        L_c42 = Label(F_c42  ,bg='#DCE9F1', text="42")
        L_c42.pack( side= TOP)
        
        photobg = PhotoImage(file = "./gambar/odon/gigisusu.gif")
        self.c42 = Button (F_c42, image = photobg, fg = 'white', bg = '#DCE9F1', command= self.ganti_gambar_c42)
        self.c42.photo = photobg
        self.c42.pack(side = 'top')


        #_________c41_____________
        
        F_c41 = Frame(tengah_bawah2_kiri,bg='#DCE9F1' )
        F_c41.pack( side= LEFT)

        L_c41 = Label(F_c41  ,bg='#DCE9F1', text="41")
        L_c41.pack( side= TOP)
        
        photobg = PhotoImage(file = "./gambar/odon/gigisusu.gif")
        self.c41 = Button (F_c41, image = photobg, fg = 'white', bg = '#DCE9F1', command= self.ganti_gambar_c41)
        self.c41.photo = photobg
        self.c41.pack(side = 'top')


        #_________DDD_____________
        #_________d31_____________
        
        F_d31 = Frame(tengah_bawah2_kanan,bg='#DCE9F1' )
        F_d31.pack( side= LEFT)

        L_d31 = Label(F_d31  ,bg='#DCE9F1', text="31")
        L_d31.pack( side= TOP)
        
        photobg = PhotoImage(file = "./gambar/odon/gigisusu.gif")
        self.d31 = Button (F_d31, image = photobg, fg = 'white', bg = '#DCE9F1', command= self.ganti_gambar_d31)
        self.d31.photo = photobg
        self.d31.pack(side = 'top')

        #_________d32_____________
        
        F_d32 = Frame(tengah_bawah2_kanan,bg='#DCE9F1' )
        F_d32.pack( side= LEFT)

        L_d32 = Label(F_d32  ,bg='#DCE9F1', text="32")
        L_d32.pack( side= TOP)
        
        photobg = PhotoImage(file = "./gambar/odon/gigisusu.gif")
        self.d32 = Button (F_d32, image = photobg, fg = 'white', bg = '#DCE9F1', command= self.ganti_gambar_d32)
        self.d32.photo = photobg
        self.d32.pack(side = 'top')

        #_________d33_____________
        
        F_d33 = Frame(tengah_bawah2_kanan,bg='#DCE9F1' )
        F_d33.pack( side= LEFT)

        L_d33 = Label(F_d33  ,bg='#DCE9F1', text="33")
        L_d33.pack( side= TOP)
        
        photobg = PhotoImage(file = "./gambar/odon/gigisusu.gif")
        self.d33 = Button (F_d33, image = photobg, fg = 'white', bg = '#DCE9F1', command= self.ganti_gambar_d33)
        self.d33.photo = photobg
        self.d33.pack(side = 'top')


        #_________d34_____________
        
        F_d34 = Frame(tengah_bawah2_kanan,bg='#DCE9F1' )
        F_d34.pack( side= LEFT)

        L_d34 = Label(F_d34  ,bg='#DCE9F1', text="34")
        L_d34.pack( side= TOP)
        
        photobg = PhotoImage(file = "./gambar/odon/gigi.gif")
        self.d34 = Button (F_d34, image = photobg, fg = 'white', bg = '#DCE9F1', command= self.ganti_gambar_d34)
        self.d34.photo = photobg
        self.d34.pack(side = 'top')

        #_________d35_____________
        
        F_d35 = Frame(tengah_bawah2_kanan,bg='#DCE9F1' )
        F_d35.pack( side= LEFT)

        L_d35 = Label(F_d35  ,bg='#DCE9F1', text="35")
        L_d35.pack( side= TOP)
        
        photobg = PhotoImage(file = "./gambar/odon/gigi.gif")
        self.d35 = Button (F_d35, image = photobg, fg = 'white', bg = '#DCE9F1', command= self.ganti_gambar_d35)
        self.d35.photo = photobg
        self.d35.pack(side = 'top')

        #_________d36_____________
        
        F_d36 = Frame(tengah_bawah2_kanan,bg='#DCE9F1' )
        F_d36.pack( side= LEFT)

        L_d36 = Label(F_d36  ,bg='#DCE9F1', text="36")
        L_d36.pack( side= TOP)
        
        photobg = PhotoImage(file = "./gambar/odon/gigi.gif")
        self.d36 = Button (F_d36, image = photobg, fg = 'white', bg = '#DCE9F1', command= self.ganti_gambar_d36)
        self.d36.photo = photobg
        self.d36.pack(side = 'top')


        #_________d37_____________
        
        F_d37 = Frame(tengah_bawah2_kanan,bg='#DCE9F1' )
        F_d37.pack( side= LEFT)

        L_d37 = Label(F_d37  ,bg='#DCE9F1', text="37")
        L_d37.pack( side= TOP)
        
        photobg = PhotoImage(file = "./gambar/odon/gigi.gif")
        self.d37 = Button (F_d37, image = photobg, fg = 'white', bg = '#DCE9F1', command= self.ganti_gambar_d37)
        self.d37.photo = photobg
        self.d37.pack(side = 'top')


        #_________d38_____________
        
        F_d38 = Frame(tengah_bawah2_kanan,bg='#DCE9F1' )
        F_d38.pack( side= LEFT)

        L_d38 = Label(F_d38  ,bg='#DCE9F1', text="38")
        L_d38.pack( side= TOP)
        
        photobg = PhotoImage(file = "./gambar/odon/gigi.gif")
        self.d38 = Button (F_d38, image = photobg, fg = 'white', bg = '#DCE9F1', command= self.ganti_gambar_d38)
        self.d38.photo = photobg
        self.d38.pack(side = 'top')


        #----------------------BAWAH-------------------------
        photobg = PhotoImage(file = "./gambar/bg_rekamm.gif")
        bawah = Label(self.pusat_odontogram,bg='#DCE9F1', image = photobg )
        bawah.photo = photobg
        bawah.pack(fill=BOTH, expand=YES, side= TOP, pady=5)


        photobg = PhotoImage(file = "./gambar/simbol.gif")
        self.simbol_odontogram = Label (bawah, image = photobg, fg = 'white', bg = '#DCE9F1')
        self.simbol_odontogram.photo = photobg
        self.simbol_odontogram.pack(side = 'top')

        pilihan = Label(bawah,bg='#DCE9F1' )
        pilihan.pack( side= TOP, pady=5)
        
        tanda_gigi = Label(pilihan,bg='#DCE9F1' ,text = "Tandai Gigi", relief=FLAT,bd=5)
        tanda_gigi.pack( side= LEFT)         

        n = PhotoImage(file = "./gambar/bg_rekamm.gif")
        self.tanda_gigi_value = IntVar()
        self.box_tanda_gigi = ttk.Combobox(pilihan, textvariable=self.tanda_gigi_value ,width=5)
        self.box_tanda_gigi['values'] = ( 18,17,16,15,14,13,12,11,21,22,23,24,25,26,27,28,48,47,46,45,44,43,42,41,31,32,33,34,35,36,37,38)
        self.box_tanda_gigi.current(0)
        self.box_tanda_gigi.pack(side=LEFT,padx=3)
        
        #________odontogram_kanan____________#________odontogram_kanan____________#________odontogram_kanan____________#________odontogram_kanan____________
        self.kanan_atas = Label(self.pusat_odontogram2  ,bg='#00AACC' )
        self.kanan_atas.pack( side= TOP)

        kanan_atas_1 = Label(self.kanan_atas  ,bg='#00AACC' )
        kanan_atas_1.pack( side= LEFT,fill=BOTH)

        kanan_atas_2 = Label(self.kanan_atas  ,bg='#00AACC' )
        kanan_atas_2.pack( side= LEFT,fill=BOTH)

        self.kanan_tengah= Label(self.pusat_odontogram2  ,bg='#00AACC' )
        self.kanan_tengah.pack( side= TOP,pady=5)

        kanan_tengah_1 = Label(self.kanan_tengah  ,bg='#00AACC' )
        kanan_tengah_1.pack( side= LEFT,fill=BOTH)

        kanan_tengah_2 = Label(self.kanan_tengah  ,bg='#00AACC' )
        kanan_tengah_2.pack( side= LEFT,fill=BOTH)


        #___KANAN ATAS1
        self.F_a_11_51 = Frame (kanan_atas_1 , bg ='#D2D7FD' , relief = FLAT , bd=3)
        self.F_a_11_51.pack(fill=BOTH,side=TOP)
        self.Label_a_11_51 = Label (self.F_a_11_51 , text='11 [51] ', bg ='#D2D7FD')#DCE9F1
        self.Label_a_11_51.pack( side=LEFT)
        self.Entry_a_11_51 = Entry (self.F_a_11_51 , width=28, relief = GROOVE , bd=2)
        self.Entry_a_11_51.pack( side=LEFT)

        self.F_a_12_52 = Frame (kanan_atas_1 , bg ='#D2D7FD' , relief = FLAT , bd=3)
        self.F_a_12_52.pack(fill=BOTH,side=TOP)
        self.Label_a_12_52 = Label (self.F_a_12_52 , text='12 [52] ', bg ='#D2D7FD')#DCE9F1
        self.Label_a_12_52.pack( side=LEFT)
        self.Entry_a_12_52 = Entry (self.F_a_12_52 , width=28, relief = GROOVE , bd=2)
        self.Entry_a_12_52.pack( side=LEFT)

        self.F_a_13_53 = Frame (kanan_atas_1 , bg ='#D2D7FD' , relief = FLAT , bd=3)
        self.F_a_13_53.pack(fill=BOTH,side=TOP)
        self.Label_a_13_53 = Label (self.F_a_13_53 , text='13 [53] ', bg ='#D2D7FD')#DCE9F1
        self.Label_a_13_53.pack( side=LEFT)
        self.Entry_a_13_53 = Entry (self.F_a_13_53 , width=28, relief = GROOVE , bd=2)
        self.Entry_a_13_53.pack( side=LEFT)

        self.F_a_14_54 = Frame (kanan_atas_1 , bg ='#D2D7FD' , relief = FLAT , bd=3)
        self.F_a_14_54.pack(fill=BOTH,side=TOP)
        self.Label_a_14_54 = Label (self.F_a_14_54 , text='14 [54] ', bg ='#D2D7FD')#DCE9F1
        self.Label_a_14_54.pack( side=LEFT)
        self.Entry_a_14_54 = Entry (self.F_a_14_54 , width=28, relief = GROOVE , bd=2)
        self.Entry_a_14_54.pack( side=LEFT)

        self.F_a_15_55 = Frame (kanan_atas_1 , bg ='#D2D7FD' , relief = FLAT , bd=3)
        self.F_a_15_55.pack(fill=BOTH,side=TOP)
        self.Label_a_15_55 = Label (self.F_a_15_55 , text='15 [55] ', bg ='#D2D7FD')#DCE9F1
        self.Label_a_15_55.pack( side=LEFT)
        self.Entry_a_15_55 = Entry (self.F_a_15_55 , width=28, relief = GROOVE , bd=2)
        self.Entry_a_15_55.pack( side=LEFT)

        self.F_a_16 = Frame (kanan_atas_1 , bg ='#D2D7FD' , relief = FLAT , bd=3)
        self.F_a_16.pack(fill=BOTH,side=TOP)
        self.Label_a_16 = Label (self.F_a_16 , text='16 '+' '*8, bg ='#D2D7FD')#DCE9F1
        self.Label_a_16.pack( side=LEFT)
        self.Entry_a_16 = Entry (self.F_a_16 , width=28, relief = GROOVE , bd=2)
        self.Entry_a_16.pack( side=LEFT)

        self.F_a_17 = Frame (kanan_atas_1 , bg ='#D2D7FD' , relief = FLAT , bd=3)
        self.F_a_17.pack(fill=BOTH,side=TOP)
        self.Label_a_17 = Label (self.F_a_17 , text='17 '+' '*8, bg ='#D2D7FD')#DCE9F1
        self.Label_a_17.pack( side=LEFT)
        self.Entry_a_17 = Entry (self.F_a_17 , width=28, relief = GROOVE , bd=2)
        self.Entry_a_17.pack( side=LEFT)

        self.F_a_18 = Frame (kanan_atas_1 , bg ='#D2D7FD' , relief = FLAT , bd=3)
        self.F_a_18.pack(fill=BOTH,side=TOP)
        self.Label_a_18 = Label (self.F_a_18 , text='18 '+' '*8, bg ='#D2D7FD')#DCE9F1
        self.Label_a_18.pack( side=LEFT)
        self.Entry_a_18 = Entry (self.F_a_18 , width=28, relief = GROOVE , bd=2)
        self.Entry_a_18.pack( side=LEFT)

        #___KANAN ATAS2
        self.F_a_21_62 = Frame (kanan_atas_2 , bg ='#D2D7FD' , relief = FLAT , bd=3)
        self.F_a_21_62.pack(fill=BOTH,side=TOP)
        self.Entry_a_21_62 = Entry (self.F_a_21_62 , width=28, relief = GROOVE , bd=2)
        self.Entry_a_21_62.pack( side=LEFT)
        self.Label_a_21_62 = Label (self.F_a_21_62 , text='[62] 21 ', bg ='#D2D7FD')#DCE9F2
        self.Label_a_21_62.pack( side=LEFT)

        self.F_a_22_62 = Frame (kanan_atas_2 , bg ='#D2D7FD' , relief = FLAT , bd=3)
        self.F_a_22_62.pack(fill=BOTH,side=TOP)
        self.Entry_a_22_62 = Entry (self.F_a_22_62 , width=28, relief = GROOVE , bd=2)
        self.Entry_a_22_62.pack( side=LEFT)
        self.Label_a_22_62 = Label (self.F_a_22_62 , text='[62] 22 ', bg ='#D2D7FD')#DCE9F2
        self.Label_a_22_62.pack( side=LEFT)

        self.F_a_23_63 = Frame (kanan_atas_2 , bg ='#D2D7FD' , relief = FLAT , bd=3)
        self.F_a_23_63.pack(fill=BOTH,side=TOP)
        self.Entry_a_23_63 = Entry (self.F_a_23_63 , width=28, relief = GROOVE , bd=2)
        self.Entry_a_23_63.pack( side=LEFT)
        self.Label_a_23_63 = Label (self.F_a_23_63 , text='[63] 23 ', bg ='#D2D7FD')#DCE9F2
        self.Label_a_23_63.pack( side=LEFT)

        self.F_a_24_64 = Frame (kanan_atas_2 , bg ='#D2D7FD' , relief = FLAT , bd=3)
        self.F_a_24_64.pack(fill=BOTH,side=TOP)
        self.Entry_a_24_64 = Entry (self.F_a_24_64 , width=28, relief = GROOVE , bd=2)
        self.Entry_a_24_64.pack( side=LEFT)
        self.Label_a_24_64 = Label (self.F_a_24_64 , text='[64] 24 ', bg ='#D2D7FD')#DCE9F2
        self.Label_a_24_64.pack( side=LEFT)

        self.F_a_25_65 = Frame (kanan_atas_2 , bg ='#D2D7FD' , relief = FLAT , bd=3)
        self.F_a_25_65.pack(fill=BOTH,side=TOP)
        self.Entry_a_25_65 = Entry (self.F_a_25_65 , width=28, relief = GROOVE , bd=2)
        self.Entry_a_25_65.pack( side=LEFT)
        self.Label_a_25_65 = Label (self.F_a_25_65 , text='[65] 26 ', bg ='#D2D7FD')#DCE9F2
        self.Label_a_25_65.pack( side=LEFT)

        self.F_a_26 = Frame (kanan_atas_2 , bg ='#D2D7FD' , relief = FLAT , bd=3)
        self.F_a_26.pack(fill=BOTH,side=TOP)
        self.Entry_a_26 = Entry (self.F_a_26 , width=28, relief = GROOVE , bd=2)
        self.Entry_a_26.pack( side=LEFT)
        self.Label_a_26 = Label (self.F_a_26 , text='26 '+' '*8, bg ='#D2D7FD')#DCE9F2
        self.Label_a_26.pack( side=LEFT)

        self.F_a_27 = Frame (kanan_atas_2 , bg ='#D2D7FD' , relief = FLAT , bd=3)
        self.F_a_27.pack(fill=BOTH,side=TOP)
        self.Entry_a_27 = Entry (self.F_a_27 , width=28, relief = GROOVE , bd=2)
        self.Entry_a_27.pack( side=LEFT)
        self.Label_a_27 = Label (self.F_a_27 , text='27 '+' '*8, bg ='#D2D7FD')#DCE9F2
        self.Label_a_27.pack( side=LEFT)

        self.F_a_28 = Frame (kanan_atas_2 , bg ='#D2D7FD' , relief = FLAT , bd=3)
        self.F_a_28.pack(fill=BOTH,side=TOP)
        self.Entry_a_28 = Entry (self.F_a_28 , width=28, relief = GROOVE , bd=2)
        self.Entry_a_28.pack( side=LEFT)
        self.Label_a_28 = Label (self.F_a_28 , text='28 '+' '*8, bg ='#D2D7FD')#DCE9F2
        self.Label_a_28.pack( side=LEFT)

        #___KIRI TENGAH1
        self.F_b_48 = Frame (kanan_tengah_1 , bg ='#D2D7FD' , relief = FLAT , bd=3)
        self.F_b_48.pack(fill=BOTH,side=TOP)
        self.Label_b_48 = Label (self.F_b_48 , text='48 '+' '*8, bg ='#D2D7FD')#DCE9F1
        self.Label_b_48.pack( side=LEFT)
        self.Entry_b_48 = Entry (self.F_b_48 , width=28, relief = GROOVE , bd=2)
        self.Entry_b_48.pack( side=LEFT)

        self.F_b_47 = Frame (kanan_tengah_1 , bg ='#D2D7FD' , relief = FLAT , bd=3)
        self.F_b_47.pack(fill=BOTH,side=TOP)
        self.Label_b_47 = Label (self.F_b_47 , text='47 '+' '*8, bg ='#D2D7FD')#DCE9F1
        self.Label_b_47.pack( side=LEFT)
        self.Entry_b_47 = Entry (self.F_b_47 , width=28, relief = GROOVE , bd=2)
        self.Entry_b_47.pack( side=LEFT)

        self.F_b_46 = Frame (kanan_tengah_1 , bg ='#D2D7FD' , relief = FLAT , bd=3)
        self.F_b_46.pack(fill=BOTH,side=TOP)
        self.Label_b_46 = Label (self.F_b_46 , text='46 '+' '*8, bg ='#D2D7FD')#DCE9F1
        self.Label_b_46.pack( side=LEFT)
        self.Entry_b_46 = Entry (self.F_b_46 , width=28, relief = GROOVE , bd=2)
        self.Entry_b_46.pack( side=LEFT)

        self.F_b_45_85 = Frame (kanan_tengah_1 , bg ='#D2D7FD' , relief = FLAT , bd=3)
        self.F_b_45_85.pack(fill=BOTH,side=TOP)
        self.Label_b_45_85 = Label (self.F_b_45_85 , text='45 [85] ', bg ='#D2D7FD')#DCE9F1
        self.Label_b_45_85.pack( side=LEFT)
        self.Entry_b_45_85 = Entry (self.F_b_45_85 , width=28, relief = GROOVE , bd=2)
        self.Entry_b_45_85.pack( side=LEFT)

        self.F_b_44_84 = Frame (kanan_tengah_1 , bg ='#D2D7FD' , relief = FLAT , bd=3)
        self.F_b_44_84.pack(fill=BOTH,side=TOP)
        self.Label_b_44_84 = Label (self.F_b_44_84 , text='44 [84] ', bg ='#D2D7FD')#DCE9F1
        self.Label_b_44_84.pack( side=LEFT)
        self.Entry_b_44_84 = Entry (self.F_b_44_84 , width=28, relief = GROOVE , bd=2)
        self.Entry_b_44_84.pack( side=LEFT)

        self.F_b_43_83 = Frame (kanan_tengah_1 , bg ='#D2D7FD' , relief = FLAT , bd=3)
        self.F_b_43_83.pack(fill=BOTH,side=TOP)
        self.Label_b_43_83 = Label (self.F_b_43_83 , text='43 [83] ', bg ='#D2D7FD')#DCE9F1
        self.Label_b_43_83.pack( side=LEFT)
        self.Entry_b_43_83 = Entry (self.F_b_43_83 , width=28, relief = GROOVE , bd=2)
        self.Entry_b_43_83.pack( side=LEFT)

        self.F_b_42_82 = Frame (kanan_tengah_1 , bg ='#D2D7FD' , relief = FLAT , bd=3)
        self.F_b_42_82.pack(fill=BOTH,side=TOP)
        self.Label_b_42_82 = Label (self.F_b_42_82 , text='42 [82] ', bg ='#D2D7FD')#DCE9F1
        self.Label_b_42_82.pack( side=LEFT)
        self.Entry_b_42_82 = Entry (self.F_b_42_82 , width=28, relief = GROOVE , bd=2)
        self.Entry_b_42_82.pack( side=LEFT)

        self.F_b_41_81 = Frame (kanan_tengah_1 , bg ='#D2D7FD' , relief = FLAT , bd=3)
        self.F_b_41_81.pack(fill=BOTH,side=TOP)
        self.Label_b_41_81 = Label (self.F_b_41_81 , text='41 [81] ', bg ='#D2D7FD')#DCE9F1
        self.Label_b_41_81.pack( side=LEFT)
        self.Entry_b_41_81 = Entry (self.F_b_41_81 , width=28, relief = GROOVE , bd=2)
        self.Entry_b_41_81.pack( side=LEFT)

        #___KANAN TENGAH2
        self.F_b_38 = Frame (kanan_tengah_2 , bg ='#D2D7FD' , relief = FLAT , bd=3)
        self.F_b_38.pack(fill=BOTH,side=TOP)
        self.Entry_b_38 = Entry (self.F_b_38 , width=27, relief = GROOVE , bd=2)
        self.Entry_b_38.pack( side=LEFT)
        self.Label_b_38 = Label (self.F_b_38 , text='37 '+' '*7, bg ='#D2D7FD')#DCE9F1
        self.Label_b_38.pack( side=LEFT)

        self.F_b_37 = Frame (kanan_tengah_2 , bg ='#D2D7FD' , relief = FLAT , bd=3)
        self.F_b_37.pack(fill=BOTH,side=TOP)
        self.Entry_b_37 = Entry (self.F_b_37 , width=27, relief = GROOVE , bd=2)
        self.Entry_b_37.pack( side=LEFT)
        self.Label_b_37 = Label (self.F_b_37 , text='37 '+' '*7, bg ='#D2D7FD')#DCE9F1
        self.Label_b_37.pack( side=LEFT)

        self.F_b_36 = Frame (kanan_tengah_2 , bg ='#D2D7FD' , relief = FLAT , bd=3)
        self.F_b_36.pack(fill=BOTH,side=TOP)
        self.Entry_b_36 = Entry (self.F_b_36 , width=27, relief = GROOVE , bd=2)
        self.Entry_b_36.pack( side=LEFT)
        self.Label_b_36 = Label (self.F_b_36 , text='36 '+' '*7, bg ='#D2D7FD')#DCE9F1
        self.Label_b_36.pack( side=LEFT)

        self.F_b_35_75 = Frame (kanan_tengah_2 , bg ='#D2D7FD' , relief = FLAT , bd=3)
        self.F_b_35_75.pack(fill=BOTH,side=TOP)
        self.Entry_b_35_75 = Entry (self.F_b_35_75 , width=27, relief = GROOVE , bd=2)
        self.Entry_b_35_75.pack( side=LEFT)
        self.Label_b_35_75 = Label (self.F_b_35_75 , text='[75] 35 ', bg ='#D2D7FD')#DCE9F1
        self.Label_b_35_75.pack( side=LEFT)

        self.F_b_33_73 = Frame (kanan_tengah_2 , bg ='#D2D7FD' , relief = FLAT , bd=3)
        self.F_b_33_73.pack(fill=BOTH,side=TOP)
        self.Entry_b_33_73 = Entry (self.F_b_33_73 , width=27, relief = GROOVE , bd=2)
        self.Entry_b_33_73.pack( side=LEFT)
        self.Label_b_33_73 = Label (self.F_b_33_73 , text='[73] 33 ', bg ='#D2D7FD')#DCE9F1
        self.Label_b_33_73.pack( side=LEFT)

        self.F_b_33_73 = Frame (kanan_tengah_2 , bg ='#D2D7FD' , relief = FLAT , bd=3)
        self.F_b_33_73.pack(fill=BOTH,side=TOP)
        self.Entry_b_33_73 = Entry (self.F_b_33_73 , width=27, relief = GROOVE , bd=2)
        self.Entry_b_33_73.pack( side=LEFT)
        self.Label_b_33_73 = Label (self.F_b_33_73 , text='[73] 33 ', bg ='#D2D7FD')#DCE9F1
        self.Label_b_33_73.pack( side=LEFT)

        self.F_b_32_72 = Frame (kanan_tengah_2 , bg ='#D2D7FD' , relief = FLAT , bd=3)
        self.F_b_32_72.pack(fill=BOTH,side=TOP)
        self.Entry_b_32_72 = Entry (self.F_b_32_72 , width=27, relief = GROOVE , bd=2)
        self.Entry_b_32_72.pack( side=LEFT)
        self.Label_b_32_72 = Label (self.F_b_32_72 , text='[72] 32 ', bg ='#D2D7FD')#DCE9F1
        self.Label_b_32_72.pack( side=LEFT)

        self.F_b_31_71 = Frame (kanan_tengah_2 , bg ='#D2D7FD' , relief = FLAT , bd=3)
        self.F_b_31_71.pack(fill=BOTH,side=TOP)
        self.Entry_b_31_71 = Entry (self.F_b_31_71 , width=27, relief = GROOVE , bd=2)
        self.Entry_b_31_71.pack( side=LEFT)
        self.Label_b_31_71 = Label (self.F_b_31_71 , text='[71] 31 ', bg ='#D2D7FD')#DCE9F1
        self.Label_b_31_71.pack( side=LEFT)

        #BAWAH TTD
        self.kanan_bawah = Label (self.pusat_odontogram2 , fg = 'white', bg = '#DCE9F1')
        self.kanan_bawah.pack(fill=BOTH,side = 'top')
        
        #occlusi_odontogram
        self.F_occlusi_odontogram = Frame (self.kanan_bawah , bg ='#D2D7FD' )
        self.F_occlusi_odontogram.pack(fill=BOTH,side=TOP,pady=2)
        self.Label_occlusi_odontogram = Label (self.F_occlusi_odontogram , text='Occlusi'+' '*23+':', bg ='#D2D7FD')
        self.Label_occlusi_odontogram.pack( side=LEFT)
        
        self.occlusi_odontogram_value = StringVar()
        self.box_occlusi_odontogram = ttk.Combobox(self.F_occlusi_odontogram, textvariable=self.occlusi_odontogram_value ,width=20)
        self.box_occlusi_odontogram['values'] = ('Nnormal Bite', 'Cross Bite' , 'Steep Bite')
        self.box_occlusi_odontogram.pack(side=LEFT)

        self.Label_lain_lain_odontogram = Label (self.F_occlusi_odontogram , text='Lain-lain'+' '*2+':', bg ='#D2D7FD')
        self.Label_lain_lain_odontogram.pack( side=LEFT,padx=4)
        
        self.occlusi_odontogram_value = StringVar()
        self.box_lain_lain_odontogram = ttk.Combobox(self.F_occlusi_odontogram, textvariable=self.occlusi_odontogram_value ,width=15)
        self.box_lain_lain_odontogram['values'] = ('Ada', 'Tidak Ada')
        self.box_lain_lain_odontogram.pack(side=LEFT)

        #Torus_Palatinus
        self.F_Torus_Palatinus_odontogram = Frame (self.kanan_bawah , bg ='#D2D7FD' )
        self.F_Torus_Palatinus_odontogram.pack(fill=BOTH,side=TOP,pady=2)
        self.Label_Torus_Palatinus_odontogram = Label (self.F_Torus_Palatinus_odontogram , text='Torus Palatinus'+' '*9+':', bg ='#D2D7FD')
        self.Label_Torus_Palatinus_odontogram.pack( side=LEFT)
        
        self.Torus_Palatinus_odontogram_value = StringVar()
        self.box_Torus_Palatinus_odontogram = ttk.Combobox(self.F_Torus_Palatinus_odontogram, textvariable=self.Torus_Palatinus_odontogram_value ,width=20)
        self.box_Torus_Palatinus_odontogram['values'] = ('Tidak Ada', 'Kecil' , 'Sedang' , 'Besar' , 'Multiple')
        self.box_Torus_Palatinus_odontogram.pack(side=LEFT)

        #Torus_Mandibularis
        self.F_Torus_Mandibularis_odontogram = Frame (self.kanan_bawah , bg ='#D2D7FD' )
        self.F_Torus_Mandibularis_odontogram.pack(fill=BOTH,side=TOP,pady=2)
        self.Label_Torus_Mandibularis_odontogram = Label (self.F_Torus_Mandibularis_odontogram , text='Torus Mandibularis'+' '*2+':', bg ='#D2D7FD')
        self.Label_Torus_Mandibularis_odontogram.pack( side=LEFT)
        
        self.Torus_Mandibularis_odontogram_value = StringVar()
        self.box_Torus_Mandibularis_odontogram = ttk.Combobox(self.F_Torus_Mandibularis_odontogram, textvariable=self.Torus_Mandibularis_odontogram_value ,width=20)
        self.box_Torus_Mandibularis_odontogram['values'] = ('Tidak Ada', 'Sisi Kiri' , 'Sisi Kanan' , 'Kedua Sisi' )
        self.box_Torus_Mandibularis_odontogram.pack(side=LEFT)

        #Palatum
        self.F_Palatum_odontogram = Frame (self.kanan_bawah , bg ='#D2D7FD' )
        self.F_Palatum_odontogram.pack(fill=BOTH,side=TOP,padx=2)
        self.Label_Palatum_odontogram = Label (self.F_Palatum_odontogram , text='Palatum'+' '*21+':', bg ='#D2D7FD')
        self.Label_Palatum_odontogram.pack( side=LEFT)
        
        self.Palatum_odontogram_value = StringVar()
        self.box_Palatum_odontogram = ttk.Combobox(self.F_Palatum_odontogram, textvariable=self.Palatum_odontogram_value ,width=20)
        self.box_Palatum_odontogram['values'] = ('Dalam', 'Sedang' , 'Rendah' )
        self.box_Palatum_odontogram.pack(side=LEFT)

        #supernumerary_teeth
        self.F_supernumerary_teeth_odontogram = Frame (self.kanan_bawah , bg ='#D2D7FD' )
        self.F_supernumerary_teeth_odontogram.pack(fill=BOTH,side=TOP,pady=2)
        self.Label_supernumerary_teeth_odontogram = Label (self.F_supernumerary_teeth_odontogram , text='Supernumerary Teeth:', bg ='#D2D7FD')
        self.Label_supernumerary_teeth_odontogram.pack( side=LEFT) 
        
        self.supernumerary_teeth_odontogram_value = StringVar()
        self.box_supernumerary_teeth_odontogram = ttk.Combobox(self.F_supernumerary_teeth_odontogram, textvariable=self.supernumerary_teeth_odontogram_value,width=19)
        self.box_supernumerary_teeth_odontogram['values'] = ('Tidak Ada', 'Ada')
        self.box_supernumerary_teeth_odontogram.pack(side=LEFT)
        
        #Diastema
        self.F_Diastema_odontogram = Frame (self.kanan_bawah , bg ='#D2D7FD' )
        self.F_Diastema_odontogram.pack(fill=BOTH,side=TOP,pady=2)
        self.Label_Diastema_odontogram = Label (self.F_Diastema_odontogram , text='Diastema'+' '*20+':', bg ='#D2D7FD')
        self.Label_Diastema_odontogram.pack( side=LEFT)
        
        self.Diastema_odontogram_value = StringVar()
        self.box_Diastema_odontogram = ttk.Combobox(self.F_Diastema_odontogram, textvariable=self.Diastema_odontogram_value ,width=20)
        self.box_Diastema_odontogram['values'] = ('Tidak Ada', 'Ada' )
        self.box_Diastema_odontogram.pack(side=LEFT)
        
        self.Label_atau_Diastema_odontogram = Label (self.F_Diastema_odontogram , text='/', bg ='#D2D7FD')
        self.Label_atau_Diastema_odontogram.pack( side=LEFT,padx=3)

        self.Entry_Diastema_odontogram = Entry (self.F_Diastema_odontogram , width=20, relief = GROOVE , bd=2)
        self.Entry_Diastema_odontogram.pack(fill=BOTH, side=LEFT)

        #Gigi_Anomali
        self.F_Gigi_Anomali_odontogram = Frame (self.kanan_bawah , bg ='#D2D7FD' )
        self.F_Gigi_Anomali_odontogram.pack(fill=BOTH,side=TOP,pady=2)
        self.Label_Gigi_Anomali_odontogram = Label (self.F_Gigi_Anomali_odontogram , text='Gigi Anomali'+' '*14+':', bg ='#D2D7FD')
        self.Label_Gigi_Anomali_odontogram.pack( side=LEFT)
        
        self.Gigi_Anomali_odontogram_value = StringVar()
        self.box_Gigi_Anomali_odontogram = ttk.Combobox(self.F_Gigi_Anomali_odontogram, textvariable=self.Gigi_Anomali_odontogram_value ,width=20)
        self.box_Gigi_Anomali_odontogram['values'] = ('Tidak Ada', 'Ada' )
        self.box_Gigi_Anomali_odontogram.pack(side=LEFT)
        
        self.Label_atau_Gigi_Anomali_odontogram = Label (self.F_Gigi_Anomali_odontogram , text='/', bg ='#D2D7FD')
        self.Label_atau_Gigi_Anomali_odontogram.pack( side=LEFT,padx=3)

        self.Entry_Gigi_Anomali_odontogram = Entry (self.F_Gigi_Anomali_odontogram , width=20, relief = GROOVE , bd=2)
        self.Entry_Gigi_Anomali_odontogram.pack(fill=BOTH, side=LEFT)

        ##HOME SIMPAN CETAK ODONTOGRAM
        self.F_home_simpan_cetak_odontogram = Frame (self.pusat_odontogram2 , bg ='#D2D7FD' )
        self.F_home_simpan_cetak_odontogram.pack(fill=BOTH,side=TOP,pady=4)

        self.gmbr = PhotoImage(file='./gambar/ok.gif')
        self.Tombol_tombol_oke_odontogram = ttk.Button (self.F_home_simpan_cetak_odontogram ,compound='bottom',image= self.gmbr,
                                         text='SIMPAN',command=self.input_identitas)
        self.Tombol_tombol_oke_odontogram.pack( side=LEFT)
        
    def cetak_gambar(self):
        # remove screenhoot
        from os import remove
        remove("Surat_ijin.pdf")
        
        # SCREENSHOT
##        import pyscreenshot as ImageGrab
####        if __name__ == "__main__":
##            # part of the screen
##        im=ImageGrab.grab(bbox=(0,100,850,395))
##        if (im != None):
##            im.save("screenshot.png","png")
##            print "Screenshot saved to screenshot.png."
##           
##        else:
##            pesan.showerror('WARNING!!!',"Unable to get the screenshot.")
##            print "Unable to get the screenshot."

        from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Frame, Spacer
        from reportlab.lib import colors
        from reportlab.lib.units import cm
        from reportlab.lib.pagesizes import A3, A4, landscape, portrait
        from reportlab.lib.pagesizes import letter
        from reportlab.lib.styles import getSampleStyleSheet , ParagraphStyle
        from reportlab.lib.units import mm, inch
        from reportlab.pdfgen import canvas
        from reportlab.platypus import Image, Paragraph, Table
        from reportlab.pdfgen import canvas
        from reportlab.lib.units import inch, cm
        c = canvas.Canvas('Surat_Rujukan.pdf', pagesize=A4)
##        c.drawImage('screenshot.png', 62, 300, 17*cm, 8*cm) #tempel gambar
        
        self.styles = getSampleStyleSheet()
        self.width, self.height = letter

        voffset = 65
        
        header_text = "<b>PRAKTEK DOKTER GIGI SRIMURTINI</b>"
        p = Paragraph(header_text, self.styles["Title"])
        p.wrapOn(c, self.width, self.height)
        p.drawOn(c, 7, 800, mm)

        ptext = """
        No SIP :
        """ 
        p = Paragraph(ptext, self.styles["Normal"])
        p.wrapOn(c, self.width-70, self.height)
        p.drawOn(c, 230, voffset+720, mm)

        ptext = """
        Singosaren RT 02/RW XIV, Malangjiwan Colomadu, Karanganyar
        """ 
        p = Paragraph(ptext, self.styles["Normal"])
        p.wrapOn(c, self.width-70, self.height)
        p.drawOn(c, 165, voffset+705, mm)        
        
        ptext = """
        ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        """ 
        p = Paragraph(ptext, self.styles["Normal"])
        p.wrapOn(c, self.width-70, self.height)
        p.drawOn(c, 20, voffset+680, mm)

        ptext = """
        SURAT RUJUKAN
        """ 
        p = Paragraph(ptext, self.styles["Heading1"])
        p.wrapOn(c, self.width-70, self.height)
        p.drawOn(c, 220, voffset+660, mm)

        ptext = """
        NO :
        """ 
        p = Paragraph(ptext, self.styles["Normal"])
        p.wrapOn(c, self.width-70, self.height)
        p.drawOn(c, 220, voffset+650, mm)

        ptext = """
        Kepada :
        """ 
        p = Paragraph(ptext, self.styles["Normal"])
        p.wrapOn(c, self.width-70, self.height)
        p.drawOn(c, 460, voffset+630, mm)

        ptext = """
        Yth. 
        """ 
        p = Paragraph(ptext, self.styles["Normal"])
        p.wrapOn(c, self.width-70, self.height)
        p.drawOn(c, 390, voffset+610, mm)

        ptext = """
        Di 
        """ 
        p = Paragraph(ptext, self.styles["Normal"])
        p.wrapOn(c, self.width-70, self.height)
        p.drawOn(c, 390, voffset+590, mm)

        
        ptext = """<font size="12">
        Dengan hormat,<br/>
        Bersama ini kami kirimkan penderita<br/></font>
        """
        p = Paragraph(ptext, self.styles["Normal"])
        p.wrapOn(c, self.width, self.height)
        p.drawOn(c, 50, voffset+540, mm)

        ptext = """
        Nama............................:
        """ 
        p = Paragraph(ptext, self.styles["Normal"])
        p.wrapOn(c, self.width-70, self.height)
        p.drawOn(c, 80, voffset+500, mm)

        ptext = """
        Umur : 
        """ 
        p = Paragraph(ptext, self.styles["Normal"])
        p.wrapOn(c, self.width-70, self.height)
        p.drawOn(c, 390, voffset+500, mm)        

        ptext = """
        Jenis Kelamin...............:
                     
        """ 
        p = Paragraph(ptext, self.styles["Normal"])
        p.wrapOn(c, self.width-70, self.height)
        p.drawOn(c, 80, voffset+470, mm)

        ptext = """
        Alamat..........................:
        """ 
        p = Paragraph(ptext, self.styles["Normal"])
        p.wrapOn(c, self.width-70, self.height)
        p.drawOn(c, 80, voffset+440, mm)

        ptext = """
        Anamnesa....................:
        """ 
        p = Paragraph(ptext, self.styles["Normal"])
        p.wrapOn(c, self.width-70, self.height)
        p.drawOn(c, 80, voffset+410, mm)

        ptext = """
        Diagnosa Sementara...:
        """ 
        p = Paragraph(ptext, self.styles["Normal"])
        p.wrapOn(c, self.width-70, self.height)
        p.drawOn(c, 80, voffset+380, mm)

        ptext = """
        Terapi...........................:
        """ 
        p = Paragraph(ptext, self.styles["Normal"])
        p.wrapOn(c, self.width-70, self.height)
        p.drawOn(c, 80, voffset+350, mm)

        ptext = """<font size="12">
        Mohon konsultasi dan perawatan selanjutnya<br/>
        Atas kerjasamanya diucapkan terimakasih<br/></font>
        """
        p = Paragraph(ptext, self.styles["Normal"])
        p.wrapOn(c, self.width, self.height)
        p.drawOn(c, 50, voffset+300, mm)

        ptext ="""
        Colomadu, 
        """ 
        p = Paragraph(ptext, self.styles["Normal"])
        p.wrapOn(c, self.width-70, self.height)
        p.drawOn(c, 390, voffset+270, mm)

        ptext ="""
        Dokter Yang Merawat 
        """ 
        p = Paragraph(ptext, self.styles["Normal"])
        p.wrapOn(c, self.width-70, self.height)
        p.drawOn(c, 390, voffset+250, mm)

        ptext = """
        <b>%s</b>
        """ % ("Dr ")
        p = Paragraph(ptext, self.styles["Normal"])
        p.wrapOn(c, self.width-70, self.height)
        p.drawOn(c, 390, voffset+230, mm)

        ptext = """
        Keterangan<br/>
        <b>%s</b><br/>
        """ % ("Lorem Ipsum ")
        p = Paragraph(ptext, self.styles["Normal"])
        p.wrapOn(c, self.width-70, self.height)
        p.drawOn(c, 50, voffset+200, mm)  


        c.showPage()
        c.save()
        pesan.showinfo('SELAMAT!',"SURAT RUJUKAN BERHASIL DIBUAT \n DENGAN NAMA SURAT RUJUKAN.PDF")
        
    def ganti_gambar_a18(self):
        pilih = self.box_tanda_gigi.get()
        print pilih
        xx = "./gambar/odon/"+pilih+".gif"
        photobg = PhotoImage(file = xx)
        self.a18.configure(image = photobg)
        self.a18.photo = photobg
    def ganti_gambar_a17(self):
        pilih = self.box_tanda_gigi.get()
        print pilih
        xx = "./gambar/odon/"+pilih+".gif"
        photobg = PhotoImage(file = xx)
        self.a17.configure(image = photobg)
        self.a17.photo = photobg
    def ganti_gambar_a16(self):
        pilih = self.box_tanda_gigi.get()
        print pilih
        xx = "./gambar/odon/"+pilih+".gif"
        photobg = PhotoImage(file = xx)
        self.a16.configure(image = photobg)
        self.a16.photo = photobg
    def ganti_gambar_a15(self):
        pilih = self.box_tanda_gigi.get()
        print pilih
        xx = "./gambar/odon/"+pilih+".gif"
        photobg = PhotoImage(file = xx)
        self.a15.configure(image = photobg)
        self.a15.photo = photobg
    def ganti_gambar_a14(self):
        pilih = self.box_tanda_gigi.get()
        print pilih
        xx = "./gambar/odon/"+pilih+".gif"
        photobg = PhotoImage(file = xx)
        self.a14.configure(image = photobg)
        self.a14.photo = photobg
    def ganti_gambar_a13(self):
        pilih = self.box_tanda_gigi.get()
        print pilih
        xx = "./gambar/odon/"+pilih+".gif"
        photobg = PhotoImage(file = xx)
        self.a13.configure(image = photobg)
        self.a13.photo = photobg
    def ganti_gambar_a12(self):
        pilih = self.box_tanda_gigi.get()
        print pilih
        xx = "./gambar/odon/"+pilih+".gif"
        photobg = PhotoImage(file = xx)
        self.a12.configure(image = photobg)
        self.a12.photo = photobg
    def ganti_gambar_a11(self):
        pilih = self.box_tanda_gigi.get()
        print pilih
        xx = "./gambar/odon/"+pilih+".gif"
        photobg = PhotoImage(file = xx)
        self.a11.configure(image = photobg)
        self.a11.photo = photobg

    def ganti_gambar_b21(self):
        pilih = self.box_tanda_gigi.get()
        print pilih
        xx = "./gambar/odon/"+pilih+".gif"
        photobg = PhotoImage(file = xx)
        self.b21.configure(image = photobg)
        self.b21.photo = photobg
    def ganti_gambar_b22(self):
        pilih = self.box_tanda_gigi.get()
        print pilih
        xx = "./gambar/odon/"+pilih+".gif"
        photobg = PhotoImage(file = xx)
        self.b22.configure(image = photobg)
        self.b22.photo = photobg
    def ganti_gambar_b23(self):
        pilih = self.box_tanda_gigi.get()
        print pilih
        xx = "./gambar/odon/"+pilih+".gif"
        photobg = PhotoImage(file = xx)
        self.b23.configure(image = photobg)
        self.b23.photo = photobg
    def ganti_gambar_b24(self):
        pilih = self.box_tanda_gigi.get()
        print pilih
        xx = "./gambar/odon/"+pilih+".gif"
        photobg = PhotoImage(file = xx)
        self.b24.configure(image = photobg)
        self.b24.photo = photobg
    def ganti_gambar_b25(self):
        pilih = self.box_tanda_gigi.get()
        print pilih
        xx = "./gambar/odon/"+pilih+".gif"
        photobg = PhotoImage(file = xx)
        self.b25.configure(image = photobg)
        self.b25.photo = photobg
    def ganti_gambar_b26(self):
        pilih = self.box_tanda_gigi.get()
        print pilih
        xx = "./gambar/odon/"+pilih+".gif"
        photobg = PhotoImage(file = xx)
        self.b26.configure(image = photobg)
        self.b26.photo = photobg
    def ganti_gambar_b27(self):
        pilih = self.box_tanda_gigi.get()
        print pilih
        xx = "./gambar/odon/"+pilih+".gif"
        photobg = PhotoImage(file = xx)
        self.b27.configure(image = photobg)
        self.b27.photo = photobg
    def ganti_gambar_b28(self):
        pilih = self.box_tanda_gigi.get()
        print pilih
        xx = "./gambar/odon/"+pilih+".gif"
        photobg = PhotoImage(file = xx)
        self.b28.configure(image = photobg)
        self.b28.photo = photobg

    def ganti_gambar_c48(self):
        pilih = self.box_tanda_gigi.get()
        print pilih
        xx = "./gambar/odon/"+pilih+".gif"
        photobg = PhotoImage(file = xx)
        self.c48.configure(image = photobg)
        self.c48.photo = photobg
    def ganti_gambar_c47(self):
        pilih = self.box_tanda_gigi.get()
        print pilih
        xx = "./gambar/odon/"+pilih+".gif"
        photobg = PhotoImage(file = xx)
        self.c47.configure(image = photobg)
        self.c47.photo = photobg
    def ganti_gambar_c46(self):
        pilih = self.box_tanda_gigi.get()
        print pilih
        xx = "./gambar/odon/"+pilih+".gif"
        photobg = PhotoImage(file = xx)
        self.c46.configure(image = photobg)
        self.c46.photo = photobg
    def ganti_gambar_c45(self):
        pilih = self.box_tanda_gigi.get()
        print pilih
        xx = "./gambar/odon/"+pilih+".gif"
        photobg = PhotoImage(file = xx)
        self.c45.configure(image = photobg)
        self.c45.photo = photobg
    def ganti_gambar_c44(self):
        pilih = self.box_tanda_gigi.get()
        print pilih
        xx = "./gambar/odon/"+pilih+".gif"
        photobg = PhotoImage(file = xx)
        self.c44.configure(image = photobg)
        self.c44.photo = photobg
    def ganti_gambar_c43(self):
        pilih = self.box_tanda_gigi.get()
        print pilih
        xx = "./gambar/odon/"+pilih+".gif"
        photobg = PhotoImage(file = xx)
        self.c43.configure(image = photobg)
        self.c43.photo = photobg
    def ganti_gambar_c42(self):
        pilih = self.box_tanda_gigi.get()
        print pilih
        xx = "./gambar/odon/"+pilih+".gif"
        photobg = PhotoImage(file = xx)
        self.c42.configure(image = photobg)
        self.c42.photo = photobg
    def ganti_gambar_c41(self):
        pilih = self.box_tanda_gigi.get()
        print pilih
        xx = "./gambar/odon/"+pilih+".gif"
        photobg = PhotoImage(file = xx)
        self.c41.configure(image = photobg)
        self.c41.photo = photobg


    def ganti_gambar_d31(self):
        pilih = self.box_tanda_gigi.get()
        print pilih
        xx = "./gambar/odon/"+pilih+".gif"
        photobg = PhotoImage(file = xx)
        self.d31.configure(image = photobg)
        self.d31.photo = photobg
    def ganti_gambar_d32(self):
        pilih = self.box_tanda_gigi.get()
        print pilih
        xx = "./gambar/odon/"+pilih+".gif"
        photobg = PhotoImage(file = xx)
        self.d32.configure(image = photobg)
        self.d32.photo = photobg
    def ganti_gambar_d33(self):
        pilih = self.box_tanda_gigi.get()
        print pilih
        xx = "./gambar/odon/"+pilih+".gif"
        photobg = PhotoImage(file = xx)
        self.d33.configure(image = photobg)
        self.d33.photo = photobg
    def ganti_gambar_d34(self):
        pilih = self.box_tanda_gigi.get()
        print pilih
        xx = "./gambar/odon/"+pilih+".gif"
        photobg = PhotoImage(file = xx)
        self.d34.configure(image = photobg)
        self.d34.photo = photobg
    def ganti_gambar_d35(self):
        pilih = self.box_tanda_gigi.get()
        print pilih
        xx = "./gambar/odon/"+pilih+".gif"
        photobg = PhotoImage(file = xx)
        self.d35.configure(image = photobg)
        self.d35.photo = photobg
    def ganti_gambar_d36(self):
        pilih = self.box_tanda_gigi.get()
        print pilih
        xx = "./gambar/odon/"+pilih+".gif"
        photobg = PhotoImage(file = xx)
        self.d36.configure(image = photobg)
        self.d36.photo = photobg
    def ganti_gambar_d37(self):
        pilih = self.box_tanda_gigi.get()
        print pilih
        xx = "./gambar/odon/"+pilih+".gif"
        photobg = PhotoImage(file = xx)
        self.d37.configure(image = photobg)
        self.d37.photo = photobg
    def ganti_gambar_d38(self):
        pilih = self.box_tanda_gigi.get()
        print pilih
        xx = "./gambar/odon/"+pilih+".gif"
        photobg = PhotoImage(file = xx)
        self.d38.configure(image = photobg)
        self.d38.photo = photobg

    def ganti_gambar_aa55(self):
        pilih = self.box_tanda_gigi.get()
        print pilih
        xx = "./gambar/odon/"+pilih+".gif"
        photobg = PhotoImage(file = xx)
        self.aa55.configure(image = photobg)
        self.aa55.photo = photobg
    def ganti_gambar_aa54(self):
        pilih = self.box_tanda_gigi.get()
        print pilih
        xx = "./gambar/odon/"+pilih+".gif"
        photobg = PhotoImage(file = xx)
        self.aa54.configure(image = photobg)
        self.aa54.photo = photobg
    def ganti_gambar_aa53(self):
        pilih = self.box_tanda_gigi.get()
        print pilih
        xx = "./gambar/odon/"+pilih+".gif"
        photobg = PhotoImage(file = xx)
        self.aa53.configure(image = photobg)
        self.aa53.photo = photobg
    def ganti_gambar_aa52(self):
        pilih = self.box_tanda_gigi.get()
        print pilih
        xx = "./gambar/odon/"+pilih+".gif"
        photobg = PhotoImage(file = xx)
        self.aa52.configure(image = photobg)
        self.aa52.photo = photobg
    def ganti_gambar_aa51(self):
        pilih = self.box_tanda_gigi.get()
        print pilih
        xx = "./gambar/odon/"+pilih+".gif"
        photobg = PhotoImage(file = xx)
        self.aa51.configure(image = photobg)
        self.aa51.photo = photobg

    def ganti_gambar_bb61(self):
        pilih = self.box_tanda_gigi.get()
        print pilih
        xx = "./gambar/odon/"+pilih+".gif"
        photobg = PhotoImage(file = xx)
        self.bb61.configure(image = photobg)
        self.bb61.photo = photobg
    def ganti_gambar_bb62(self):
        pilih = self.box_tanda_gigi.get()
        print pilih
        xx = "./gambar/odon/"+pilih+".gif"
        photobg = PhotoImage(file = xx)
        self.bb62.configure(image = photobg)
        self.bb62.photo = photobg
    def ganti_gambar_bb63(self):
        pilih = self.box_tanda_gigi.get()
        print pilih
        xx = "./gambar/odon/"+pilih+".gif"
        photobg = PhotoImage(file = xx)
        self.bb63.configure(image = photobg)
        self.bb63.photo = photobg
    def ganti_gambar_bb64(self):
        pilih = self.box_tanda_gigi.get()
        print pilih
        xx = "./gambar/odon/"+pilih+".gif"
        photobg = PhotoImage(file = xx)
        self.bb64.configure(image = photobg)
        self.bb64.photo = photobg
    def ganti_gambar_bb65(self):
        pilih = self.box_tanda_gigi.get()
        print pilih
        xx = "./gambar/odon/"+pilih+".gif"
        photobg = PhotoImage(file = xx)
        self.bb65.configure(image = photobg)
        self.bb65.photo = photobg


    def ganti_gambar_cc85(self):
        pilih = self.box_tanda_gigi.get()
        print pilih
        xx = "./gambar/odon/"+pilih+".gif"
        photobg = PhotoImage(file = xx)
        self.cc85.configure(image = photobg)
        self.cc85.photo = photobg
    def ganti_gambar_cc84(self):
        pilih = self.box_tanda_gigi.get()
        print pilih
        xx = "./gambar/odon/"+pilih+".gif"
        photobg = PhotoImage(file = xx)
        self.cc84.configure(image = photobg)
        self.cc84.photo = photobg
    def ganti_gambar_cc83(self):
        pilih = self.box_tanda_gigi.get()
        print pilih
        xx = "./gambar/odon/"+pilih+".gif"
        photobg = PhotoImage(file = xx)
        self.cc83.configure(image = photobg)
        self.cc83.photo = photobg
    def ganti_gambar_cc82(self):
        pilih = self.box_tanda_gigi.get()
        print pilih
        xx = "./gambar/odon/"+pilih+".gif"
        photobg = PhotoImage(file = xx)
        self.cc82.configure(image = photobg)
        self.cc82.photo = photobg
    def ganti_gambar_cc81(self):
        pilih = self.box_tanda_gigi.get()
        print pilih
        xx = "./gambar/odon/"+pilih+".gif"
        photobg = PhotoImage(file = xx)
        self.cc81.configure(image = photobg)
        self.cc81.photo = photobg


    def ganti_gambar_dd71(self):
        pilih = self.box_tanda_gigi.get()
        print pilih
        xx = "./gambar/odon/"+pilih+".gif"
        photobg = PhotoImage(file = xx)
        self.dd71.configure(image = photobg)
        self.dd71.photo = photobg
    def ganti_gambar_dd72(self):
        pilih = self.box_tanda_gigi.get()
        print pilih
        xx = "./gambar/odon/"+pilih+".gif"
        photobg = PhotoImage(file = xx)
        self.dd72.configure(image = photobg)
        self.dd72.photo = photobg
    def ganti_gambar_dd73(self):
        pilih = self.box_tanda_gigi.get()
        print pilih
        xx = "./gambar/odon/"+pilih+".gif"
        photobg = PhotoImage(file = xx)
        self.dd73.configure(image = photobg)
        self.dd73.photo = photobg
    def ganti_gambar_dd74(self):
        pilih = self.box_tanda_gigi.get()
        print pilih
        xx = "./gambar/odon/"+pilih+".gif"
        photobg = PhotoImage(file = xx)
        self.dd74.configure(image = photobg)
        self.dd74.photo = photobg
    def ganti_gambar_dd75(self):
        pilih = self.box_tanda_gigi.get()
        print pilih
        xx = "./gambar/odon/"+pilih+".gif"
        photobg = PhotoImage(file = xx)
        self.dd75.configure(image = photobg)
        self.dd75.photo = photobg

    def tampil_data_ke_odontogram(self):
        nama            = self.Entry_nama.get()
        kelamin         = self.box_kelamin.get()
        tempat_lahir    = self.Entry_ttl.get()
        tanggal_lahir   = self.box_ttl_tanggal.get()+ ' '+self.box_ttl_bulan.get()+ ' '+self.box_ttl_tahun.get()
        alamat          = self.Entry_alamat.get()
        pekerjaan       = self.Entry_pekerjaan.get()

        golongan_darah          = self.box_golongan_darah.get()
        tekanan_darah_normal    = self.box_tekanan_darah_normal.get()
        penyakit_jantung        = self.box_penyakit_jantung.get()
        diabetes                = self.box_diabetes.get()
        haemophilia             = self.box_haemophilia.get()
        hepatitis               = self.box_hepatitis.get()
        penyakit_lainya         = self.box_penyakit_lainya.get()
        alergi_thd_obat_obatan  = self.box_alergi_thd_obat_obatan.get()
        alergi_thd_makanan      = self.box_alergi_thd_makanan.get()

        occulusi                = self.box_occulusi.get()
        torus_palantinus        = self.box_torus_palantinus.get()
        torus_mandibularis      = self.box_torus_mandibularis.get()
        palatum                 = self.box_palatum.get()
        supernumerary_teeth     = self.box_supernumerary_teeth.get()
        diasterna               = self.box_diasterna.get()
        gigi_anomali            = self.box_gigi_anomali.get()
        lain_lain               = self.box_lain_lain.get()
        if nama == "" or kelamin ==  "" or tempat_lahir == "" or tanggal_lahir == "" or alamat == "" or pekerjaan == "" or\
           golongan_darah == "" or tekanan_darah_normal ==  "" or penyakit_jantung == "" or diabetes == "" or haemophilia == "" or hepatitis == "" or\
           penyakit_lainya == "" or alergi_thd_obat_obatan ==  "" or alergi_thd_makanan == "" or\
           occulusi == "" or torus_palantinus ==  "" or torus_mandibularis == "" or palatum == "" or supernumerary_teeth == "" or diasterna == "" or\
           gigi_anomali == "" or lain_lain == "":
            pesan.showerror('WARNING!!!','PASTIKAN DATA SUDAH LENGKAP')

        else:
            self.ke_odontogram()
            self.box_ttl_tanggal_odontogram.delete(0,END)
            self.box_ttl_bulan_odontogram.delete(0,END)
            self.box_ttl_tahun_odontogram.delete(0,END)
            
            self.Entry_nama_odontogram.insert(0,self.Entry_nama.get())
            self.box_kelamin_odontogram.insert(0,self.box_kelamin.get())
            self.Entry_alamat_odontogram.insert(0,self.Entry_alamat.get())
            self.Entry_ttl_odontogram.insert(0,self.Entry_ttl.get())
            self.box_ttl_tanggal_odontogram.insert(END,self.box_ttl_tanggal.get())
            self.box_ttl_bulan_odontogram.insert(END,self.box_ttl_bulan.get())
            self.box_ttl_tahun_odontogram.insert(END,self.box_ttl_tahun.get())

            self.box_occlusi_odontogram.insert(0,self.box_occulusi.get())
            self.box_Torus_Palatinus_odontogram.insert(0,self.box_torus_palantinus.get())
            self.box_Torus_Mandibularis_odontogram.insert(0,self.box_torus_mandibularis.get())
            self.box_Palatum_odontogram.insert(0,self.box_palatum.get())
            self.box_supernumerary_teeth_odontogram.insert(0,self.box_supernumerary_teeth.get())
            self.box_Diastema_odontogram.insert(0,self.box_diasterna.get())
            self.box_Gigi_Anomali_odontogram.insert(0,self.box_gigi_anomali.get())
            self.box_lain_lain_odontogram.insert(0,self.box_lain_lain.get())
            

        
############################################################################################################################
    def pilihan_kelamin(self, event):
        self.value_kelamin = self.box_kelamin.get()
        #print(self.value_kelamin)
        
    def pilihan_ttl_tanggal(self, event):
        self.value_ttl_tanggal = self.box_ttl_tanggal.get()
        #print(self.value_ttl_tanggal)

    def pilihan_ttl_bulan(self, event):
        self.value_ttl_bulan = self.box_ttl_bulan.get()
        #print(self.value_ttl_bulan)

    def pilihan_ttl_tahun(self, event):
        self.value_ttl_tahun = self.box_ttl_tahun.get()
        #print(self.value_ttl_tahun)
        
    def input_identitas_kosongan(self):
        self.Entry_nama.delete(0, END)
        self.box_kelamin.delete(0, END)
        self.Entry_ttl.delete(0, END)
        self.box_ttl_tanggal.delete(0, END)
        self.box_ttl_bulan.delete(0, END)
        self.box_ttl_tahun.delete(0, END)
        self.Entry_alamat.delete(0, END)
        self.Entry_pekerjaan.delete(0, END)
        
        self.box_golongan_darah.delete(0, END)
        self.box_tekanan_darah_normal.delete(0, END)
        self.box_penyakit_jantung.delete(0, END)
        self.box_diabetes.delete(0, END)
        self.box_haemophilia.delete(0, END)
        self.box_hepatitis.delete(0, END)
        self.box_penyakit_lainya.delete(0, END)
        self.box_alergi_thd_obat_obatan.delete(0, END)
        self.box_alergi_thd_makanan.delete(0, END)

        self.box_occulusi.delete(0, END)
        self.box_torus_palantinus.delete(0, END)
        self.box_torus_mandibularis.delete(0, END)
        self.box_palatum.delete(0, END)
        self.box_supernumerary_teeth.delete(0, END)
        self.box_diasterna.delete(0, END)
        self.box_gigi_anomali.delete(0, END)
        self.box_lain_lain.delete(0, END)

        
    def input_identitas(self,event=None):
        import pyscreenshot as ImageGrab
##        if __name__ == "__main__":
            # part of the screen
        im=ImageGrab.grab(bbox=(0,119,856,413))
        if (im != None):
            im.save("screenshot.png","png")
            print "Screenshot saved to screenshot.png."
            pesan.showinfo('SELAMAT!!!',"Screenshot saved to screenshot.png.")
        else:
            pesan.showerror('WARNING!!!',"Unable to get the screenshot.")
            print "Unable to get the screenshot."

            
        nama            = self.Entry_nama.get()
        kelamin         = self.box_kelamin.get()
        tempat_lahir    = self.Entry_ttl.get()
        tanggal_lahir   = self.box_ttl_tanggal.get()+ ' '+self.box_ttl_bulan.get()+ ' '+self.box_ttl_tahun.get()
        alamat          = self.Entry_alamat.get()
        pekerjaan       = self.Entry_pekerjaan.get()

        golongan_darah          = self.box_golongan_darah.get()
        tekanan_darah_normal    = self.box_tekanan_darah_normal.get()
        penyakit_jantung        = self.box_penyakit_jantung.get()
        diabetes                = self.box_diabetes.get()
        haemophilia             = self.box_haemophilia.get()
        hepatitis               = self.box_hepatitis.get()
        penyakit_lainya         = self.box_penyakit_lainya.get()
        alergi_thd_obat_obatan  = self.box_alergi_thd_obat_obatan.get()
        alergi_thd_makanan      = self.box_alergi_thd_makanan.get()

        occulusi                = self.box_occulusi.get()
        torus_palantinus        = self.box_torus_palantinus.get()
        torus_mandibularis      = self.box_torus_mandibularis.get()
        palatum                 = self.box_palatum.get()
        supernumerary_teeth     = self.box_supernumerary_teeth.get()
        diasterna               = self.box_diasterna.get()
        gigi_anomali            = self.box_gigi_anomali.get()
        lain_lain               = self.box_lain_lain.get()

        if nama == "" or kelamin ==  "" or tempat_lahir == "" or tanggal_lahir == "" or alamat == "" or pekerjaan == "" or\
           golongan_darah == "" or tekanan_darah_normal ==  "" or penyakit_jantung == "" or diabetes == "" or haemophilia == "" or hepatitis == "" or\
           penyakit_lainya == "" or alergi_thd_obat_obatan ==  "" or alergi_thd_makanan == "" or\
           occulusi == "" or torus_palantinus ==  "" or torus_mandibularis == "" or palatum == "" or supernumerary_teeth == "" or diasterna == "" or\
           gigi_anomali == "" or lain_lain == "":
            pesan.showerror('WARNING!!!','PASTIKAN DATA SUDAH LENGKAP')
        else:
            #_>__>_>_>_>_>_>___>_>_>_>>>__syntax
            connection = MySQLdb.connect(
                            host = 'localhost',
                            user = 'root',
                            passwd = '')  # create the connection

            cursor = connection.cursor()
            sql = "use pasien;"
            data = "INSERT INTO `identitas`(`nama`, `jenis_kelamin`, `tempat_lahir`, `tanggal_lahir`, `alamat`, `pekerjaan`,`golongan_darah`, `tekanan_darah_normal`, `penyakit_jantung`, `diabetes`, `haemophilia`, `hepatitis`, `penyakit_lainya`, `alergi_obat`, `alergi_makanan`,`occulusi`, `torus_palantinus`, `torus_mandibularis`, `palatium`, `supernumerary_teeth`, `diasterna`, `gigi_anomaly`, `lain_lain`, `gambar`)VALUES ('"+\
                   nama+"','"+kelamin+"','"+tempat_lahir+"','"+tanggal_lahir+"','"+alamat+"','"+pekerjaan+\
                   "','"+golongan_darah+"','"+tekanan_darah_normal+"','"+penyakit_jantung+"','"+diabetes+"','"+haemophilia+"','"+hepatitis+"','"+penyakit_lainya+"','"+alergi_thd_obat_obatan+"','"+alergi_thd_makanan+\
                   "','"+occulusi+"','"+torus_palantinus+"','"+torus_mandibularis+"','"+palatum+"','"+supernumerary_teeth+"','"+diasterna+"','"+gigi_anomali+"','"+lain_lain+"',%s);"

            image = Image.open("screenshot.png")
            blob_value = open("screenshot.png", 'rb').read()
            args = (blob_value, )
            
            cursor.execute(sql)
            cursor.execute(data,args)
            connection.commit()
            connection.close()
            pesan.showinfo('INFO','DATA BERHASIL DISIMPAN')
            self.input_identitas_kosongan()
            #print "INSERT INTO `identitas`(`id`, `nama`, `jenis_kelamin`, `tempat_lahir`, `tanggal_lahir`, `alamat`, `pekerjaan`)VALUES ('"+"not null"+"','"+nama+"','"+kelamin+"','"+tempat_lahir+"','"+tanggal_lahir+"','"+alamat+"','"+pekerjaan+"');"
         
    def Pencarian(self):
        self.Pencarian_window = Toplevel(self)
        self.Pencarian_window.wm_title('Pencarian Data Pasien')
            # atur ukuran window
            # menempatkan window di tengah layar PC/Laptop
        lebar = 1200
        tinggi = 600
        # ************************* penggunaan fungsi winfo_screenwidth()
        setTengahX = (self.winfo_screenwidth() - lebar)//2
        # ************************* penggunaan fungsi winfo_screenheight()
        setTengahY = (self.winfo_screenheight() - tinggi)//4
        self.Pencarian_window.geometry("%ix%i+%i+%i" %(lebar, tinggi, setTengahX, setTengahY))
        # ****************************************************************
        self.induk.withdraw()

        mainFrame = Frame(self.Pencarian_window,bg='#DCE9F1' )
        mainFrame.pack(fill=BOTH, expand=YES)
        self.main_c = mainFrame
        # ********************* INPUT **********************************************

        self.F_atas_c = Frame (self.main_c , bg ='#DCE9F1' , relief = FLAT , bd=3)
        self.F_atas_c.pack(fill=BOTH,side=TOP)
        
        self.F_atas_kiri_c = Frame (self.F_atas_c , bg ='#DCE9F1' , relief = RIDGE , bd=3)
        self.F_atas_kiri_c.pack(fill=BOTH,side=LEFT)
        
        self.F_atas_kiri_c_x = Frame (self.F_atas_kiri_c , bg ='#DCE9F1' )
        self.F_atas_kiri_c_x.pack(fill=BOTH,side=LEFT)

        self.F_atas_kiri_c_xx = Frame (self.F_atas_kiri_c , bg ='#DCE9F1' )
        self.F_atas_kiri_c_xx.pack(fill=BOTH,side=LEFT)

        self.F_atas_kanan_c = Frame (self.F_atas_c , bg ='#DCE9F1' )
        self.F_atas_kanan_c.pack(fill=BOTH,side=LEFT)

        #________nama____________
        self.F_nama_c = Frame (self.F_atas_kiri_c_x , bg ='#DCE9F1' , relief = FLAT , bd=3)
        self.F_nama_c.pack(fill=BOTH,side=TOP)
        self.Label_nama_c = Label (self.F_nama_c , text='Nama'+' '*38+':', bg ='#DCE9F1')#DCE9F1
        self.Label_nama_c.pack( side=LEFT)
        self.Entry_nama_c = Entry (self.F_nama_c , width=70, relief = GROOVE , bd=2)
        self.Entry_nama_c.pack(fill=BOTH, side=LEFT)

        #________Tempat_Tanggal_Lahir____________
        self.F_ttl_c = Frame (self.F_atas_kiri_c_x , bg ='#DCE9F1', relief = FLAT , bd=3)
        self.F_ttl_c.pack(fill=BOTH,side=TOP)
        self.Label_ttl_c = Label (self.F_ttl_c , text='Tempat,Tanggal Lahir'+' '*10+':', bg ='#DCE9F1')
        self.Label_ttl_c.pack( side=LEFT)

        #***cari_tempat_lahir_yang_sudah_pernah_input***#
        #select distinct tempat_lahir from identitas; < syntax
        #_>__>_>_>_>_>_>___>_>_>_>>>__syntax
        connection = MySQLdb.connect(
                        host = 'localhost',
                        user = 'root',
                        passwd = '')  # create the connection

        cursor = connection.cursor()
        sql = "use pasien;"
        cari = "select distinct tempat_lahir from identitas;"
        cursor.execute(sql)
        cursor.execute(cari)
        tempat_lahir_old  =cursor.fetchall()
        connection.commit()
        
        self.ttl_tempat_value_c = StringVar()
        self.box_ttl_tempat_c = ttk.Combobox(self.F_ttl_c, textvariable=self.ttl_tempat_value_c ,width=13)
        self.box_ttl_tempat_c['values'] = (tempat_lahir_old)
        self.box_ttl_tempat_c.pack(side=LEFT,padx=6)
        
        #***********************************************#
        
        self.ttl_tanggal_value_c = IntVar()
        self.box_ttl_tanggal_c = ttk.Combobox(self.F_ttl_c, textvariable=self.ttl_tanggal_value_c ,width=5)
        self.box_ttl_tanggal_c['values'] = ( range(1,32))
        self.box_ttl_tanggal_c.current(0)
        self.box_ttl_tanggal_c.pack(side=LEFT,padx=3)

        self.ttl_bulan_value_c = StringVar()
        self.box_ttl_bulan_c = ttk.Combobox(self.F_ttl_c, textvariable=self.ttl_bulan_value_c ,width=13)
        self.box_ttl_bulan_c['values'] = ('JANUARI', 'FEBUARI' , 'MARET' ,'APRIL', 'MEI', 'JUNI', 'JULI', 'AGUSTUS', 'SEPTEMBER', 'OKTOBER', 'NOVEMBER',
                                        'DESEMBER')
        self.box_ttl_bulan_c.current(0)
        self.box_ttl_bulan_c.pack(side=LEFT,padx=3)

        self.ttl_tahun_value_c = IntVar()
        self.box_ttl_tahun_c = ttk.Combobox(self.F_ttl_c, textvariable=self.ttl_tahun_value_c ,width=5)
        self.box_ttl_tahun_c['values'] = ( range(1901,2018))
        self.box_ttl_tahun_c.current(0)
        self.box_ttl_tahun_c.pack(side=LEFT,padx=3)

        #________Tombol_cari____________

        self.gmbrc = PhotoImage(file='./gambar/cari_c.gif')
        self.Tombol_tombol_cari_c = ttk.Button (self.F_atas_kiri_c_xx ,image= self.gmbrc, command=self.mencari_data)
        self.Tombol_tombol_cari_c.pack( side=RIGHT,pady=8,padx=8)

        #________Tombol_home____________

        self.gmbrcc = PhotoImage(file='./gambar/home_c.gif')
        self.Tombol_tombol_tampil_c = ttk.Button (self.F_atas_kanan_c ,text="HOME",compound="top",image= self.gmbrcc, command=self.kembali)
        self.Tombol_tombol_tampil_c.pack( side=RIGHT,pady=8,padx=10)
        #________Tombol_tambah____________

        self.gmbrcccc = PhotoImage(file='./gambar/tambah.gif')
        self.Tombol_tombol_tambah_c = ttk.Button (self.F_atas_kanan_c ,text="DATA BARU",compound="top",image= self.gmbrcccc, command=self.ke_rekam_medis)
        self.Tombol_tombol_tambah_c.pack( side=RIGHT,pady=8,padx=10)
        #________Tombol_tampil____________

        self.gmbrccc = PhotoImage(file='./gambar/tampilkan_c.gif')
        self.Tombol_tombol_tampil_c = ttk.Button (self.F_atas_kanan_c ,text="TAMPILKAN",compound="top",image= self.gmbrccc,
                                                state=DISABLED,command=self.tampil_data_lama_ke_rekam)
        self.Tombol_tombol_tampil_c.pack( side=RIGHT,pady=8,padx=30)

        #________Tombol_delete____________

        self.gmbrccccc = PhotoImage(file='./gambar/delete.gif')
        self.Tombol_tombol_delete_c = ttk.Button (self.F_atas_kanan_c ,text="DELETE",compound="top",image= self.gmbrccccc,
                                                state=DISABLED,command=self.delete_data_lama_rekam)
        self.Tombol_tombol_delete_c.pack( side=RIGHT,pady=8,padx=30)

        s = ttk.Style()
        s.configure('TButton', relief=RIDGE, background ='#DCE9F1',fontground="#DCE9F1",foreground="maroon", fieldbackground="#DCE9F1")
        s.theme_use('clam')

        photoc = PhotoImage(file = "./gambar/bg_c.gif")
        self.FmenuTrv_c = Label(self.main_c , image = photoc ,bg='#D2D7FD',relief=GROOVE,bd=2)
        self.FmenuTrv_c.photo = photoc
        self.FmenuTrv_c.pack(side=TOP,fill=BOTH, expand = 'yes',pady=15)
       
    def mencari_data (self,event=None):
        nama_c            = self.Entry_nama_c.get()
        tempat_lahir_c    = self.box_ttl_tempat_c.get()
        tanggal_lahir_c   = self.box_ttl_tanggal_c.get()+ ' '+self.box_ttl_bulan_c.get()+ ' '+self.box_ttl_tahun_c.get()
        
         #_>__>_>_>_>_>_>___>_>_>_>>>__syntax
        connection = MySQLdb.connect(
                        host = 'localhost',
                        user = 'root',
                        passwd = '')  # create the connection

        cursor = connection.cursor()
        sql = "use pasien;"
        data = "desc identitas;"
        cursor.execute(sql)
        cursor.execute(data)
        response = cursor.fetchall()
        data_heading = []
        for row in response:
            #print row[0]
            data_heading.append(row[0])
        data_heading = data_heading[0:7]
        
        #D2D7FD
        #EAEBFF
        #select * from identitas where nama="danias" or tempat_lahir="solo" and tanggal_lahir="7 juli 1997" ;
        coba = 'select * from identitas where nama="'+nama_c+'" or tempat_lahir="'+tempat_lahir_c+'" and tanggal_lahir="'+tanggal_lahir_c+'" ;'
##        cursor.execute('select *   from identitas where nama="'+nama_c+'" or tempat_lahir="'+tempat_lahir_c+'" and tanggal_lahir="'+tanggal_lahir_c+'" ;')
        cursor.execute('select *   from identitas where nama like"%'+nama_c+'%" or tempat_lahir="'+tempat_lahir_c+'" and tanggal_lahir="'+tanggal_lahir_c+'" ;')
        
        numrows = int(cursor.rowcount)
        
        data_isi = []
        if numrows == 0:
            pesan.showinfo('ONDOTOGRAM','MAAF , DATA TIDAK DITEMUKAN') 
        else:
            for x in range(0,numrows):
                row = cursor.fetchone()
                data_isi.append(row[0:7])
            
            self.Tombol_tombol_tampil_c.configure(state=NORMAL)
            self.Tombol_tombol_delete_c.configure(state=NORMAL)


        #_________buat__tabel__dengan__Treeview
        
        self.menuTrv_c = LabelFrame(self.FmenuTrv_c,bg='#EAEBFF',
                                  fg='#e1f5fe',relief=GROOVE,bd=2)
        self.menuTrv_c.pack(side=TOP,fill=BOTH,pady=8,padx=6,expand=YES)
        
        self.trvTabel_c = ttk.Treeview(self.menuTrv_c, columns=data_heading,
                show='headings',height=20)
        s = ttk.Style()
        s.theme_use('clam')
        s.configure("Treeview", background="#EAEBFF",foreground="black", fieldbackground="#EAEBFF")#004d40
        s.configure("Treeview.Heading", background="#D2D7FD",foreground="black", fieldbackground="#EAEBFF")
        #4A6984
        
        #_________buat___________________scrollbar
        sbVer = ttk.Scrollbar(self.menuTrv_c, orient='vertical',
                command=self.trvTabel_c.yview,cursor='hand2')
        sbHor = ttk.Scrollbar(self.menuTrv_c, orient='horizontal',
                command=self.trvTabel_c.xview,cursor='hand2')
        #_________pasang____dengan___layout____manager____pack()
        sbVer.pack(side=RIGHT, fill=Y)
        sbHor.pack(side=BOTTOM, fill=X)
        self.trvTabel_c.pack(side=LEFT, expand=YES,fill=BOTH)

        for kolom in data_heading:
            self.trvTabel_c.heading(kolom, text=kolom)
            
        for x in data_isi:
            self.trvTabel_c.insert('', 'end', values=x)
                
        self.data_isi=data_isi
        self.data_heading=data_heading
        self.Tombol_tombol_cari_c.configure(command=self.mencari_data_2)
        
    def mencari_data_2 (self):
        self.FmenuTrv_c.destroy()        
        photoc = PhotoImage(file = "./gambar/bg_cc.gif")
        self.FmenuTrv_c = Label(self.main_c , image = photoc ,bg='#D2D7FD',relief=GROOVE,bd=2)
        self.FmenuTrv_c.photo = photoc
        self.FmenuTrv_c.pack(side=TOP,fill=BOTH, expand = 'yes',pady=15)
        
        self.mencari_data()

    def kembali(self):
        try:
            self.rekam_medis_window.withdraw()
            self.induk.deiconify()
        except:
            self.Pencarian_window.withdraw()
            self.induk.deiconify()
            
    def ke_rekam_medis(self):
        self.Pencarian_window.withdraw()
        self.rekam_medis()
        
    def ke_odontogram(self):
        self.rekam_medis_window.withdraw()
        self.odontogram()
        
    def odontogram_ke_rekam_medis(self):    
        self.odontogram_window.withdraw()
        self.rekam_medis_window.deiconify()

    def odontogram_ke_home(self):    
        self.odontogram_window.withdraw()
        self.induk.deiconify() 

    def tampil_data_lama_ke_rekam(self ):
        ####______cari_data_selection_berdasar_id
        try:
            item = self.trvTabel_c.selection()[0]
        
            
    ##        print(self.trvTabel_c.item(item,"values"))
            self.fokus_data=[]
            for row in (self.trvTabel_c.item(item,"values")):
                self.fokus_data.append(row)
            self.fokus_data_id=self.fokus_data[0:]
    ##        print self.fokus_data_id[0:]
            print self.fokus_data_id[0]
            
             #_>__>_>_>_>_>_>___>_>_>_>>>__syntax
            connection = MySQLdb.connect(
                            host = 'localhost',
                            user = 'root',
                            passwd = '')  # create the connection

            cursor = connection.cursor()
            sql = "use pasien;"
            data = 'select * from identitas where id='+self.fokus_data_id[0]+';'
            cursor.execute(sql)
            cursor.execute(data)
            numrows = int(cursor.rowcount)
            data_tampil = []
            for x in range(0,numrows):
                row = cursor.fetchone()
                data_tampil.append(row[1:])
            data_siap_tampil = data_tampil[0]
            
            #________data_split_ttl
            bahan_split = data_siap_tampil[3].split()
            ttl=[]
            for kata in bahan_split:
                ttl.append(kata)
                
            #________data_siap tampil
            
            self.Tampil_nama            = data_siap_tampil[0]
            self.Tampil_kelamin         = data_siap_tampil[1]
            self.Tampil_tempat_lahir    = data_siap_tampil[2]
            self.Tampil_tanggal_lahir   = ttl[0]
            self.Tampil_bulan_lahir     = ttl[1]
            self.Tampil_tahun_lahir     = ttl[2]
            self.Tampil_alamat          = data_siap_tampil[4]
            self.Tampil_pekerjaan       = data_siap_tampil[5]

            self.Tampil_golongan_darah          = data_siap_tampil[6]
            self.Tampil_tekanan_darah_normal    = data_siap_tampil[7]
            self.Tampil_penyakit_jantung        = data_siap_tampil[8]
            self.Tampil_diabetes                = data_siap_tampil[9]
            self.Tampil_haemophilia             = data_siap_tampil[10]
            self.Tampil_hepatitis               = data_siap_tampil[11]
            self.Tampil_penyakit_lainya         = data_siap_tampil[12]
            self.Tampil_alergi_thd_obat_obatan  = data_siap_tampil[13]
            self.Tampil_alergi_thd_makanan      = data_siap_tampil[14]

            self.Tampil_occulusi                = data_siap_tampil[15]
            self.Tampil_torus_palantinus        = data_siap_tampil[16]
            self.Tampil_torus_mandibularis      = data_siap_tampil[17]
            self.Tampil_palatum                 = data_siap_tampil[18]
            self.Tampil_supernumerary_teeth     = data_siap_tampil[19]
            self.Tampil_diasterna               = data_siap_tampil[20]
            self.Tampil_gigi_anomali            = data_siap_tampil[21]
            self.Tampil_lain_lain               = data_siap_tampil[22]

            #=================[ PROSES TAMPIL GAMBAR ODONTO LAMA ] ===============
            #Encode Gambar Lalu Simpan dengan nama odonto_lama.gif
            target_id_tampil = self.fokus_data_id[0]
            with connection:

                cursor = connection.cursor()
                permisi = 'use pasien;'
                cursor.execute(permisi)

                cursor.execute("SELECT gambar FROM identitas WHERE id=%s"%(target_id_tampil))
                data = cursor.fetchone()[0]
                fout = open('odonto_lama.gif', 'wb')
                with fout:
                    fout.write(data)

            #Baca dan buka gambar odonto_lama.gif
            width = 680
            height = 295
            filename = 'odonto_lama.gif'
            image = Image.open(filename)
            im2 = image.resize((width,height), Image.ANTIALIAS)

            image_tk = ImageTk.PhotoImage(im2)
            
            #=================[ ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ] ===============
                
            #panggil rekam medis 
            self.ke_rekam_medis()
            self.input_identitas_kosongan()

            #Tampil gambar odontogram lama
            self.F_odonto_lama = Frame(self.pusat_rekam)
            self.F_odonto_lama.pack( side= LEFT, expand=YES)
            self.gambar_odonto_lama = Label(self.F_odonto_lama  ,bg='#00AACC' ,image=image_tk)
            self.gambar_odonto_lama.photo = image_tk
            self.gambar_odonto_lama.pack( side= LEFT, expand=YES)

            #Tampil data odontogram lama
            self.Entry_nama.insert(0,self.Tampil_nama)
            self.box_kelamin.insert(0,self.Tampil_kelamin)
            self.Entry_ttl.insert(0,self.Tampil_tempat_lahir)
            self.box_ttl_tanggal.insert(END,self.Tampil_tanggal_lahir)
            self.box_ttl_bulan.insert(END,self.Tampil_bulan_lahir)
            self.box_ttl_tahun.insert(END,self.Tampil_tahun_lahir)
            self.Entry_alamat.insert(0,self.Tampil_alamat)
            self.Entry_pekerjaan.insert(0,self.Tampil_pekerjaan)
            
            self.box_golongan_darah.insert(0,self.Tampil_golongan_darah)
            self.box_tekanan_darah_normal.insert(0,self.Tampil_tekanan_darah_normal)
            self.box_penyakit_jantung.insert(0,self.Tampil_penyakit_jantung)
            self.box_diabetes.insert(0,self.Tampil_diabetes)
            self.box_haemophilia.insert(0,self.Tampil_haemophilia)
            self.box_hepatitis.insert(0,self.Tampil_hepatitis)
            self.box_penyakit_lainya.insert(0,self.Tampil_penyakit_lainya)
            self.box_alergi_thd_obat_obatan.insert(0,self.Tampil_alergi_thd_obat_obatan)
            self.box_alergi_thd_makanan.insert(0,self.Tampil_alergi_thd_makanan)

            self.box_occulusi.insert(0,self.Tampil_occulusi)
            self.box_torus_palantinus.insert(0,self.Tampil_torus_palantinus)
            self.box_torus_mandibularis.insert(0,self.Tampil_torus_mandibularis)
            self.box_palatum.insert(0,self.Tampil_palatum)
            self.box_supernumerary_teeth.insert(0,self.Tampil_supernumerary_teeth)
            self.box_diasterna.insert(0,self.Tampil_diasterna)
            self.box_gigi_anomali.insert(0,self.Tampil_gigi_anomali)
            self.box_lain_lain.insert(0,self.Tampil_lain_lain)
        except IndexError:
             pesan.showerror('WARNING!!!',"Silahkan pilih data yang akan ditampilkan")
             
    def delete_data_lama_rekam(self ):
        ####______cari_data_selection_berdasar_id
        try:
            item = self.trvTabel_c.selection()[0]
            
            self.fokus_data=[]
            for row in (self.trvTabel_c.item(item,"values")):
                self.fokus_data.append(row)
            self.fokus_data_id=self.fokus_data[0:]
            print self.fokus_data_id[0]
            
             #_>__>_>_>_>_>_>___>_>_>_>>>__syntax
            connection = MySQLdb.connect(
                            host = 'localhost',
                            user = 'root',
                            passwd = '')  # create the connection

            cursor = connection.cursor()
            sql = "use pasien;"
            delete = 'DELETE FROM `identitas` WHERE `identitas`.`id`='+self.fokus_data_id[0]+';'
            cursor.execute(sql)
            cursor.execute(delete)
            connection.commit()
            connection.close()
            self.mencari_data_2()
        except IndexError:
             pesan.showerror('WARNING!!!',"Silahkan pilih data yang akan ditampilkan")
             
    def baru_data(self):
        self.rekam_medis_window.withdraw()
##        self.induk.deiconify()
##        self.induk.withdraw()
        self.rekam_medis()
                
if __name__ =='__main__':
    root = Tk()
    app = Data(root)
    root.mainloop()
    
##self.FmenuTrv.destroy()
