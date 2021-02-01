from tkinter import *
from PIL import ImageTk, Image
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.chrome.options import Options

#Selenium Ayarları
chrome_options = Options()
chrome_options.headless = True

#CHROME WEB DRİVER CHROME VERSİYON 88 İÇİN ÇALIŞMAKTADIR!
driver = webdriver.Chrome(executable_path="chromedriver.exe",options=chrome_options)

app = Tk()
app.geometry("930x640")
app.resizable(False,False)
app.title("Mentor")
app.iconphoto(False,PhotoImage(file='icon.png'))
C = Canvas(app,bg="blue", height=1080, width=1920)
img = Image.open("background.jpg")
img = img.resize((1920,1080))
img = ImageTk.PhotoImage(img)
C.create_image(960,530,image=img)
C.pack(side='top', fill='both', expand='yes')
x = IntVar()
x.set(0)
bolum_variable = IntVar()
hesaplandi = False
def sifirla():
    item_names = [turkce_dogru,turkce_yanlis,mat_dogru,mat_yanlis,sos_dogru,
    sos_yanlis,fen_dogru,fen_yanlis,mat2_dogru,mat2_yanlis,fizik_dogru,
    fizik_yanlis,kimya_dogru,kimya_yanlis,biyoloji_dogru,biyoloji_yanlis,edebiyat_dogru,
    edebiyat_yanlis,tarih1_dogru,tarih1_yanlis,cografya1_dogru,cografya1_yanlis,
    tarih2_dogru,tarih2_yanlis,cografya2_dogru,cografya2_yanlis,felsefe_dogru,
    felsefe_yanlis,din_dogru,din_yanlis,dil_dogru,dil_yanlis]

    for i in item_names:
        i.delete(first=0,last=len(i.get()))

def hedefAra():
    driver.get("https://www.google.com/search?q="+hedef_uni.get()+" "+hedef_bolum.get()+" "+"yök atlas")
    try:
        driver.find_element_by_xpath('//a[starts-with(@href,"https://yokatlas.yok.gov.tr/")]').click()
        sleep(.5)
        driver.find_element_by_xpath('//*[@id="headingOne"]/a/h4').click()
        sleep(.5)
        hedef_puan = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[7]/div/div[1]/div[2]/div/div/table[3]/tbody/tr[1]/td[2]').get_attribute("innerHTML")
        hedef_puan_label["text"] = "Hedef Puan: "+ hedef_puan
    except:
        hedef_puan_label["text"]="Hata! Tekrar Deneyin."
        degerlendirme_label["text"] = ""
    finally:
        if hesaplandi == True:
            if int(hedef_puan[:3])-int(yks_puan_dinamik["text"][:3]) <= 0:
                degerlendirme_label["fg"] = "green"
                degerlendirme_label["text"] = "Tebrikler, Hedefine Ulaştın!\nAynen Devam!"
            elif 0< int(hedef_puan[:3])-int(yks_puan_dinamik["text"][:3]) <= 30:
                degerlendirme_label["fg"] = "#07588f"
                degerlendirme_label["text"] = "Ha Gayret!\nHedefine Yaklaşıyorsun!"
            else:
                degerlendirme_label["fg"] = "red"
                degerlendirme_label["text"] ="Daha Çok Çalışman Lazım!\nBırakmak Yok!"

