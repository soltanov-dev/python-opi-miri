
# from abc import ABC, abstractmethod

# def __init__(self,ad):
#     self.ad=ad
#     print(f"{self.ad} aparat hazirdir")
#     @abstractmethod
#     def mehsul_hazirlandi(self):
#         pass
#     @abstractmethod

#     def _bisir(self):
#         pass
#     @abstractmethod
#     def _fincani_doldur(self):
#         pass
#     def icki_hazirla(self):
#         self._fincani_doldur()
#         self._bisir()
#         self.mehsul_hazirlandi(self,boyuk_fincan=True)
#         olcu=boyuk_fincan else "kicik_fincan"
# print(f"{self.ad} {olcu} hazirlandi")
# print(f"{self.ad}hazirdir nus olsun")


# class KofeAparati(IckiAparati):
#     def _mehsul_hazirla(self):
#         print("kofe denleri uyudur")

#     def _bisir(self):
#         print("kofe demlenir")

#     def _fincan_doldur(self):
#         print("Fincana tokulur")


#         class cayaparati(IckiAparati):
#     def _mehsul_hazirla(self):
#         print("cay denleri uyudur")

#     def _bisir(self):
#         print("cay demlenir")

#     def _fincan_doldur(self):
#         print("Fincana tokulur")


#         class kakoaparati(IckiAparati):
#     def _mehsul_hazirla(self):
#         print("kakou denleri uyudur")

#     def _bisir(self):
#         print("kakou demlenir")

#     def _fincan_doldur(self):
#         print("Fincana tokulur")

#         kofe_aparati = KofeAparati("Espresso")
# cay_aparati = CayAparati("Early Grey")
# kakao_aparati = KakaoAparati("Hot chocolate")


# kofe_aparati.icki_hazirla(boyuk_olsun=True)
# cay_aparati.icki_hazirla()
# kakao_aparati.icki_hazirla()




# class isci:
#     sirket_adi="MIVA"
#     def __init__(self,ad,soyad,iscinin_id,iscinin_ise_qebul_tarixi):
#         self.__ad = ad
#         self.__soyad = soyad
#         self.__iscinin_id = iscinin_id
#         self.__iscinin_ise_qebul_tarixi = iscinin_ise_qebul_tarixi
#         self.__aktiv=True
# print(f"isci yaradildi: {self.__ad} {self.__soyad} ")

# def tam_ad(self):
#     return f"{self.__ad} {self.__soyad}"
# def ise_basla(self):
#     print(f"{self.tam_ad()}ise basladi")

#     def ise_bitir(self):
#        self.__aktiv=False
#        print(f"{self.tam_ad()}ise bitirdi")

#        def melumatlar_goster(self):
#            print(f"isci adi: {self.__ad} {self.__soyad}")
#            print(f"isci id: {self.__iscinin_id}")
#            print(f"isci ise qebul tarixi: {self.__iscinin_ise_qebul_tarixi}")
#            print(f"isci aktivdir: {self.__aktiv}")

#            class proqramci(isci):
#                def __init__(self,ad,soyad,iscinin_id,iscinin_ise_qebul_tarixi,proqramlasdirma_dilleri):
#                 super().__init__(ad,soyad,iscinin_id,iscinin_ise_qebul_tarixi)
#                 self.__proqramlasdirma_dilleri=proqramlasdirma_dilleri
#                 self.__tecrube_ili=tecrube_ili
#                 self.proyektler=[]
#                 def kod_yaz(self,proyekt_adi):
#                     self.proyektler.append(proyekt_adi)
#                     print(f"{self.tam_ad()} {proyekt_adi} proyektinde kod yazir")
#                     self.proyektler.append(proyekt_adi)
#                def melumat_goster(self):
#                    super().melumat_goster()
#                  print(f"vezife: proqramci")
#                print(f"proqramlasdirma dilleri: {self.__proqramlasdirma_dilleri}")
#                print(f"tecrube ili: {self.__tecrube_ili}")
#                print(f"proyektler: {self.proyektler}")
#                print(f"proyektler: {len(self.proyektler)} eded")

#                class menecer(isci):
#                    def __init__(self,ad,soyad,iscinin_id,iscinin_ise_qebul_tarixi,komanda_hecmi):
#     super().__init__(ad,soyad,iscinin_id,iscinin_ise_qebul_tarixi)
#     self.komanda_hecmi=komanda_hecmi
#     self.komanda=[]

# def komandaya_elave_et(self,isci):
#     if(len(self.komanda)<self.komanda_hecmi):
#         self.komanda.append(isci)
#         print(f"{isci.ad} ... komandasina elave edildi.")  
#     else:
#         print("Komanda hecmi doludur.")

