import panda3d.core as p3d


class SceneExporter:
    '''Export a scene'''

    def export(self, scene_root, filepath):
        '''Export the given scene root to the given filepath'''
        filepath = p3d.Filename().from_os_specific(filepath)
        ext = filepath.get_extension()

        if ext == 'bam':
            scene_root.write_bam_file(filepath)
        else:
            raise Exception(f'Unsupported export format: {ext}')
