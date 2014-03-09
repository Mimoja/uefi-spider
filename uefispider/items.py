# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class UefispiderItem(Item):
    item_id = Field()
    binary = Field()
    pass

class BinaryItem(UefispiderItem):
    ### This item will only write a binary object.
    binary_name = Field()
    pass

class IntelBiosUpdateLinkItem(UefispiderItem):
    url = Field()
    name = Field()
    date = Field()
    version = Field()
    desc = Field()
    status = Field()

class IntelBiosUpdatePageItem(UefispiderItem):
    bios_url = Field()
    notes_url = Field()
    products = Field()
    attrs = Field() # attributes from LinkItem

class DellBiosResultsItem(Item):
    total = Field()

class DellBiosUpdateLinkItem(UefispiderItem):
    url = Field()
    release_date = Field()
    driver_type = Field()
    compatibility = Field()
    desc = Field()

class DellBiosUpdatePageItem(UefispiderItem):
    bios_urls = Field()
    file_names = Field()
    notes_url = Field()
    previous_versions = Field()
    importance = Field()
    version = Field()
    fixes = Field()
    attrs = Field() # attributes from LinkItem