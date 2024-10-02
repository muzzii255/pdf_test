
import pdfkit
import os
import datetime
def image_convertor(plaintiff_name,lein):
    # exe_loc = f'C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe'
    # config = pdfkit.configuration(wkhtmltopdf=exe_loc)
    # options = {
    # "enable-local-file-access": "",
    # 'footer-right': "[page]/[topage]",
    # 'footer-font-name': 'Sans Pro',
    # 'footer-font-size': 8,
    # 'footer-spacing':2,
    # 'footer-left': 'https://apps.nyc.gov/nyc-mailform/validation',
    # 'header-font-name': 'Sans Pro',
    # 'header-font-size': 8,
    # 'header-spacing':2,
    # 'header-left': datetime.datetime.now().strftime('%m/%#d/%y, %H:%M%p'),
    # 'header-center': 'Thank you',
    # 'user-style-sheet': 'formsubmit.css'
    # }
    options = {
        'enable-local-file-access': None,  # Enable access to local files like CSS/JS
        'page-size': 'A4',
        'margin-top': '0.05in',
        'margin-right': '0.05in',
        'margin-bottom': '0.05in',
        'margin-left': '0.05in',
        'encoding': "UTF-8",
        'no-outline': None,
        'footer-right': "[page]/[topage]",
        'footer-font-name': 'Sans Pro',
        'footer-font-size': 8,
        'footer-spacing':2,
        'footer-left': 'https://apps.nyc.gov/nyc-mailform/validation',
        'header-font-name': 'Sans Pro',
        'header-font-size': 8,
        'header-spacing':2,
        'header-left': datetime.datetime.now().strftime('%m/%#d/%y, %H:%M%p'),
        'header-center': 'Thank you',
        
    }

    current_cwd = os.getcwd()
    try:
        pdfkit.from_file(f'{current_cwd}/test.html',f'{current_cwd}/{plaintiff_name} {lein} Medicaid Submission Form.pdf',options=options)
    except Exception as e:
        print(e)
        
        
# print(datetime.datetime.now().strftime('%m/%#d/%y, %H:%M%p'))
image_convertor('test1 test2','test2')




# import undetected_chromedriver as uc

# options = uc.ChromeOptions()
# options.add_experimental_option('prefs', {
# "download.default_directory": "C:/Users/XXXX/Desktop", #Change default directory for downloads
# "download.prompt_for_download": False, #To auto download the file
# "download.directory_upgrade": True,
# "plugins.always_open_pdf_externally": True #It will not show PDF directly in chrome
# })
# driver = uc.Chrome()

