import dearpygui.dearpygui as dpg  # type: ignore


def apply() -> None:
    with dpg.font_registry():
        bold_font = dpg.add_font("./cleanpixels/assets/font/inter_bold.ttf", 16)
        regular_font = dpg.add_font("./cleanpixels/assets/font/inter_regular.ttf", 16)

    dpg.bind_font(regular_font)

    with dpg.theme(tag="global_theme"):
        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_color(dpg.mvThemeCol_Border, [16, 16, 16, 254])
            dpg.add_theme_color(dpg.mvThemeCol_ChildBg, [16, 16, 16, 254])
            dpg.add_theme_color(dpg.mvThemeCol_Text, [192, 192, 192, 254])
            dpg.add_theme_color(dpg.mvThemeCol_WindowBg, [16, 16, 16, 254])
            dpg.add_theme_style(dpg.mvStyleVar_ChildRounding, 8)
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 8)
            dpg.add_theme_style(dpg.mvStyleVar_GrabRounding, 8)
            dpg.add_theme_style(dpg.mvStyleVar_WindowBorderSize, 0)

    with dpg.theme(tag="sidebar_button_theme"):
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_color(dpg.mvThemeCol_Button, [16, 16, 16, 254])
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, [16, 16, 16, 254])
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [16, 16, 16, 254])

    with dpg.theme(tag="sidebar_active_button_theme"):
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_color(dpg.mvThemeCol_Button, [16, 16, 16, 254])
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, [16, 16, 16, 254])
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [16, 16, 16, 254])
            dpg.add_theme_color(dpg.mvThemeCol_Text, [128, 16, 16, 254])

    with dpg.theme(tag="content_child_window_theme"):
        with dpg.theme_component(dpg.mvChildWindow):
            dpg.add_theme_style(dpg.mvStyleVar_WindowPadding, x=16, y=16)

    with dpg.theme(tag="content_child_button_theme"):
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_color(dpg.mvThemeCol_Button, [48, 48, 48, 254])
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, [40, 40, 40, 254])
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [56, 56, 56, 254])
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, x=16, y=8)

    with dpg.theme(tag="content_child_slider_theme"):
        with dpg.theme_component(dpg.mvSliderInt):
            dpg.add_theme_color(dpg.mvThemeCol_FrameBg, [22, 22, 22, 254])
            dpg.add_theme_color(dpg.mvThemeCol_FrameBgActive, [30, 30, 30, 254])
            dpg.add_theme_color(dpg.mvThemeCol_FrameBgHovered, [26, 26, 26, 254])
            dpg.add_theme_color(dpg.mvThemeCol_SliderGrab, [128, 16, 16, 254])
            dpg.add_theme_color(dpg.mvThemeCol_SliderGrabActive, [100, 12, 12, 254])
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, x=16, y=8)

    with dpg.theme(tag="content_compress_button_theme"):
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_color(dpg.mvThemeCol_Button, [128, 16, 16, 254])
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, [100, 12, 12, 254])
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [150, 24, 24, 254])
            dpg.add_theme_color(dpg.mvThemeCol_Text, [254, 254, 254, 254])
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, x=16, y=8)

    dpg.bind_theme("global_theme")

    dpg.bind_item_theme("compressor_compress_button", "content_compress_button_theme")
    dpg.bind_item_theme("compressor_quality_slider", "content_child_slider_theme")
    dpg.bind_item_theme("compressor_select_file_button", "content_child_button_theme")
    dpg.bind_item_theme("content_child_window", "content_child_window_theme")

    dpg.bind_item_font("compressor_sidebar_button", bold_font)
    dpg.bind_item_font("format_converter_sidebar_button", bold_font)
    dpg.bind_item_font("metadata_stripper_sidebar_button", bold_font)
