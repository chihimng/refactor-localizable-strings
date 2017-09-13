# Refactor-Localizable-Strings
This script is for refactoring Xcode localizable strings (after refactoring storyboards).

## Usage
1. Rename the .strings of your previous storyboard to somethings else (we will call this the base file from now on)
2. In Xcode, open each storyboard and enable localization so that xcode will generate new .strings
3. For your previous storyboards, uncheck and recheck the box for localized language so new .strings is generated with necessary items only
4. Run the script: `python3 refactor_localizable_strings.py /path/to/project/target_lang.lproj/ base_file.strings` (notice the space!)
5. Voila! The script searches for matching object ids in base file and pastes the translation to new files. Original files are backed up with extension .orig
