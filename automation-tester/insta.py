from seleniumbase import SB
import random
import pyperclip
import pyautogui
import pandas as pd
from bs4 import BeautifulSoup
def extract_instagram_username(url):
    """Extract username from Instagram URL"""
    # Remove trailing slash if present
    url = url.rstrip('/')
    # Get the last part of the URL after the last /
    return url.split('/')[-1]
with SB(uc=True, test=True, locale_code="en") as sb:
    accounts = ['https://www.instagram.com/danigray/','https://www.instagram.com/missbrisolo/', 'https://www.instagram.com/dkffkskk/','https://www.instagram.com/chokoblackie/','https://www.instagram.com/azalialexi/','https://www.instagram.com/lupefuentes/']
    url = "https://www.instagram.com/"
    sb.activate_cdp_mode(url)
    sb.sleep(9000000)
    
    #sb.cdp.gui_click_x_y(329, 304)
    #sb.sleep(1)
    # for account in accounts:
    #     sb.cdp.gui_click_x_y(75, 392)
    #     sb.sleep(1)
    #     sb.cdp.gui_write(extract_instagram_username(account))
    #     sb.sleep(3)
    #     pyautogui.click(255, 382)
    #     sb.sleep(4)
    #     html = sb.cdp.get_element_html("header")
    #     soup = BeautifulSoup(html, 'html.parser')
    # # Find all divs with role="button" and text "Message"
    #     similar_accounts = soup.find('svg', attrs={'aria-label': 'Similar accounts'})
    #     message_button = soup.find('div', attrs={'role': 'button'}, string=lambda x: x and x.strip() == "Message")
    #     if message_button:
    #         if similar_accounts:#danigray825
    #             sb.cdp.gui_click_x_y(699, 266)
    #             sb.sleep(4)
    #             sb.cdp.gui_click_x_y(825, 266)
    #             sb.sleep(4)
    #         else:#missbrisolo850
    #             sb.cdp.gui_click_x_y(718, 266)
    #             sb.sleep(4)
    #             sb.cdp.gui_click_x_y(850, 266)
    #             sb.sleep(4)

    #     elif similar_accounts:#dkffkskk800
    #         sb.cdp.gui_click_x_y(667, 266)
    #         sb.sleep(4)
    #         sb.cdp.gui_click_x_y(800, 266)
    #         sb.sleep(5)
    #         #sb.cdp.gui_click_x_y(658, 638)
    #         sb.sleep(5)

    #     else:#chokoblackie
    #         sb.cdp.gui_click_x_y(730, 266)
    #         sb.sleep(4)
    #         sb.cdp.gui_click_x_y(828,266)
    #         #sb.cdp.gui_click_x_y(863, 266)
    #         sb.sleep(5)
    #         sb.cdp.gui_click_x_y(658, 638)
    #         sb.sleep(5)

    #     sb.cdp.gui_write("hi")
    #     sb.sleep(1)
    #     pyautogui.press('enter')
    #     sb.sleep(13)

    
    