from core import Core

if __name__ == "__main__":
    try:
        core = Core()
        core.init_config()
        core.init_ble()
        core.init_keyboard()
        core.init_ws2812b()
        core.init_rfp602_ao()
        core.run()
    except KeyboardInterrupt:
        import logging

        logging.info("exit")

        del core
