import os
import tkinter as tk
from tkinter import *
from Bio.Align import AlignInfo
from Bio import AlignIO
import os.path
import os 
import subprocess
import numpy
from tkinter import filedialog
from tkinter import font
from Bio.Align.Applications import ClustalwCommandline
import xlsxwriter



class PrimerDesigner(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        container = Frame(self)
        container.pack()
        self.frames = {}

        for F in (WelcomePage, Implement_MSA, Generate_Consensus_Find_Conserved_Region, Design_Primers):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(WelcomePage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class WelcomePage(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        self.__class__.appTitleFont = font.Font(family='Futura', size=30)

        self.__class__.appNormalFont = font.Font(family='Futura', size=16)

        self.__class__.appButtonFont= font.Font(family='Futura',size=12)

        self.label1=tk.Label(self)
        self.label1.pack(side=BOTTOM)

        self.label = tk.Label(self, text="Welcome to PrimerDesigner!",font=self.__class__.appTitleFont)
        self.label.pack(side=TOP)

        self.button2= tk.Button(self, text="Design primers",command=lambda: controller.show_frame(Design_Primers),font=self.__class__.appButtonFont)
        self.button2.pack(side= BOTTOM)

        self.button1 = tk.Button(self, text="Detect conserved regions",command=lambda: controller.show_frame(Generate_Consensus_Find_Conserved_Region),font=self.__class__.appButtonFont)
        self.button1.pack(side= BOTTOM)

        self.button = tk.Button(self, text="Implement MSA",command=lambda: controller.show_frame(Implement_MSA),font=self.__class__.appButtonFont)
        self.button.pack(side= BOTTOM)


class Implement_MSA(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.files = []

        self.label = tk.Label(self, text="Implement MSA",font=WelcomePage.appTitleFont)
        self.label.pack(pady=10, padx=10)

        self.label2= tk.Label(self,text='Choose your fasta files:',font=WelcomePage.appNormalFont)
        self.label2.pack(anchor=CENTER)

        self.button1= tk.Button(self,text='Browse',command=self.browse_files,font=WelcomePage.appButtonFont)
        self.button1.pack(anchor=CENTER)

        self.label5=tk.Label(self,text='Creat your alignment file',font=WelcomePage.appNormalFont)
        self.label5.pack()

        self.button5=tk.Button(self,text='Browse',command=self.browse_output,font=WelcomePage.appButtonFont)
        self.button5.pack()

        self.label3 = tk.Label(self)
        self.label3.pack(side=BOTTOM)

        self.button4 = tk.Button(self, text="Back", command=lambda: controller.show_frame(WelcomePage),font=WelcomePage.appButtonFont)
        self.button4.pack(side=BOTTOM)

        self.button3 = tk.Button(self, text='Next', command=lambda: controller.show_frame(Generate_Consensus_Find_Conserved_Region),font=WelcomePage.appButtonFont)
        self.button3.pack(side=BOTTOM)

        self.button2 = tk.Button(self, text="Run",command=self.RunClustalw2,font=WelcomePage.appButtonFont)
        self.button2.pack(side=BOTTOM)

        self.label4=tk.Label(self)
        self.label4.pack(side=BOTTOM)

        self.textbox=tk.Text(self,width=100,height=10)
        self.textbox.pack(side=BOTTOM)

    def browse_file(self):

        self.file = filedialog.askopenfilename()
        if self.file:
            self.textbox.insert(INSERT,'Clustalw file chosen:'+ self.file+'\n')

    def browse_files(self):

        self.files=filedialog.askopenfilenames()
        self.file_list=list(self.files)
        for self.filename in self.file_list:
            if self.filename:
                self.textbox.insert(INSERT,'Fasta files chosen:'+self.filename+'\n')

    def browse_output(self):

        self.output=filedialog.asksaveasfilename()
        if self.output:
            self.textbox.insert(INSERT,'Output file created:'+self.output+'\n')

    def RunClustalw2(self):

        for self.fasta_file in self.file_list:
            self.clustalw_cline = ClustalwCommandline('./clustalw2', infile=self.fasta_file,outfile=self.output)
            self.clustalw_cline()
            self.textbox.insert(INSERT,'Your MSA results for'+ self.fasta_file +' can be found in '+self.output+'!'+'\n')


class Generate_Consensus_Find_Conserved_Region(tk.Frame):

    position_pair = []

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.new_file_list=[]

        self.label = tk.Label(self, text="Generate Consensus and Find Conserved Regions",font=WelcomePage.appTitleFont)
        self.label.pack()

        self.label1 = tk.Label(self, text='Choose alignment file',font=WelcomePage.appNormalFont)
        self.label1.pack()

        self.button =tk.Button(self, text='Browse',command=self.browse_aln_file,font=WelcomePage.appButtonFont)
        self.button.pack()

        self.label2=tk.Label(self, text='Name consensus sequence (For example: IMP):',font=WelcomePage.appNormalFont)
        self.label2.pack()

        self.entry= tk.Entry(self)
        self.entry.pack()

        self.label3=tk.Label(self, text='Type in MSA threshold (Default is 0.7, meaning 70%)',font=WelcomePage.appNormalFont)
        self.label3.pack()

        self.entry1 = tk.Entry(self)
        self.entry1.pack()

        self.label4=tk.Label(self, text='Create consensus file',font=WelcomePage.appNormalFont)
        self.label4.pack()

        self.button1 = tk.Button(self,text='Browse',command=self.creat_consensus_seq_file,font=WelcomePage.appButtonFont)
        self.button1.pack()

        self.label5=tk.Label(self, text='Create conserved region file:',font=WelcomePage.appNormalFont)
        self.label5.pack()

        self.button2=tk.Button(self,text='Browse',command=self.creat_conserved_region_file,font=WelcomePage.appButtonFont)
        self.button2.pack()

        self.label6=tk.Label(self)
        self.label6.pack()

        self.label7=tk.Label(self)
        self.label7.pack(side=BOTTOM)

        self.button6 = tk.Button(self, text="Back to Homepage",command=lambda: controller.show_frame(WelcomePage),font=WelcomePage.appButtonFont)
        self.button6.pack(side=BOTTOM)

        self.button5 = tk.Button(self,text='Back', command=lambda: controller.show_frame(Implement_MSA),font=WelcomePage.appButtonFont)
        self.button5.pack(side=BOTTOM)

        self.button4 = tk.Button(self, text='Next', command=lambda: controller.show_frame(Design_Primers),font=WelcomePage.appButtonFont)
        self.button4.pack(side=BOTTOM)

        self.button3 = tk.Button(self, text='Run', command=self.Generate_Consensus_conserved_region,font=WelcomePage.appButtonFont)
        self.button3.pack(side=BOTTOM)

        self.label8=tk.Label(self)
        self.label8.pack(side=BOTTOM)

        self.textbox=tk.Text(self,width=100,height=10)
        self.textbox.pack(side=BOTTOM)

    def get_from_keyboard(self, input):
         return input.get()

    def creat_consensus_seq_file(self):
        self.consensus_seq_file=filedialog.asksaveasfilename()
        if self.consensus_seq_file:
            self.textbox.insert(INSERT,'Consensus sequence file created:'+self.consensus_seq_file+'\n')

    def creat_conserved_region_file(self):
        self.__class__.conserved_region_file=filedialog.asksaveasfilename()
        if self.__class__.conserved_region_file:
            self.textbox.insert(INSERT,'Conserved regions file created:'+self.__class__.conserved_region_file+'\n')

    def browse_aln_file(self):
        self.alignment_file = filedialog.askopenfilename()
        if self.alignment_file:
            self.textbox.insert(INSERT,'Alignment file chosen:' +self.alignment_file+'\n')

    def Generate_Consensus_conserved_region(self):

        with open('para.txt') as para:
            self.alllines = para.readlines()
            for self.para_index, self.para_line in enumerate(self.alllines):
                self.seperate = self.para_line.split(':')
                if 'Minimum length of conserved regions' in self.para_line:
                    self.conserved_region_minimum_size = self.seperate[-1]
                    if self.conserved_region_minimum_size[-1] == '\n':
                        self.conserved_region_minimum_size = self.conserved_region_minimum_size[0:-1]
                    else:
                        pass

        self.alignment = AlignIO.read(self.alignment_file, "clustal")
        self.summary_align = AlignInfo.SummaryInfo(self.alignment)
        self.consensus = self.summary_align.dumb_consensus(float(self.get_from_keyboard(self.entry1)))
        if self.consensus_seq_file:
            f = open(self.consensus_seq_file, "w+")
            f.write('>' + self.get_from_keyboard(self.entry) + '\n' + str(self.consensus))
            f.close()

        self.star_list=[]
        try:
            for self.index in range(0,len(self.consensus)):
                if str(self.consensus[self.index]) == 'X':
                    self.star_list.append(self.index)
            try:
                if self.star_list[0]==0:
                    pass
                else:
                    self.star_list=[0]+self.star_list
                if self.star_list[-1]==len(self.consensus):
                    pass
                else:
                    self.star_list.append(len(self.consensus))

                for self.region_start in range(0,len(self.star_list) - 1):
                    self.region_end=self.region_start+1
                    self.region=self.consensus[self.star_list[self.region_start]+1:self.star_list[self.region_end]]

                    if len(self.region)>=int(self.conserved_region_minimum_size):
                        f = open(self.conserved_region_file, 'a+')
                        f.write('Length:' + str(len(self.region)) + '\n' + str(self.region) + '\n'
                                    'Startposition is: ' + str(self.star_list[self.region_start]) + '\n' + 'Endposition is ' + str(self.star_list[self.region_end]) + '\n')
                        f.close()
                        self.__class__.position_pair.append([self.star_list[self.region_start], self.star_list[self.region_end]])

                    else:
                        pass
            except IndexError:
                f = open(self.conserved_region_file, 'a+')
                f.write('Length:' + str(len(self.consensus)) + '\n' + str(self.consensus) + '\n'
                                    'Startposition is: 1' + '\n' + 'Endposition is ' + str(len(self.consensus)) + '\n')
                f.close()
                self.__class__.position_pair.append([1, len(self.consensus)])
        except TypeError:
            pass

        try:
            if os.path.isfile(self.conserved_region_file) == False:
                self.textbox.insert(INSERT,'No conserved regions found under this threshold for'+ self.get_from_keyboard(self.entry) +', please lower the threshold!!!'+'\n')
            if os.path.isfile(self.conserved_region_file) ==True:
                self.textbox.insert(INSERT,'You can get your detected conserved regions at' + self.conserved_region_file+'\n')
        except FileNotFoundError:
            pass



class Design_Primers(tk.Frame):


    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        self.label = tk.Label(self, text='Design Primers',font=WelcomePage.appTitleFont)
        self.label.pack()

        self.label1 = tk.Label(self, text='Choose template fasta file:',font=WelcomePage.appNormalFont)
        self.label1.pack()

        self.button = tk.Button(self,text='Browse',command=self.browse_template_file,font=WelcomePage.appButtonFont)
        self.button.pack()

        self.label2 = tk.Label(self, text='Create parameters file:',font=WelcomePage.appNormalFont)
        self.label2.pack()

        self.button1 = tk.Button(self,text='Browse',command=self.creat_parameters_file,font=WelcomePage.appButtonFont)
        self.button1.pack()

        self.label3 = tk.Label(self, text='Create primer files:',font=WelcomePage.appNormalFont)
        self.label3.pack()

        self.button2 = tk.Button(self,text='Browse',command=self.creat_primers_file,font=WelcomePage.appButtonFont)
        self.button2.pack()

        self.label9=tk.Label(self)
        self.label9.pack()

        self.button3 = tk.Button(self, text="Show primers' quality", command=self.creat_graph,font=WelcomePage.appButtonFont)
        self.button3.pack()

        self.label6=tk.Label(self)
        self.label6.pack()

        self.label7=tk.Label(self,font=WelcomePage.appNormalFont)
        self.label7.pack(side=BOTTOM)

        self.button4 = tk.Button(self, text="Back to Homepage", command=lambda: controller.show_frame(WelcomePage),font=WelcomePage.appButtonFont)
        self.button4.pack(side=BOTTOM)

        self.button5 = tk.Button(self, text='Back', command=lambda: controller.show_frame(Generate_Consensus_Find_Conserved_Region),font=WelcomePage.appButtonFont)
        self.button5.pack(side=BOTTOM)

        self.button6 = tk.Button(self, text='Run', command=self.Run_Primer3,font=WelcomePage.appButtonFont)
        self.button6.pack(side=BOTTOM)

        self.label8=tk.Label(self)
        self.label8.pack(side=BOTTOM)

        self.textbox=tk.Text(self,width=100,height=10)
        self.textbox.pack(side=BOTTOM)

        self.primer_tm_list = []
        self.left_primer_tm_list = []
        self.right_primer_tm_list = []
        self.primer_gc_list = []
        self.left_primer_gc_list = []
        self.right_primer_gc_list = []
        self.primer_hairpin_list = []
        self.left_primer_hairpin_list = []
        self.right_primer_hairpin_list = []
        self.primer_self_dimer_list = []
        self.left_primer_self_dimer_list = []
        self.right_primer_self_dimer_list = []
        self.left_primer_seq_list = []
        self.right_primer_seq_list = []
        self.left_primer_startp_list = []
        self.right_primer_startp_list = []
        self.left_primer_len_list = []
        self.right_primer_len_list = []
        self.geneid_list=[]
        self.record_start_index_list = []
        self.record_end_index_list = []
        self.newrecord_list=[]


    def creat_parameters_file(self):
        self.parameters_file = filedialog.asksaveasfilename()
        if self.parameters_file:
            self.textbox.insert(INSERT,'Parameter file created:'+self.parameters_file+'\n')

    def creat_primers_file(self):
        self.primers_file = filedialog.asksaveasfilename()
        if self.primers_file:
            self.textbox.insert(INSERT,'Primer file created:'+self.primers_file+'\n')

    def browse_template_file(self):
        self.template_file = filedialog.askopenfilename()
        if self.template_file:
            self.textbox.insert(INSERT,'Template file chosen:'+self.template_file+'\n')

    def Remove_repeat(self,record_list_not_changeable):
        self.record_list_changeable = []
        for self.element in record_list_not_changeable:
            self.record_list_changeable.append(self.element)
        for self.record_A_index in range(0, len(record_list_not_changeable) - 1):
            self.record_A = record_list_not_changeable[self.record_A_index]
            for self.record_B_index in range(self.record_A_index + 1, len(record_list_not_changeable)):
                self.record_B = record_list_not_changeable[self.record_B_index]
                if self.record_A[0] == self.record_B[0]:
                    self.record_list_changeable.remove(self.record_A)
                break
        return self.record_list_changeable

    def Get_data(self,record):
        self.left_primer_data=record[5]
        self.left_primer_line_uc = self.left_primer_data.split(' ')
        self.left_primer_line_c = self.left_primer_data.split(' ')
        for self.space in self.left_primer_line_uc:
            if self.space == '':
                self.left_primer_line_c.remove(self.space)
            else:
                pass
        self.left_primer_startp=int(self.left_primer_line_c[2])
        self.left_primer_startp_list.append(self.left_primer_startp)

        self.left_primer_len=int(self.left_primer_line_c[3])
        self.left_primer_len_list.append(self.left_primer_len)
        
        self.left_primer_tm = float(self.left_primer_line_c[4])
        self.left_primer_tm_list.append(self.left_primer_tm)

        self.left_primer_gc = float(self.left_primer_line_c[5])
        self.left_primer_gc_list.append(self.left_primer_gc)

        self.left_primer_self_dimer= float(self.left_primer_line_c[6])
        self.left_primer_self_dimer_list.append(self.left_primer_self_dimer)

        self.left_primer_hairpin = float(self.left_primer_line_c[8])
        self.left_primer_hairpin_list.append(self.left_primer_hairpin)

        self.left_primer_seq=self.left_primer_line_c[9][0:-1]
        self.left_primer_seq_list.append(self.left_primer_seq)


                #Right primer
        self.right_primer=record[6]
        self.right_primer_line_uc = self.right_primer.split(' ')
        self.right_primer_line_c = self.right_primer.split(' ')

        for self.space in self.right_primer_line_uc:
            if self.space == '':
                self.right_primer_line_c.remove(self.space)
            else:
                pass

        self.right_primer_startp = int(self.right_primer_line_c[2])
        self.right_primer_startp_list.append(self.right_primer_startp)

        self.right_primer_len=int(self.right_primer_line_c[3])
        self.right_primer_len_list.append(self.right_primer_len)
        
        self.right_primer_tm = float(self.right_primer_line_c[4])
        self.right_primer_tm_list.append(self.right_primer_tm)

        self.right_primer_gc = float(self.right_primer_line_c[5])
        self.right_primer_gc_list.append(self.right_primer_gc)

        self.right_primer_self_dimer = float(self.right_primer_line_c[6])
        self.right_primer_self_dimer_list.append(self.right_primer_self_dimer)

        self.right_primer_hairpin = float(self.right_primer_line_c[8])
        self.right_primer_hairpin_list.append(self.right_primer_hairpin)

        self.right_primer_seq=self.right_primer_line_c[9][0:-1]
        self.right_primer_seq_list.append(self.right_primer_seq)

        self.av_primer_tm = (self.left_primer_tm + self.right_primer_tm) / 2
        self.primer_tm_list.append(self.av_primer_tm)

        self.av_primer_gc = (self.left_primer_gc + self.right_primer_gc) / 2
        self.primer_gc_list.append(self.av_primer_gc)

        self.av_primer_self_dimer = (self.left_primer_self_dimer + self.right_primer_self_dimer) / 2
        self.primer_self_dimer_list.append(self.av_primer_self_dimer)

        self.av_primer_hairpin = (self.left_primer_hairpin + self.right_primer_hairpin) / 2
        self.primer_hairpin_list.append(self.av_primer_hairpin)

        self.data_sumup = self.av_primer_self_dimer + self.av_primer_hairpin

        return self.data_sumup


    def reorder(self,records):
        for self.record_1_index in range(0,len(records)-1):
            self.record_1=records[self.record_1_index]
            for self.record_2_index in range(self.record_1_index+1, len(records)):
                self.record_2=records[self.record_2_index]
                if self.record_1[0]==self.record_2[0]:
                    if self.Get_data(self.record_1) < self.Get_data(self.record_2):
                        records[self.record_1_index], records[self.record_2_index] =records[self.record_2_index], records[self.record_1_index]
                    else:
                        pass
                else:
                    break
        return records

    def Getpara(self):
        with open('para.txt') as para:
            self.alllines = para.readlines()
            for self.para_index, self.para_line in enumerate(self.alllines):
                self.seperate = self.para_line.split(':')
                if 'PRIMER_MIN_SIZE' in self.para_line:
                    self.primer_min_size = self.seperate[-1]
                    if self.primer_min_size[-1] == '\n':
                        self.primer_min_size = self.primer_min_size[0:-1]
                    else:
                        pass
                if 'PRIMER_MAX_SIZE' in self.para_line:
                    self.primer_max_size = self.seperate[-1]
                    if self.primer_max_size[-1] == '\n':
                        self.primer_max_size = self.primer_max_size[0:-1]
                    else:
                        pass
                if 'PRODUCT_SIZE_RANGE' in self.para_line:
                    self.product_size = self.seperate[-1]
                    if self.product_size[-1] == '\n':
                        self.product_size = self.product_size[0:-1]
                    else:
                        pass

    def Run_Primer3(self):

        self.Getpara()

        with open(self.template_file) as seq:
            
            self.id_list=[]

            for self.line in seq:

                if '>' in self.line:
                    self.template_id = self.line
                    self.template_seq = seq.readline()
                    self.id_list.append(str(self.template_id))

                else:
                    pass

                with open(self.parameters_file, "a+") as para:

                    for pair in range(0, len(Generate_Consensus_Find_Conserved_Region.position_pair)):

                        para.write("SEQUENCE_ID=" + str(self.template_id) +

                                   'SEQUENCE_TEMPLATE=' + str(self.template_seq) +

                                   # 'PRIMER_MAX_HAIRPIN_TH=0' + '\n' +
                                   #
                                   # 'PRIMER_PAIR_MAX_COMPL_ANY_TH=0' + '\n' +
                                   #
                                   # 'PRIMER_MAX_SELF_ANY_TH=0' + '\n' +
                                       
                                   'PRIMER_NUM_RETURN=1' + '\n' +

                                   'PRIMER_MIN_SIZE=' + self.primer_min_size + '\n' +

                                   'PRIMER_MAX_SIZE=' + self.primer_max_size + '\n' +

                                   'PRIMER_PRODUCT_SIZE_RANGE=' + self.product_size + '\n' +

                                   'SEQUENCE_PRIMER_PAIR_OK_REGION_LIST=' +

                                   str(Generate_Consensus_Find_Conserved_Region.position_pair[pair][0]) + ',' +

                                   '50' + ',' +

                                   str(Generate_Consensus_Find_Conserved_Region.position_pair[pair][1]-35) + ',' +

                                   '50' + '\n' +

                                   'PRIMER_THERMODYNAMIC_PARAMETERS_PATH=./primer3/src/primer3_config/' + '\n' +

                                   "=" + '\n'
                                   )

        self.args = ['./primer3/src/primer3_core',
                    '--format_output',
                    '--output',self.primers_file,
                     self.parameters_file]

        subprocess.run(self.args)

        with open(self.primers_file) as pris:
            self.record_positions_list = []
            self.line_list = pris.readlines()
            for self.index, self.line in enumerate(self.line_list):
                if 'PRIMER PICKING RESULTS FOR' in self.line:
                    self.record_positions_list.append(self.index)
                else:
                    pass

            self.length_list = []
            for self.start_position in range(0,len(self.record_positions_list)-1):
                self.end_position=self.start_position+1
                self.length_list.append(self.record_positions_list[self.end_position] - self.record_positions_list[self.start_position])

            self.filtered_record_list = []
            self.filtered_list=[]
            for self.filtered_start_position in range(0, len(self.record_positions_list)-1):
                self.filtered_end_position=self.filtered_start_position+1
                if self.record_positions_list[self.filtered_end_position] - self.record_positions_list[self.filtered_start_position] > numpy.mean(self.length_list):
                    self.filtered_record_list.append(''.join(self.line_list[self.record_positions_list[self.filtered_start_position]:self.record_positions_list[self.filtered_end_position]]))
                    self.filtered_list.append(self.line_list[self.record_positions_list[self.filtered_start_position]:self.record_positions_list[self.filtered_end_position]])
                else:
                    pass

        self.count=0
        for self.id in self.id_list:
            self.family=self.id.split('|')[-1][0:3]
            if self.id in ''.join(self.filtered_record_list):
                self.count=self.count+1
               
        if self.count==len(self.id_list):

            self.reordered_list=self.reorder(self.filtered_list)
            self.filtered_reordered_list=self.Remove_repeat(self.reordered_list)

            with open(self.primers_file,'w') as fpri:
                for self.filtered_record in self.filtered_reordered_list:
                    fpri.write(''.join(self.filtered_record))

            self.primer_tm_list = []
            self.left_primer_tm_list = []
            self.right_primer_tm_list = []
            self.primer_gc_list = []
            self.left_primer_gc_list = []
            self.right_primer_gc_list = []
            self.primer_hairpin_list = []
            self.left_primer_hairpin_list = []
            self.right_primer_hairpin_list = []
            self.primer_self_dimer_list = []
            self.left_primer_self_dimer_list = []
            self.right_primer_self_dimer_list = []
            self.left_primer_seq_list = []
            self.right_primer_seq_list = []
            self.left_primer_startp_list = []
            self.right_primer_startp_list = []
            self.left_primer_len_list = []
            self.right_primer_len_list = []
            self.geneid_list=[]
            self.record_start_index_list = []
            self.record_end_index_list = []
            self.newrecord_list=[]
            
            with open(self.primers_file) as file:
                self.allnewlines=file.readlines()
                for self.new_index, self.new_line in enumerate(self.allnewlines):
                    if 'PRIMER PICKING RESULTS FOR' in self.new_line:
                        self.record_start_index_list.append(self.new_index)
                        self.idline=self.new_line.split(' ')[-1]
                        self.geneid=self.idline.split('|')[-1][0:-1]
                        self.geneid_list.append(self.geneid)
                    if 'right primer' in self.new_line:
                        self.record_end_index_list.append(self.new_index)
                for self.record_number in range(0, len(self.record_start_index_list)):
                    self.newrecord=self.allnewlines[self.record_start_index_list[self.record_number]:self.record_end_index_list[self.record_number]]
                    self.Get_data(self.newrecord)
                
            self.dir_path = os.path.dirname(os.path.realpath(self.primers_file))
            self.workbook = xlsxwriter.Workbook(self.dir_path+'/'+self.family+'_primer_datas.xlsx')
            self.worksheet = self.workbook.add_worksheet()
            
            self.row=1
            self.worksheet.write(0, 0, 'Gene')
            for self.gene_id in self.geneid_list:
                self.worksheet.write(self.row, 0, self.gene_id)
                self.row=self.row+1

            self.row=1
            self.worksheet.write(0, 1, 'Left Primer Start Position')
            for self.leftprimerp in self.left_primer_startp_list:
                self.worksheet.write(self.row,1, self.leftprimerp)
                self.row = self.row+ 1

            self.row=1

            self.worksheet.write(0, 2, 'Left Primer Length')
            for self.l_primer_length in self.left_primer_len_list:
                self.worksheet.write( self.row,2, self.l_primer_length)
                self.row= self.row +1

            self.row=1
            self.worksheet.write(0, 3, 'Left Primer Tm Value')
            for self.l_primer_tm in self.left_primer_tm_list:
                self.worksheet.write(self.row,3, self.l_primer_tm)
                self.row = self.row +1

            self.row=1
            self.worksheet.write(0, 4, 'Left Primer GC %')
            for self.l_primer_gc in self.left_primer_gc_list:
                self.worksheet.write(self.row,4, self.l_primer_gc)
                self.row = self.row +1
            self.row=1
            self.worksheet.write(0, 5, 'Left Primer Dimer value')
            for self.l_primer_dimer in self.left_primer_self_dimer_list:
                self.worksheet.write(self.row,5, self.l_primer_dimer)
                self.row = self.row+1

            self.row=1
            self.worksheet.write(0, 6, 'Left Primer Hairpin value')
            for self.l_primer_hairpin in self.left_primer_hairpin_list:
                self.worksheet.write(self.row,6, self.l_primer_hairpin)
                self.row = self.row +1
            self.row=1
            self.worksheet.write(0, 7, 'Left Primer seq')
            for self.l_primer_seq in self.left_primer_seq_list:
                self.worksheet.write(self.row,7, self.l_primer_seq)
                self.row = self.row+1
            self.row=1
            self.worksheet.write(0, 8, 'Right Primer Start Position')
            for self.r_primer_startp in self.right_primer_startp_list:
                self.worksheet.write(self.row,8, self.r_primer_startp)
                self.row = self.row+1
            self.row=1
            self.worksheet.write(0, 9, 'Right Primer Length')
            for self.r_primer_len in self.right_primer_len_list:
                self.worksheet.write(self.row,9, self.r_primer_len)
                self.row= self.row +1
            self.row=1
            self.worksheet.write(0, 10, 'Right Primer Tm Value')
            for self.r_primer_tm in self.right_primer_tm_list:
                self.worksheet.write(self.row,10, self.r_primer_tm)
                self.row = self.row+1

            self.row=1
            self.worksheet.write(0, 11, 'Right Primer GC %')
            for self.r_primer_gc in self.right_primer_gc_list:
                self.worksheet.write(self.row,11, self.r_primer_gc)
                self.row = self.row+1

            self.row=1
            self.worksheet.write(0, 12, 'Right Primer Dimer value')
            for self.r_primer_dimer in self.right_primer_self_dimer_list:
                self.worksheet.write(self.row,12, self.r_primer_dimer)
                self.row = self.row +1

            self.row=1
            self.worksheet.write(0, 13, 'Right Primer Hairpin value')
            for self.r_primer_hairpin in self.right_primer_hairpin_list:
                self.worksheet.write(self.row,13, self.r_primer_hairpin)
                self.row = self.row +1

            self.row=1
            self.worksheet.write(0, 14, 'Right Primer seq')
            for self.r_primer_seq in self.right_primer_seq_list:
                self.worksheet.write(self.row,14, self.r_primer_seq)
                self.row = self.row +1
            self.row=1                    

            self.workbook.close()
            
            self.textbox.insert(INSERT,'Program finished, you can get your results from'+ self.primers_file+'\n')
        else:
            self.textbox.insert(INSERT,'Some primers are not generated!'+'\n')

    def creat_graph(self):
        import matplotlib.pyplot as plt
        import matplotlib.ticker as plticker
        import matplotlib
        import numpy as np
        plt.plot(range(len(self.geneid_list)),self.primer_tm_list,'c.',label='Tm', markersize=6)
        plt.plot(range(len(self.geneid_list)),self.primer_gc_list,'g.',label='GC%', markersize=6)
        plt.plot(range(len(self.geneid_list)),self.primer_hairpin_list,'r.',label='Hairpin', markersize=10)
        plt.plot(range(len(self.geneid_list)),self.primer_self_dimer_list,'y.',label='Self_dimer', markersize=8)
        leg=plt.legend(loc='upper right')
        plt.title('The quality of primers of IMP')
        plt.ylabel('The sum of dimer and hairpin value')
        plt.xticks(range(len(self.geneid_list)),self.geneid_list,rotation=90)
        matplotlib.figure.Figure(figsize=(25,20))
        plt.tight_layout()
        plt.savefig(self.dir_path+'/'+self.family+'_primer_quality.png',dpi=1200)        
        plt.clf()

app = PrimerDesigner()
app.title('PrimerDesigner')
app.mainloop()
