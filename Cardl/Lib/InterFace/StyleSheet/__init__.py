from pathlib import Path
from tempfile import mkstemp

CardiTheme = str(Path(__file__).parent) + "//Cardi.json"

CardiTemp = """
{
  "color": {
    "window_bg_color": ["#f7f0f5", "#000000"],
    "button": ["#007AFF", "#007AFF"],
    "button_hover": ["#0069FF", "#0069FF"],
    "button_border": ["#0079FC", "#0079FC"],
    "checkbox_border": ["gray40", "gray60"],
    "checkmark": ["white", "gray90"],
    "entry": ["#007AFF", "#007AFF"],
    "entry_border": ["#007AFF", "#007AFF"],
    "entry_placeholder_text": ["gray52", "gray62"],
    "frame_border": ["#A7C2E0", "#5FB4DD"],
    "frame_low": ["gray92", "gray16"],
    "frame_high": ["gray86", "gray20"],
    "label": [null, null],
    "text": ["black", "white"],
    "text_disabled": ["gray60", "gray50"],
    "text_button_disabled": ["gray40", "gray74"],
    "progressbar": ["#6B6B6B", "gray0"],
    "progressbar_progress": ["#608BD5", "#395E9C"],
    "progressbar_border": ["gray", "gray"],
    "slider": ["#6B6B6B", "gray6"],
    "slider_progress": ["gray70", "gray30"],
    "slider_button": ["#608BD5", "#395E9C"],
    "slider_button_hover": ["#A4BDE6", "#748BB3"],
    "switch": ["gray70", "gray35"],
    "switch_progress": ["#608BD5", "#395E9C"],
    "switch_button": ["gray38", "gray70"],
    "switch_button_hover": ["gray30", "gray90"],
    "optionmenu_button": ["#36719F", "#144870"],
    "optionmenu_button_hover": ["#27577D", "#203A4F"],
    "combobox_border": ["#007AFF", "#007AFF"],
    "combobox_button_hover": ["#0069FF", "#0069FF"],
    "dropdown_color": ["gray90", "gray20"],
    "dropdown_hover": ["gray75", "gray28"],
    "dropdown_text": ["gray10", "#DCE4EE"],
    "scrollbar_button": ["gray55", "gray41"],
    "scrollbar_button_hover": ["gray40", "gray53"]
  },
  "text": {
    "macOS": {
      "font": "SF Display",
      "size": -13
    },
    "Windows": {
      "font": "Roboto",
      "size": -13
    },
    "Linux": {
      "font": "Roboto",
      "size": -13
    }
  },
  "shape": {
    "button_corner_radius": 15,
    "button_border_width": 1,
    "checkbox_corner_radius": 7,
    "checkbox_border_width": 3,
    "radiobutton_corner_radius": 1000,
    "radiobutton_border_width_unchecked": 3,
    "radiobutton_border_width_checked": 6,
    "entry_border_width": 1,
    "frame_corner_radius": 18,
    "frame_border_width": 0,
    "label_corner_radius": 0,
    "progressbar_border_width": 0,
    "progressbar_corner_radius": 1000,
    "slider_border_width": 6,
    "slider_corner_radius": 8,
    "slider_button_length": 0,
    "slider_button_corner_radius": 1000,
    "switch_border_width": 3,
    "switch_corner_radius": 1000,
    "switch_button_corner_radius": 1000,
    "switch_button_length": 0,
    "scrollbar_corner_radius": 1000,
    "scrollbar_border_spacing": 4
  }
}

"""

CardiTempFile = mkstemp()

with open(CardiTempFile[1], "w") as CardiFile:
    CardiFile.write(CardiTemp)

CardiTempTheme = CardiTempFile[1]