# gat
After working in multiple tech companies that have tools to streamline project management with git,
I decided to create a tool that can be used to simplify the setup of a git project from scratch.  

---
## Table of Contents
- [gat](#gat)
  - [Table of Contents](#table-of-contents)
- [Setup](#setup)
  - [Configuration File - `~/.gatconfig`](#configuration-file---gatconfig)
    - [Purpose](#purpose)
    - [Example](#example)
    - [Properties](#properties)
- [Usage](#usage)
  - [Commands](#commands)
    - [`gat clone`](#gat-clone)
      - [Example](#example-1)
---
# Setup  
## Configuration File - `~/.gatconfig`  
### Purpose  
The purpose of the `.gatconfig` file is too add a layer of configurability to the gat program.
### Example
```
# ~/.gatconfig
USER = TheWongGuy
```
### Properties
A list of the properties that can be set in `.gatconfig`.  

| USER | Stores the default user that repositories should be found under. |
|:----:|------------------------------------------------------------------|

# Usage
## Commands
### `gat clone`
`gat clone` is a replacement for the `git clone` command.  
`gat clone` will search within the users (set in the [gat config](#configuration-file---gatconfig)) github and look for repositories that are stored under that user.

This removes the need to provide an explicit url, however a url can be provided if needed. This ability to provide a url allows cloning of repositories from other users that may share the same name.

#### Example
```bash
git clone git@github.com:TheWongGuy/gat.git

gat clone gat
gat clone --url git@github.com:TheWongGuy/gat.git
```