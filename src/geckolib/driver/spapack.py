import os
import xml.etree.ElementTree as ET
import logging
import urllib3

from ..const import GeckoConstants

logger = logging.getLogger(__name__)


class GeckoSpaPack:
    """ Class to manage the SpaPackStruct.xml file """

    def __init__(self):
        GeckoSpaPack.download_if_needed()
        self._spa_pack_struct = ET.parse(GeckoConstants.SPA_PACK_STRUCT_FILE)
        self._spa_pack_struct_revision = self._spa_pack_struct.find(
            GeckoConstants.SPA_PACK_REVISION_XPATH
        ).attrib[GeckoConstants.SPA_PACK_REVISION_ATTRIB]
        logger.info("SpaPackStruct v%s", self.revision)

    @property
    def revision(self):
        """ Get the revision of the spa pack structure """
        return self._spa_pack_struct_revision

    @classmethod
    def download_if_needed(cls):
        """ Download SpaPackStruct.xml if it isn't already present """
        if not os.path.exists(GeckoConstants.SPA_PACK_STRUCT_FILE):
            logger.info("SpaPackStruct.xml not found, downloading from the internet...")
            GeckoSpaPack.download()

    @classmethod
    def download(cls):
        """ Download SpaPackStruct.xml from it's permanent home """
        logger.info("Downloading SpaPackStruct.xml")
        http = urllib3.PoolManager()
        response = http.request(
            "GET", GeckoConstants.SPA_PACK_STRUCT_URL, preload_content=False
        )

        with open(GeckoConstants.SPA_PACK_STRUCT_FILE, "wb") as out:
            while True:
                data = response.read(4096)
                if not data:
                    break
                out.write(data)

        response.release_conn()
        logger.info("SpaPackStruct.xml downloaded")

    @property
    def xml(self):
        """ Get the SpaPackStruct.xml root """
        return self._spa_pack_struct
