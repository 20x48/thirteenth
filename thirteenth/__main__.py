if __name__ != '__main__':
    exit()

try:
    from .ovo import Thirteenth
except ImportError:
    from ovo import Thirteenth

print(str(Thirteenth()))