#         def gorus_teskil_et(self,tarix):
#             print(f"{self.tam_ad()} {tarix} tarixinde gorus teskil etdi.")
#             print(f"istirak edenler:")
#             for i in self.komanda:
#                 print(f"  - {i.tam_ad()}")
#                 def melumat_goster(self):
#                     super().melumat_goster()
#                     print(f"vezife: menecer")
#                     print(f"komanda hecmi: {self.komanda_hecmi}")
#                     print(f"komanda:")
#                     for i in self.komanda:
#                         print(f"  - {i.tam_ad()}")

#                         class dizayner(isci):
#                             def __init__(self,ad,soyad,iscinin_id,iscinin_ise_qebul_tarixi, dizayn_proqramlari):
#                                 super().__init__(ad,soyad,iscinin_id,iscinin_ise_qebul_tarixi)
#                                 self.__dizayn_proqramlari=dizayn_proqramlari
#                                 self.__tecrube_ili=tecrube_ili
#                                 self.proyektler=[]
#                             def dizayn_et(self,proyekt_adi):
#                                 self.proyektler.append(proyekt_adi)
#                                 print(f"{self.tam_ad()} {proyekt_adi} proyektinde dizayn edir")
#                             def melumat_goster(self):
#                                 super().melumat_goster()
#                                 print(f"vezife: dizayner")
#                                 print(f"dizayn proqramlari: {self.__dizayn_proqramlari}")
#                                 print(f"tecrube ili: {self.__tecrube_ili}")
#                                 print(f"proyektler: {self.proyektler}")
#                                 print(f"proyektler: {len(self.proyektler)} eded")

#                                 proqramci1=proqramci("Ali","Aliyev",1,"2020-01-01","Python,Java",5)
#                                 proqramci2=proqramci("Veli","Veliev",2,"2021-01-01","C++,JavaScript",3)
#                                 menecer1=menecer("Nigar","Nigarova",3,"2019-01-01",5)
#                                 dizayner1=dizayner("Aysel","Ayselova",4,"2022-01-01","Photoshop,Illustrator",2)

#                                 programci1.kod_yaz("Proyekt1")
#                                 programci2.kod_yaz("Proyekt2")
#                                 dizayner1.dizayn_et("Proyekt1")
#                                 menecer1.komandaya_elave_et(proqramci1)
#                                 menecer1.komandaya_elave_et(proqramci2)
#                                 menecer1.komandaya_elave_et(dizayner1)

#                                 menecer1.gorus_teskil_et("2023-01-01")
#                                 programci1.melumat_goster()
#                                 programci2.melumat_goster()
#                                 dizayner1.melumat_goster()


# from abc import ABC, abstractmethod


# class odenis_yonetimi(ABC):
#     def __init__(self, sahibi):
#         self.sahibi = sahibi
#         self.balans = 0.0

#     @abstractmethod
#     def pul_yatir(self, mebleg):
#         pass

#     @abstractmethod
#     def pul_cek(self, mebleg):
#         pass

#     @abstractmethod
#     def balans_goster(self):
#         pass


# class kredit_karti(odenis_yonetimi):
#     def __init__(self, sahibi, limit):
#         super().__init__(sahibi)
#         self.limit = limit
#         self.borclu_miqdar = 0.0

#     def pul_yatir(self, mebleg):
#         if mebleg > 0:
#             self.borclu_miqdar -= mebleg
#             if self.borclu_miqdar < 0:
#                 self.borclu_miqdar = 0
#             print(f"{mebleg} AZN yatirildi. borc miqdari: {self.borclu_miqdar} AZN")
#         else:
#             print("sef mebleg. musbet mebleg daxil edin")

#     def pul_cek(self, mebleg):
#         if mebleg <= 0:
#             print("sef mebleg")
#             return
#         if self.borclu_miqdar + mebleg > self.limit:
#             print(f"limit asildi. movcud limit: {self.limit - self.borclu_miqdar} AZN")
#             return
#         self.borclu_miqdar += mebleg
#         print(f"{mebleg} AZN cekildi. borc miqdari: {self.borclu_miqdar} AZN")

#     def balans_goster(self):
#         print(f"sahibi: {self.sahibi}, borc miqdari: {self.borclu_miqdar} AZN, limit: {self.limit} AZN")


# class kriptovalyuta_cuzdani(odenis_yonetimi):
#     def pul_yatir(self, mebleg):
#         if mebleg > 0:
#             self.balans += mebleg
#             print(f"{mebleg} AZN yatirildi. yeni balans: {self.balans} AZN")
#         else:
#             print("sef mebleg. musbet mebleg daxil edin")

#     def pul_cek(self, mebleg):
#         if mebleg <= 0:
#             print("sef mebleg")
#             return
#         if mebleg > self.balans:
#             print(f"balans kifayet qeder deyil. movcud balans: {self.balans} AZN")
#             return
#         self.balans -= mebleg
#         print(f"{mebleg} AZN cekildi. yeni balans: {self.balans} AZN")

