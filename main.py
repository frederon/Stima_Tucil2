import time
from dearpygui.core import *
from dearpygui.simple import *

from FileController import FileController, export
from Graph import Graph, topologicalSort
from Logger import Logger
from utils import number_to_roman, get_max_rows, get_row

logger = Logger("primary")

toExport = []

def theme_callback(sender, data):
    set_theme(sender)

def file_picker(sender, data):
    open_file_dialog(callback=process_selected_file, extensions=".txt")

def directory_picker(sender, data):
    select_directory_dialog(process_file_export)

def process_file_export(sender, data):
    directory = data[0]
    selected_folder = data[1]
    if selected_folder in directory:
        output_directory = directory
    else:
        output_directory = '\\'.join(data)

    export(output_directory, toExport)
    logger.add_log("Export success!")


def process_selected_file(sender, data):
    log_debug(data)

    directory = data[0]
    file = data[1]
    filePath = f"{directory}\\{file}"

    set_value("file_path", filePath)

    fc = FileController(filePath)
    g = Graph(fc.data)

    logger.add_log(f"{data[1]} has been loaded!", color=(46, 204, 113))

    startTime = time.time()

    result = topologicalSort(g.data, [])

    endTime = time.time()

    toExport.append([file, result])

    with window(file, autosize=True, horizontal_scrollbar=True):
        sem = range(1, len(result) + 1)
        add_table("table_" + file, ["Semester " +
                                    number_to_roman(s) for s in sem], width=100*len(sem))

        max_row = get_max_rows(result)
        for i in range(max_row):
            add_row("table_" + file, [res for res in get_row(result, i)])


    logger.add_log(
        "{} - Total waktu: {:.5f} detik".format(file, endTime-startTime))

with window("about.txt", width=350, height=100, x_pos=835, y_pos=15, no_close=True, no_resize=True) as aboutgui:
    add_text("Tugas Kecil 2", color=(255, 195, 0))
    add_text("IF2551 - Strategi Algoritma")
    add_spacing()
    add_text("By: Frederic Ronaldi - 13519134")

with window("primary", width=300, height=200, x_pos=0, y_pos=0) as primarygui:
    add_text("Logs: ", color=(52, 152, 219))

    add_menu_bar("MenuBar", parent="primary")

    add_menu("File")
    add_menu_item("Open file", callback=file_picker)
    add_menu_item("Export all", callback=directory_picker)
    end()

    add_menu("Themes")
    add_menu_item("Dark", callback=theme_callback)
    add_menu_item("Light", callback=theme_callback)
    add_menu_item("Classic", callback=theme_callback)
    add_menu_item("Dark 2", callback=theme_callback)
    add_menu_item("Grey", callback=theme_callback)
    add_menu_item("Dark Grey", callback=theme_callback)
    add_menu_item("Cherry", callback=theme_callback)
    add_menu_item("Purple", callback=theme_callback)
    add_menu_item("Gold", callback=theme_callback)
    add_menu_item("Red", callback=theme_callback)
    end()

    add_button("Clear Logs", callback=logger.clear_logs)
    end()

set_main_window_title("Matcool")
set_main_window_size(1200, 900)

start_dearpygui(primary_window="primary")
