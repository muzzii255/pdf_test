
import pdfkit
import os
import datetime
        
        
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
    'header-left': datetime.datetime.now().strftime('%m/%-d/%y, %H:%M%p'),
    'header-center': 'Thank you',
    
}

current_cwd = os.getcwd()
pdfkit.from_file(input='test.html',output_path='./test.pdf',options=options)




# import undetected_chromedriver as uc

# options = uc.ChromeOptions()
# options.add_experimental_option('prefs', {
# "download.default_directory": "C:/Users/XXXX/Desktop", #Change default directory for downloads
# "download.prompt_for_download": False, #To auto download the file
# "download.directory_upgrade": True,
# "plugins.always_open_pdf_externally": True #It will not show PDF directly in chrome
# })
# driver = uc.Chrome()

