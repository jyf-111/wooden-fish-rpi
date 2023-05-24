from __future__ import absolute_import, print_function, unicode_literals
import dbus
import dbus.service
import dbus.mainloop.glib
from gi.repository import GLib
import logging


class Rejected(dbus.DBusException):
    _dbus_error_name = "org.bluez.Error.Rejected"


class Agent(dbus.service.Object):
    # dbus.set_default_main_loop(dbus.mainloop.glib.DBusGMainLoop())
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
    bus = dbus.SystemBus()
    exit_on_release = True
    agent_interface = "org.bluez.Agent1"
    dev_path = None
    device_obj = None

    def set_trusted(self, path):
        props = dbus.Interface(self.bus, "org.freedesktop.DBus.Properties")
        props.Set("org.bluez.Device1", "Trusted", True)

    def dev_connect(self, path):
        dev = dbus.Interface(self.bus, "org.bluez.Device1")
        dev.Connect()

    def pair_reply(self):
        logging.info("Device paired")
        self.set_trusted(self.dev_path)
        self.dev_connect(self.dev_path)
        GLib.mainloop.quit()

    def pair_error(self, error):
        err_name = error.get_dbus_name()
        if err_name == "org.freedesktop.DBus.Error.NoReply" and self.device_obj:
            logging.info("Timed out. Cancelling pairing")
            self.device_obj.CancelPairing()
        else:
            logging.info("Creating device failed: %s" % (error))
        GLib.mainloop.quit()

    def set_exit_on_release(self, exit_on_release):
        self.exit_on_release = exit_on_release

    @dbus.service.method(agent_interface, in_signature="", out_signature="")
    def Release(self):
        logging.info("Release")
        if self.exit_on_release:
            GLib.mainloop.quit()

    @dbus.service.method(agent_interface, in_signature="os", out_signature="")
    def AuthorizeService(self, device, uuid):
        logging.info("AuthorizeService (%s, %s)" % (device, uuid))

    @dbus.service.method(agent_interface, in_signature="o", out_signature="s")
    def RequestPinCode(self, device):
        logging.info("RequestPinCode (%s)" % (device))
        self.set_trusted(device)
        return input("Enter PIN Code: ")

    @dbus.service.method(agent_interface, in_signature="o", out_signature="u")
    def RequestPasskey(self, device):
        logging.info("RequestPasskey (%s)" % (device))
        self.set_trusted(device)
        passkey = input("Enter passkey: ")
        return dbus.UInt32(passkey)

    @dbus.service.method(agent_interface, in_signature="ouq", out_signature="")
    def DisplayPasskey(self, device, passkey, entered):
        logging.info(
            "DisplayPasskey (%s, %06u entered %u)" % (device, passkey, entered)
        )

    @dbus.service.method(agent_interface, in_signature="os", out_signature="")
    def DisplayPinCode(self, device, pincode):
        logging.info("DisplayPinCode (%s, %s)" % (device, pincode))

    @dbus.service.method(agent_interface, in_signature="ou", out_signature="")
    def RequestConfirmation(self, device, passkey):
        logging.info("RequestConfirmation (%s, %06d)" % (device, passkey))

    @dbus.service.method(agent_interface, in_signature="o", out_signature="")
    def RequestAuthorization(self, device):
        logging.info("RequestAuthorization (%s)" % (device))

    @dbus.service.method(agent_interface, in_signature="", out_signature="")
    def Cancel(self):
        logging.info("Cancel")
