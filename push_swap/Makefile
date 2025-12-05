# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/05 22:05:53 by diosoare          #+#    #+#              #
#    Updated: 2025/12/05 22:22:20 by diosoare         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME     := push_swap

CC       := cc
CFLAGS   := -Wall -Wextra -Werror -I.
RM       := rm -f

SRCS := \
	push_swap.c push_swap_utils.c

OBJS := $(SRCS:.c=.o)

%.o: %.c push_swap.h
	$(CC) $(CFLAGS) -c $< -o $@

# **************************************************************************** #

all: $(NAME)

$(NAME): $(OBJS)
	$(CC) $(CFLAGS) $(OBJS) -o $(NAME)

clean:
	$(RM) $(OBJS)

fclean: clean
	$(RM) $(NAME)

re: fclean all

.PHONY: all bonus clean fclean re
