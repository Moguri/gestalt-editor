import panda3d.core as p3d


class AssetLibrary:
    '''A collection of imported assets'''

    def __init__(self):
        self.libraries = []
        self._loader = p3d.Loader.get_global_ptr()
        self._loader_opts = p3d.LoaderOptions()

    def import_file(self, filepath):
        '''Import the given filepath as a library'''
        filepath = p3d.Filename().from_os_specific(filepath)
        lib = self._loader.load_sync(
            filepath,
            self._loader_opts
        )

        if not lib:
            raise Exception(f'Failed to load {filepath}')

        self.libraries.append(lib)