def hesapla():
    global hesaplandi
    try:
        driver.get('https://www.basarisiralamalari.com/tyt-yks-puan-hesaplama/')
        diploma_puan = float(diploma_entry.get())
        if x.get() == 1:
            diploma_puan = diploma_puan/2
    except:
        hesap_hata["text"] = "Bir Hata Oluştu!"
    #TYT Kısmı
    driver.find_element_by_xpath('//*[@id="diploma-notu"]').send_keys(str(diploma_puan))

    driver.find_element_by_xpath('//*[@id="tyt-tr-d"]').send_keys(turkce_dogru.get())
    driver.find_element_by_xpath('//*[@id="tyt-tr-y"]').send_keys(turkce_yanlis.get())

    driver.find_element_by_xpath('//*[@id="tyt-mat-d"]').send_keys(mat_dogru.get())
    driver.find_element_by_xpath('//*[@id="tyt-mat-y"]').send_keys(mat_yanlis.get())

    driver.find_element_by_xpath('//*[@id="tyt-sos-d"]').send_keys(sos_dogru.get())
    driver.find_element_by_xpath('//*[@id="tyt-sos-y"]').send_keys(sos_yanlis.get())

    driver.find_element_by_xpath('//*[@id="tyt-fen-d"]').send_keys(biyoloji_dogru.get())
    driver.find_element_by_xpath('//*[@id="tyt-fen-y"]').send_keys(biyoloji_yanlis.get())

    driver.find_element_by_xpath('//*[@id="btn_tyt"]').click()

    tytpuan =driver.find_element_by_css_selector('#tyt-puan-yer').get_attribute('value')

    tytsiralama = driver.find_element_by_css_selector('#tyt-siralama-yer').get_attribute('value')

    #AYT Kısmı
    driver.find_element_by_xpath('//*[@id="yks-mat-d"]').send_keys(mat2_dogru.get())
    driver.find_element_by_xpath('//*[@id="yks-mat-y"]').send_keys(mat2_yanlis.get())

    driver.find_element_by_xpath('//*[@id="yks-fiz-d"]').send_keys(fizik_dogru.get())
    driver.find_element_by_xpath('//*[@id="yks-fiz-y"]').send_keys(fizik_yanlis.get())

    driver.find_element_by_xpath('//*[@id="yks-kim-d"]').send_keys(kimya_dogru.get())
    driver.find_element_by_xpath('//*[@id="yks-kim-y"]').send_keys(kimya_yanlis.get())

    driver.find_element_by_xpath('//*[@id="yks-biy-d"]').send_keys(biyoloji_dogru.get())
    driver.find_element_by_xpath('//*[@id="yks-biy-y"]').send_keys(biyoloji_yanlis.get())

    driver.find_element_by_xpath('//*[@id="yks-ede-d"]').send_keys(edebiyat_dogru.get())
    driver.find_element_by_xpath('//*[@id="yks-ede-y"]').send_keys(edebiyat_yanlis.get())

    driver.find_element_by_xpath('//*[@id="yks-tar-1-d"]').send_keys(tarih1_dogru.get())
    driver.find_element_by_xpath('//*[@id="yks-tar-1-y"]').send_keys(tarih1_yanlis.get())

    driver.find_element_by_xpath('//*[@id="yks-cog-1-d"]').send_keys(cografya1_dogru.get())
    driver.find_element_by_xpath('//*[@id="yks-cog-1-y"]').send_keys(cografya1_yanlis.get())

    driver.find_element_by_xpath('//*[@id="yks-tar-2-d"]').send_keys(tarih2_dogru.get())
    driver.find_element_by_xpath('//*[@id="yks-tar-2-y"]').send_keys(tarih2_yanlis.get())

    driver.find_element_by_xpath('//*[@id="yks-cog-2-d"]').send_keys(cografya2_dogru.get())
    driver.find_element_by_xpath('//*[@id="yks-cog-2-y"]').send_keys(cografya2_yanlis.get())

    driver.find_element_by_xpath('//*[@id="yks-fel-d"]').send_keys(felsefe_dogru.get())
    driver.find_element_by_xpath('//*[@id="yks-fel-y"]').send_keys(felsefe_yanlis.get())

    driver.find_element_by_xpath('//*[@id="yks-din-d"]').send_keys(din_dogru.get())
    driver.find_element_by_xpath('//*[@id="yks-din-y"]').send_keys(din_yanlis.get())

    driver.find_element_by_xpath('//*[@id="yks-dil-d"]').send_keys(dil_dogru.get())
    driver.find_element_by_xpath('//*[@id="yks-dil-y"]').send_keys(dil_yanlis.get())
    
    #Sonuçlandırma Kısmı
    driver.find_element_by_xpath('//*[@id="singleContent"]/div[6]/div[1]/button').click()

    if bolum_variable.get()==1:
        ykspuan = driver.find_element_by_css_selector('#yks-sayisal-puan-yer').get_attribute('value')
        ykssiralama = driver.find_element_by_css_selector('#yks-sayisal-siralama-yer').get_attribute('value')

    elif bolum_variable.get()==2:
        ykspuan = driver.find_element_by_css_selector('#yks-esit-agirlik-puan-yer').get_attribute('value')
        ykssiralama = driver.find_element_by_css_selector('#yks-esit-agirlik-siralama-yer').get_attribute('value') 

    elif bolum_variable.get()==3:
        ykspuan = driver.find_element_by_css_selector('#yks-sozel-puan-yer').get_attribute('value')
        ykssiralama = driver.find_element_by_css_selector('#yks-sozel-siralama-yer').get_attribute('value')

    elif bolum_variable.get()==4:
        ykspuan = driver.find_element_by_css_selector('#yks-dil-puan-yer').get_attribute('value')
        ykssiralama = driver.find_element_by_css_selector('#yks-dil-siralama-yer').get_attribute('value')

    yks_puan_dinamik["text"] = ykspuan
    yks_siralama_label["text"] = " "+ ykssiralama

    tyt_puan_dinamik["text"] = tytpuan
    tyt_siralama_label["text"] = " "+ tytsiralama
    hesaplandi =True

