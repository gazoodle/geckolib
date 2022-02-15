#!/usr/bin/python3
""" Complete sample client

    This sample is built as a complete async client demonstrating all
    the code that might be needed in a full client of the library,
    e.g. in a home automation system.

    It was used to help develop the change from sync to async as
    this seems to be where all the HA integrations are going anyway

    I would have loved to have one library that could do both, but
    this was increasingly difficult to acheive and I was spending
    quite a bit of time in thread faff which is something that I'm
    sure is not needed in the async world ... time will tell

"""
import time

from context import GeckoAsyncLocator
from tui import init_tui
import logging
import configparser
import asyncio

# Replace with your own UUID, see https://www.uuidgenerator.net/>
CLIENT_ID = "1eca3a27-9b00-476a-9645-d13f4b1f9b56"

# Configuration file constants
CONFIG_FILE = "sample.ini"
CK_DEFAULT = "DEFAULT"
CK_SPA_ID = "SPA_ID"
CK_SPA_ADDR = "SPA_ADDR"

# Module globals
_LOGGER = logging.getLogger(__name__)
_CONFIG = configparser.ConfigParser()
_FACADE = None


########################################################################################
#
#                               Utility functions
#
def install_logging():
    """ Everyone needs logging, you say when, you say where, you say how much"""
    stream_logger = logging.StreamHandler()
    stream_logger.setLevel(logging.DEBUG)
    stream_logger.setFormatter(
        logging.Formatter("%(asctime)s> %(levelname)s %(message)s")
    )
    logging.getLogger().addHandler(stream_logger)
    logging.getLogger().setLevel(logging.WARNING)


def save_config():
    """Save the current configuration state to the persistent file in CONFIG_FILE"""
    with open(CONFIG_FILE, "w") as configfile:
        _CONFIG.write(configfile)


########################################################################################
#
#   Integration phase. This is when the user elects to manage a spa with their
#   automation system. You can either scan the network for all suitable spas, or if the
#   is on an a subnet that doesn't support broadcast, you can provide an IP address to
#   work with.
#
#   Once the spa has been found, or you've prompted the user to select it from a list
#   you store the address (and optionally the IP address) in the automation system
#   persistent configuration so that you can find it again without having to go through
#   this process
#
async def locate_spa(force_address=None):

    print("Locating spas on your network ", end="", flush=True)

    locator = GeckoAsyncLocator(CLIENT_ID, static_ip=force_address)
    locator.discover(asyncio.get_running_loop())

    # We can perform other operations while this is progressing, like output a dot
    while not locator.has_had_enough_time:
        await asyncio.sleep(1)
        print(".", end="", flush=True)

    print("")

    if len(locator.spas) == 0:
        print("Sorry, cannot continue as there were no spas detected on your network")
        return False

    # For simplicity sake we take the first spa, but your UI ought to offer
    # to choose one of them. This is a list of GeckoSpaDescriptor. The class
    # offers the following properties needed to establish a connection to the
    # spa
    #
    #   GeckoSpaDescriptor.client_identifier    - A client identifier
    #   GeckoSpaDescriptor.identifier           - The spa identifier (binary)
    #   GeckoSpaDescriptor.identifier_as_string - The spa identifier (string)
    #   GeckoSpaDescriptor.name                 - The spa name
    #   GeckoSpaDescriptor.ipaddress            - The in.touch2 module ip address
    #   GeckoSpaDescriptor.port                 - The UDP port of the in.touch2 module
    spa = locator.spas[0]

    print(f"Located spa '{spa}' at {spa.ipaddress}:{spa.port} to use")

    # Save the information about the chosen spa to the config block. The only
    # mandatory piece of information is the identifier. I choose to save the
    # address too since it speeds up the initial find, but this is done
    # knowing that on my LAN (and many others) the in.touch2 module gets the
    # same IP address. If this isn't the case, don't provide the address
    _CONFIG[CK_DEFAULT][CK_SPA_ID] = spa.identifier_as_string
    _CONFIG[CK_DEFAULT][CK_SPA_ADDR] = spa.ipaddress
    save_config()


########################################################################################
#
#   Automation start phase. This is when the automation system is starting and you will
#   get the persistence informatioin about the spa that you had previously stored in the
#   automation configuration system and try to reconnect to it.
#


def connect_spa(spa_id, spa_address):
    print(f"Connecting to spa {spa_id} at {spa_address}")

    global _FACADE
    _FACADE = GeckoLocator.get_facade(CLIENT_ID, spa_id, spa_addr)

    # Now we have a facade, wait for it to be connected
    print(f"Connecting to {_FACADE.name} ", end="", flush=True)
    while not _FACADE.is_connected:
        # Could also be `await asyncio.sleep(1)`
        _FACADE.wait(1)
        print(".", end="", flush=True)
    print(" connected")

########################################################################################
#
#


async def main():
    install_logging()
    init_tui()
    _LOGGER.debug("Read config")
    _CONFIG.read(CONFIG_FILE)

    # We have not previously run the client, we need to run a discovery
    if CK_SPA_ID not in _CONFIG[CK_DEFAULT]:
        if not await locate_spa():
            return

    # Get the spa info from the config block
    spa_id = _CONFIG[CK_DEFAULT][CK_SPA_ID]
    spa_addr = _CONFIG[CK_DEFAULT][CK_SPA_ADDR]
    #connect_spa(spa_id, spa_addr)

    #for item in _FACADE.all_automation_devices:
    #    print(item)

########################################################################################
#
#                                       Entry point
if __name__ == "__main__":
    asyncio.run(main())

if False:

    # Do some things with the facade
    print(f"Water heater : {facade.water_heater}")

    def pump_1_change(sender, old_value, new_value):
        print(f"Pump 1 changed from {old_value} to {new_value}")

    # Watch pump 1 for changes and report on them
    facade.pumps[0].watch(pump_1_change)

    print("Turn pump 1 on")
    facade.pumps[0].turn_on()

    time.sleep(5)

    print("Turning pump 1 off")
    facade.pumps[0].turn_off()

    time.sleep(2)
    facade.complete()
