from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

import cv2
import pytesseract

imagem = cv2.imread('imagem.png')
pytesseract.pytesseract.tesseract_cmd='C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
texto = pytesseract.image_to_string(imagem)
print(texto)

