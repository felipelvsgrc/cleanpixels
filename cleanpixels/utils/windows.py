import ctypes
import os

user32 = ctypes.windll.user32

GWL_STYLE = -16
SWP_FLAGS = 0x0027
WS_MAXIMIZEBOX = 0x00010000

user32.GetWindowThreadProcessId.argtypes = [
    ctypes.c_void_p,
    ctypes.POINTER(ctypes.c_ulong),
]
user32.GetWindowThreadProcessId.restype = ctypes.c_ulong


def get_hwnd_by_pid() -> int | None:
    hwnds: list[int] = []
    pid = os.getpid()

    EnumWindowsProc = ctypes.WINFUNCTYPE(
        ctypes.c_bool,
        ctypes.c_void_p,
        ctypes.c_size_t,
    )

    def callback(hwnd: int, _: int) -> bool:
        lpdw_process_id = ctypes.c_ulong()
        user32.GetWindowThreadProcessId(hwnd, ctypes.byref(lpdw_process_id))

        if lpdw_process_id.value == pid:
            hwnds.append(hwnd)

            return False

        return True

    user32.EnumWindows(EnumWindowsProc(callback), 0)

    return hwnds[0] if hwnds else None


def disable_maximize() -> None:
    hwnd = get_hwnd_by_pid()

    if not hwnd:
        return

    style = user32.GetWindowLongW(hwnd, GWL_STYLE)
    style &= ~WS_MAXIMIZEBOX

    user32.SetWindowLongW(hwnd, GWL_STYLE, style)
    user32.SetWindowPos(hwnd, None, 0, 0, 0, 0, SWP_FLAGS)
