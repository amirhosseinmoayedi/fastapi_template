# Template for Fastapi projects
included
- [ ] sample-app-with-structure
- [ ] fix mypy in ci 


## start project
- need python version 3.12+
- need [poetry](https://python-poetry.org/) version 1.7.1+ 


### command will install main packages with packages used for development.
```bash
poetry install --with dev
```
### before any commit please run this
```bash
pre-commit install --hook-type commit-msg --hook-type pre-push
```
### running linter manually ([Ruff](https://docs.astral.sh/ruff/linter/))
```bash
ruff check                  # Lint all files in the current directory.
ruff check --fix
```
### running formatter manually (black)
```bash
black 
```
#### project uses mypy see the typehint [cheatsheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)

## increase the project version via [commitizen](https://commitizen-tools.github.io/commitizen/commands/bump/)
```bash
cz bump
cz bump --check-consistency # Check if the version in your configuration file matches the latest tag.
cz bump --increment minor #  Manually specify the version increment (patch, minor, major).
git push && git push --tags #  Push the changes and the new tag to your repository.
```

## App setting
to set the env copy the .env.sample and create .env file.
ant variable that start with `CUSTOM_` will be read to the project and can be used.
note: if you want to change the prefix to read env to something else you can do it in `app/settings.py`