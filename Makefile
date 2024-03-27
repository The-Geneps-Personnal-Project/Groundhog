SRC	=	main.py

NAME	=	groundhog

$(NAME)	:
			cp $(SRC) groundhog.py
			mv groundhog.py groundhog
			chmod 755 groundhog

all	:	$(NAME)

clean:
		rm -f groundhog

fclean:	clean

re	:	fclean all

.PHONY	:	re fclean clean all