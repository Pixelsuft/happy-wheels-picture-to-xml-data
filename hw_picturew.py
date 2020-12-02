from sys import argv

log_prefix='Log'

try:
    def log(text):
        print(str('[')+str(log_prefix)+str(']')+str(' ')+str(text)+str(';'))
    
    print('Press Ctrl+C to Quit\n\n\n')
    
    log(f'Starting "{argv[0]}"')
    
    log('Importing Pillow...')
    try:
        from PIL import Image as PIL_Image, ImageColor
    except:
        if input('Pillow is not installed. Install it? [y/n]: ')=='y':
            log('Installing Pillow')
            exit()
        else:
            log('Download Canceled, Exiting...')
            exit()
    
    log('Importing File Exists...')
    from os import access as file_exists
    from os import F_OK as exists_param
    
    log('Importing Themed TKinter...')
    try:
        from ttkthemes import themed_tk as tk
    except:
        if input('Themed tk is not installed. Install it? [y/n]: ')=='y':
            log('Installing Themed tk')
            exit()
        else:
            log('Download Canceled, Exiting...')
            exit()
    log('Importing TTK...')
    try:
        from tkinter import ttk
        
        log('Importing All From TTK...')
        from tkinter.ttk import *
        
        log('Importing Message Box...')
        from tkinter import messagebox
        
        log('Importing File Dialog...')
        from tkinter import filedialog
    except:
        if input('TKinter is not installed. Install it? [y/n]: ')=='y':
            log('Installing TKinter')
            exit()
        else:
            log('Download Canceled, Exiting...')
            exit()
    
    log('')
    log('Creating Window:')
    log('Creating Root...')
    root = tk.ThemedTk()
    log('Changing Title...')
    root.title('Happy Wheels Picture Level Data Generator')
    log('Loading Icon...')
    try:
        root.iconbitmap('data\\icon.ico')
        log('Icon Loaded!')
    except:
        log('Icon Don\'t Loaded!')
    log('Changing Resulution...')
    root.geometry('640x480')
    log('Changing To Unresizeable...')
    log('')
    root.resizable(False, False)
    
    log('Creating Input "Open File Name"')
    file_open_input = ttk.Entry(root, font=('Segoe UI', 12))
    
    log('Placing Input "Open File Name"')
    file_open_input.place(x=5,y=5, width=490, height=40)
    
    log('Creating Input "Save File Name"')
    file_save_input = ttk.Entry(root, font=('Segoe UI', 12))
    
    log('Placing Input "Save File Name"')
    file_save_input.place(x=5,y=50, width=490, height=40)
    
    log('Creating Label "Down Grade"')
    label_downgrade = ttk.Label(root, text='DownGrade:',background='#f0f0f0', font=('Segoe UI', 16))
    
    log('Placing Label "Down Grade"')
    label_downgrade.place(x=265,y=95, width=200, height=40)
    
    log('Creating Label "X For DownGrade"')
    labelx_downgrade = ttk.Label(root, text='X',background='#f0f0f0', font=('Segoe UI', 15))
    
    log('Placing Label "X For DownGrade"')
    labelx_downgrade.place(x=312,y=140, width=16, height=40)
    
    log('Creating Input "DownGrade X"')
    x_down_input = ttk.Entry(root, font=('Segoe UI', 22))
    
    log('Placing Input "DownGrade X"')
    x_down_input.place(x=5,y=140, width=304, height=40)
    
    x_down_input.insert(0,'2')
    
    log('Creating Input "DownGrade Y"')
    y_down_input = ttk.Entry(root, font=('Segoe UI', 22))
    
    log('Placing Input "DownGrade Y"')
    y_down_input.place(x=331,y=140, width=304, height=40)
    
    y_down_input.insert(0,'2')
    
    log('Creating Label "Shape Size"')
    shape_size_label = ttk.Label(root, text='Shape Size (5 - min):',background='#f0f0f0', font=('Segoe UI', 16))
    
    log('Placing Bugged Label "Shape Size"')
    shape_size_label.place(x=227,y=269, width=200, height=40)# Y bugged, i'm don't now about it
    
    log('Creating Label "Chroma Key"')
    label_ck = ttk.Label(root, text='Chroma Key:',background='#f0f0f0', font=('Segoe UI', 16))
    
    log('Placing Label "Chroma Key"')
    label_ck.place(x=263,y=185, width=200, height=40)
    
    log('Creating Input "Chroma Key"')
    chroma_input = ttk.Entry(root, font=('Segoe UI', 22))
    
    log('Placing Input "Chroma Key"')
    chroma_input.place(x=5,y=230, width=630, height=40)
    
    chroma_input.insert(0,'rgb (0, 0, 0)')
    
    log('Creating Label "X For Shape Size"')
    labelx_shape = ttk.Label(root, text='X',background='#f0f0f0', font=('Segoe UI', 15))
    
    log('Placing Label "X For Shape Size"')
    labelx_shape.place(x=312,y=310, width=16, height=40)
    
    log('Creating Input "Shape Size X"')
    x_shape_input = ttk.Entry(root, font=('Segoe UI', 22))
    
    log('Placing Input "Shape Size X"')
    x_shape_input.place(x=5,y=310, width=304, height=40)
    
    x_shape_input.insert(0,'5')
    
    log('Creating Input "Shape Size Y"')
    y_shape_input = ttk.Entry(root, font=('Segoe UI', 22))
    
    log('Placing Input "Shape Size Y"')
    y_shape_input.place(x=331,y=310, width=304, height=40)
    
    y_shape_input.insert(0,'5')
    
    def generateb_def():
        log('Checking Values...')
        try:
        #if True:
            chroma_type=-1
            chroma_key=''
            
            for_ck=chroma_input.get().replace(' ','').replace(' ','').replace('(',' ').replace(')',' ').replace(',',' ')
            if for_ck=='':
                chroma_type=-1
                chroma_key=''
            elif for_ck[0]=='#':
                chroma_type=0
                chroma_key=for_ck[1:len(for_ck)]
            else:
                for_cyl=for_ck.split(' ')
                log(f'{for_cyl}')
                for i in range(len(for_cyl)):
                    if i==0:
                        if for_cyl[0]=='rgb':
                            chroma_type=1
                        elif for_cyl[0]=='rgba':
                            chroma_type=2
                        elif for_cyl[0]=='hw':
                            chroma_type=3
                        else:
                            chroma_type=-1
                            break
                    elif i==1:
                        chroma_key=for_cyl[1]
                    else:
                        chroma_key+=' '+for_cyl[i]
            log(f'Chroma Type Is "{chroma_type}"')
            log(f'Chroma Key Is "{chroma_key}"')
            x_downgrade=int(x_down_input.get())
            y_downgrade=int(y_down_input.get())
            x_size=int(x_shape_input.get())
            y_size=int(y_shape_input.get())
            log('All OK!')
            generate_def(x_downgrade, y_downgrade, chroma_type, chroma_key, x_size, y_size)
        except:
            log('Error With Values!')
            messagebox.showerror('Error!',f'Error with values!')
    
    log('Creating Generate Function')
    def generate_def(x_downgrade, y_downgrade, chroma_type, chroma_key, x_size, y_size):
        log('Generate Function Called')
        image_file_name = file_open_input.get()
        log(f'Picture file is "{image_file_name}"')
        data_file_name = file_save_input.get()
        log(f'Data file is "{data_file_name}"')
        try:
            if data_file_name[::-1][0]=='t' and data_file_name[::-1][1]=='x' and data_file_name[::-1][2]=='t' and data_file_name[::-1][3]=='.':
                log(f'File "{data_file_name}" Is Already Text File!')
            else:
                log(f'File "{data_file_name}" Is Not Text File!')
                data_file_name+='.txt'
                log(f'File "{data_file_name}" Is Already Text File!')
        except:
            log(f'File "{data_file_name}" Is Not Text File!')
            log('Index Is Out Of Range, Adding .txt On The End')
            data_file_name+='.txt'
            log(f'File "{data_file_name}" Is Already Text File!')
        log('Opening Image...')
        if file_exists(image_file_name, mode=exists_param)==True:
            try:
            #if True:
                imag = PIL_Image.open(f'{image_file_name}')
                width, height=imag.size
                level_data='<levelXML><info v="1.87" x="121.35" y="67.7" c="11" f="t" h="f" bg="1" bgc="16777215" e="1"/><groups><g x="150" y="50" r="0" ox="-150" oy="-50" s="f" f="t" o="100" im="f" fr="f">'
                alphable=False
                log('Checking For Alpha...')
                try:
                    a,b,c,d=imag.getpixel((1,1))
                    alphable=True
                    log('Alpha Detected!')
                except:
                    alphable=False
                    log('No Alpha Detected!')
                log('Generating Data...')
                skip_x=0
                skip_y=0
                rgb_a=[]
                if chroma_type==1 or chroma_type==2 or chroma_type==3:
                    log(chroma_key)
                    rgb_a=chroma_key.split(' ')
                    log(rgb_a)
                otvet_a=''
                if alphable==True:
                    otvet_a=messagebox.askquestion('Question!',f'File {image_file_name} has alpha. It\'s BETA!\nContinue?')
                if alphable==False or otvet_a=='yes':
                    for for_x in range(width):
                        if skip_x==for_x:
                            skip_y=0
                            for for_y in range(height):
                                if skip_y==for_y:
                                    if alphable==False:
                                        r,g,b = imag.getpixel((for_x,for_y))
                                        rgb10=(r*65536)+(g*256)+(b)
                                        cancont=False
                                        if chroma_type==-1:
                                            cancont=True
                                        elif chroma_type==0:
                                            fr,fg,fb=ImageColor.getcolor(str(f'#{chroma_key}'), "RGB")
                                            if fr==int(rgb_a[0]) and fg==int(rgb_a[1]) and fb==int(rgb_a[2]):
                                                cancont=False
                                            else:
                                                cancont=True
                                        elif chroma_type==1 or chroma_type==2:
                                            if r==int(rgb_a[0]) and g==int(rgb_a[1]) and b==int(rgb_a[2]):
                                                cancont=False
                                            else:
                                                cancont=True
                                        elif chroma_type==3:
                                            if rgb10==int(rgb_a[0]):
                                                cancont=False
                                            else:
                                                cancont=True
                                        if cancont==True:
                                            level_data+=f'<sh t="0" i="f" p0="{for_x+3}" p1="{for_y+3}" p2="{x_size}" p3="{y_size}" p4="0" p5="t" p6="f" p7="1" p8="{rgb10}" p9="-1" p10="100" p11="1"/>'
                                    else:
                                        r,g,b,a = imag.getpixel((for_x,for_y))
                                        rgb10=(r*65536)+(g*256)+(b)
                                        cancont=False
                                        if chroma_type==-1:
                                            cancont=True
                                        elif chroma_type==0:
                                            fr,fg,fb=ImageColor.getcolor(str(f'#{chroma_key}'), "RGB")
                                            if fr==int(rgb_a[0]) and fg==int(rgb_a[1]) and fb==int(rgb_a[2]):
                                                cancont=False
                                            else:
                                                cancont=True
                                        elif chroma_type==1:
                                            if r==int(rgb_a[0]) and g==int(rgb_a[1]) and b==int(rgb_a[2]):
                                                cancont=False
                                            else:
                                                cancont=True
                                        elif chroma_type==2:
                                            if r==int(rgb_a[0]) and g==int(rgb_a[1]) and b==int(rgb_a[2]) and a==int(rgb_a[3]):
                                                cancont=False
                                            else:
                                                cancont=True
                                        elif chroma_type==3:
                                            if rgb10==int(rgb_a[0]):
                                                cancont=False
                                            else:
                                                cancont=True
                                        if cancont==True:
                                            level_data+=f'<sh t="0" i="f" p0="{for_x+3}" p1="{for_y+3}" p2="9" p3="7" p4="0" p5="t" p6="f" p7="1" p8="{rgb10}" p9="-1" p10="100" p11="1"/>' 
                                    skip_y+=y_downgrade
                            skip_x+=x_downgrade
                    level_data+='</g></groups></levelXML>'
                    log('Data Generated!')
                    can=True
                    log('Checking Exists...')
                    if file_exists(data_file_name, mode=exists_param)==True:
                        log(f'File {data_file_name} is already exists.')
                        otvet=messagebox.askquestion('Question!',f'File {data_file_name} is already exists. Replace it?')
                        if otvet=='yes':
                            can=True
                            log(True)
                        else:
                            can=False
                            log(False)
                    if can==True:
                        log('Opening File...')
                        file=open(data_file_name,'w')
                        log('Writing Lines...')
                        file.write(level_data)
                        log('Closing File...')
                        file.close()
                    else:
                        log('Operation Canceled!')
            except:
                log('Error With File!')
                messagebox.showerror('Error!',f'Error with file!!')
        else:
            if str(image_file_name)=='':
                log('Empty Image Path')
                messagebox.showerror('Error!',f'Image path is empty!')
            else:
                log(f'Image "{image_file_name}" Is Not Exists!')
                messagebox.showerror('Error!',f'Image "{image_file_name}" is not exists!')
    
    
    log('Creating Open Picture Dialog Function')
    def open_picture_dialog_def():    
        log('Open Picture Dialog Function Called')
        file_name=filedialog.askopenfile(
            parent=root,
            title='Open picture',
            filetypes=[("All files (*.*)", "*.*")]
        )
        try:
            log(f'Picture "{file_name.name}" Selected!')
            try:
                file_open_input.delete(0, len(file_open_input.get()))
                file_open_input.insert(0, file_name.name)
            except:
                log(f'Failed To Delete And Insert {file_name.name}')
        except:
            log('No picture selected')
        
    log('Creating Open Picture Dialog Function')
    def save_file_dialog_def():    
        log('Save Level Data Dialog Function Called')
        file_name=filedialog.asksaveasfilename(
            parent=root,
            title='Level Data File',
            filetypes=[("Text files (*.txt)", "*.txt")]
        )
        if not file_name=='':
            log(f'File "{file_name}" Will Be Saved!')
            try:
                file_save_input.delete(0, len(file_save_input.get()))
                file_save_input.insert(0, file_name)
            except:
                log(f'Failed To Delete And Insert {file_name}')
        else:
            log('No file selected')
    
    log('Creating Button "Open File Name"')
    select_picture = ttk.Button(root, text="Select Picture", command=open_picture_dialog_def)
    
    log('Placing Button "Open File Name"')
    select_picture.place(x=500, y=5, width=135, height=40)
    
    log('Creating Button "Save File Name"')
    select_data = ttk.Button(root, text="Select File To Save Data", command=save_file_dialog_def)
    
    log('Placing Button "Save File Name"')
    select_data.place(x=500, y=50, width=135, height=40)
    
    log('Creating Button "Generate"')
    select_data = ttk.Button(root, text="Generate!", command=generateb_def)
    
    log('Placing Button "Generate"')
    select_data.place(x=5, y=435, width=630, height=40)
    
    log('Setting Windows XP Theme...')
    root.set_theme('winxpblue')
    
    log('Starting Main Loop...')
    root.mainloop()
    
    log('Good, bye!')
except KeyboardInterrupt:
    log('\nCtrl+C Pressed, Exiting...\n')