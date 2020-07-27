from picamera import PiCamera

from app import BerryCam


def main():
    with PiCamera() as camera:
        app = BerryCam(camera)
        app.run()


if __name__ == "__main__":
    main()
