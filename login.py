from playwright.sync_api import Page as page 

def test_ackcio_login(page: page):
    page.goto("https://qnc5wr4xyqkf.connect.remote.it/signin")
    page.wait_for_timeout(5000)
    page.get_by_label("Password").fill("Admin@123")
    page.wait_for_timeout(5000)
    page.get_by_role("button", name="Login").click()