#KİŞİSEL HEDEF DİZAYN
hedef_uni_label = Label(app, text='Hedef Üniversite:',font="Lucida 10 bold").place(x=10,y=130)
hedef_uni = Entry(app,width=20,fg="black")
hedef_uni.place(x=10,y=160)

hedef_bolum_label = Label(app, text='Hedef Bölüm:',font="Lucida 10 bold").place(x=10,y=190)
hedef_bolum = Entry(app,width=20,fg="black")
hedef_bolum.place(x=10,y=220)

ara_button = Button(app,text="Ara",font="Lucida 12 bold",command=hedefAra,bg="#808080",fg="#e6e6e6",width=9).place(x=20,y=250)

hedef_puan_label = Label(app,font="Lucida 10 bold")
hedef_puan_label.place(x=0,y=330)

degerlendirme_label = Label(app,font="Lucida 10 bold")
degerlendirme_label.place(x=0,y=390)
#GİRİŞ DİZAYN

gecensene_label = Label(app, text='Geçen sene bir bölüme yerleştim',font="Lucida 10 bold",bg="#f4f4f4").place(x=285,y=70)
gecensene_check = Checkbutton(app,variable=x,bg="#ececec").place(x=260,y=70)
diploma_label = Label(app, text='Diploma Notu:',font="Lucida 10 bold").place(x=260,y=25)
diploma_entry= Entry(app,width=21,bg="#808080",fg="white",justify="center")
diploma_entry.place(x=370,y=25)
#TYT DİZAYN


turkce_label = Label(app, text='Türkçe',font="Lucida 10 bold").place(x=310,y=150)

turkce_dogru =Entry(app,width=20,bg="#808080",fg="white",justify="center")
turkce_dogru.place(x=270,y=200)

turkce_yanlis =Entry(app,width=20,bg="#808080",fg="white",justify="center")
turkce_yanlis.place(x=270,y=250)

mat_label = Label(app, text='Matematik',font="Lucida 10 bold").place(x=455,y=150)

mat_dogru =Entry(app,width=20,bg="#808080",fg="white",justify="center")
mat_dogru.place(x=430,y=200)

mat_yanlis =Entry(app,width=20,bg="#808080",fg="white",justify="center")
mat_yanlis.place(x=430,y=250)

sos_label = Label(app, text='Sosyal Bilimler',font="Lucida 10 bold",bg="#f9f9f9").place(x=600,y=150)

sos_dogru =Entry(app,width=20,bg="#808080",fg="white",justify="center")
sos_dogru.place(x=590,y=200)

sos_yanlis =Entry(app,width=20,bg="#808080",fg="white",justify="center")
sos_yanlis.place(x=590,y=250)

fen_label = Label(app, text="Fen Bilimleri",font="Lucida 10 bold").place(x=765,y=150)

fen_dogru =Entry(app,width=20,bg="#808080",fg="white",justify="center")
fen_dogru.place(x=750,y=200)

fen_yanlis =Entry(app,width=20,bg="#808080",fg="white",justify="center")
fen_yanlis.place(x=750,y=250)

