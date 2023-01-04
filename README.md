# Start using browser automation to get free things.

## Tools needed
* Playwright (https://playwright.dev)
* DeepL (https://www.deepl.com)
* Python (https://www.python.org)
* Click (https://palletsprojects.com/p/click/)
* pyperclip (https://github.com/asweigart/pyperclip)


## How to do

Use **playwright codegen** to start a firefox instance

    playwright codegen -b firefox

Navigate to the url you want to automate, on the **Playwright Inspector** window some code will appear inside boilerplate code.

    page.goto("https://www.deepl.com/translator")
    page.get_by_role("button", name="Select target language. Currently selected: English (US)").click()
    page.get_by_role("option", name="German").click()
    page.get_by_role("textbox", name="Source text").click()
    page.get_by_role("textbox", name="Source text").fill("Tutorial")
    page.get_by_role("button", name="Copy to clipboard").click()


Perfect! Now the translated text is inside clipboard. You can use **pyperclip** to retrive it.

    translated_text = pyperclip.paste()


We want the script to have a *CLI* (Command Line Interface) that is easy to use and easy to write. We can use **Click** to simplify our lifes.

    @click.command()
    @click.option('--input', prompt='Input text path',
              help='Input text path')
    @click.option('--output', prompt='Output text path',
              help='Output text path')
    @click.option('--lang', prompt='Output language',
              help='Output language')
    def translate_cli(input: str, output: str, lang: str):


When you start your script without arguments it will ask you the parameters automatically.

    Input text path: sample.txt
    Output text path: ita.txt
    Output language: Italian

Or you can specify them when starting the script

    python deepl_automation.py --input=sample.txt --output=ita.txt --lang=Italian

**Have fun!**