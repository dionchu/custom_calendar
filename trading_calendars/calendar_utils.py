from .always_open import AlwaysOpenCalendar
from .errors import (
    CalendarNameCollision,
    CyclicCalendarAlias,
    InvalidCalendarName,
)
from .all_days import AllDaysCalendar
from .exchange_calendar_bmex import BMEXExchangeCalendar
from .exchange_calendar_ifeu import IFEUExchangeCalendar
from .exchange_calendar_ifus import IFUSExchangeCalendar
from .exchange_calendar_xasx import XASXExchangeCalendar
from .exchange_calendar_xbru import XBRUExchangeCalendar
from .exchange_calendar_xcme import XCMEExchangeCalendar
from .exchange_calendar_xjpx import XJPXExchangeCalendar
from .exchange_calendar_xmil import XMILExchangeCalendar
from .exchange_calendar_xmod import XMODExchangeCalendar
from .exchange_calendar_xnym import XNYMExchangeCalendar
from .exchange_calendar_xnys import XNYSExchangeCalendar
from .exchange_calendar_xpar import XPARExchangeCalendar
from .exchange_calendar_xtse import XTSEExchangeCalendar
from .exchange_calendar_xeur import XEURExchangeCalendar
from .exchange_calendar_xosl import XOSLExchangeCalendar
from .exchange_calendar_xsto import XSTOExchangeCalendar
from .exchange_calendar_usbond import USBONDExchangeCalendar
from .weekday_calendar import WeekdayCalendar

_default_calendar_factories = {
    # Exchange calendars.
    'BMEX': BMEXExchangeCalendar,
    'IFEU': IFEUExchangeCalendar,
    'IFUS': IFUSExchangeCalendar,
    'XASX': XASXExchangeCalendar,
    'XBRU': XBRUExchangeCalendar,
    'XCME': XCMEExchangeCalendar,
    'XJPX': XJPXExchangeCalendar,
    'XMIL': XMILExchangeCalendar,
    'XMOD': XMODExchangeCalendar,
    'XNYM': XNYMExchangeCalendar,
    'XNYS': XNYSExchangeCalendar,
    'XPAR': XPARExchangeCalendar,
    'XTSE': XTSEExchangeCalendar,
    'XEUR': XEURExchangeCalendar,
    'XOSL': XOSLExchangeCalendar,
    'XSTO': XSTOExchangeCalendar,
    'USBOND': USBONDExchangeCalendar,
    'ALL': AllDaysCalendar,
    # Miscellaneous calendars.
    '24/7': AlwaysOpenCalendar,
    '24/5': WeekdayCalendar,
}
_default_calendar_aliases = {
    'TSX': 'XTSE',
    'CME': 'CMES',
    'CBOT': 'XCME',
    'COMEX': 'XCME',
    'ICE': 'IFEU',
    'ICEUS': 'IFUS',
}
default_calendar_names = sorted(_default_calendar_factories.keys())


