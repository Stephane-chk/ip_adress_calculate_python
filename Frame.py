from tkinter import *
from tkinter import messagebox
from Ipv4 import Ipv4
from  Ipv6 import  Ipv6
class Win:
    def __init__(self):
        self.fenetre = Tk()

        self.value1_ipv4_with_class = StringVar()
        self.value2_ipv4_with_class = StringVar()
        self.value3_ipv4_with_class = StringVar()
        self.value4_ipv4_with_class = StringVar()

        self.value1_ipv4_no_class = StringVar()
        self.value2_ipv4_no_class = StringVar()
        self.value3_ipv4_no_class = StringVar()
        self.value4_ipv4_no_class = StringVar()
        self.cidr_no_class = StringVar()

        self.address_ipv6 = StringVar()
        self.prefixe = StringVar()

        pass

    def constructFrame(self):
        self.fenetre.title("Ipv4-Ipv6")
        self.width_fenetre = 600
        self.height_fenetre = 400
        self.fenetre.geometry(''+str(self.width_fenetre)+'x'+str(self.height_fenetre)+'')
        self.fenetre.resizable("false","false")

        #Ipv4 avec classe
        address_label_with_class = Label(self.fenetre, text="Ipv4 Avec Classe: ",font=("oxygen",10))
        address_label_with_class.grid(row=1, column=1, padx=10, pady=10)
        value_1_ipv4_with_class = Entry(self.fenetre,textvariable=self.value1_ipv4_with_class,width=5)
        value_2_ipv4_with_class = Entry(self.fenetre,textvariable=self.value2_ipv4_with_class,width=5)
        value_3_ipv4_with_class = Entry(self.fenetre,textvariable=self.value3_ipv4_with_class,width=5)
        value_4_ipv4_with_class = Entry(self.fenetre,textvariable=self.value4_ipv4_with_class,width=5)
        validate_btn_ipv4_with_class = Button(self.fenetre, text="Valider", command=self.executingIpv4WithClass,fg="blue",font=("oxygen",8))
        value_1_ipv4_with_class.grid(row=1, column=2, padx=2, pady=10)
        value_2_ipv4_with_class.grid(row=1, column=3, padx=2, pady=10)
        value_3_ipv4_with_class.grid(row=1, column=4, padx=2, pady=10)
        value_4_ipv4_with_class.grid(row=1, column=5, padx=2, pady=10)
        validate_btn_ipv4_with_class.grid(row=1, column=6, padx=20, pady=10)

        #Ipv4 sans classe
        address_label_no_class = Label(self.fenetre, text="Ipv4 Sans Classe: ", font=("oxygen", 10))
        address_label_no_class.grid(row=3, column=1, padx=10, pady=10)
        cidr_label_no_class = Label(self.fenetre, text="CIDR /? : ", font=("oxygen", 10))
        cidr_label_no_class.grid(row=4, column=1, padx=10, pady=10)
        value_1_ipv4_no_class = Entry(self.fenetre, textvariable=self.value1_ipv4_no_class, width=5)
        value_2_ipv4_no_class = Entry(self.fenetre, textvariable=self.value2_ipv4_no_class, width=5)
        value_3_ipv4_no_class = Entry(self.fenetre, textvariable=self.value3_ipv4_no_class, width=5)
        value_4_ipv4_no_class = Entry(self.fenetre, textvariable=self.value4_ipv4_no_class, width=5)
        cidr_ipv4_no_class = Entry(self.fenetre, textvariable=self.cidr_no_class, width=5)
        validate_btn_ipv4_no_class = Button(self.fenetre, text="Valider", command=self.executingIpv4NoClass, fg="green", font=("oxygen", 8))
        value_1_ipv4_no_class.grid(row=3, column=2, padx=2, pady=10)
        value_2_ipv4_no_class.grid(row=3, column=3, padx=2, pady=10)
        value_3_ipv4_no_class.grid(row=3, column=4, padx=2, pady=10)
        value_4_ipv4_no_class.grid(row=3, column=5, padx=2, pady=10)
        cidr_ipv4_no_class.grid(row=4, column=2, padx=2, pady=10)
        validate_btn_ipv4_no_class.grid(row=4, column=6, padx=20, pady=10)


        #Ipv6 abreviation
        ipv6_label_title = Label(self.fenetre, text="Ipv6 : ", font=("oxygen", 10))
        ipv6_label_title.grid(row=5, column=1, padx=10, pady=10)
        ipv6_label_prefixe = Label(self.fenetre, text="Prefixe : ", font=("oxygen", 10))
        ipv6_label_prefixe.grid(row=6, column=1, padx=10, pady=10)
        value_ipv6 = Entry(self.fenetre, textvariable=self.address_ipv6, width=30)
        prefixe_ipv6 = Entry(self.fenetre, textvariable=self.prefixe, width=5)
        validate_btn_ipv6_abreviation = Button(self.fenetre, text="Valider", command=self.executingIpv6, fg="purple",font=("oxygen", 8))
        prefixe_ipv6.grid(row=6, column=2, padx=2, pady=10)
        value_ipv6.grid(row=5, column=2, columnspan=4,padx=2, pady=10)
        validate_btn_ipv6_abreviation.grid(row=6, column=6, padx=20, pady=10)
        pass

    def executingIpv4WithClass(self):
        try:
            ipv4 = Ipv4(self.value1_ipv4_with_class.get(),self.value2_ipv4_with_class.get(),self.value3_ipv4_with_class.get(),self.value4_ipv4_with_class.get())
            ipv4.initData()
            self.creatingMessageBoxResultIpv4(ipv4)
        except Exception as e:
            self.creatingMessageBoxError(e)
        pass

    def executingIpv4NoClass(self):
        try:
            ipv4 = Ipv4(self.value1_ipv4_no_class.get(),self.value2_ipv4_no_class.get(),self.value3_ipv4_no_class.get(),self.value4_ipv4_no_class.get())
            ipv4.setCidr(self.cidr_no_class.get())
            ipv4.initData()
            self.creatingMessageBoxResultIpv4(ipv4)
        except Exception as e:
            self.creatingMessageBoxError(e)
        pass

    def executingIpv6(self):
        try:
            ipv6 = Ipv6()
            ipv6.setAddress(self.address_ipv6.get())
            ipv6.setPrefixe(self.prefixe.get())
            ipv6.initData()
            self.creatingMessageBoxResultIpv6(ipv6)
        except Exception as e:
            self.creatingMessageBoxError(e)
        pass

    def creatingMessageBoxResultIpv6(self,ipv6:Ipv6):
        mess = 'RESULTAT IPV6'+'\n'
        mess += 'Adresse ip non-abreviation: '+'\n'+ipv6.displayAddressIpExpand()+'\n'
        mess += 'Adresse ip avec abreviation: '+'\n'+ipv6.displayAddressIpCompress()+'\n'+'\n'
        mess += 'Adresse Reseau non-abreviation: '+'\n'+ipv6.getAddressReseauExpand()+'\n'
        mess += 'Adresse Reseau avec abreviation: '+'\n'+ipv6.getAddressReseauCompress()+'\n'
        messagebox.showinfo("RESULTAT IPV6",mess)

    def creatingMessageBoxResultIpv4(self,ipv4:Ipv4):
        cidr = ipv4.getCidr()
        if cidr==0:
            messCidr = 'AUCUN'
        else:
            messCidr = str(cidr)
            pass
        messageResult = "RESULTAT IPV4\n"
        messageResult += 'Addresse IP: '+ipv4.displayToDecimal()+'\n'
        messageResult += 'CIDR: ' + messCidr +'\n'
        messageResult += 'Classe: ' + ipv4.getClass() +'\n'
        messageResult += 'Masque de sous reseau: ' + ipv4.getMask().displayToDecimal() +'\n'
        messageResult += 'Addresse Reseau: ' + ipv4.getAddressReseau().displayToDecimal() +'\n'
        messageResult += 'Addresse de Diffusion: ' + ipv4.getAddressDiffusion().displayToDecimal() +'\n'
        messageResult += '1ere addresse : '+ipv4.getFirstAddress().displayToDecimal()+'\n'
        messageResult += 'Derniere addresse: '+ipv4.getLastAddress().displayToDecimal()+'\n'
        messageResult += 'Nombre addresse disponible : '+str(ipv4.getNbAddressDispo())+'\n'
        messagebox.showinfo('Resultat IPV4',messageResult)

    def creatingMessageBoxError(self,message):
        messagebox.showerror('Erreur',message)
        pass

    def showFrame(self):
        self.fenetre.mainloop()
