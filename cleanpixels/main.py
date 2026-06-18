import dearpygui.dearpygui as dpg  # type: ignore
from utils.ui_data import (
    CHILD_HEIGHT,
    CHILD_WIDTH,
    CONTENT_CHILD_WINDOW,
    CONTENT_CHILD_WINDOW_BROWSE_IMAGE_BUTTON,
    CONTENT_CHILD_WINDOW_STATUS_TEXT,
    PRIMARY_WINDOW,
)
from utils.ui_functions import dpg_render_loop


def main() -> None:
    dpg.create_context()

    dpg.create_viewport(
        height=200,
        resizable=False,
        title="CleanPixels",
        width=400,
    )

    with dpg.window(tag=PRIMARY_WINDOW):
        with dpg.child_window(
            height=CHILD_HEIGHT,
            tag=CONTENT_CHILD_WINDOW,
            width=CHILD_WIDTH,
        ):
            dpg.add_text(
                "Please select an image to begin",
                tag=CONTENT_CHILD_WINDOW_STATUS_TEXT,
            )

            dpg.add_button(
                height=32,
                label="Browse Image",
                tag=CONTENT_CHILD_WINDOW_BROWSE_IMAGE_BUTTON,
                width=160,
            )

    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window(PRIMARY_WINDOW, True)

    dpg_render_loop()

    dpg.destroy_context()


if __name__ == "__main__":
    main()
