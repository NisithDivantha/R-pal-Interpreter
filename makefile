# PYTHON2 = python
# PYTHON3 = python3

# # Targets
# .PHONY: all clean run_lexical_analyzer -ast

# all: run

# run: run_lexical_analyzer -ast

# run_lexical_analyzer:
# 	$(PYTHON2) Test/test_lexical_analyzer.py || $(PYTHON3) Test/test_lexical_analyzer.py

# -ast:
# 	$(PYTHON2) Test/test_parser.py || $(PYTHON3) Test/test_parser.py

# clean:
# 	# Add commands to clean up generated files or directories

# PYTHON2 = python
# PYTHON3 = python3

# # Get the current directory
# CURRENT_DIR := $(shell pwd)

# # Set the path to the project directory
# PROJECT_DIR := $(CURRENT_DIR)

# # Set PYTHONPATH to include the project directory
# export PYTHONPATH := $(PROJECT_DIR):$(PYTHONPATH)

# # Targets
# .PHONY: all clean run_lexical_analyzer -ast

# all: run

# run: run_lexical_analyzer -ast

# run_lexical_analyzer:
# 	@echo "Running lexical analyzer..."
# 	$(PYTHON2) $(PROJECT_DIR)/Test/test_lexical_analyzer.py || $(PYTHON3) $(PROJECT_DIR)/Test/test_lexical_analyzer.py

# -ast:
# 	@echo "Running parser..."
# 	$(PYTHON2) $(PROJECT_DIR)/Test/test_parser.py || $(PYTHON3) $(PROJECT_DIR)/Test/test_parser.py

# clean:
# 	# Add commands to clean up generated files or directories


PYTHON2 := python
PYTHON3 := python3

# Set the Python path
export PYTHONPATH := $(PWD):$(PYTHONPATH)

# Targets
.PHONY: all clean run_lexical_analyzer -ast run_standardizer run_cse_machine

all: run

run: run_lexical_analyzer ast run_standardizer run_cse_machine

run_lexical_analyzer:
	@echo "Running lexical analyzer..."
	@if command -v $(PYTHON2) >/dev/null; then \
		$(PYTHON2) Test/test_lexical_analyzer.py; \
	elif command -v $(PYTHON3) >/dev/null; then \
		$(PYTHON3) Test/test_lexical_analyzer.py; \
	else \
		echo "Python 2 and Python 3 not found"; \
	fi


ast:
	@echo "Running parser..."
	@if command -v $(PYTHON2) >/dev/null; then \
		$(PYTHON2) Test/test_parser.py ast; \
	elif command -v $(PYTHON3) >/dev/null; then \
		$(PYTHON3) Test/test_parser.py ast; \
	else \
		echo "Python 2 and Python 3 not found"; \
	fi



run_standardizer:
	@echo "Running standardizer..."
	@if command -v $(PYTHON2) >/dev/null; then \
		$(PYTHON2) Test/test_st.py; \
	elif command -v $(PYTHON3) >/dev/null; then \
		$(PYTHON3) Test/test_st.py; \
	else \
		echo "Python 2 and Python 3 not found"; \
	fi

run_cse_machine:
	@echo "Running cse machine..."
	@if command -v $(PYTHON2) >/dev/null; then \
		$(PYTHON2) Test/test_cse_machine.py; \
	elif command -v $(PYTHON3) >/dev/null; then \
		$(PYTHON3) Test/test_cse_machine.py; \
	else \
		echo "Python 2 and Python 3 not found"; \
	fi

clean:
	# Add commands to clean up generated files or directories
