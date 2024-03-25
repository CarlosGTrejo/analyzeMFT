#!/usr/bin/env python3

try:
    from analyzemft import mftsession
except:
    from .analyzemft import mftsession

def main():
    session = mftsession.MftSession()
    session.mft_options()
    session.open_files()
    session.process_mft_file()


if __name__ == "__main__":
    main()
