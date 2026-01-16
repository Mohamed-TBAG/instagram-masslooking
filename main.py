from asyncio import create_task, run
from masslooking import masslooking
from behaviours import behaviours_selector
from time import sleep
from logging import info, INFO, error, basicConfig
from seleniumdriver import Selinum_driver
from utils import login_info
from sys import exit

basicConfig(
    filename='masslooking.log',
    level=INFO,
    format='%(asctime)s - %(message)s'
)

async def main():
    sele_class = Selinum_driver()
    sele_class.login(login_info["username"], login_info["password"])
    info("logged in")
    user_agent = sele_class.get_user_agent()
    masslooking_obj = masslooking(sele_class.driver, sele_class, user_agent)
    behaviour_task = create_task(behaviours_selector(sele_class).run())
    create_task(masslooking_obj.run())
    await behaviour_task

try:
    run(main())
except Exception as e:
    error(f"An error occurred in main function : {e}")
    exit(0)