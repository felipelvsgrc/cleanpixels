import sys

import dearpygui.dearpygui as dpg  # type: ignore

IS_WINDOWS = sys.platform == "win32"


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
                    dpg.add_text("Compressor")

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
