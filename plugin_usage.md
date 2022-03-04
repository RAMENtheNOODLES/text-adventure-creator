# Plugin Usage

## Commands
Plugin files share all of the commands[^1] that a regular story or area file have.

There are some unique commands as well:

- Functions
  - Example:
    - ```
      func example {
        text: This is an example function!
      }
      ```
  - Usage:
    - ```
      func [function name] {
        [commands]
        ...
      }
      ```
  - The func command allows you to create functions in a plugin file. You can run it from the `run` command (explained below) or run it from a prompt[^2].
- Run
  - Example:
    - ```
      run > hello
      
      func hello {
        text: Hello World!
      }
      ```
  - Usage:
    - `run > [function name]`
  - The run command allows you to run a function within a plugin file.

---
[^1]: [Regular Commands](instructions.md)
[^2]: Check out an example [plugin](../plugins/example.plugin) on how to do this

[Return to Table of Contents](toc.md)
