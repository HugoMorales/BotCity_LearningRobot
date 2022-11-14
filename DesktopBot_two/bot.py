from botcity.maestro import *
from botcity.plugins.excel import BotExcelPlugin
from botcity.plugins.email import BotEmailPlugin
# from navigation.frakturama_new_product import add_product as new_prod
from .navigation import frakturama_new_product as new_prod

"""
WARNING:

Please make sure you install the bot with `pip install -e .` in order to get all the dependencies
on your Python environment.

Also, if you are using PyCharm or another IDE, make sure that you use the SAME Python interpreter
as your IDE.

If you get an error like:
```
ModuleNotFoundError: No module named 'botcity'
```

This means that you are likely using a different Python interpreter than the one used to install the bot.
To fix this, you can either:
- Use the same interpreter as your IDE and install your bot with `pip install -e .`
- Use the same interpreter as the one used to install the bot (`pip install -e .`)

Please refer to the documentation for more information at https://documentation.botcity.dev/
"""

from botcity.core import DesktopBot
# Uncomment the line below for integrations with BotMaestro
# Using the Maestro SDK
# from botcity.maestro import *


# Instantiate the plugin
# bot_excel = BotExcelPlugin()


class Bot(DesktopBot):
    def action(self, execution=None):
        # Uncomment to silence Maestro errors when disconnected
        if self.maestro:
             self.maestro.RAISE_NOT_CONNECTED = False
        else:
             print("Not connected!")

        # Fetch the Activity ID from the task:
        task = self.maestro.get_task(execution.task_id)
        activity_id = task.activity_id

        """
        # Read from an Excel File
        bot_excel.read('C:\Test\input.xlsx')
        bot_excel.sort(['A'], True)

        # Print the result
        print(bot_excel.as_list())
        # Save it to a new file
        bot_excel.write('C:\Test\output.xlsx')
        """

        """
        # Instantiate the plugin
        email = BotEmailPlugin()

        # Configure IMAP with the gmail server
        # email.configure_imap("imap.gmail.com", 993)

        # Configure SMTP with the gmail server
        email.configure_smtp("smtp.office365.com", 587)

        # Login with a valid email account
        email.login("teste_qa_t2c@outlook.com", "Abacabb87")

        email_to = ["hugo.morales@t2cgroup.com.br"]
        email_subject = "Teste de envio de email"
        email_body = "Esse é um simples email de teste"

        # Sending a email as a test
        email.send_message(subject=email_subject, to_addrs=email_to, use_html=False,text_content=email_body)
        """



        # Opens Fakturama
        self.execute("C:\Program Files\Fakturama2\Fakturama.exe")
  


        # #{image:"Fakturama_MainScreen"}                                                                                                                                                                                                                                                                    




        # Tries to find the logo, indicating that the program started
        # If it does, maximize window
        if not self.find( "Img_InitialLogo", matching=0.97, waiting_time=50000):
            self.not_found("Img_InitialLogo")
        self.maximize_window()

        # Only clicks in the maximize mutton if is on the screen
        if self.find( "Btn_MaximizeWindow", matching=0.97, waiting_time=10000):
            self.click()

        # Opens the new product screen
        if not self.find( "Btn_NewProduct", matching=0.97, waiting_time=10000):
            self.not_found("Btn_NewProduct")
        self.click()


        # #{image:"Fakturama_NewProduct"}                                                                                                                                            

        
        new_prod.add_product(self)
        

        # Typing in a field
        # Click relative to a label
        
        print("Robot finished!")

        self.maestro.finish_task(
            task_id=execution.task_id,
            status=AutomationTaskFinishStatus.SUCCESS,
            message="Task Finished OK."
        )    


    def not_found(self, label):
        print(f"Element not found: {label}")

if __name__ == '__main__':
    Bot.main()
        





