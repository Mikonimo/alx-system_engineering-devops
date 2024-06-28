# Puppet File Project

This project demonstrates how to create a file using Puppet with specific permissions, ownership, and content.

## Manifest Details

- **File Path:** `/tmp/school`
- **Permissions:** `0744`
- **Owner:** `www-data`
- **Group:** `www-data`
- **Content:** `I love Puppet`

## Usage

1. Validate the Puppet manifest with `puppet-lint`.
2. Apply the manifest using `puppet apply`.

## Example Commands

```bash
puppet-lint 0-create_a_file.pp
puppet apply 0-create_a_file.pp
```
# Puppet Flask Installation Project

This project demonstrates how to install Flask version 2.1.0 using `pip3` with Puppet.

## Manifest Details

- **Package:** Flask
- **Version:** 2.1.0
- **Provider:** pip3

## Usage

1. Validate the Puppet manifest with `puppet-lint`.
2. Apply the manifest using `puppet apply`.

## Example Commands

```bash
puppet-lint 1-install_a_package.pp
puppet apply 1-install_a_package.pp

# Puppet Kill Process Project

This project demonstrates how to kill a process named `killmenow` using `pkill` and the `exec` Puppet resource.

## Manifest Details

- **Resource:** `exec`
- **Command:** `/usr/bin/pkill -f killmenow`

## Usage

1. Validate the Puppet manifest with `puppet-lint`.
2. Apply the manifest using `puppet apply`.

## Example Commands

```bash
puppet-lint 2-execute_a_command.pp
puppet apply 2-execute_a_command.pp
