import platform
import pygame
import os

pygame.init()

def log(label, entry):
    f = open("log.txt", "a")
    f.write(f"[{label}] : {entry}\n")
    f.close()

INFO = pygame.display.Info()
log("SYSTEM", f"Platform machine: {platform.machine()}")
log("SYSTEM", f"Platform version: {platform.version()}")
log("SYSTEM", f"Platform specific: {platform.platform()}")
log("SYSTEM", f"Platform uname: {platform.uname()}")
log("SYSTEM", f"Platform system: {platform.system()}")
log("SYSTEM", f"Platform processor: {platform.processor()}")

log("SYSTEM", f"USER: {os.getlogin()}")

log("SYSTEM", f"Detected monitor")

log("MON", f"hw: {INFO.hw}")
log("MON", f"wm: {INFO.wm}")

log("MON", f"video_mem: {INFO.video_mem}")

log("VIDEO/BLIT", f"blit_hw: {INFO.blit_hw}")
log("VIDEO/BLIT", f"blit_hw_CC: {INFO.blit_hw_CC}")
log("VIDEO/BLIT", f"blit_hw_A: {INFO.blit_hw_A}")
log("VIDEO/BLIT", f"blit_sw: {INFO.blit_sw}")
log("VIDEO/BLIT", f"blit_sw_CC: {INFO.blit_sw_CC}")
log("VIDEO/BLIT", f"blit_sw_A: {INFO.blit_sw_A}")

log("VIDEO", f"bitsize: {INFO.bitsize}")
log("VIDEO", f"bytesize: {INFO.bytesize}")
log("VIDEO", f"masks: {INFO.masks}")
log("VIDEO", f"shifts: {INFO.shifts}")
log("VIDEO", f"losses: {INFO.losses}")

log("VIDEO", f"resolution {INFO.current_w}, {INFO.current_h}")

log("APPLICATION", "Starting up pygame")
screen = pygame.display.set_mode((INFO.current_w, INFO.current_h))


running = True
while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                log("USER", "Pressed Escape key")
                log("USER", "Closing application")
                running = False
    screen.fill((255, 255, 255))

    pygame.display.flip()

pygame.quit()