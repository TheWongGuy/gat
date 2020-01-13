default:
	./setup.sh
	exec zsh
source:
	echo "[ -f ~/.gat/gat.sh ] && source ~/.gat/gat.sh" >> ~/.zshrc

clean:
	rm -rf ~/.gat
