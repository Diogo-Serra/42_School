# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/11/08 19:30:17 by diosoare          #+#    #+#              #
#    Updated: 2025/11/08 19:35:25 by diosoare         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME     := getlib.a

CC       := cc
CFLAGS   := -Wall -Wextra -Werror -I.
AR       := ar
ARFLAGS  := rcs
RM       := rm -f

SRCS := \
	get_next_line.c get_next_line_utils.c

OBJS := $(SRCS:.c=.o)

%.o: %.c get_next_line.h
	$(CC) $(CFLAGS) -c $< -o $@

# **************************************************************************** #

all: $(NAME)

$(NAME): $(OBJS)
	$(AR) $(ARFLAGS) $(NAME) $(OBJS)

clean:
	$(RM) $(OBJS)

fclean: clean
	$(RM) $(NAME)

re: fclean all

.PHONY: all bonus clean fclean re
