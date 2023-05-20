import tkinter as tk
import tkinter.ttk as ttk
import numpy as np


def init_variables_and_constants(self):
    self.k_avt_button = tk.IntVar()
    self.kategori_var = tk.IntVar()
    self.korotk = tk.BooleanVar(value=False)
    self.luzer = tk.BooleanVar(value=False)
    self.dni = 0
    self.kilometry = 0
    self.perepad = 0
    self.rayon = ''
    self.k_tr = 0
    self.k_geogr = 0
    self.prepaytstviay = np.zeros((6, 6))
    self.xarakteristiki = {1: [6, 100, 10, 12, 7, 20, 2],
                           2: [8, 120, 20, 24, 21, 59, 2],
                           3: [10, 140, 40, 50, 60, 94, 2],
                           4: [13, 170, 60, 70, 95, 134, 3],
                           5: [16, 210, 80, 100, 135, 184, 3],
                           6: [20, 250, 110, 140, 185, 5000, 4]
                           }

    self.bally_norm = {
        1: {
            'pereprava': [[8, 4], [0, 0], [0, 0], [0, 0], [0, 0]],
            'pereval': [[2, 4], [0, 0], [0, 0], [0, 0], [0, 0]],
            'vershina': [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
            'travers': [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
            'kanyon': [[4, 4], [0, 0], [0, 0], [0, 0], [0, 0]],
            'voda': [[1, 4], [0, 0], [0, 0], [0, 0], [0, 0]]
            },
        2: {
            'pereprava': [[8, 4], [6, 6], [0, 0], [0, 0], [0, 0]],
            'pereval': [[2, 4], [2, 8], [0, 0], [0, 0], [0, 0]],
            'vershina': [[2, 8], [0, 0], [0, 0], [0, 0], [0, 0]],
            'travers': [[2, 8], [0, 0], [0, 0], [0, 0], [0, 0]],
            'kanyon': [[4, 4], [4, 4], [0, 0], [0, 0], [0, 0]],
            'voda': [[1, 4], [1, 8], [0, 0], [0, 0], [0, 0]]
            },
        3: {
            'pereprava': [[8, 4], [6, 6], [3, 12], [0, 0], [0, 0]],
            'pereval': [[2, 4], [2, 8], [2, 12], [0, 0], [0, 0]],
            'vershina': [[2, 8], [2, 10], [0, 0], [0, 0], [0, 0]],
            'travers': [[2, 8], [2, 10], [0, 0], [0, 0], [0, 0]],
            'kanyon': [[4, 4], [4, 4], [4, 12], [0, 0], [0, 0]],
            'voda': [[1, 4], [1, 8], [1, 20], [0, 0], [0, 0]]
            },
        4: {
            'pereprava': [[0, 0], [6, 6], [3, 12], [2, 14], [0, 0]],
            'pereval': [[0, 0], [3, 12], [2, 12], [2, 16], [0, 0]],
            'vershina': [[2, 8], [2, 10], [2, 14], [0, 0], [0, 0]],
            'travers': [[2, 8], [2, 10], [2, 14], [0, 0], [0, 0]],
            'kanyon': [[4, 4], [4, 4], [4, 12], [4, 20], [0, 0]],
            'voda': [[1, 4], [1, 8], [1, 20], [1, 40], [0, 0]]
            },
        5: {
            'pereprava': [[0, 0], [0, 0], [3, 12], [2, 14], [2, 24]],
            'pereval': [[0, 0], [0, 0], [2, 12], [2, 16], [3, 36]],
            'vershina': [[0, 0], [3, 15], [3, 21], [2, 18], [0, 0]],
            'travers': [[1, 4], [2, 10], [2, 14], [2, 18], [0, 0]],
            'kanyon': [[4, 4], [4, 4], [4, 12], [4, 20], [2, 16]],
            'voda': [[1, 4], [1, 8], [1, 20], [1, 40], [1, 56]]
            },
        6: {
            'pereprava': [[0, 0], [0, 0], [1, 4], [3, 21], [4, 48]],
            'pereval': [[0, 0], [0, 0], [2, 12], [3, 24], [4, 48]],
            'vershina': [[0, 0], [2, 10], [3, 21], [4, 36], [0, 0]],
            'travers': [[0, 0], [2, 10], [3, 21], [4, 36], [0, 0]],
            'kanyon': [[4, 4], [4, 4], [4, 12], [4, 20], [4, 32]],
            'voda': [[1, 4], [1, 8], [1, 20], [1, 40], [1, 56]]
            },
        }

    self.slovar_rayon = {
        'Кольский полуостров': [0.4, 9],
        'Карелия': [0.3, 6],
        'Архангельская обл. и Республика Коми': [0.3, 8],
        'Ленинградская, Вологодская обл.': [0.28, 4],
        'Европейская часть России': [0.28, 1],
        'Белоруссия': [0.28, 1],
        'Украина': [0.28, 1],
        'Карпаты': [0.3, 2],
        'Крым': [0.3, 2],
        'Западный Кавказ': [0.35, 4],
        'Восточный Кавказ': [0.4, 5],
        'Центральный Кавказ': [0.42, 5],
        'Закавказье': [0.33, 4],
        'Полярный Урал': [0.5, 9],
        'Приполярный Урал': [0.63, 10],
        'Северный Урал': [0.5, 7],
        'Средний Урал': [0.35, 6],
        'Южный Урал': [0.38, 6],
        'Западная Сибирь': [0.42, 8],
        'Средняя Азия и Казахстан (пуст.)': [0.4, 10],
        'Западный Тянь-Шань': [0.5, 8],
        'Северный Тянь-Шань': [0.53, 8],
        'Центральный Тянь-Шань': [0.55, 8],
        'Памир': [0.7, 9],
        'Памиро-Алай': [0.63, 8],
        'Джунгарский Алатау': [0.53, 8],
        'Алтай': [0.6, 8],
        'Кузнецкий Алатау': [0.55, 6],
        'Горная Шория': [0.5, 6],
        'Салаирский кряж': [0.38, 6],
        'Западный Саян': [0.65, 7],
        'Западная Тыва, Шапшальский хребет': [0.55, 8],
        'Монгольский Алтай': [0.45, 7],
        'Центральный и Восточный Саян': [0.7, 9],
        'Северные тундровые районы': [0.55, 16],
        'Плато Путорана': [0.65, 15],
        'Хамар-Дабан': [0.6, 7],
        'Байкальский хребет': [0.65, 10],
        'Верхнеангарский хребет': [0.85, 12],
        'Баргузинский хребет': [0.75, 10],
        'Икатский и Муйские хребты': [1, 12],
        'Хребты Кодар и Удокан': [1, 13],
        'Становой хребет и Алданское нагорье': [0.9, 14],
        'Верхоянский хребет': [0.83, 18],
        'Хребет Черского': [0.9, 18],
        'Хребет Сунтар-Хаята': [0.85, 18],
        'Хабаровский край': [0.83, 12],
        'Приморье': [0.83, 9],
        'Сахалин': [0.75, 7],
        'Курильские острова (сев.)': [0.8, 10],
        'Курильские острова (южн.)': [0.95, 10],
        'Камчатка (Срединный и Восточный хребты)': [0.88, 13],
        'Камчатка (южная часть)': [0.63, 13],
        'Камчатка (северная группа вулканов)': [0.65, 13],
        'Магаданская область, Чукотка': [0.75, 18],
        'Корякское нагорье': [0.75, 19],
        'Северная Земля, Новая Земля, Земля Франца-Иосифа': [0.9, 30]
        }


def init_ui(self):
    self.parent.title('Рассчет категории сложности')
    self.columnconfigure([0, 9], minsize=50)
    self.rowconfigure([0, 23], minsize=40)

    lbl_kc = tk.Label(self, text='Заявленная к.с.')
    lbl_kc.grid(row=0, rowspan=3, column=0, sticky='e')
    self.zayavka = tk.Spinbox(
        self,
        textvariable=self.kategori_var,
        width=5,
        from_=1,
        to=6
        )
    self.zayavka.grid(row=0, rowspan=3, column=1, sticky='w')

    lbl_dni = tk.Label(self, text='Продолжительность, дни:')
    lbl_dni.grid(row=3, rowspan=2, column=0, sticky='e', pady=2)
    self.etr_dni = tk.Entry(self, width=6)
    self.etr_dni.grid(row=3, rowspan=2, column=1, sticky='w', pady=2)

    lbl_kilometry = tk.Label(self, text='Протяженность, км:')
    lbl_kilometry.grid(row=5, rowspan=2, column=0, sticky='e', pady=2)
    self.etr_kilometry = tk.Entry(self, width=6)
    self.etr_kilometry.grid(row=5, rowspan=2, column=1, sticky='w', pady=2)

    lbl_perepad = tk.Label(self, text='Перепад высот, м:')
    lbl_perepad.grid(row=7, rowspan=2, column=0, sticky='e', pady=2)
    self.etr_perepad = tk.Entry(self, width=6)
    self.etr_perepad.grid(row=7, rowspan=2, column=1, sticky='w', pady=2)

    self.ckb_korotk = tk.Checkbutton(self, text='Короткий поход',
                                     variable=self.korotk, onvalue=True,
                                     offvalue=False)
    self.ckb_korotk.grid(row=0, rowspan=3, column=2)

    lbl_lp = tk.Label(self, text='Таблица ЛП (количество)')
    lbl_lp.grid(row=0, rowspan=2, column=3, columnspan=5)

    btn_vvod = tk.Button(self, text='Получить из нитки', width=16,
                         height=1, relief='ridge',
                         command=self.get_LP_from_track_win)
    btn_vvod.grid(row=0, rowspan=2, column=8, columnspan=3)

    lbl_lp = tk.Label(self, text='н/к')
    lbl_lp.grid(row=2, column=3)

    lbl_lp = tk.Label(self, text='1А')
    lbl_lp.grid(row=2, column=4)

    lbl_lp = tk.Label(self, text='1Б')
    lbl_lp.grid(row=2, column=5)

    lbl_lp = tk.Label(self, text='2А')
    lbl_lp.grid(row=2, column=6)

    lbl_lp = tk.Label(self, text='2Б')
    lbl_lp.grid(row=2, column=7)

    lbl_lp = tk.Label(self, text='выше')
    lbl_lp.grid(row=2, column=8)

    lbl_lp = tk.Label(self, text='Переправа')
    lbl_lp.grid(row=3, column=2, sticky='e')

    lbl_lp = tk.Label(self, text='Перевал')
    lbl_lp.grid(row=4, column=2, sticky='e')

    lbl_lp = tk.Label(self, text='Вершина')
    lbl_lp.grid(row=5, column=2, sticky='e')

    lbl_lp = tk.Label(self, text='Траверс')
    lbl_lp.grid(row=6, column=2, sticky='e')

    lbl_lp = tk.Label(self, text='Каньон')
    lbl_lp.grid(row=7, column=2, sticky='e')

    lbl_lp = tk.Label(self, text='Водный участок')
    lbl_lp.grid(row=8, column=2, sticky='e')

    self.etr_pereprava_nk = tk.Entry(self, width=4,
                                     relief=tk.RAISED, borderwidth=2)
    self.etr_pereprava_nk.grid(row=3, column=3)

    self.etr_pereprava_1a = tk.Entry(self, width=4,
                                     relief=tk.RAISED, borderwidth=2)
    self.etr_pereprava_1a.grid(row=3, column=4)

    self.etr_pereprava_1b = tk.Entry(self, width=4,
                                     relief=tk.RAISED, borderwidth=2)
    self.etr_pereprava_1b.grid(row=3, column=5)

    self.etr_pereprava_2a = tk.Entry(self, width=4,
                                     relief=tk.RAISED, borderwidth=2)
    self.etr_pereprava_2a.grid(row=3, column=6)

    self.etr_pereprava_2b = tk.Entry(self, width=4,
                                     relief=tk.RAISED, borderwidth=2)
    self.etr_pereprava_2b.grid(row=3, column=7)

    self.etr_pereval_nk = tk.Entry(self, width=4,
                                   relief=tk.RAISED, borderwidth=2)
    self.etr_pereval_nk.grid(row=4, column=3)

    self.etr_pereval_1a = tk.Entry(self, width=4,
                                   relief=tk.RAISED, borderwidth=2)
    self.etr_pereval_1a.grid(row=4, column=4)

    self.etr_pereval_1b = tk.Entry(self, width=4,
                                   relief=tk.RAISED, borderwidth=2)
    self.etr_pereval_1b.grid(row=4, column=5)

    self.etr_pereval_2a = tk.Entry(self, width=4,
                                   relief=tk.RAISED, borderwidth=2)
    self.etr_pereval_2a.grid(row=4, column=6)

    self.etr_pereval_2b = tk.Entry(self, width=4,
                                   relief=tk.RAISED, borderwidth=2)
    self.etr_pereval_2b.grid(row=4, column=7)

    self.etr_pereval_v = tk.Entry(self, width=4,
                                  relief=tk.RAISED, borderwidth=2)
    self.etr_pereval_v.grid(row=4, column=8)

    self.etr_vershina_nk = tk.Entry(self, width=4,
                                    relief=tk.RAISED, borderwidth=2)
    self.etr_vershina_nk.grid(row=5, column=3)

    self.etr_vershina_1a = tk.Entry(self, width=4,
                                    relief=tk.RAISED, borderwidth=2)
    self.etr_vershina_1a.grid(row=5, column=4)

    self.etr_vershina_1b = tk.Entry(self, width=4,
                                    relief=tk.RAISED, borderwidth=2)
    self.etr_vershina_1b.grid(row=5, column=5)

    self.etr_vershina_2a = tk.Entry(self, width=4,
                                    relief=tk.RAISED, borderwidth=2)
    self.etr_vershina_2a.grid(row=5, column=6)

    self.etr_vershina_v = tk.Entry(self, width=4,
                                   relief=tk.RAISED, borderwidth=2)
    self.etr_vershina_v.grid(row=5, column=8)

    self.etr_travers_nk = tk.Entry(self, width=4,
                                   relief=tk.RAISED, borderwidth=2)
    self.etr_travers_nk.grid(row=6, column=3)

    self.etr_travers_1a = tk.Entry(self, width=4,
                                   relief=tk.RAISED, borderwidth=2)
    self.etr_travers_1a.grid(row=6, column=4)

    self.etr_travers_1b = tk.Entry(self, width=4,
                                   relief=tk.RAISED, borderwidth=2)
    self.etr_travers_1b.grid(row=6, column=5)

    self.etr_travers_2a = tk.Entry(self, width=4,
                                   relief=tk.RAISED, borderwidth=2)
    self.etr_travers_2a.grid(row=6, column=6)

    self.etr_travers_v = tk.Entry(self, width=4,
                                  relief=tk.RAISED, borderwidth=2)
    self.etr_travers_v.grid(row=6, column=8)

    self.etr_kanyon_nk = tk.Entry(self, width=4,
                                  relief=tk.RAISED, borderwidth=2)
    self.etr_kanyon_nk.grid(row=7, column=3)

    self.etr_kanyon_1a = tk.Entry(self, width=4,
                                  relief=tk.RAISED, borderwidth=2)
    self.etr_kanyon_1a.grid(row=7, column=4)

    self.etr_kanyon_1b = tk.Entry(self, width=4,
                                  relief=tk.RAISED, borderwidth=2)
    self.etr_kanyon_1b.grid(row=7, column=5)

    self.etr_kanyon_2a = tk.Entry(self, width=4,
                                  relief=tk.RAISED, borderwidth=2)
    self.etr_kanyon_2a.grid(row=7, column=6)

    self.etr_kanyon_2b = tk.Entry(self, width=4,
                                  relief=tk.RAISED, borderwidth=2)
    self.etr_kanyon_2b.grid(row=7, column=7)

    self.etr_voda_nk = tk.Entry(self, width=4,
                                relief=tk.RAISED, borderwidth=2)
    self.etr_voda_nk.grid(row=8, column=3)

    self.etr_voda_1 = tk.Entry(self, width=4,
                               relief=tk.RAISED, borderwidth=2)
    self.etr_voda_1.grid(row=8, column=4)

    self.etr_voda_2 = tk.Entry(self, width=4,
                               relief=tk.RAISED, borderwidth=2)
    self.etr_voda_2.grid(row=8, column=5)

    self.etr_voda_3 = tk.Entry(self, width=4,
                               relief=tk.RAISED, borderwidth=2)
    self.etr_voda_3.grid(row=8, column=6)

    self.etr_voda_4 = tk.Entry(self, width=4,
                               relief=tk.RAISED, borderwidth=2)
    self.etr_voda_4.grid(row=8, column=7)

    lbl_lp = tk.Label(self, text='н/к')
    lbl_lp.grid(row=9, column=3)

    lbl_lp = tk.Label(self, text='1 к.т.')
    lbl_lp.grid(row=9, column=4)

    lbl_lp = tk.Label(self, text='2 к.т.')
    lbl_lp.grid(row=9, column=5)

    lbl_lp = tk.Label(self, text='3 к.т.')
    lbl_lp.grid(row=9, column=6)

    lbl_lp = tk.Label(self, text='4 к.т.')
    lbl_lp.grid(row=9, column=7)

    self.ckb_voda = tk.Checkbutton(
        self,
        text='Зачесть в км',
        variable=self.luzer,
        width=15,
        onvalue=True,
        offvalue=False
        )
    self.ckb_voda.grid(row=8, column=8, columnspan=3)

    lbl_avtonomnost = tk.Label(self, text='Выбери автономность')
    lbl_avtonomnost.grid(row=10, rowspan=4, column=0, sticky='e', pady=2)

    self.rdb_avt1 = tk.Radiobutton(
        self,
        text='Маршрут пройден группой при полной автономии',
        variable=self.k_avt_button,
        value=1
        )
    self.rdb_avt1.grid(row=10, column=1, columnspan=8, sticky='w', pady=2)

    self.rdb_avt2 = tk.Radiobutton(
        self,
        text='Маршрут пройден группой с привлечением транспортных средств для организации заброски',
        variable=self.k_avt_button,
        value=2
        )
    self.rdb_avt2.grid(row=11, column=1, columnspan=8, sticky='w', pady=2)

    self.rdb_avt3 = tk.Radiobutton(
        self,
        text='Маршрут проходит через один населенный пункт',
        variable=self.k_avt_button,
        value=3
        )
    self.rdb_avt3.grid(row=12, column=1, columnspan=8, sticky='w', pady=2)

    self.rdb_avt4 = tk.Radiobutton(
        self,
        text='Маршрут проходит через два и более населенных пункта',
        variable=self.k_avt_button,
        value=4
        )
    self.rdb_avt4.grid(row=13, column=1, columnspan=8, sticky='w', pady=2)

    lbl_rayon = tk.Label(self, text='Выбери район')
    lbl_rayon.grid(row=15, rowspan=2, column=0, sticky='e', pady=2)

    self.combo_rayon = ttk.Combobox(
        self,
        values=list(self.slovar_rayon.keys()),
        width=50
        )
    self.combo_rayon.grid(row=15, rowspan=2, column=1, columnspan=7,
                          sticky='w', pady=2, padx=5)

    btn_clean = tk.Button(self, text='Очистить всё', width=12, height=1,
                          relief='groove', command=self.clean)
    btn_clean.grid(row=15, rowspan=2, column=7, columnspan=2)

    btn_check = tk.Button(self, text='Проверить',
                          font=('Arial', '14', 'bold'), width=12, height=1,
                          command=self.clicked)
    btn_check.grid(row=17, column=0, columnspan=10)

    self.lbl_verdikt = tk.Label(self)
    self.lbl_verdikt.grid(row=23, column=0, columnspan=10)
    self.lbl_verdikt.grid_remove()

    self.lbl_itog2 = tk.Label(self)
    self.lbl_itog2.grid(row=18, column=4)
    self.lbl_itog2.grid_remove()

    self.lbl_itog3 = tk.Label(self)
    self.lbl_itog3.grid(row=18, column=5)
    self.lbl_itog3.grid_remove()

    self.lbl_LP2 = tk.Label(self)
    self.lbl_LP2.grid(row=19, column=4)
    self.lbl_LP2.grid_remove()

    self.lbl_PP2 = tk.Label(self)
    self.lbl_PP2.grid(row=20, column=4)
    self.lbl_PP2.grid_remove()

    self.lbl_R2 = tk.Label(self)
    self.lbl_R2.grid(row=21, column=4)
    self.lbl_R2.grid_remove()

    self.pack()
