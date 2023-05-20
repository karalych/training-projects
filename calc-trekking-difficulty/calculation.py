import tkinter as tk
import numpy as np

from win_position import Win_position
from init_ui_and_param import init_variables_and_constants, init_ui


class Сalculation(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        init_variables_and_constants(self)
        init_ui(self)
        self.kilometry_za_vodu = 0

    def change_k_avt(self, x):
        if self.k_avt_button.get() == 1:
            x = 1
        elif self.k_avt_button.get() == 2:
            x = 0.7
        elif self.k_avt_button.get() == 3:
            x = 0.5
        elif self.k_avt_button.get() == 4:
            x = 0.2
        return x

    def proverka_kategorii(self, t, lenght, b, korotkii):
        proverka = False
        check_slojnodti = False
        xarakteristika = self.xarakteristiki[int(self.zayavka.get())]
        if t >= xarakteristika[0] and lenght >= xarakteristika[1] and \
                b >= xarakteristika[4]:
            proverka = True
        elif korotkii and t >= xarakteristika[0] - xarakteristika[6] and \
                lenght >= xarakteristika[1] and b >= xarakteristika[4]:
            proverka = True
        elif korotkii and t >= xarakteristika[0] and \
                lenght >= 3 * xarakteristika[1] / 4 and b >= xarakteristika[4]:
            proverka = True
            check_slojnodti = True
        return proverka, check_slojnodti

    def clicked(self):
        if self.luzer.get():
            if self.etr_voda_nk.get() != '' or self.etr_voda_1.get() != '' or \
                self.etr_voda_2.get() != '' or self.etr_voda_3.get() != '' or \
                    self.etr_voda_4.get() != '':
                self.voda_window()
            elif self.etr_voda_nk.get() == '' and self.etr_voda_1.get() == '' and \
                self.etr_voda_2.get() == '' and self.etr_voda_3.get() == '' and \
                    self.etr_voda_4.get() == '':
                self.kilometry_za_vodu = 0
                tk.messagebox.showwarning('Предупреждение',
                                          'Вы не указали к.т. водного участка')
        else:
            self.kilometry_za_vodu = 0
            self.proverka()

    def proverka(self):
        if self.etr_dni.get() != '':
            self.dni = int(self.etr_dni.get())
        else:
            self.dni = 0

        if self.etr_kilometry.get() != '':
            self.kilometry = float(self.etr_kilometry.get())
        else:
            self.kilometry = 0

        if self.etr_perepad.get() != '':
            self.perepad = int(self.etr_perepad.get())
        else:
            self.perepad = 0

        if self.etr_pereprava_nk.get() != '':
            self.prepaytstviay[0, 0] = int(self.etr_pereprava_nk.get())
        else:
            self.prepaytstviay[0, 0] = 0

        if self.etr_pereprava_1a.get() != '':
            self.prepaytstviay[1, 0] = int(self.etr_pereprava_1a.get())
        else:
            self.prepaytstviay[1, 0] = 0

        if self.etr_pereprava_1b.get() != '':
            self.prepaytstviay[2, 0] = int(self.etr_pereprava_1b.get())
        else:
            self.prepaytstviay[2, 0] = 0

        if self.etr_pereprava_2a.get() != '':
            self.prepaytstviay[3, 0] = int(self.etr_pereprava_2a.get())
        else:
            self.prepaytstviay[3, 0] = 0

        if self.etr_pereprava_2b.get() != '':
            self.prepaytstviay[4, 0] = int(self.etr_pereprava_2b.get())
        else:
            self.prepaytstviay[4, 0] = 0

        if self.etr_pereval_nk.get() != '':
            self.prepaytstviay[0, 1] = int(self.etr_pereval_nk.get())
        else:
            self.prepaytstviay[0, 1] = 0

        if self.etr_pereval_1a.get() != '':
            self.prepaytstviay[1, 1] = int(self.etr_pereval_1a.get())
        else:
            self.prepaytstviay[1, 1] = 0

        if self.etr_pereval_1b.get() != '':
            self.prepaytstviay[2, 1] = int(self.etr_pereval_1b.get())
        else:
            self.prepaytstviay[2, 1] = 0

        if self.etr_pereval_2a.get() != '':
            self.prepaytstviay[3, 1] = int(self.etr_pereval_2a.get())
        else:
            self.prepaytstviay[3, 1] = 0

        if self.etr_pereval_2b.get() != '':
            self.prepaytstviay[4, 1] = int(self.etr_pereval_2b.get())
        else:
            self.prepaytstviay[4, 1] = 0

        if self.etr_pereval_v.get() != '':
            self.prepaytstviay[5, 1] = int(self.etr_pereval_v.get())
        else:
            self.prepaytstviay[5, 1] = 0

        if self.etr_vershina_nk.get() != '':
            self.prepaytstviay[0, 2] = int(self.etr_vershina_nk.get())
        else:
            self.prepaytstviay[0, 2] = 0

        if self.etr_vershina_1a.get() != '':
            self.prepaytstviay[1, 2] = int(self.etr_vershina_1a.get())
        else:
            self.prepaytstviay[1, 2] = 0

        if self.etr_vershina_1b.get() != '':
            self.prepaytstviay[2, 2] = int(self.etr_vershina_1b.get())
        else:
            self.prepaytstviay[2, 2] = 0

        if self.etr_vershina_2a.get() != '':
            self.prepaytstviay[3, 2] = int(self.etr_vershina_2a.get())
        else:
            self.prepaytstviay[3, 2] = 0

        if self.etr_vershina_v.get() != '':
            self.prepaytstviay[5, 2] = int(self.etr_vershina_v.get())
        else:
            self.prepaytstviay[5, 2] = 0

        if self.etr_travers_nk.get() != '':
            self.prepaytstviay[0, 3] = int(self.etr_travers_nk.get())
        else:
            self.prepaytstviay[0, 3] = 0

        if self.etr_travers_1a.get() != '':
            self.prepaytstviay[1, 3] = int(self.etr_travers_1a.get())
        else:
            self.prepaytstviay[1, 3] = 0

        if self.etr_travers_1b.get() != '':
            self.prepaytstviay[2, 3] = int(self.etr_travers_1b.get())
        else:
            self.prepaytstviay[2, 3] = 0

        if self.etr_travers_2a.get() != '':
            self.prepaytstviay[3, 3] = int(self.etr_travers_2a.get())
        else:
            self.prepaytstviay[3, 3] = 0

        if self.etr_travers_v.get() != '':
            self.prepaytstviay[5, 3] = int(self.etr_travers_v.get())
        else:
            self.prepaytstviay[5, 3] = 0

        if self.etr_kanyon_nk.get() != '':
            self.prepaytstviay[0, 4] = int(self.etr_kanyon_nk.get())
        else:
            self.prepaytstviay[0, 4] = 0

        if self.etr_kanyon_1a.get() != '':
            self.prepaytstviay[1, 4] = int(self.etr_kanyon_1a.get())
        else:
            self.prepaytstviay[1, 4] = 0

        if self.etr_kanyon_1b.get() != '':
            self.prepaytstviay[2, 4] = int(self.etr_kanyon_1b.get())
        else:
            self.prepaytstviay[2, 4] = 0

        if self.etr_kanyon_2a.get() != '':
            self.prepaytstviay[3, 4] = int(self.etr_kanyon_2a.get())
        else:
            self.prepaytstviay[3, 4] = 0

        if self.etr_kanyon_2b.get() != '':
            self.prepaytstviay[4, 4] = int(self.etr_kanyon_2b.get())
        else:
            self.prepaytstviay[4, 4] = 0

        if self.etr_voda_nk.get() != '':
            self.prepaytstviay[0, 5] = int(self.etr_voda_nk.get())
        else:
            self.prepaytstviay[0, 5] = 0

        if self.etr_voda_1.get() != '':
            self.prepaytstviay[1, 5] = int(self.etr_voda_1.get())
        else:
            self.prepaytstviay[1, 5] = 0

        if self.etr_voda_2.get() != '':
            self.prepaytstviay[2, 5] = int(self.etr_voda_2.get())
        else:
            self.prepaytstviay[2, 5] = 0

        if self.etr_voda_3.get() != '':
            self.prepaytstviay[3, 5] = int(self.etr_voda_3.get())
        else:
            self.prepaytstviay[3, 5] = 0

        if self.etr_voda_4.get() != '':
            self.prepaytstviay[4, 5] = int(self.etr_voda_4.get())
        else:
            self.prepaytstviay[4, 5] = 0

        if self.combo_rayon.get() != '':
            self.k_tr = self.slovar_rayon[str(self.combo_rayon.get())][0]
            self.k_geogr = self.slovar_rayon[str(self.combo_rayon.get())][1]

        self.lbl_verdikt.destroy()
        self.lbl_itog2.destroy()
        self.lbl_itog3.destroy()
        self.lbl_LP2.destroy()
        self.lbl_PP2.destroy()
        self.lbl_R2.destroy()

        xarakteristika = self.xarakteristiki[int(self.zayavka.get())]
        bally = self.bally_norm[int(self.zayavka.get())]

        LP_bally = 0
        slojnost = False

        i = 0
        for key in bally:
            perebor = False
            for j in range(len(bally[key])):
                if bally[key][j][0] != 0 and \
                        self.prepaytstviay[j, i] <= bally[key][j][0]:
                    LP_bally += bally[key][j][1] / bally[key][j][0] * \
                            self.prepaytstviay[j, i]
                if bally[key][j][0] != 0 and \
                        self.prepaytstviay[j, i] > bally[key][j][0]:
                    LP_bally += bally[key][j][1]
                    slojnost = True
                    perebor = True

            cena = []
            for j in range(len(bally[key])):
                if bally[key][j][0] != 0:
                    cena.append(bally[key][j][1] / bally[key][j][0])
                else:
                    cena.append(0)

            n = 0
            while any(cena[n:]) > 0:
                n += 1

            if any(self.prepaytstviay[n:, i]) > 0 or perebor:
                kolichestvo = []
                for k in range(5):
                    kolichestvo.append(int(bally[key][k][0]))
                kolichestvo.append(0)

                lishnee = self.prepaytstviay[:, i] - kolichestvo[:]
                for k in range(len(lishnee)):
                    if lishnee[k] < 0:
                        lishnee[k] = 0
                lishnee = np.append(lishnee, 0)

                ostatok = []
                for j in range(n):
                    if int(bally[key][j][0]) < self.prepaytstviay[j, i]:
                        ostatok.append(0)
                    elif int(bally[key][j][0]) >= self.prepaytstviay[j, i]:
                        ostatok.append(
                            int(bally[key][j][0] - self.prepaytstviay[j, i])
                            )
                while j <= 5:
                    ostatok.append(0)
                    j += 1
                ostatok.reverse()

                dobavka = [0] * len(ostatok)
                for j in range(len(ostatok)):
                    if ostatok[j] == 0 and lishnee[-j-1] == 0:
                        continue
                    elif ostatok[j] != 0 and lishnee[-j-1] == 0:
                        continue
                    elif ostatok[j] == 0 and lishnee[-j-1] != 0:
                        if j != 6:
                            lishnee[-j-2] += lishnee[-j-1]
                            lishnee[-j-1] = 0

                    elif ostatok[j] != 0 and lishnee[-j-1] != 0:
                        if ostatok[j] >= lishnee[-j-1]:
                            dobavka[-j-1] = lishnee[-j-1]
                        elif ostatok[j] < lishnee[-j-1]:
                            dobavka[-j-1] += ostatok[j]
                            lishnee[-j-1] += lishnee[-j-1] - ostatok[j]

                for j in range(len(bally[key])):
                    if bally[key][j][0] != 0:
                        LP_bally += cena[j] * dobavka[j]

            i += 1

        if LP_bally > xarakteristika[2]:
            LP_bally = xarakteristika[2]

        if self.kilometry_za_vodu != 0:
            if self.kilometry_za_vodu <= xarakteristika[1] * 1 / 4:
                self.kilometry += self.kilometry_za_vodu
            else:
                self.kilometry += xarakteristika[1] * 1 / 4

        PP_bally = round(
            self.k_tr * xarakteristika[3] * self.kilometry / xarakteristika[1],
            3
            )

        if PP_bally > xarakteristika[3]:
            PP_bally = xarakteristika[3]

        k_perepada = round(1 + self.perepad / (1000 * 12), 3)

        k_avt = 1

        if int(self.zayavka.get()) > 2:
            k_avt = self.change_k_avt(k_avt)

        R_bally = round(self.k_geogr * k_perepada * k_avt, 3)

        Itogo_bally = round(LP_bally + PP_bally + R_bally, 2)

        lbl_itog1 = tk.Label(
            self,
            text='Всего баллов за поход:',
            font=('Arial', 12)
            )
        lbl_itog1.grid(
            row=18,
            column=0,
            columnspan=4,
            sticky='e',
            padx=10,
            pady=10
            )
        self.lbl_itog2 = tk.Label(self, text=Itogo_bally, font=('Arial', 14))
        self.lbl_itog2.grid(row=18, column=4)

        self.lbl_itog3 = tk.Label(
            self,
            text='Надо ' + str(xarakteristika[4]) + '-' + str(xarakteristika[5]),
            font=('Arial', 10, 'italic')
            )
        self.lbl_itog3.grid(row=18, column=5)

        lbl_LP1 = tk.Label(
            self,
            text='За локальные препятствия (ЛП):',
            font=('Arial', 10)
            )
        lbl_LP1.grid(row=19, column=0, columnspan=4, sticky='e', padx=10)
        self.lbl_LP2 = tk.Label(self, text=LP_bally, font=('Arial', 12))
        self.lbl_LP2.grid(row=19, column=4)

        lbl_PP1 = tk.Label(
            self,
            text='За протяжённые препятствия (ПП):',
            font=('Arial', 10)
            )
        lbl_PP1.grid(row=20, column=0, columnspan=4, sticky='e', padx=10)
        self.lbl_PP2 = tk.Label(self, text=PP_bally, font=('Arial', 12))
        self.lbl_PP2.grid(row=20, column=4)

        lbl_R1 = tk.Label(self, text='За район (Р):', font=('Arial', 10))
        lbl_R1.grid(row=21, column=0, columnspan=4, sticky='e', padx=10)
        self.lbl_R2 = tk.Label(self, text=R_bally, font=('Arial', 12))
        self.lbl_R2.grid(row=21, column=4)

        korotkii = self.korotk.get()

        proverka, check_slojnosti = self.proverka_kategorii(
            self.dni,
            self.kilometry,
            Itogo_bally,
            korotkii
            )

        if proverka:
            self.lbl_verdikt = tk.Label(
                self,
                text='         Маршрут соответствует заявленной категории         ',
                font=('Arial', 14),
                bg='OliveDrab1'
                )
            self.lbl_verdikt.grid(row=23, column=0, columnspan=10)
            if Itogo_bally > xarakteristika[5] and self.kilometry >= 3 * \
                    self.xarakteristiki[int(self.zayavka.get())+1][5] / 4:
                self.lbl_verdikt = tk.Label(
                    self,
                    text='         Маршрут охрененно крут, вы набрали на категорию выше         ',
                    font=('Arial', 14),
                    bg='DarkOrchid1'
                    )
                self.lbl_verdikt.grid(row=23, column=0, columnspan=10)
            elif check_slojnosti and slojnost:
                self.lbl_verdikt = tk.Label(
                    self,
                    text='         Маршрут может соответствовать заявленной категории (п.1 Методики)         ',
                    font=('Arial', 14),
                    bg='khaki'
                    )
                self.lbl_verdikt.grid(row=23, column=0, columnspan=10)
            elif check_slojnosti and slojnost is False:
                self.lbl_verdikt = tk.Label(
                    self,
                    text='         Маршрут может соответствовать заявленной категории (п. 1.9.14.5 Правил)         ',
                    font=('Arial', 14),
                    bg='khaki'
                    )
                self.lbl_verdikt.grid(row=23, column=0, columnspan=10)
        else:
            self.lbl_verdikt = tk.Label(
                self,
                text='         Маршрут НЕ соответствует заявленной категории         ',
                font=('Arial', 14),
                bg='red'
                )
            self.lbl_verdikt.grid(row=23, column=0, columnspan=10)


    def voda_window(self, *arg):
        self.newWindow = tk.Toplevel(self)
        self.newWindow.iconbitmap('icon.ico')
        self.newWindow.title('Водный участок')
        self.newWindow.resizable(False, False)
        x = int((self.newWindow.winfo_screenwidth() - 100) / 2)
        y = int((self.newWindow.winfo_screenheight() - 160) / 2)
        self.newWindow.wm_geometry("+%d+%d" % (x, y))
        self.newWindow.columnconfigure([0, 3], minsize=50)
        self.newWindow.rowconfigure([0, 3], minsize=40)

        label1 = tk.Label(
            self.newWindow,
            text='Вы хотите включить часть протяженности водного участка \n в протяженность маршрута.'
            )
        label1.grid(row=0, column=0, columnspan=4, pady=10)

        label2 = tk.Label(
            self.newWindow,
            text='Для этого введите протяженность вашего водного участка.'
            )
        label2.grid(row=1, column=0, columnspan=4, pady=10)

        self.kilometry_vody = tk.Entry(self.newWindow, width=6,
                                       relief=tk.RAISED, borderwidth=2)
        self.kilometry_vody.grid(row=2, column=1, columnspan=2, pady=10)

        btm_ok = tk.Button(self.newWindow, text='Ок',
                           command=self.close_window, width=8)
        btm_ok.grid(row=3, column=1)

        btm_otmena = tk.Button(self.newWindow, text='Отмена',
                               command=self.otmena_window, width=8)
        btm_otmena.grid(row=3, column=2)

    def close_window(self):
        self.ckb_voda.select()
        if self.kilometry_vody.get() != '':
            self.kilometry_za_vodu = int(self.kilometry_vody.get())
        self.newWindow.destroy()
        self.proverka()

    def otmena_window(self):
        self.ckb_voda.deselect()
        self.newWindow.destroy()

    def clean(self):
        self.kategori_var.set(1)
        self.etr_dni.delete(0, 'end')
        self.etr_kilometry.delete(0, 'end')
        self.etr_perepad.delete(0, 'end')
        self.ckb_voda.deselect()
        self.ckb_korotk.deselect()
        self.etr_pereprava_nk.delete(0, 'end')
        self.etr_pereprava_1a.delete(0, 'end')
        self.etr_pereprava_1b.delete(0, 'end')
        self.etr_pereprava_2a.delete(0, 'end')
        self.etr_pereprava_2b.delete(0, 'end')
        self.etr_pereval_nk.delete(0, 'end')
        self.etr_pereval_1a.delete(0, 'end')
        self.etr_pereval_1b.delete(0, 'end')
        self.etr_pereval_2a.delete(0, 'end')
        self.etr_pereval_2b.delete(0, 'end')
        self.etr_pereval_v.delete(0, 'end')
        self.etr_vershina_nk.delete(0, 'end')
        self.etr_vershina_1a.delete(0, 'end')
        self.etr_vershina_1b.delete(0, 'end')
        self.etr_vershina_2a.delete(0, 'end')
        self.etr_vershina_v.delete(0, 'end')
        self.etr_travers_nk.delete(0, 'end')
        self.etr_travers_1a.delete(0, 'end')
        self.etr_travers_1b.delete(0, 'end')
        self.etr_travers_2a.delete(0, 'end')
        self.etr_travers_v.delete(0, 'end')
        self.etr_kanyon_nk.delete(0, 'end')
        self.etr_kanyon_1a.delete(0, 'end')
        self.etr_kanyon_1b.delete(0, 'end')
        self.etr_kanyon_2a.delete(0, 'end')
        self.etr_kanyon_2b.delete(0, 'end')
        self.etr_voda_nk.delete(0, 'end')
        self.etr_voda_1.delete(0, 'end')
        self.etr_voda_2.delete(0, 'end')
        self.etr_voda_3.delete(0, 'end')
        self.etr_voda_4.delete(0, 'end')
        self.k_avt_button.set(1)
        self.combo_rayon.set('')
        self.k_tr = 0
        self.k_geogr = 0

    def clean_LP(self):
        self.etr_pereprava_nk.delete(0, 'end')
        self.etr_pereprava_1a.delete(0, 'end')
        self.etr_pereprava_1b.delete(0, 'end')
        self.etr_pereprava_2a.delete(0, 'end')
        self.etr_pereprava_2b.delete(0, 'end')
        self.etr_pereval_nk.delete(0, 'end')
        self.etr_pereval_1a.delete(0, 'end')
        self.etr_pereval_1b.delete(0, 'end')
        self.etr_pereval_2a.delete(0, 'end')
        self.etr_pereval_2b.delete(0, 'end')
        self.etr_pereval_v.delete(0, 'end')
        self.etr_vershina_nk.delete(0, 'end')
        self.etr_vershina_1a.delete(0, 'end')
        self.etr_vershina_1b.delete(0, 'end')
        self.etr_vershina_2a.delete(0, 'end')
        self.etr_vershina_v.delete(0, 'end')
        self.etr_travers_nk.delete(0, 'end')
        self.etr_travers_1a.delete(0, 'end')
        self.etr_travers_1b.delete(0, 'end')
        self.etr_travers_2a.delete(0, 'end')
        self.etr_travers_v.delete(0, 'end')
        self.etr_kanyon_nk.delete(0, 'end')
        self.etr_kanyon_1a.delete(0, 'end')
        self.etr_kanyon_1b.delete(0, 'end')
        self.etr_kanyon_2a.delete(0, 'end')
        self.etr_kanyon_2b.delete(0, 'end')
        self.etr_voda_nk.delete(0, 'end')
        self.etr_voda_1.delete(0, 'end')
        self.etr_voda_2.delete(0, 'end')
        self.etr_voda_3.delete(0, 'end')
        self.etr_voda_4.delete(0, 'end')
        self.prepaytstviay = np.zeros((6, 6))

    def get_LP_from_track_win(self):
        self.track_win = tk.Toplevel(self)
        self.track_win.iconbitmap('icon.ico')
        self.track_win.title('Окно ввода трека')
        self.track_win.resizable(False, False)
        self.text_s_LP = tk.Text(self.track_win, width=80,
                                 height=15, wrap=tk.WORD)
        self.text_s_LP.pack()
        btn_get_LP = tk.Button(self.track_win, text='Получить', font='12',
                               width=12, height=1, command=self.get_LP_from_track)
        btn_get_LP.pack()
        Win_position.center(self.track_win)

    def get_LP_from_track(self):
        self.clean_LP()
        if self.text_s_LP.get(1.0, tk.END) != '':
            track = str(self.text_s_LP.get(1.0, tk.END))
        else:
            self.track_win.destroy()
        list_of_points = []
        temp = ''
        n = 1
        for elem in track:
            if elem == '-' or elem == '–' or n == len(track):
                list_of_points.append(temp)
                temp = ''
                n += 1
            else:
                temp += elem
                n += 1

        key_symbols = {
            'type_of_LP': ['в.', 'г.', 'пер.', 'р.', 'каньон',
                           'траверс', 'вер.', 'сплав', 'водный участок'],
            'kt': ['н/к', '1А', '1Б', '2А', '2Б', '3А', '3Б', '1 к.с.',
                   '2 к.с.', '3 к.с.', '4 к.с.', '1 КС', '2 КС', '3 КС', '4 КС']
            }

        list_of_points2 = []
        for elem in list_of_points:
            for key_word in key_symbols['type_of_LP']:
                if key_word in elem:
                    for key_word2 in key_symbols['kt']:
                        if key_word2 in elem:
                            list_of_points2.append(elem)
                            break
                    break

        for elem in list_of_points2:
            if 'р.' in elem and 'каньон' not in elem and 'пер.' not in elem:
                if 'н/к' in elem:
                    self.prepaytstviay[0, 0] += 1
                if '1А' in elem:
                    self.prepaytstviay[1, 0] += 1
                if '1Б' in elem:
                    self.prepaytstviay[2, 0] += 1
                if '2А' in elem:
                    self.prepaytstviay[3, 0] += 1
                if '2Б' in elem:
                    self.prepaytstviay[4, 0] += 1

            elif 'пер.' in elem:
                if 'н/к' in elem:
                    self.prepaytstviay[0, 1] += 1
                if '1А' in elem:
                    self.prepaytstviay[1, 1] += 1
                if '1Б' in elem:
                    self.prepaytstviay[2, 1] += 1
                if '2А' in elem:
                    self.prepaytstviay[3, 1] += 1
                if '2Б' in elem:
                    self.prepaytstviay[4, 1] += 1
                if '3А' in elem or '3Б' in elem:
                    self.prepaytstviay[5, 1] += 1

            elif 'в.' in elem or 'г.' in elem or 'вер.' in elem:
                if 'н/к' in elem:
                    self.prepaytstviay[0, 2] += 1
                if '1А' in elem:
                    self.prepaytstviay[1, 2] += 1
                if '1Б' in elem:
                    self.prepaytstviay[2, 2] += 1
                if '2А' in elem:
                    self.prepaytstviay[3, 2] += 1
                if '2Б' in elem or '3А' in elem or '3Б' in elem:
                    self.prepaytstviay[5, 2] += 1

            elif 'траверс' in elem:
                if 'н/к' in elem:
                    self.prepaytstviay[0, 3] += 1
                if '1А' in elem:
                    self.prepaytstviay[1, 3] += 1
                if '1Б' in elem:
                    self.prepaytstviay[2, 3] += 1
                if '2А' in elem:
                    self.prepaytstviay[3, 3] += 1
                if '2Б' in elem or '3А' in elem or '3Б' in elem:
                    self.prepaytstviay[5, 3] += 1

            elif 'каньон' in elem:
                if 'н/к' in elem:
                    self.prepaytstviay[0, 4] += 1
                if '1А' in elem:
                    self.prepaytstviay[1, 4] += 1
                if '1Б' in elem:
                    self.prepaytstviay[2, 4] += 1
                if '2А' in elem:
                    self.prepaytstviay[3, 4] += 1
                if '2Б' in elem:
                    self.prepaytstviay[4, 4] += 1

            elif 'сплав' in elem or 'водный участок' in elem:
                if 'н/к' in elem:
                    self.prepaytstviay[0, 5] += 1
                if '1 к.с.' in elem or '1 КС' in elem:
                    self.prepaytstviay[1, 5] += 1
                if '2 к.с.' in elem or '2 КС' in elem:
                    self.prepaytstviay[2, 5] += 1
                if '3 к.с.' in elem or '3 КС' in elem:
                    self.prepaytstviay[3, 5] += 1
                if '4 к.с.' in elem or '4 КС' in elem:
                    self.prepaytstviay[4, 5] += 1

        self.etr_pereprava_nk.insert(0, int(self.prepaytstviay[0, 0]))
        self.etr_pereprava_1a.insert(0, int(self.prepaytstviay[1, 0]))
        self.etr_pereprava_1b.insert(0, int(self.prepaytstviay[2, 0]))
        self.etr_pereprava_2a.insert(0, int(self.prepaytstviay[3, 0]))
        self.etr_pereprava_2b.insert(0, int(self.prepaytstviay[4, 0]))
        self.etr_pereval_nk.insert(0, int(self.prepaytstviay[0, 1]))
        self.etr_pereval_1a.insert(0, int(self.prepaytstviay[1, 1]))
        self.etr_pereval_1b.insert(0, int(self.prepaytstviay[2, 1]))
        self.etr_pereval_2a.insert(0, int(self.prepaytstviay[3, 1]))
        self.etr_pereval_2b.insert(0, int(self.prepaytstviay[4, 1]))
        self.etr_pereval_v.insert(0, int(self.prepaytstviay[5, 1]))
        self.etr_vershina_nk.insert(0, int(self.prepaytstviay[0, 2]))
        self.etr_vershina_1a.insert(0, int(self.prepaytstviay[1, 2]))
        self.etr_vershina_1b.insert(0, int(self.prepaytstviay[2, 2]))
        self.etr_vershina_2a.insert(0, int(self.prepaytstviay[3, 2]))
        self.etr_vershina_v.insert(0, int(self.prepaytstviay[5, 2]))
        self.etr_travers_nk.insert(0, int(self.prepaytstviay[0, 3]))
        self.etr_travers_1a.insert(0, int(self.prepaytstviay[1, 3]))
        self.etr_travers_1b.insert(0, int(self.prepaytstviay[2, 3]))
        self.etr_travers_2a.insert(0, int(self.prepaytstviay[3, 3]))
        self.etr_travers_v.insert(0, int(self.prepaytstviay[4, 3]))
        self.etr_kanyon_nk.insert(0, int(self.prepaytstviay[0, 4]))
        self.etr_kanyon_1a.insert(0, int(self.prepaytstviay[1, 4]))
        self.etr_kanyon_1b.insert(0, int(self.prepaytstviay[2, 4]))
        self.etr_kanyon_2a.insert(0, int(self.prepaytstviay[3, 4]))
        self.etr_kanyon_2b.insert(0, int(self.prepaytstviay[4, 4]))
        self.etr_voda_nk.insert(0, int(self.prepaytstviay[0, 5]))
        self.etr_voda_1.insert(0, int(self.prepaytstviay[1, 5]))
        self.etr_voda_2.insert(0, int(self.prepaytstviay[2, 5]))
        self.etr_voda_3.insert(0, int(self.prepaytstviay[3, 5]))
        self.etr_voda_4.insert(0, int(self.prepaytstviay[4, 5]))
