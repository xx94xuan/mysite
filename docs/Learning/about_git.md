Git Notes

## manage the commits 
eg. merge latest two commits

`git rebase --interactive HEAD~2`

then, modify in the editor by the following instruction:
```
# Commands:
#  p, pick = use commit
#  r, reword = use commit, but edit the commit message
#  e, edit = use commit, but stop for amending
#  s, squash = use commit, but meld into previous commit
#  f, fixup = like "squash", but discard this commit's log message
```

## show git log concise

`git log --pretty=oneline`