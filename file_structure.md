# File Structure
---

The file structure goes as follows:
```
.
├── docs
│   ├── TOC.md                  # Table of Contents
│   ├── file_structure.md       # This file
│   ├── plugin_usage.md         # Usage of plugins
│   └── instructions.md         # Instructions on how to use TAC
├── [chapter_name]              # Name of the chapter, you can add as many as you want, but you have to have at least one
│   ├── story.txt               # Required file that contains the story for the chapter
│   ├── [area_name].txt         # Optional secondary file that contains the story for an area
│   └── ...                     # You can add as many area files as you want
├── story_chapters.txt          # Required file that contains the names of all the chapters (the folder name)
└── plugins                     # Optional folder that contains all of the plugins for the adventure
    ├── example.plugin          # An example plugin that shows the usage of unique commands
    ├── [plugin_name].plugin    # Optional plugin file that contains the code that is customizable
    └── ...                     # You can create as many plugins as you want
```
---
[Return to the Table of Contents](toc.md)
