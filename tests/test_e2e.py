from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

def test_compra_e2e():

    options = Options()

    options.add_argument("--headless")

    options.add_argument("--no-sandbox")

    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    driver.get("http://localhost:5000")

    botao = driver.find_element(
        By.TAG_NAME,
        "button"
    )

    botao.click()

    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(
            (By.ID, "mensagem"),
            "sucesso"
        )
    )

    texto = driver.find_element(
        By.ID,
        "mensagem"
    ).text

    assert "sucesso" in texto.lower()

    driver.quit()