tyt_dogru_label = Label(app, text='Doğru:',font="Lucida 10 bold",bg="#e6e6e6").place(x=190,y=200)

tyt_yanlis_label = Label(app, text='Yanlış:',font="Lucida 10 bold",bg="#e0e0e0").place(x=190,y=250)

#AYT DİZAYN
mat2_label = Label(app, text='Matematik',font="Lucida 10 bold",bg="#e5e5e5").place(x=190,y=350)

mat2_dogru =Entry(app,width=15,bg="#808080",fg="white",justify="center")
mat2_dogru.place(x=270,y=350)

mat2_yanlis =Entry(app,width=15,bg="#808080",fg="white",justify="center")
mat2_yanlis.place(x=400,y=350)

fizik_label = Label(app, text='Fizik',font="Lucida 10 bold",bg="#e4e4e4").place(x=190,y=385)

fizik_dogru =Entry(app,width=15,bg="#808080",fg="white",justify="center")
fizik_dogru.place(x=270,y=385)

fizik_yanlis =Entry(app,width=15,bg="#808080",fg="white",justify="center")
fizik_yanlis.place(x=400,y=385)

kimya_label = Label(app, text='Kimya',font="Lucida 10 bold").place(x=190,y=420)

kimya_dogru =Entry(app,width=15,bg="#808080",fg="white",justify="center")
kimya_dogru.place(x=270,y=420)

kimya_yanlis =Entry(app,width=15,bg="#808080",fg="white",justify="center")
kimya_yanlis.place(x=400,y=420)

biyoloji_label = Label(app, text='Biyoloji',font="Lucida 10 bold",bg="#fafafa").place(x=190,y=455)

biyoloji_dogru =Entry(app,width=15,bg="#808080",fg="white",justify="center")
biyoloji_dogru.place(x=270,y=455)

biyoloji_yanlis =Entry(app,width=15,bg="#808080",fg="white",justify="center")
biyoloji_yanlis.place(x=400,y=455)

edebiyat_label = Label(app, text='Edebiyat',font="Lucida 10 bold",bg="#f9f9f9").place(x=190,y=490)

edebiyat_dogru =Entry(app,width=15,bg="#808080",fg="white",justify="center")
edebiyat_dogru.place(x=270,y=490)

edebiyat_yanlis =Entry(app,width=15,bg="#808080",fg="white",justify="center")
edebiyat_yanlis.place(x=400,y=490)

tarih1_label = Label(app, text='Tarih-1',font="Lucida 10 bold").place(x=190,y=525)

tarih1_dogru =Entry(app,width=15,bg="#808080",fg="white",justify="center")
tarih1_dogru.place(x=270,y=525)

tarih1_yanlis =Entry(app,width=15,bg="#808080",fg="white",justify="center")
tarih1_yanlis.place(x=400,y=525)

cografya1_label = Label(app, text='Coğrafya-1',font="Lucida 10 bold").place(x=510,y=350)

cografya1_dogru =Entry(app,width=15,bg="#808080",fg="white",justify="center")
cografya1_dogru.place(x=619,y=350)

cografya1_yanlis =Entry(app,width=15,bg="#808080",fg="white",justify="center")
cografya1_yanlis.place(x=749,y=350)

tarih2_label = Label(app, text='Tarih-2',font="Lucida 10 bold").place(x=510,y=385)

tarih2_dogru =Entry(app,width=15,bg="#808080",fg="white",justify="center")
tarih2_dogru.place(x=619,y=385)

tarih2_yanlis =Entry(app,width=15,bg="#808080",fg="white",justify="center")
tarih2_yanlis.place(x=749,y=385)

cografya2_label = Label(app, text='Coğrafya-2',font="Lucida 10 bold").place(x=510,y=420)

cografya2_dogru =Entry(app,width=15,bg="#808080",fg="white",justify="center")
cografya2_dogru.place(x=619,y=420)

cografya2_yanlis =Entry(app,width=15,bg="#808080",fg="white",justify="center")
cografya2_yanlis.place(x=749,y=420)

felsefe_label = Label(app, text='Felsefe',font="Lucida 10 bold").place(x=510,y=455)