class TradingCalendarDispatcher(object):
    """
    A class for dispatching and caching trading calendars.

    Methods of a global instance of this class are provided by
    calendars.calendar_utils.

    Parameters
    ----------
    calendars : dict[str -> TradingCalendar]
        Initial set of calendars.
    calendar_factories : dict[str -> function]
        Factories for lazy calendar creation.
    aliases : dict[str -> str]
        Calendar name aliases.
    """
    def __init__(self, calendars, calendar_factories, aliases):
        self._calendars = calendars
        self._calendar_factories = calendar_factories
        self._aliases = aliases

    def get_calendar(self, name, group = None):
        """
        Retrieves an instance of an TradingCalendar whose name is given.

        Parameters
        ----------
        name : str
            The name of the TradingCalendar to be retrieved.

        Returns
        -------
        calendar : calendars.TradingCalendar
            The desired calendar.
        """
        canonical_name = self.resolve_alias(name)

        try:
            if group is not None:
                calendar = self._calendars[canonical_name]
                calendar.product_group = group
                calendar.__init__()
                return calendar
            else:
                return self._calendars[canonical_name]
        except KeyError:
            # We haven't loaded this calendar yet, so make a new one.
            pass

        try:
            factory = self._calendar_factories[canonical_name]
        except KeyError:
            # We don't have a factory registered for this name.  Barf.
            raise InvalidCalendarName(calendar_name=name)

        # Cache the calendar for future use.
        calendar = self._calendars[canonical_name] = factory()
        if group is not None:
            calendar.product_group = group
            calendar.__init__()
            return calendar
        else:
            return calendar

    def has_calendar(self, name):
        """
        Do we have (or have the ability to make) a calendar with ``name``?
        """
        return (
            name in self._calendars
            or name in self._calendar_factories
            or name in self._aliases
        )

    def register_calendar(self, name, calendar, force=False):
        """
        Registers a calendar for retrieval by the get_calendar method.

        Parameters
        ----------
        name: str
            The key with which to register this calendar.
        calendar: TradingCalendar
            The calendar to be registered for retrieval.
        force : bool, optional
            If True, old calendars will be overwritten on a name collision.
            If False, name collisions will raise an exception.
            Default is False.

        Raises
        ------
        CalendarNameCollision
            If a calendar is already registered with the given calendar's name.
        """
        if force:
            self.deregister_calendar(name)

        if self.has_calendar(name):
            raise CalendarNameCollision(calendar_name=name)

        self._calendars[name] = calendar

    def register_calendar_type(self, name, calendar_type, force=False):
        """
        Registers a calendar by type.

        This is useful for registering a new calendar to be lazily instantiated
        at some future point in time.

        Parameters
        ----------
        name: str
            The key with which to register this calendar.
        calendar_type: type
            The type of the calendar to register.
        force : bool, optional
            If True, old calendars will be overwritten on a name collision.
            If False, name collisions will raise an exception.
            Default is False.

        Raises
        ------
        CalendarNameCollision
            If a calendar is already registered with the given calendar's name.
        """
        if force:
            self.deregister_calendar(name)

        if self.has_calendar(name):
            raise CalendarNameCollision(calendar_name=name)

        self._calendar_factories[name] = calendar_type

    def register_calendar_alias(self, alias, real_name, force=False):
        """
        Register an alias for a calendar.

        This is useful when multiple exchanges should share a calendar, or when
        there are multiple ways to refer to the same exchange.

        After calling ``register_alias('alias', 'real_name')``, subsequent
        calls to ``get_calendar('alias')`` will return the same result as
        ``get_calendar('real_name')``.

        Parameters
        ----------
        alias : str
            The name to be used to refer to a calendar.
        real_name : str
            The canonical name of the registered calendar.
        force : bool, optional
            If True, old calendars will be overwritten on a name collision.
            If False, name collisions will raise an exception.
            Default is False.
        """
        if force:
            self.deregister_calendar(alias)

        if self.has_calendar(alias):
            raise CalendarNameCollision(calendar_name=alias)

        self._aliases[alias] = real_name

        # Ensure that the new alias doesn't create a cycle, and back it out if
        # we did.
        try:
            self.resolve_alias(alias)
        except CyclicCalendarAlias:
            del self._aliases[alias]
            raise

    def resolve_alias(self, name):
        """
        Resolve a calendar alias for retrieval.

        Parameters
        ----------
        name : str
            The name of the requested calendar.

        Returns
        -------
        canonical_name : str
            The real name of the calendar to create/return.
        """
        seen = []

        while name in self._aliases:
            seen.append(name)
            name = self._aliases[name]

            # This is O(N ** 2), but if there's an alias chain longer than 2,
            # something strange has happened.
            if name in seen:
                seen.append(name)
                raise CyclicCalendarAlias(
                    cycle=" -> ".join(repr(k) for k in seen)
                )

        return name

    def deregister_calendar(self, name):
        """
        If a calendar is registered with the given name, it is de-registered.

        Parameters
        ----------
        cal_name : str
            The name of the calendar to be deregistered.
        """
        self._calendars.pop(name, None)
        self._calendar_factories.pop(name, None)
        self._aliases.pop(name, None)

    def clear_calendars(self):
        """
        Deregisters all current registered calendars
        """
        self._calendars.clear()
        self._calendar_factories.clear()
        self._aliases.clear()


# We maintain a global calendar dispatcher so that users can just do
# `register_calendar('my_calendar', calendar) and then use `get_calendar`
# without having to thread around a dispatcher.
global_calendar_dispatcher = TradingCalendarDispatcher(
    calendars={},
    calendar_factories=_default_calendar_factories,
    aliases=_default_calendar_aliases,
)

get_calendar = global_calendar_dispatcher.get_calendar
clear_calendars = global_calendar_dispatcher.clear_calendars
deregister_calendar = global_calendar_dispatcher.deregister_calendar
register_calendar = global_calendar_dispatcher.register_calendar
register_calendar_type = global_calendar_dispatcher.register_calendar_type
register_calendar_alias = global_calendar_dispatcher.register_calendar_alias
resolve_alias = global_calendar_dispatcher.resolve_alias
