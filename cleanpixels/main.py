import os
import sys
from tkinter import Tk, filedialog

import dearpygui.dearpygui as dpg  # type: ignore
import image_utils
import theme

IS_WINDOWS = sys.platform == "win32"
SELECTED_FILE_PATH = None


def compress_callback() -> None:
    global SELECTED_FILE_PATH

    if not SELECTED_FILE_PATH:
        dpg.set_value("compressor_status_text", "No file selected")

        return

    try:
        dpg.set_value("compressor_status_text", "Compressing...")

        value_from_slider = dpg.get_value("compressor_quality_slider")
        result = image_utils.compress(SELECTED_FILE_PATH, value_from_slider)

        if result == "":
            dpg.set_value(
                "compressor_status_text", "Kept original (no size reduction achieved)"
            )

        else:
            dpg.set_value("compressor_status_text", "Image compressed!")

    except Exception as e:
        dpg.set_value("compressor_status_text", f"Error: {str(e)}")


def select_file(group: str) -> None:
    global SELECTED_FILE_PATH

    root = Tk()
    root.withdraw()
    root.attributes("-topmost", True)

    file_path = filedialog.askopenfilename(
        filetypes=[("Images", "*.jpeg *.jpg *.png *.webp")],
        title="Select an image",
    )

    root.destroy()

    if file_path:
        SELECTED_FILE_PATH = file_path

        filename = os.path.basename(file_path)

        if group == "compressor_group":
            dpg.set_value("compressor_file_text", filename)
            dpg.show_item("compressor_file_text")

            dpg.show_item("compressor_quality_text")
            dpg.show_item("compressor_quality_slider")
            dpg.show_item("compressor_spacer")

            dpg.show_item("compressor_action_group")

            if image_utils.get_extension(SELECTED_FILE_PATH) in [
                ".jpeg",
                ".jpg",
                ".webp",
            ]:
                dpg.set_value("compressor_quality_text", "Quality")

                dpg.configure_item(
                    "compressor_quality_slider",
                    default_value=80,
                    max_value=92,
                    min_value=46,
                )

            else:
                dpg.set_value("compressor_quality_text", "Compression level")

                dpg.configure_item(
                    "compressor_quality_slider",
                    default_value=6,
                    max_value=8,
                    min_value=4,
                )


def show_group(group: str) -> None:
    dpg.hide_item("compressor_group")
    dpg.hide_item("format_converter_group")
    dpg.hide_item("metadata_stripper_group")

    dpg.show_item(group)

    dpg.bind_item_theme("compressor_sidebar_button", "sidebar_button_theme")
    dpg.bind_item_theme("format_converter_sidebar_button", "sidebar_button_theme")
    dpg.bind_item_theme("metadata_stripper_sidebar_button", "sidebar_button_theme")

    if group == "compressor_group":
        dpg.bind_item_theme("compressor_sidebar_button", "sidebar_active_button_theme")

    elif group == "format_converter_group":
        dpg.bind_item_theme(
            "format_converter_sidebar_button", "sidebar_active_button_theme"
        )

    else:
        dpg.bind_item_theme(
            "metadata_stripper_sidebar_button", "sidebar_active_button_theme"
        )


def main() -> None:
    dpg.create_context()
    dpg.create_viewport(
        height=384,
        max_height=384,
        max_width=640,
        resizable=False,
        title="CleanPixels",
        width=640,
    )

    with dpg.window(tag="primary_window"):
        with dpg.group(horizontal=True):
            # Sidebar
            with dpg.child_window(width=160):
                dpg.add_button(
                    callback=lambda: show_group("compressor_group"),
                    height=40,
                    label="Compressor",
                    tag="compressor_sidebar_button",
                    width=-1,
                )

                dpg.add_button(
                    callback=lambda: show_group("format_converter_group"),
                    height=40,
                    label="Format Converter",
                    tag="format_converter_sidebar_button",
                    width=-1,
                )

                dpg.add_button(
                    callback=lambda: show_group("metadata_stripper_group"),
                    height=40,
                    label="Metadata Stripper",
                    tag="metadata_stripper_sidebar_button",
                    width=-1,
                )

            # Main content
            with dpg.child_window(tag="content_child_window", width=-1):
                with dpg.group(tag="compressor_group"):
                    dpg.add_text("", tag="compressor_file_text")
                    dpg.hide_item("compressor_file_text")

                    dpg.add_button(
                        callback=lambda: select_file("compressor_group"),
                        label="Select File",
                        tag="compressor_select_file_button",
                    )

                    dpg.add_text("", tag="compressor_quality_text")
                    dpg.hide_item("compressor_quality_text")

                    dpg.add_slider_int(
                        default_value=0,
                        max_value=0,
                        min_value=0,
                        tag="compressor_quality_slider",
                        width=-1,
                    )
                    dpg.hide_item("compressor_quality_slider")

                    dpg.add_spacer(height=137, tag="compressor_spacer")
                    dpg.hide_item("compressor_spacer")

                    with dpg.group(horizontal=True, tag="compressor_action_group"):
                        dpg.add_button(
                            callback=compress_callback,
                            label="Compress",
                            tag="compressor_compress_button",
                            width=100,
                        )

                        dpg.add_text("", tag="compressor_status_text")

                    dpg.hide_item("compressor_action_group")

                with dpg.group(tag="format_converter_group"):
                    dpg.add_text("In development")

                with dpg.group(tag="metadata_stripper_group"):
                    dpg.add_text("In development")

    dpg.setup_dearpygui()

    theme.apply()

    dpg.show_viewport()

    if IS_WINDOWS:
        from windows_utils import disable_maximize

        dpg.set_frame_callback(16, disable_maximize)

    dpg.set_primary_window("primary_window", True)

    show_group("compressor_group")

    dpg.start_dearpygui()
    dpg.destroy_context()


if __name__ == "__main__":
    main()
