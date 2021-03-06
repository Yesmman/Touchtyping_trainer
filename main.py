import tkinter as tk
import threading as tr
import work_with_database as db
import random
from classes import Typing
import time

typing = Typing()
window = tk.Tk()

label_width = 450

list_of_label = []

q = []


def second_window_form():
    second_window = tk.Tk()
    text_field = tk.Text(second_window,
                         height=5,
                         width=typing.width,
                         font=typing.font)

    text_field.pack(side=tk.TOP)

    f1 = tk.Frame(second_window)
    f1.pack(pady=20)

    def get():
        text_to_load = text_field.get("1.0", "end")
        db.add_text(text_to_load)

    button = tk.Button(f1,
                       text="Load",
                       command=get,
                       bg=typing.buttons_color,
                       font=typing.font)
    button.pack(side=tk.RIGHT)

    exit_button = tk.Button(f1,
                            text="Done",
                            command=second_window.destroy,
                            bg=typing.buttons_color,
                            font=typing.font)

    exit_button.pack(side=tk.RIGHT, padx=30)

    second_window.mainloop()


def thread_start():
    get_text()
    parser(typing.string)

    typing.reset_values()
    t.tag_delete("Done")
    input_text.delete(0, "end")

    thread = tr.Thread(target=check, daemon=True)
    thread.start()


def get_text():
    t.destroy()
    max_id = db.get_id()
    random_number = random.randint(1, max_id)
    typing.string = db.get_text_by_id(random_number)


def labels_from_dict(dict_):
    for item in dict_:
        label = tk.Label(text=f"{item}: {dict_[item]}", font=typing.font)
        label.pack()
        list_of_label.append(label)


def generate_labels():
    destroy_labels_from_list(list_of_label)
    labels_from_dict(dict_=typing.get_result())


def destroy_labels_from_list(list_):
    for labels in list_:
        labels.destroy()


def typing_process(event):
    typing.reset_timer()
    word = input_text.get()
    t["bg"] = typing.background_color
    t["fg"] = "gray"
    t.tag_delete("Active")
    t.tag_add("Active", f"{typing.string_index}.0", f"{typing.string_index}.end")
    t.tag_config("Active", foreground="black")
    text_index = f"{typing.string_index}.{typing.char_index}"
    example = t.get(text_index)

    if word != "":
        if len(word) == len(t.get(f"{typing.string_index}.0", f"{typing.string_index}.{typing.char_index + 1}")):
            if word[typing.char_index] == example:
                typing.char_index += 1
                t.tag_delete("Mistake")
                t.tag_add("Done", text_index)
                t.tag_config("Done", background="PaleGreen1")
            else:
                t.tag_add("Mistake", text_index)
                t.tag_config("Mistake", background="red")
                typing.number_of_mistakes += 1
        if word == t.get(f"{typing.string_index}.0", f"{typing.string_index}.end"):

            for number_ in range(t["height"] - 1):
                number = number_ + 1
                data = t.get(f"{number + 1}.0", f"{number + 1}.end")
                t["state"] = "normal"
                t.delete(f"{number}.0", f"{number}.end")
                t.insert(f"{number}.0", data)

            t.delete(f'{t["height"] - 1}.0', f'{t["height"] - 1}.end')
            t["state"] = "disable"
            t.update()
            window.update()

            typing.char_index = 0
            input_text.delete("0", "end")

        if word == t.get("1.0", "end"):
            get_text()
            parser(typing.string)
            t.tag_delete("Done")
            input_text.delete(0, "end")
            # typing.reset_values()


def check():
    typing.time = 0
    x = window.bind("<Key>", typing_process)
    while True:
        time.sleep(1)
        typing.time += 1
        time_label["text"] = typing.time
        time_label.update()
        if typing.time == 60:
            typing.do_stop()
        if typing.stop:
            window.unbind("<Key>", x)
            break
    generate_labels()


t = tk.Text(width=60,
            height=1,
            font=typing.font,
            wrap="word")


def parser(any_text):
    global t

    t = tk.Text(frame,
                width=60,
                height=1,
                font=typing.font,
                wrap="word")

    word = ""

    l_ = tk.Label(frame,
                  height=1,
                  font=typing.font,
                  bg=typing.buttons_color)
    l_.pack()
    window.update()
    typing.string_index = 1
    count = 0
    c = 0
    c2 = 0
    for char in any_text:

        count += 1
        if char == "\n":
            c += 1
            if c >= 1:
                char = " "
            else:
                char = " "
        if char == " ":
            c2 += 1
            if c2 > 1:
                char = ""
        else:
            c2 = 0
        word += char
        l_.update()
        print(l_.winfo_reqwidth(), l_.winfo_width(), t["width"], l_["width"], l_["text"])

        if char == " " or count == len(any_text):
            l_["text"] += word
            word = ""
            c = 0

        if l_.winfo_width() / 13 >= t["width"] or count == len(any_text):
            text = l_["text"]
            q.append(text)
            t.insert(f"{typing.string_index}.0", text)
            t.insert("end", "\n")
            l_["text"] = ""
            typing.string_index += 1
    l_.destroy()
    t["height"] = typing.string_index
    t["state"] = "disable"
    t.pack(side=tk.TOP)


greeting = tk.Label(text="Hi",
                    font=typing.font)
greeting.pack()

frame = tk.Frame()
frame.pack(side=tk.TOP)

frame_2 = tk.Frame()
frame_2.pack(pady=40)

input_text = tk.Entry(frame_2, width=60, font=typing.font)
input_text.pack(side=tk.TOP, pady=40)

endb = tk.Button(frame_2,
                 text="Click to end",
                 bg=typing.buttons_color,
                 command=typing.do_stop,
                 font=typing.font)
endb.pack(side=tk.RIGHT)

start = tk.Button(frame_2,
                  text="Click to start",
                  bg=typing.buttons_color,
                  command=thread_start,
                  font=typing.font)
start.pack(side=tk.RIGHT, padx=30)

add_text = tk.Button(frame_2,
                     text="Add text to database",
                     command=second_window_form,
                     bg=typing.buttons_color,
                     font=typing.font)
add_text.pack(side=tk.RIGHT)

time_label = tk.Label(text=f"{typing.time}",
                      bg="white",
                      font=typing.font)
time_label.pack()

window.wm_minsize(500, 500)
window.mainloop()
