import dbus
import dbus.service
import dbus.mainloop.glib
import logging
from gi.repository import GLib
from keyboard.agent import Agent

bus = None


class Ble:
    def __init__(self):
        global bus
        dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
        bus = dbus.SystemBus()
        Agent(bus, "/bluetooth/agent")

    def run(self):
        mainloop = GLib.MainLoop()

        obj = bus.get_object("org.bluez", "/org/bluez")
        manager = dbus.Interface(obj, "org.bluez.AgentManager1")
        manager.RegisterAgent("/bluetooth/agent", "KeyboardDisplay")

        logging.info("Agent registered")
        manager.RequestDefaultAgent("/bluetooth/agent")

        mainloop.run()
