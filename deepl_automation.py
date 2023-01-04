import os
import click
import pyperclip
import re
import time

from playwright.sync_api import Playwright, sync_playwright, expect

@click.command()
@click.option('--input', prompt='Input text path',
              help='Input text path')
@click.option('--output', prompt='Output text path',
              help='Output text path')
@click.option('--lang', prompt='Output language',
              help='Output language')
def translate_cli(input: str, output: str, lang: str):
    input = os.path.abspath(input)
    
    if not os.path.exists(input):
        print("ERROR: Input file missing")
        return

    output = os.path.abspath(output)

    if os.path.exists(output):
        print("ERROR: Output file already exists")
        return

    input_text = ""

    with open(input, "r", encoding="utf8") as i:
        input_text = i.read()

    if input_text == "":
        print("ERROR: Empty file")
        return
    
    translated_text = translate(input_text, lang)

    with open(output, "w", encoding="utf8") as o:
            o.write(translated_text)


def translate(input_text: str, lang: str) -> str:
    with sync_playwright() as playwright:
        browser = playwright.firefox.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.deepl.com/translator")
        page.get_by_role("button", name=re.compile("Select target language", re.IGNORECASE)).click()
        page.get_by_role("option", name=lang).click()
        page.get_by_role("textbox", name="Source text").click()
        page.get_by_role("textbox", name="Source text").fill(input_text)
        
        #wait for translation to appear before copying to clipboard
        time.sleep(30)
        
        page.get_by_role("button", name="Copy to clipboard").click()

        translated_text = pyperclip.paste()

        context.close()
        browser.close()
        return translated_text

if __name__ == '__main__':
    translate_cli()