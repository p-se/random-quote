# random-quote

## Example configuration

```bash
# /etc/zsh/zshrc or ~/.zshrc
if [ -f $HOME/src/criminal-mind-quotes/quotes.txt ] ; then
    if which random-quote 2>&1 >/dev/null ; then
        random-quote $HOME/src/criminal-mind-quotes/quotes.txt
    fi
fi
```