felsefe_dogru =Entry(app,width=15,bg="#808080",fg="white",justify="center")
felsefe_dogru.place(x=619,y=455)

felsefe_yanlis =Entry(app,width=15,bg="#808080",fg="white",justify="center")
felsefe_yanlis.place(x=749,y=455)

din_label = Label(app, text='Din Kültürü',font="Lucida 10 bold").place(x=510,y=490)

din_dogru =Entry(app,width=15,bg="#808080",fg="white",justify="center")
din_dogru.place(x=619,y=490)

din_yanlis =Entry(app,width=15,bg="#808080",fg="white",justify="center")
din_yanlis.place(x=749,y=490)

dil_label = Label(app, text='Yabancı Dil',font="Lucida 10 bold").place(x=510,y=525)

dil_dogru =Entry(app,width=15,bg="#808080",fg="white",justify="center")
dil_dogru.place(x=619,y=525)

dil_yanlis =Entry(app,width=15,bg="#808080",fg="white",justify="center")
dil_yanlis.place(x=749,y=525)

ayt_dogru_label = Label(app, text='Doğru',font="Lucida 10 bold",bg="#f3f3f3").place(x=295,y=300)

ayt_yanlis_label = Label(app, text='Yanlış',font="Lucida 10 bold",bg="#fcfcfc").place(x=425,y=300)

ayt_dogru_label1 = Label(app, text='Doğru',font="Lucida 10 bold",bg="#fdfdfd").place(x=645,y=300)

ayt_yanlis_label1 = Label(app, text='Yanlış',font="Lucida 10 bold",bg="#fefefe").place(x=775,y=300)

#SONUÇ DİZAYN
puan_label =  Label(app, text='PUAN',font="Lucida 12 bold",bg="#fbfbfb").place(x=657,y=10)  
siralama_label =  Label(app, text='SIRALAMA',font="Lucida 12 bold",bg="#f5f5f5").place(x=780,y=10)

tyt_puan_label = Label(app, text='TYT -->',font="Lucida 12 bold",bg="#fdfdfd").place(x=550,y=40)

tyt_puan_dinamik = Label(app,font="Lucida 12 bold",bg="#f5f5f5",justify="center")
tyt_puan_dinamik.place(x=650,y=40)
tyt_siralama_label = Label(app,font="Lucida 12 bold",bg="#fbfbfb",justify="center")
tyt_siralama_label.place(x=790,y=40)

yks_puan_label = Label(app, text='YKS -->',font="Lucida 12 bold",bg="#f7f7f7").place(x=550,y=70)

yks_puan_dinamik = Label(app,font="Lucida 12 bold",bg="#f5f5f5",justify="center")
yks_puan_dinamik.place(x=650,y=70)
yks_siralama_label = Label(app,font="Lucida 12 bold",bg="#fbfbfb",justify="center")
yks_siralama_label.place(x=790,y=70)

say_radio = Radiobutton(app,text="SAY",font="Lucida 9 bold",variable=bolum_variable,value=1)
say_radio.place(x=290,y=110)
say_radio.select() #Varsayılan olarak SAY seçilmesi için ekliyoruz.

ea_radio = Radiobutton(app,text="EA",font="Lucida 9 bold",variable=bolum_variable,value=2)
ea_radio.place(x=340,y=110)

soz_radio = Radiobutton(app,text="SÖZ",font="Lucida 9 bold",variable=bolum_variable,value=3)
soz_radio.place(x=380,y=110)

dil_radio = Radiobutton(app,text="DİL",font="Lucida 9 bold",variable=bolum_variable,value=4)
dil_radio.place(x=430,y=110)


hesapla_button = Button(app,text="Hesapla",font="Lucida 12 bold",command=hesapla,bg="#808080",fg="#e6e6e6").place(x=500,y=580)
sıfırla_button = Button(app,text="X",font="Lucida 12 bold",bg="#808080",fg="#e6e6e6",command=sifirla).place(x=580,y=580)
hesap_hata = Label(app,font="Lucida 11 bold",bg="#e8e8e8")
hesap_hata.place(x=380,y=585)
#Uygulamanın çalışması için.
app.mainloop()