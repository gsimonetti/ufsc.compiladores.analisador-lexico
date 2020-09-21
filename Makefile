.PHONY : install

install:
	pip install --user --upgrade .
	@echo "Pronto! 'alex' instalado com sucesso."
	@echo "Agora você pode executá-lo com 'alex <arquivo-fonte>'"


clean:
	pip uninstall -y alex ply
