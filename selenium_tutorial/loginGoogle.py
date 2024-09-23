from seleniumbase import BaseCase
from seleniumbase import Driver


class undetectedLoginToNotion(BaseCase):
    driver = Driver(uc=True)

    url = "https://www.notion.so/login"
    driver.uc_open_with_reconnect(url, 3)

    driver.wait_for_element(
        '//*[@id="notion-app"]/div/div[1]/div/main/div[1]/section/div/div/div/div[2]/div[1]/div[1]/div[1]/div'
    )
    driver.click(
        '//*[@id="notion-app"]/div/div[1]/div/main/div[1]/section/div/div/div/div[2]/div[1]/div[1]/div[1]/div'
    )

    window_handles = driver.window_handles
    print("window_handles:", window_handles)
    driver.switch_to.window(window_handles[1])
    driver.type("//input[@id='identifierId']", "feri.chess@gmail.com")
    driver.click("#identifierNext")

    driver.wait_for_element_visible("[aria-label='Enter your password']")
    driver.type("[aria-label='Enter your password']", "rapibersih")
    driver.click("#passwordNext")
    print("you should be logged in to your notion by now!")


if __name__ == "__main__":
    undetectedLoginToNotion()
