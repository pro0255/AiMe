# AiMe

# Troubleshoot

`
INFO:     Will watch for changes in these directories: ['/Users/Vojtech.Prokop/Desktop/Projects/Personal/Python/AiMe']
ERROR:    [Errno 48] Address already in use
make: *** [run-server] Error 1
`

It's because the defined port is used by background process. We need to kill it.

- Run `ps -a | grep python | grep uvicorn`
- Read the first number example: "68108 ttys003" -> `68108`
- Run `kill -9 68108`


# How to docker it?

- `docker build -t aime .`
- `docker run -d --name AI_ME -p 8000:8000 aime`

After that, you should be able to see running container inside of docker.