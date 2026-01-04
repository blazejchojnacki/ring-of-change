import os.path
import unittest

os.chdir('..')

import source.root as rt
import source.ground


class Test_Settings(unittest.TestCase):
    def setUp(self):
        pass

    def test_create_directories(self):
        settings_to_inititate = {
            source.ground.KEY_LIBRARY: "./trials/__test_lib",
            source.ground.KEY_ARCHIVE: "./trials/__test_arch",
            source.ground.KEY_GAMES: ["./trials/__test_game1", "./trials/__test_game2"],
            source.ground.KEY_NOT_MODS: ["./trials/__test_not_mod1"],
        }
        rt.settings.create_directories(settings_to_inititate)
        for key in settings_to_inititate:
            paths = []
            if isinstance(settings_to_inititate[key], str):
                paths = [settings_to_inititate[key]]
            elif isinstance(settings_to_inititate[key], list):
                paths = settings_to_inititate[key]
            for path in paths:
                self.assertTrue(os.path.isdir(path))
                os.rmdir(path)

    def test_propagate(self):
        value_copy = rt.settings[source.ground.KEY_LIBRARY]
        rt.settings[source.ground.KEY_LIBRARY] = "./trials/__test_lib"
        rt.settings.propagate()
        self.assertEqual(rt.library, "./trials/__test_lib")
        rt.settings[source.ground.KEY_LIBRARY] = value_copy
        rt.settings.propagate()

    def test_load(self):
        # # # loading before the file is created
        if not os.path.isfile(source.ground.SETTINGS_FILE_PATH):
            self.assertDictEqual(rt.settings, source.ground._SETTINGS_FORMAT)
            self.assertFalse(rt.loaded)
        # # # loading from file
        else:
            for key in source.ground._SETTINGS_FORMAT:
                self.assertIn(key, rt.settings)
            self.assertTrue(rt.loaded)

    def test_check_format(self):
        rt.settings['test_key'] = 'test_value'
        self.assertRaises(source.ground.InternalError, rt.settings.check_format)
        value_copy = rt.settings.pop(source.ground.KEY_LIBRARY)
        self.assertRaises(source.ground.InternalError, rt.settings.check_format)
        rt.settings.pop('test_key')
        rt.settings[source.ground.KEY_LIBRARY] = value_copy

    def test_check_paths__existing(self):
        settings_to_check = {
            source.ground.KEY_LIBRARY: "./source",
        }
        self.assertTrue(rt.settings.check_paths(settings_to_check))

    def test_check_paths__not_existing(self):
        settings_to_check = {
            source.ground.KEY_LIBRARY: "./trials/__test_lib",
            source.ground.KEY_ARCHIVE: "./trials/__test_arch",
        }
        self.assertFalse(rt.settings.check_paths(settings_to_check))

    def test_check_paths__missing(self):
        settings_to_check = {
            source.ground.KEY_LIBRARY: "",
        }
        self.assertFalse(rt.settings.check_paths(settings_to_check))

    def test_save__valid_new(self):
        if not os.path.isfile(source.ground.SETTINGS_FILE_PATH):
            settings_to_save = {
                source.ground.KEY_LIBRARY: "./trials/__test_lib",
            }
            for key in settings_to_save:
                paths = []
                if isinstance(settings_to_save[key], str):
                    paths = [settings_to_save[key]]
                elif isinstance(settings_to_save[key], list):
                    paths = settings_to_save[key]
                for path in paths:
                    os.makedirs(path)

            rt.settings.save(settings_to_save)
            self.assertTrue(os.path.isfile(source.ground.SETTINGS_FILE_PATH))

            for key in settings_to_save:
                paths = []
                if isinstance(settings_to_save[key], str):
                    paths = [settings_to_save[key]]
                elif isinstance(settings_to_save[key], list):
                    paths = settings_to_save[key]
                for path in paths:
                    os.rmdir(path)

    def test_save__invalid(self):
        settings_to_save = {
            source.ground.KEY_LIBRARY: "./trials/__test_lib",
        }
        self.assertRaises(source.ground.InternalError, rt.settings.save, settings_to_save)
