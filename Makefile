NAME=dws

docker-build:
	docker build -t $(NAME) .

docker-run:
	docker run  -p 5000:5000 $(NAME):latest
