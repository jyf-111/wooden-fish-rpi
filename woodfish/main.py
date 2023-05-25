from core import Core

if __name__ == "__main__":
    try:
        core = Core()
        core.bootstrap()
        core.run()
    except OSError:
        print("OSError")
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
    finally:
        del core
