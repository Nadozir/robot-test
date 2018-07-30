1. Created a class PageLoaded

2. Created a function def setUp for load setting:create a new Chrome session, wait and 
windows setting, navigate to the application home page "https://atomcream.com/".

3.In this function test_check_button:
        a. get the buttons: GET A QUOTE, CONTACT US NOW, scroll;
        b. check GET A QUOTE, CONTACT US NOW, scroll buttons is displayed and enabled;
        c. click on GET A QUOTE, CONTACT US NOW, scroll buttons. This will display new page.
       
4. Created function test_image_url where:
        a. get logo image_url;
        b. check logo is displayed on home page;
        c. click on logo images to open the page;
        d. get logo_footer image_url;
        e. check logo_footer is displayed on home page;
        f. click on logo_footer images to open the page;
        g. check page title.

5. Created function test_home_page_links_is_displayed where:
        a. get the home page links: stack_footer_link, projects_footer_link, about_footer_link
contact_footer_link, stack_header_link, case_header_link, about_header_link,
contact_header_link, mail_link;
        b. check home page links is displayed/visible: stack_footer_link, projects_footer_link, about_footer_link
contact_footer_link, stack_header_link, case_header_link, about_header_link,
contact_header_link, mail_link;
        c. click on home page links to open the page: stack_footer_link, projects_footer_link, about_footer_link
contact_footer_link, stack_header_link, case_header_link, about_header_link,
contact_header_link, mail_link;

6. Created function test_contact_form where:
        a. get all the fields from Create an Account form: first_name, last_name,
email_address, telephone_number, text_area, send_button;    
        b. check maxlength of first name and last name textbox: first_name, last_name,
email_address, telephone_number, text_area, send_button;
        c. check all fields are enabled: first_name, last_name,
email_address, telephone_number, text_area, send_button;
        d. fill out all the fields: first_name, last_name,
email_address, telephone_number, text_area;
        e. click Send button to submit the form.

7. Created function test_check_button_links where:
        a. get the buttons: linkedin_button, twitter_button, facebook_button,
google_button;
        b. check buttons is displayed and enabled: linkedin_button, twitter_button, facebook_button,
google_button;
        c. click on buttons. This will display new page: linkedin_button, twitter_button, facebook_button,
google_button.

8. Created function test_page_links_is_displayed where: 
        a. get the page links: rdbs_link, rwd_link, erp_link, el_link,
ccbd_link, bs_link;
        b. check page links is displayed/visible: rdbs_link, rwd_link, erp_link, el_link,
ccbd_link, bs_link;
        c. click on page links to open the page: rdbs_link, rwd_link, erp_link, el_link,
ccbd_link, bs_link.

9. Created function tearDown where:
        a. close the browser window;
        b. close the programm.
10. Created file runtest.robot:
*** Settings ***
Library           Selenium2Library
Library           C:/****/robottest.py
Library           PageLoaded

*** Test Cases ***
    ${result} =    Run test_check_button
    stdout={C:/*****}/stdout.txt
    Terminate test_check_button   ${handle}
    ${result} =    Wait For test_check_button	timeout=20 secs
    Should Be Equal As Integers  ${result.rc}	0

