from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup


class ScraperCommon:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        

        self.driver = webdriver.Chrome(options=self.options)
        self.wait = WebDriverWait(self.driver, 300)

    def wait_default(self, by: By, element: str):
        return self.wait.until(EC.element_to_be_clickable((by, element)))

    def login(self):
        from src.backend.config.settings import linkedin_email, linkedin_pwd
        self.driver.get("https://www.linkedin.com/login/pt?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")
        
        self.wait_default(By.ID, 'username').send_keys(linkedin_email)
        self.driver.find_element(By.ID, 'password').send_keys(linkedin_pwd)

        self.driver.find_element(By.XPATH, "//button[@data-litms-control-urn='login-submit']").click()

    def get_into_jobs_page(self):
        self.wait_default(By.XPATH, '//div[@aria-label="Itens salvos"]')
        
        self.driver.get('https://www.linkedin.com/jobs/search/?keywords=dados') #Não seria melhor se isso estivesse dentro de outra função?

    def get_teste(self):
        html = self.driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        print(self.get_descr(soup.find_all('div', class_="mt4")))

    def get_descr(self, divs):
        descricoes = []
        for div in divs:
            
            if not isinstance(div, BeautifulSoup):
                soup = BeautifulSoup(str(div), 'html.parser')
            else:
                soup = div

            texto = soup.get_text(separator=' ', strip=True) #são sempre 3 get text? Pq o primeiro é a info do nome do cargo E da empresa e a 3 é a descrição.
            print(texto)
            
            if len(texto) < 200:
                continue
            if any(palavra in texto.lower() for palavra in ['candidatura', 'salvar', 'premium', 'experimente', 'insights exclusivos']):
                continue
            
            
            descricoes.append(texto)
            
        if not descricoes:
            return None

        return ' '.join(descricoes)

if __name__ == '__main__':
    i = ScraperCommon()
    i.login()
    i.get_into_jobs_page()
    i.get_teste()