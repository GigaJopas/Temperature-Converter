import tkinter as tk
import pyperclip
import random

root = tk.Tk()
root.title('Temperature Converter') 
root.geometry('400x335')
root.resizable(False, False)
root.configure(bg="#F3FFAA")

scale_value = True

frame_tc = tk.Frame(root, bg='#F3FFAA', width=400, height=335)

frame_tc.pack(side='top')

root.title('Temperature Calculator') 

def switchall():
	global scale_value
	if scale_value == True:
		scale_value = False
	elif scale_value == False:
		scale_value = True

switch = tk.Button(frame_tc, text='SWITCH SCALES', font=("Arial, 12"), bg="#D8E298", fg='black', command=switchall, pady=13)

intro = tk.Label(frame_tc, text='Enter degrees Celcius:', font=("Arial", 17), bg="#F3FFAA", fg='black',
 height=2, width=40)
intro.pack()

entry1 = tk.Entry(frame_tc, width=20, font=("Arial", 12, ), bg="#D8E298", relief='sunken')
entry1.pack()

outro = tk.Label(frame_tc, text='...in degrees Fahrenheit is:', font=("Arial", 17), bg="#F3FFAA", fg='black',
 height=2, width=40)
outro.pack()

def switching():
	global scale_value
	if scale_value == True:
		intro.config(text='Enter degrees Fahrenheit:')
		outro.config(text='...in degrees Celcius is')
		scale_value = False
	elif scale_value == False:
		intro.config(text='Enter degrees Celcius:')
		outro.config(text='...in degrees Fahrenheit is')
		scale_value = True

switch.config(command=switching)

def on_enter(event):
	if scale_value == True:
		print('true')
		user_input = entry1.get()
		entry1.get()
		onpointeigh = float(1.8)
		try:
			input_degree = int(user_input)
			input_degree *= onpointeigh
			cnv_fahrenheit = input_degree + 32
			end_frnh = str(cnv_fahrenheit)
			print(end_frnh)
			label3.config(text=(end_frnh))

			def copy_t():
				pyperclip.copy(end_frnh)
			copy_temp = tk.Button(frame_tc, text='copy to clipboard', bg='#D8E298', fg='black', command=copy_t, relief='groove')
			copy_temp.place_forget()
			copy_temp.place(x=149, y=221)
		except ValueError:
			label3.config(text='Enter a number.')
	elif scale_value == False:
		print('false')
		user_input = entry1.get()
		entry1.get()
		try:
			input_degree = int(user_input)
			input_degree -= 32
			dividfiv = input_degree * 5
			cnv_calcius = dividfiv / 9
			end_calc = str(cnv_calcius)
			print(end_calc)
			label3.config(text=(end_calc))

			def copy_t():
				pyperclip.copy(end_calc)
			copy_temp = tk.Button(frame_tc, text='copy to clipboard', bg='#D8E298', fg='black', command=copy_t, relief='groove')
			copy_temp.place_forget()
			copy_temp.place(x=149, y=221)
		except ValueError:
			label3.config(text='Enter a number.')


	# copy_temp.place_forget()
	# copy_temp.place(x=149, y=221)

label3 = tk.Label(frame_tc, text=' ', font=("Arial", 17), bg="#D8E298", fg='black',
 height=3, width=17, relief='groove')
label3.pack()

label_slop2 = tk.Label(frame_tc, text='', fg='black', height=1, bg='#F3FFAA')
label_slop2.pack()

switch.pack(pady=25)

entry1.bind("<Return>", on_enter)

root.mainloop()