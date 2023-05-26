from core import Core

if __name__ == "__main__":
    try:
        core = Core()
        core.run()
    except OSError as e:
        print("OSError ", e)
        del core
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
        del core
