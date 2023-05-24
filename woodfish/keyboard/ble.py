import dbus
import dbus.service
import dbus.mainloop.glib
import logging
from gi.repository import GLib
from keyboard.agent import Agent

from multiprocessing import Process


class Ble(Process):
    def __init__(self):
        Process.__init__(self)
        self.daemon = True
        dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
        self.bus = dbus.SystemBus()
        Agent(self.bus, "/bluetooth/agent")

    def run(self):
        mainloop = GLib.MainLoop()

        obj = self.bus.get_object("org.bluez", "/org/bluez")
        manager = dbus.Interface(obj, "org.bluez.AgentManager1")
        manager.RegisterAgent("/bluetooth/agent", "KeyboardDisplay")

        logging.info("Agent registered")
        manager.RequestDefaultAgent("/bluetooth/agent")

        mainloop.run()
