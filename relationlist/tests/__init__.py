def test(verbosity=2, *, failfast=False):
    ff = " -f" if failfast else ""
    try:
        import green
        # import green_ # test
    except ImportError:
        import warnings
        warnings.simplefilter('once', ImportWarning)
        warnings.warn('green module missing, falling back to unittest.',
                      ImportWarning, 2)
        import unittest
        unittest.main('test', verbosity=verbosity)
    else:
        import subprocess, os
        os.chdir(os.path.sep.join(__file__.split(os.path.sep)[:-1]))
        os.chdir('..')
        os.chdir('..')
        try:
            subprocess.run('echo')
        except FileNotFoundError:
            shell = True
        else:
            shell = False
        if verbosity:
            subprocess.run(f'green _relationlist -{"v"*verbosity}{ff}', 
                           shell=shell)
        else:
            subprocess.run(f'green _relationlist{ff}', shell=shell)
if __name__ == '__main__':
    test(int(input()))
