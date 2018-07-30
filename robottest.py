import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By 
from selenium.common.exceptions import TimeoutException
from time import gmtime, strftime


class PageLoaded(unittest.TestCase):
    def setUp(self):
        # create a new Chrome session
        self.driver = webdriver.Chrome(executable_path = 
            '*:/***/***/chromedriver.exe')
        self.driver.implicitly_wait(60)
        self.driver.maximize_window()

        # navigate to the application home page
        self.driver.get("https://atomcream.com/")

    def test_check_button(self):
        driver = self.driver

        # get the buttons: GET A QUOTE, CONTACT US NOW, scroll
        get_a_quote_button = driver.find_element_by_link_text("GET A QUOTE")
        contact_us_now_button = driver.find_element_by_link_text("CONTACT US NOW")
        scroll = driver.find_element_by_xpath("//button[@data-ui='scroll-top']")

        # check GET A QUOTE, CONTACT US NOW, scroll buttons is displayed and enabled
        self.assertTrue(get_a_quote_button.is_displayed() and 
        get_a_quote_button.is_enabled())
        self.assertTrue(contact_us_now_button.is_displayed() and 
        contact_us_now_button.is_enabled())
        self.assertTrue(scroll.is_displayed() and 
        scroll.is_enabled())

        # click on GET A QUOTE, CONTACT US NOW, scroll buttons. This will display new page.
        get_a_quote_button.click()
        contact_us_now_button.click()
        scroll.click()

    def test_image_url(self):
        # get logo image_url
        logo = self.driver.find_element_by_xpath("//a[@class='logo']//img[@alt='']")
        # check logo is displayed on home page
        self.assertTrue(logo.is_displayed())
        # click on logo images to open the page
        logo.click()

        # get logo_footer image_url
        logo_footer = self.driver.find_element_by_xpath("//img[@alt='logo in footer']")
        # check logo_footer is displayed on home page
        self.assertTrue(logo_footer.is_displayed())
        # click on logo_footer images to open the page
        logo_footer.click()

        # check page title
        self.assertEqual("Atom Cream", self.driver.title)

    def test_home_page_links_is_displayed(self):
        # get the home page links
        stack_footer_link = self.driver.find_element_by_link_text("TECHNOLOGY STACK")
        projects_footer_link = self.driver.find_element_by_link_text("PROJECTS")
        about_footer_link = self.driver.find_element_by_link_text("ABOUT US")
        contact_footer_link = self.driver.find_element_by_link_text("CONTACT US")
        stack_header_link = self.driver.find_element_by_css_selector("#stack")
        case_header_link = self.driver.find_element_by_css_selector("#case")
        about_header_link = self.driver.find_element_by_css_selector("#about")
        contact_header_link = self.driver.find_element_by_css_selector("#contact")
        mail_link = self.driver.find_element_by_link_text("contact@atomcream.com")

        # check home page links is displayed/visible
        self.assertTrue(stack_footer_link.is_displayed())
        self.assertTrue(projects_footer_link.is_displayed())
        self.assertTrue(about_footer_link.is_displayed())
        self.assertTrue(contact_footer_link.is_displayed())
        self.assertTrue(stack_header_link.is_displayed())
        self.assertTrue(case_header_link.is_displayed())
        self.assertTrue(about_header_link.is_displayed())
        self.assertTrue(contact_header_link.is_displayed())
        self.assertTrue(mail_link.is_displayed())

        # click on home page links to open the page
        stack_footer_link.click()
        projects_footer_link.click()
        about_footer_link.click()
        contact_footer_link.click()
        stack_header_link.click()
        case_header_link.click()
        about_header_link.click()
        contact_header_link.click()
        mail_link.click()

    def test_contact_form(self):
        driver = self.driver

        # get all the fields from Create an Account form
        first_name = driver.find_element_by_xpath("//input[@placeholder='First name']")
        last_name = driver.find_element_by_xpath("//input[@placeholder='Last name']")
        email_address = driver.find_element_by_xpath("//input[@placeholder='Email']")
        telephone_number = driver.find_element_by_xpath("//input[@placeholder='Telephone number']")
        text_area = driver.find_element_by_xpath("//textarea[@name='info']")
        send_button = driver.find_element_by_xpath("//input[@value='Send']")
        
        # check maxlength of first name and last name textbox
        self.assertEqual("100", first_name.get_attribute("maxlength"))
        self.assertEqual("100", last_name.get_attribute("maxlength"))
        self.assertEqual("40", email_address.get_attribute("maxlength"))
        self.assertEqual("40", telephone_number.get_attribute("maxlength"))
        self.assertEqual("500", text_area.get_attribute("maxlength"))

        # check all fields are enabled
        self.assertTrue(first_name.is_enabled() and last_name.is_enabled()
        and email_address.is_enabled() and telephone_number.is_enabled()
        and text_area.is_enabled() and send_button.is_enabled())

        user_name = "user_" + strftime("%Y%m%d%H%M%S", gmtime())

        # fill out all the fields
        first_name.send_keys("Test")
        last_name.send_keys(user_name)
        email_address.send_keys(user_name + "@example.com")
        telephone_number.send_keys("tester")
        text_area.send_keys("tester")

        # click Send button to submit the form
        send_button.click()

    def test_check_button_links(self):
        driver = self.driver

        # get the buttons
        linkedin_button = driver.find_element_by_xpath("//*[@id='contact']/div[1]/div[2]/div[2]/nav/a[1]/svg")
        twitter_button = driver.find_element_by_xpath("//*[@id='contact']/div[1]/div[2]/div[2]/nav/a[2]/svg")
        facebook_button = driver.find_element_by_xpath("//*[@id='contact']/div[1]/div[2]/div[2]/nav/a[3]/svg")
        google_button = driver.find_element_by_xpath("//*[@id='contact']/div[1]/div[2]/div[2]/nav/a[4]/svg")

        # check buttons is displayed and enabled
        self.assertTrue(linkedin_button.is_displayed() and 
        linkedin_button.is_enabled())
        self.assertTrue(twitter_button.is_displayed() and 
        twitter_button.is_enabled())
        self.assertTrue(facebook_button.is_displayed() and 
        facebook_button.is_enabled())
        self.assertTrue(google_button.is_displayed() and 
        google_button.is_enabled())

        # click on buttons. This will display new page.
        linkedin_button.click()
        twitter_button.click()
        facebook_button.click()
        google_button.click()

    def test_page_links_is_displayed(self):
        # get the page links
        rdbs_link = self.driver.find_element_by_xpath("html/body/div[3]/div[1]/div[3]/h3")
        rwd_link = self.driver.find_element_by_xpath("html/body/div[3]/div[1]/div[2]/h3")
        erp_link = self.driver.find_element_by_xpath("html/body/div[3]/div[1]/div[5]/h3")
        el_link = self.driver.find_element_by_xpath("html/body/div[3]/div[1]/div[4]/h3")
        ccbd_link = self.driver.find_element_by_xpath("//div[@data-num='5']")
        bs_link = self.driver.find_element_by_xpath("html/body/div[3]/div[1]/div[6]/h3")

        # check page links is displayed/visible
        self.assertTrue(rdbs_link.is_displayed())
        self.assertTrue(rwd_link.is_displayed())
        self.assertTrue(erp_link.is_displayed())
        self.assertTrue(el_link.is_displayed())
        self.assertTrue(ccbd_link.is_displayed())
        self.assertTrue(bs_link.is_displayed())

        # click on page links to open the page
        rdbs_link.click()
        rwd_link.click()
        erp_link.click()
        el_link.click()
        ccbd_link.click()
        bs_link.click()

    def tearDown(self):
        # close the browser window
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)

