from IMagazzino_service import IMagazzino
import socket, sys, time
from abc import ABC, abstractmethod
import threading
from magazzinoImpl import MagazzinoImpl
import multiprocess as mp
import foo

if __name__ == "__main__":
    print(f'[Magazzino Main] Server Running...')
    magazzinoimpl = MagazzinoImpl(foo.HOST, int(foo.PORT))
    magazzinoimpl.run_skeleton()