#     def balans_goster(self):
#         print(f"sahibi: {self.sahibi}, balans: {self.balans} AZN")


# class nagd_pul(kriptovalyuta_cuzdani):
#     """Nagd pul de balansla isleyir, buna gore eyni məntiqi istifade edir."""
#     pass


# class mobil_odeme(kriptovalyuta_cuzdani):
#     pass


# def odemeni_proses_et(hesab, mebleg):
#     print(f"{mebleg} AZN odemeni proses edir...")
#     hesab.pul_cek(mebleg)
#     print(f"{mebleg} AZN odeme proses edildi.")


# kart = kredit_karti("Ali", limit=5000)
# nagd = nagd_pul("Veli")
# mobil = mobil_odeme("Nigar")
# kriptovalyuta = kriptovalyuta_cuzdani("Aysel")

# nagd.pul_yatir(100)
# mobil.pul_yatir(100)
# kriptovalyuta.pul_yatir(100)

# odemeni_proses_et(kart, 100)
# print("----")
# odemeni_proses_et(nagd, 50)
# print("----")
# odemeni_proses_et(mobil, 75)
# print("----")
# odemeni_proses_et(kriptovalyuta, 25)

# class Heyvan:
#     def __init__(self, ad):
#         self.ad = ad

#     def ye(self):
#         print(f"{self.ad} yemək yeyir")


# class It(Heyvan):
#     def __init__(self, ad, cins):
#         super().__init__(ad)
#         self.cins = cins

#     def ye(self):
#         super().ye()
#         print(f"{self.ad} quyruğunu tərpədir")
#         it = It("Rex", "Alman Ovçarkası")
#         it.ye()

#         class Baba:
#     def salamla(self):
#         print("Baba: Salam balaca")


# class Ata(Baba):
#     def salamla(self):
#         print("Ata: Salam oğlum")


# class Usaq(Ata):
#     pass 


# usaq = Usaq()
# usaq.salamla()


# class Ana:
#     def melumat(self):
#         print("Ana: Yemek hazir edir")


# class Ata:
#     def melumat(self):
#         print("Ata: Pul verdim")


# class Usaq(Ana, Ata):  
#     pass


# usaq = Usaq("ramin".15)
# usaq.melumat(ad="Ramin", yas=15) 

# d,c,a,y,x object
# class Insan:                     
#     def melumat(self):
#         print("Insan")


# class Ana(Insan):                
#     def melumat(self):
#         print("Ana: Yemek hazir edir")
#         super().melumat()


# class Ata(Insan):                
#     def melumat(self):
#         print("Ata: Pul verdim")
#         super().melumat()


# class Usaq(Ana, Ata):             
#     def __init__(self, ad, yas):
#         self.ad = ad
#         self.yas = yas

#     def melumat(self):
#         print(f"Usaq: {self.ad}, {self.yas} yasinda")
#         super().melumat()


# usaq = Usaq("Ramin", 15)
# usaq.melumat()

# print([c.__name__ for c in Usaq.__mro__])



# from abc import ABC, abstractmethod

# def __init__(self,ad):
#     self.ad=ad
#     print(f"{self.ad} aparat hazirdir")
#     @abstractmethod
#     def mehsul_hazirlandi(self):
#         pass
#     @abstractmethod

#     def _bisir(self):
#         pass
#     @abstractmethod
#     def _fincani_doldur(self):
#         pass
#     def icki_hazirla(self):
#         self._fincani_doldur()
#         self._bisir()
#         self.mehsul_hazirlandi(self,boyuk_fincan=True)
#         olcu=boyuk_fincan else "kicik_fincan"
# print(f"{self.ad} {olcu} hazirlandi")
# print(f"{self.ad}hazirdir nus olsun")


# class KofeAparati(IckiAparati):
#     def _mehsul_hazirla(self):
#         print("kofe denleri uyudur")

#     def _bisir(self):
#         print("kofe demlenir")

#     def _fincan_doldur(self):
#         print("Fincana tokulur")


#         class cayaparati(IckiAparati):
#     def _mehsul_hazirla(self):
#         print("cay denleri uyudur")

#     def _bisir(self):
#         print("cay demlenir")

#     def _fincan_doldur(self):
#         print("Fincana tokulur")


#         class kakoaparati(IckiAparati):
#     def _mehsul_hazirla(self):
#         print("kakou denleri uyudur")

#     def _bisir(self):
#         print("kakou demlenir")

#     def _fincan_doldur(self):
#         print("Fincana tokulur")

#         kofe_aparati = KofeAparati("Espresso")
# cay_aparati = CayAparati("Early Grey")
# kakao_aparati = KakaoAparati("Hot chocolate")


# kofe_aparati.icki_hazirla(boyuk_olsun=True)
# cay_aparati.icki_hazirla()
# kakao_aparati.icki_hazirla()

