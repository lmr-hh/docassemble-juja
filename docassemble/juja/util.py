__all__ = ["adresse", "is_time"]

from datetime import datetime
from docassemble.base.util import Address, Person, validation_error


def is_time(x: str):
    try:
        datetime.strptime(x, "%M:%S")
        return True
    except ValueError:
        validation_error("Das Format scheint nicht richtig zu sein. Geben Sie die Dauer im Format mm:ss an.")


def adresse(thing):
    """
    Gibt eine formatierte Postadresse zurück.
    """
    if isinstance(thing, str):
        return thing
    if isinstance(thing, Person):
        address = thing.address
    elif isinstance(thing, Address):
        address = thing
    else:
        raise ValueError(f"Cannot format object of type {type(thing)}")
    components = []
    if getattr(address, "route", None) and getattr(address, "street_number",
                                                   None):
        components.append(f"{address.route} {address.street_number}")
    elif getattr(address, "route", None):
        components.append(address.route)
    elif address.address:
        components.append(address.address)
    city_components = []
    if getattr(address, "zip", None):
        city_components.append(str(int(address.zip)))
    if getattr(address, "city", None):
        city_components.append(address.city)
    components.append(" ".join(city_components))
    return ", ".join(components)
