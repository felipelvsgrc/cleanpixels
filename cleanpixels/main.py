import os
import sys
from tkinter import Tk, filedialog

import dearpygui.dearpygui as dpg  # type: ignore
import image_utils

IS_WINDOWS = sys.platform == "win32"
SELECTED_FILE_PATH = None


def compress_callback() -> None:
    global SELECTED_FILE_PATH

    if not SELECTED_FILE_PATH:
        dpg.set_value("compressor_status_text", "Error: No file selected")

        return

    try:
        dpg.set_value("compressor_status_text", "Compressing...")

        value_from_slider = dpg.get_value("compressor_quality_slider")
        result = image_utils.compress(SELECTED_FILE_PATH, value_from_slider)

        if result == "":
            dpg.set_value(
                "compressor_status_text",
                "Done: Kept original (no size reduction achieved)",
            )

        else:
            dpg.set_value("compressor_status_text", "Success: Image compressed!")

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

            dpg.show_item("compressor_spacer_1")
            dpg.show_item("compressor_quality_text")
            dpg.show_item("compressor_quality_slider")
            dpg.show_item("compressor_spacer_2")
            dpg.show_item("compressor_compress_button")

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
    dpg.hide_item("convert_format_group")
    dpg.hide_item("strip_metadata_group")

    dpg.show_item(group)


def main() -> None:
    dpg.create_context()
    dpg.create_viewport(
        height=600,
        max_height=600,
        max_width=800,
        resizable=False,
        title="CleanPixels",
        width=800,
    )

    with dpg.window(tag="primary_window"):
        with dpg.group(horizontal=True):
            # Sidebar
            with dpg.child_window(width=192):
                dpg.add_button(
                    callback=lambda: show_group("compressor_group"),
                    height=32,
                    label="Compressor",
                    width=-1,
                )

                dpg.add_button(
                    callback=lambda: show_group("convert_format_group"),
                    height=32,
                    label="Convert Format",
                    width=-1,
                )

                dpg.add_button(
                    callback=lambda: show_group("strip_metadata_group"),
                    height=32,
                    label="Strip Metadata",
                    width=-1,
                )

            # Main content
            with dpg.child_window(width=-1):
                with dpg.group(tag="compressor_group"):
                    dpg.add_text("No file selected", tag="compressor_file_text")

                    dpg.add_button(
                        callback=lambda: select_file("compressor_group"),
                        label="Select File",
                    )

                    dpg.add_spacer(height=8, tag="compressor_spacer_1")
                    dpg.hide_item("compressor_spacer_1")

                    dpg.add_text("", tag="compressor_quality_text")
                    dpg.hide_item("compressor_quality_text")

                    dpg.add_slider_int(
                        default_value=0,
                        max_value=0,
                        min_value=0,
                        tag="compressor_quality_slider",
                        width=400,
                    )
                    dpg.hide_item("compressor_quality_slider")

                    dpg.add_spacer(height=8, tag="compressor_spacer_2")
                    dpg.hide_item("compressor_spacer_2")

                    dpg.add_button(
                        callback=compress_callback,
                        label="Compress",
                        tag="compressor_compress_button",
                        width=100,
                    )
                    dpg.hide_item("compressor_compress_button")

                    dpg.add_text(
                        "No action is being taken", tag="compressor_status_text"
                    )

                with dpg.group(tag="convert_format_group"):
                    dpg.add_text("Convert format")

                with dpg.group(tag="strip_metadata_group"):
                    dpg.add_text("Strip metadata")

    dpg.setup_dearpygui()
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
