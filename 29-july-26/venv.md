# Virtual Environments (venv)

A virtual environment is a **self-contained directory** that maintains a separate and isolated Python environment for a project.

This allows different projects to have different package versions without interfering with each other.

---

## Create a Virtual Environment

```bash
python3 -m venv my_name_of_the_env
```

This creates a new directory named `my_name_of_the_env`.

---

## Activate the Virtual Environment

```bash
source my_name_of_the_env/bin/activate
```

After activation, you'll see something like:

```text
(my_name_of_the_env)
```

at the beginning of your terminal prompt.

---

## Deactivate the Virtual Environment

Simply run:

```bash
deactivate
```

---

## List Installed Packages

```bash
pip list
```

Shows all packages currently installed **inside the active virtual environment**.

---

## Save Dependencies

```bash
pip freeze > requirements.txt
```

This saves all installed packages and their versions into `requirements.txt`.

---

## Install Dependencies on Another System

1. Create a virtual environment.

```bash
python3 -m venv my_name_of_the_env
```

2. Activate it.

```bash
source my_name_of_the_env/bin/activate
```

3. Install all dependencies.

```bash
pip install -r requirements.txt
```

This installs all the packages listed in `requirements.txt`.