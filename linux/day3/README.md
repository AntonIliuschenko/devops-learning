
# 📄 Day 3 — Search and text processing

```markdown

grep — search text in files

`grep` is used to search for text patterns inside files or output.

### Basic usage

```bash
grep "error" file.log        # find "error"
grep -i "error" file.log     # ignore case
grep -r "error" /var/log     # recursive search
```

---

## Useful options

```bash
grep -v "text" file          # exclude matches
grep -n "text" file          # show line numbers
grep -c "text" file          # count matches
grep -l "text" *.log         # show filenames only
grep -w "word" file          # match whole word
grep -E "error|fail" file    # multiple patterns
```

---

## Working with logs (VERY IMPORTANT)

```bash
tail -f app.log | grep "ERROR"
```

Real-world usage:

* monitor logs in real time
* filter only important messages

---

## Pipes (|)

Pipe sends output of one command to another.

```bash
cat file.log | grep "error"
ps aux | grep nginx
```

Better way (no useless cat):

```bash
grep "error" file.log
```

---

## Redirects

```bash
grep "error" file.log > errors.txt     # overwrite file
grep "error" file.log >> errors.txt    # append
```

---

## Regular expressions (basic)

```bash
grep "^ERROR" file.log     # starts with ERROR
grep "fail$" file.log      # ends with fail
grep "." file.log          # any character
```

---
## Find

Search files:

find / -name file.txt
find /var -type f


## Pipes
cat file.log | grep error


---
## wc — count

```bash
wc -l file.log     # number of lines
wc -w file.log     # words
wc -c file.log     # bytes
```

Example:

```bash
grep "error" file.log | wc -l
```

---

## sort & uniq

```bash
sort file.txt              # sort lines
uniq file.txt              # remove duplicates
sort file.txt | uniq       # correct usage
```

Count unique values:

```bash
sort file.txt | uniq -c
```

---

## cut — extract columns

```bash
cut -d ":" -f1 /etc/passwd
```

* `-d` = delimiter
* `-f` = field

---

## awk — powerful text processing

```bash
awk '{print $1}' file.txt
awk '{print $1, $3}' file.txt
```

Example:

```bash
ps aux | awk '{print $1, $2}'
```

---

## sed — stream editor

```bash
sed 's/error/warning/g' file.txt
```

Replace text:

* `s` = substitute
* `g` = global

---

## Real DevOps examples

Find failed login attempts:

```bash
grep "Failed password" /var/log/auth.log
```

Count errors:

```bash
grep "ERROR" app.log | wc -l
```

Top IP addresses:

```bash
awk '{print $1}' access.log | sort | uniq -c | sort -nr
```

---

## Key takeaway

* `grep` — search
* `awk` — extract
* `sed` — modify
* `sort/uniq` — organize
* `wc` — count

Together they form the foundation of shell data processing.

