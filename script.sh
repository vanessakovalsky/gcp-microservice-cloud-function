eval 'set +o history' 2>/dev/null || setopt HIST_IGNORE_SPACE 2>/dev/null
 touch ~/.gitcookies
 chmod 0600 ~/.gitcookies

 git config --global http.cookiefile ~/.gitcookies

 tr , \\t <<\__END__ >>~/.gitcookies
source.developers.google.com,FALSE,/,TRUE,2147483647,o,git-ib.cegos1.gmail.com=1//03crFDfWvv4yvCgYIARAAGAMSNwF-L9IrmQI1u_TWc0ZzPCgdxGyKOcSc3vySpjnb-GquEdUnzGPWmWhUxMpc6K_K9ns9a2JFTKQ
__END__
eval 'set -o history' 2>/dev/null || unsetopt HIST_IGNORE_SPACE 2>/dev/null

