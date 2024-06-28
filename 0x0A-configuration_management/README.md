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

