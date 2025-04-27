from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk, Entry, Label, filedialog



#Funktionen

# bild erzeugen und für die GUI kompatibel machen
def bild_zeigen():
    global tk_img # damit das bild auch mal angezeigt wird auf der GUI
    global neue_bild
    global breite
    global höhe 
    global Label1
    global tk_img

    breite = int(Eingabe1.get())
    höhe = int(Eingabe2.get())
    
    neue_bild = Image.open("hier kommt die bild datei rein, am besten jpg format, erstmals") # bild öffnen 
    neue_bild = neue_bild.resize((breite, höhe)) #bild skalieren
    
    tk_img = ImageTk.PhotoImage(neue_bild) #für tkinter kompatibel machen und in neue var packen

    # bild wird angezeigt
    Label1 = ttk.Label(frm, image=tk_img)# bild wird 
    Label1.configure(image=tk_img)
    Label1.grid(column=0, row=0)
    
# Datei speichern
def speichern():
    global Eingabespeicher
    filename = Eingabespeicher.get()
    try:
        if neue_bild.info == True: # Falls Metadaten vorhanden sind, bitte löschen ansonsten passen
            del neue_bild.info["exif"]
    except Exception as e:
        print(f"Findet keine Infos: {e}")
    else: pass
    try: #try exept, kurz vorm Verzweifeln, weil der Fehler keyError mich nicht in Ruhe lässt
        if not filename.endswith((",jpg", ".png")):
            filename += ".jpg"
        else: pass
        neue_bild.save(filename) # Bild speichern ohne Metadaten 
    except Exception as e:
        print(f"Fehler beim speichern: {e}")


# erstmal ignorieren
"""
def Datei():
    try:
        
        Auswahl = filedialog.askopenfile(title="Bild auswählen", filetypes=[("Bilddateien", "*.jpg *.png")]
                                         
                                         )
        if Auswahl.empty == False:
            img = Image.open(Auswahl)
            Label1.configure(image=tk_img)
            Label1.image = tk_img 
        else: print(info)   # eventinfo unten  abgespeichert     

    except Exception as e: print(f"Fehler: {e}")
"""

skal = tk.Tk()

#Main  

#GUI
frm = ttk.Frame(skal, padding=150)
frm.grid()



Label(skal, text="Bitte geben Sie die breite an").grid(column=0, row=1)
Label(skal, text="Bitte geben Sie die Höhe an").grid(column=0, row=2)
Label(skal, text="Dateiname:").grid(column=0, row=3)
#info = Label.event_info.(skal, ).grid(column=0, row=3) # ignorieren

speichern1 = ttk.Button(frm, text="speichern", command=speichern)
speichern1.grid(column=0, row=3)

Eingabespeicher = Entry(skal)
Eingabespeicher.grid(column=1, row=3)

Eingabe1 = Entry(skal)
Eingabe2 = Entry(skal)
Eingabe1.grid(column=1, row=1)
Eingabe2.grid( column=1, row=2)

button1 = ttk.Button(frm, text="anzeigen", command=bild_zeigen)
button2 = ttk.Button(frm, text="beenden", command=skal.destroy)
button1.grid(column=2, row=4)
button2.grid(column=3, row=4)

Auswahl = ttk.Button(frm, text="Datei auswählen", command=Datei)
Auswahl.grid(column=0, row=6)


skal.mainloop()



