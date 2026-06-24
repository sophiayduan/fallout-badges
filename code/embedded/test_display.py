from display import DisplayManager, nice_fonts
import time

display = DisplayManager()

# --- 1. All white ---
display.fill(1)
display.show(rotate=-90)
time.sleep(2)

# --- 2. All black ---
display.fill(0)
display.show(rotate=-90)
time.sleep(2)

# --- 3. Border + crosshair ---
W, H = 176, 264  # after -90 rotation, portrait dimensions
display.fill(1)
display.rect(0, 0, W, H, 0)           # outer border
display.hline(0, H // 2, W, 0)        # horizontal centre line
display.vline(W // 2, 0, H, 0)        # vertical centre line
display.rect(W // 2 - 10, H // 2 - 10, 20, 20, 0)  # centre box
display.show(rotate=-90)
time.sleep(2)

# --- 4. Corner dots so you can check orientation ---
display.fill(1)
r = 8
display.fill_rect(0, 0, r, r, 0)          # top-left
display.fill_rect(W - r, 0, r, r, 0)      # top-right
display.fill_rect(0, H - r, r, r, 0)      # bottom-left
display.fill_rect(W - r, H - r, r, r, 0)  # bottom-right
display.show(rotate=-90)
time.sleep(2)

# --- 5. Text sampler ---
display.fill(1)
display.nice_text("Sophia Duan", 4, 4, font=42)
display.nice_text("@sophia", 4, 30, font=18)
display.nice_text("she/her", 4, 62, font=18)
display.nice_text("The quick brown fox jumps over the lazy dog", 4, 102, font=18)
display.hline(0, 152, W, 0)
display.nice_text("OK!", 4, 158, font=68)
display.show(rotate=-90)
