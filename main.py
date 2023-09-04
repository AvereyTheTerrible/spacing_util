import tkinter as tk
import tkinter.ttk as ttk
from model import Model

lbl_list = []


def run():
    for lbl in lbl_list:
        lbl[0].destroy()
        lbl[1].destroy()
    target = float(ent_target.get())
    m = Model([0.015625, 0.03125, 0.04, 0.125, 0.25, 0.375, 0.5, 0.875])
    res = m.solve(target=target)
    val = ""
    row = 1
    for pair in res:
        if int(pair[1]) == 0:
            continue

        lbl_res_front = ttk.Label(
            master=window,
            text=f"{pair[0]} in: ",
            font=("Courier", 8, "bold"),
            justify=tk.LEFT,
            anchor="w",
        )
        lbl_res_front.grid(sticky="w", row=row, column=0, padx=15, pady=2)
        lbl_res = ttk.Label(
            master=window, text=f"{int(pair[1])}", justify=tk.LEFT, anchor="w"
        )
        lbl_res.grid(sticky="w", row=row, column=1, pady=2)
        lbl_list.append((lbl_res_front, lbl_res))
        row += 1


window = tk.Tk()
window.title("SPACEr")
frm_entry = ttk.Frame(master=window)
ent_target = ttk.Entry(master=frm_entry, width=20)
lbl_target = ttk.Label(master=frm_entry, text="in")
ent_target.grid(row=0, column=0, sticky="e")
lbl_target.grid(row=0, column=1, sticky="w")


btn_run = ttk.Button(master=window, text="Go!", command=run)

frm_entry.grid(row=0, column=0, padx=15)
btn_run.grid(row=0, column=1, pady=15)

window.mainloop()
