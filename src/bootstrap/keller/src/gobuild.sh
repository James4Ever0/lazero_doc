#!/bin/bash
cd ~/
mkdir go
cd go
mkdir bin src pkg
GO111MODULE=on GOPATH=$(pwd) go get github.com/buildkite/terminal-to-html
GO111MODULE=on GOPATH=$(pwd) go get github.com/codegangsta/cli
GO111MODULE=on GOPATH=$(pwd) go get github.com/urfave/cli
