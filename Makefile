# Nome do arquivo principal
MAIN_FILE = main.py

# Detecta o comando correto para Python
ifeq ($(OS),Windows_NT)
    PYTHON = python
    RM = del /Q __pycache__ 2>NUL || true
else
    PYTHON = python3
    RM = rm -rf __pycache__
endif

# Regras principais
run:
	$(PYTHON) $(MAIN_FILE)

clean:
	$(RM)

help:
	@echo "Comandos disponíveis:"
	@echo "  make run    - Executa o programa"
	@echo "  make clean  - Remove arquivos de cache"
