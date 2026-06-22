import platform
import tkinter as tk

import dearpygui.dearpygui as dpg  # type: ignore
from utils.ui_data import (  # type: ignore
    CHILD_HEIGHT,
    CHILD_WIDTH,
    CONTENT_CHILD_WINDOW,
    CONTENT_CHILD_WINDOW_BROWSE_IMAGE_BUTTON,
    CONTENT_CHILD_WINDOW_STATUS_TEXT,
    PRIMARY_WINDOW,
    VIEWPORT_HEIGHT,
    VIEWPORT_WIDTH,
)


def centralize_content() -> None:
    real_window_height = dpg.get_item_rect_size(PRIMARY_WINDOW)[1]
    real_window_width = dpg.get_item_rect_size(PRIMARY_WINDOW)[0]

    child_x = (real_window_width - CHILD_WIDTH) / 2
    child_y = (real_window_height - CHILD_HEIGHT) / 2
    dpg.configure_item(CONTENT_CHILD_WINDOW, pos=[child_x, child_y])

    button_size = dpg.get_item_rect_size(CONTENT_CHILD_WINDOW_BROWSE_IMAGE_BUTTON)
    text_size = dpg.get_item_rect_size(CONTENT_CHILD_WINDOW_STATUS_TEXT)

    button_height = button_size[1]
    button_width = button_size[0]

    text_height = text_size[1]
    text_width = text_size[0]

    button_x = (CHILD_WIDTH - button_width) / 2
    text_x = (CHILD_WIDTH - text_width) / 2

    element_spacing = 16

    total_content_height = text_height + element_spacing + button_height

    start_y = (CHILD_HEIGHT - total_content_height) / 2

    text_y = start_y
    button_y = text_y + text_height + element_spacing

    dpg.configure_item(
        CONTENT_CHILD_WINDOW_BROWSE_IMAGE_BUTTON,
        pos=[button_x, button_y],
    )

    dpg.configure_item(CONTENT_CHILD_WINDOW_STATUS_TEXT, pos=[text_x, text_y])


def centralize_window() -> tuple[int, int]:
    root = tk.Tk()
    root.withdraw()

    screen_height = root.winfo_screenheight()
    screen_width = root.winfo_screenwidth()

    root.destroy()

    return (
        (screen_width - VIEWPORT_WIDTH) // 2,
        (screen_height - VIEWPORT_HEIGHT) // 2,
    )


def dpg_render_loop() -> None:
    is_maximize_disabled = False
    last_height, last_width = 0, 0

    while dpg.is_dearpygui_running():
        if not is_maximize_disabled:
            if dpg.does_item_exist(
                PRIMARY_WINDOW,
            ) and dpg.does_item_exist(
                CONTENT_CHILD_WINDOW,
            ):
                window_size = dpg.get_item_rect_size(PRIMARY_WINDOW)

                if window_size and window_size[0] > 0 and window_size[1] > 0:
                    current_height = window_size[1]
                    current_width = window_size[0]

                    if current_height == last_height and current_width == last_width:
                        if platform.system() == "Windows":
                            from utils.windows import disable_maximize  # type: ignore

                            disable_maximize()

                        is_maximize_disabled = True

                    last_height = current_height
                    last_width = current_width

        centralize_content()

        dpg.render_dearpygui_frame()
