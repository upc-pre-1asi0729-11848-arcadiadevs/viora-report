OUTPUT_DIR=build
PDF_DEFAULTS=pandoc/report.yaml
WEB_DEFAULTS=pandoc/web.yaml
REFERENCE_DOC=pandoc/templates/reference.docx

PDF=$(OUTPUT_DIR)/report-pandoc.pdf
DOCX=$(OUTPUT_DIR)/report.docx
WEB_MD=$(OUTPUT_DIR)/report-web.md

all: pdf docx web

pdf:
	if not exist $(OUTPUT_DIR) mkdir $(OUTPUT_DIR)
	pandoc --defaults=$(PDF_DEFAULTS) --pdf-engine=xelatex -o $(PDF)

docx:
	if not exist $(OUTPUT_DIR) mkdir $(OUTPUT_DIR)
	pandoc --defaults=$(PDF_DEFAULTS) --reference-doc=$(REFERENCE_DOC) -o $(DOCX)

web:
	if not exist $(OUTPUT_DIR) mkdir $(OUTPUT_DIR)
	pandoc --defaults=$(WEB_DEFAULTS) -t markdown -o $(WEB_MD)

clean:
	if exist $(OUTPUT_DIR) rmdir /s /q $(OUTPUT_DIR)

rebuild: clean all