
# 📄 Day 2 — Filesystem

```markdown
# Day 2 — Filesystem

## Linux filesystem structure

/
├── home
├── etc
├── var
├── usr
├── tmp

## Key directories

- /home — user files
- /etc — configuration
- /var — logs and variable data
- /tmp — temporary files

## File operations

```bash
touch file.txt # create file
mkdir dir      # make new directory
cp file1 file2 # copy files(directories)
mv file1 file2 # move files(directories) / rename file or directory
rm file.txt    # delete file
rm -r dir      # delete directory use -r means recursive

# Important

Be careful with rm -rf (can delete everything). system will work until reboot
