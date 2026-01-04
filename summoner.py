import source.root
import source.ground

if not source.root.loaded:
    start_settings = {
        source.ground.KEY_LIBRARY: "./_LIBRARY",
        source.ground.KEY_ARCHIVE: "./_ARCHIVE",
    }
    source.root.settings.create_directories(start_settings)
    source.root.settings.save(start_settings)
    source.root.loaded = source.root.settings.load()

