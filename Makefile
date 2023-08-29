# Recipes for website builds
SHELL := /bin/bash
.PHONY = docs preview webcommit

docs: config.py $(shell find content -type f)
	iacs publish

preview: docs
	iacs launch

webcommit: docs
	git add docs && git commit -v -m "Web update by ${USER} on $(shell date)"
	@echo 'WARNING: `webcommit` only commits changes below docs/'
	@echo '         Commit your changes in the source code in a separate commit'
