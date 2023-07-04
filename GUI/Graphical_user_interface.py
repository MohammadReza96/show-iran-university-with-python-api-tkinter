import sys
sys.path.insert(0,"C:/Users/MohammadReza/Desktop/p-2")
#------------------------------------------------------------------moudules
from tkinter import *
from tkinter import font                          # use for bolding font
from external_modules.play_song import *
from tkinter import ttk
from tkinter import messagebox
from DAL.read_data_from_api import *
from external_modules.city_error_handling import City_Error_Handling
#--------------------------------------------------------------------------
###########################################################################
###########################################################################
###########################################################################
###########################################################################
###########################################################################
#------------------------------------------------------------------main program
import os
os.system('cls')
#--------------------------------
class IranUniversity:
    @staticmethod
    def set_size(window,width,height):
        w=width
        h=height
        ws=window.winfo_screenwidth()
        hs=window.winfo_screenheight()
        x=(ws/2)-(w/2)
        y=(hs/2)-(h/2)
        window.geometry("%dx%d+%d+%d"%(w,h,x,y))

    def __init__(self):
        self.main_widget=Tk()
        self.note_book=ttk.Notebook(self.main_widget)  
        self.tab_1=Frame(self.note_book)                                                                                             
        self.tab_2=Frame(self.note_book)
        self.note_book.add(self.tab_1,text='خانه')                                                                                           
        self.note_book.add(self.tab_2,text='تنظیمات')
        self.note_book.grid(row=0,column=0)                                                                                           
        self.main_widget.title('سیسـتم آشنایـی با دانشــگاه های ایران')                                                                             
        self.main_widget.iconbitmap('icon/iran_kkd_icon.ico')
        IranUniversity.set_size(self.main_widget,655,500)
        self.main_widget.resizable(width=False,height=False)
        self.music=playSong()
    ##################################################################### adding imageBackground for main widget
        self.bg1 = PhotoImage(file = "img/root_background3.png")
        self.bg2 = PhotoImage(file = "img/set_background1.png")
        self.enter_city = PhotoImage(file = "img/city_name_botton3.png")
        self.but_show = PhotoImage(file = "img/show_botton1.png")
        self.but_sound = PhotoImage(file = "img/play_botton.png")
        self.but_mute = PhotoImage(file = "img/mute_botton.png")
        self.but_ret = PhotoImage(file = "img/return_botton.png")
    ##################################################################### adding imageBackground for main widget
        self.canvas1 = Canvas(self.tab_1,width = 400,height = 400,highlightthickness=0)
        self.canvas1.pack(fill = "both", expand = True)
        self.canvas1.create_image(0,0,image = self.bg1,anchor="nw")
    ##################################################################### adding imageBackground for main widget
        self.canvas2 = Canvas(self.tab_2,width = 400,height = 400,highlightthickness=0)
        self.canvas2.pack(fill = "both", expand = True)
        self.canvas2.create_image(0,0,image = self.bg2,anchor="nw")
    ################################################################################################ add label in home
        self.lab_enter_city=Label(master=self.canvas1,image=self.enter_city,borderwidth=0,bg='#000000',activebackground='#000000') 
        self.lab_enter_city.grid(row=0,column=0,padx=(15,0),pady=(380,0))
    ################################################################################################ add entrybox in home
        self.entry_box_city=Entry(master=self.canvas1,borderwidth=2,width=13,font=('tahoma',22,font.BOLD)) 
        self.entry_box_city.grid(row=0,column=1,padx=(5,0),pady=(380,0))
    ################################################################################################ add button in home
        self.button_show=Button(master=self.canvas1,image=self.but_show,borderwidth=0,bg='#f0f0f0',activebackground="#f0f0f0",activeforeground="#f0f0f0") 
        self.button_show.grid(row=0,column=2,padx=(50,0),pady=(380,0)) 
    ################################################################################################ add button in setting
        self.button_sound=Button(master=self.canvas2,image=self.but_sound,borderwidth=0,bg='#f0f0f0') 
        self.button_sound.grid(row=0,column=1,padx=(30,0),pady=(330,0))
        self.button_mute=Button(master=self.canvas2,image=self.but_mute,borderwidth=0,bg='#f0f0f0') 
        self.button_mute.grid(row=0,column=2,padx=(10,0),pady=(330,0))
    ################################################################################################ bind 
        self.button_show.bind('<Button-1>',lambda event:self.__show_result(event))

        self.button_sound.bind('<Button-1>',lambda event:self.__change_song_status(event,'play'))
        self.button_mute.bind('<Button-1>',lambda event:self.__change_song_status(event,'off'))

    
        self.main_widget.mainloop()

    def __show_result(self,event):
        second_page=Toplevel()
        second_page.title('نتایج جستو جو')
        second_page.iconbitmap('icon/iran_kkd_icon.ico')
        IranUniversity.set_size(second_page,900,350)
        second_page.resizable(width=False,height=False)
        tree=ttk.Treeview(second_page,column=('state-province','name','web page'),show='headings',height=10)
        tree.grid(row=1,columnspan=1,padx=10,pady=20)
        self.return_but=Button(second_page,image=self.but_ret,borderwidth=0,activebackground="#f0f0f0",activeforeground="#f0f0f0",command=second_page.destroy)
        self.return_but.grid(row=2,column=0)
        tree.column('# 1',anchor=CENTER,width=150)
        tree.heading('# 1',text='نام استان')
        tree.column('# 2',anchor=CENTER,width=525)
        tree.heading('# 2',text='نام دانشگاه')
        tree.column('# 3',anchor=CENTER,width=200)
        tree.heading('# 3',text='آدرس اینترنتی دانشگاه')

        #------get all universities---------
        city_name=self.entry_box_city.get()

        try:
            if city_name=='':
                raise RuntimeError('لطفا شهر مورد نظر را به زبان انگیلیسی وارد کنید')
            result=read_api_data(city_name)
            if len(result)==0:
                raise City_Error_Handling('نام شهر مورد نظر را به درستی به زبان انگیلیسی وارد کنید')
            n=1
            for item in result:
                tree.insert('','end',text=str(n),values=(item['state-province'],item['name'],item['web_pages']))
                n+=1
        except Exception as error:
            messagebox.showwarning(message=error)
            pass
    def __change_song_status(self,event,value):
        playSong(value)