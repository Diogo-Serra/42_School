# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/11/19 16:58:36 by diosoare          #+#    #+#              #
#    Updated: 2025/11/22 20:00:51 by diosoare         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME     := libftprintf.a

CC       := cc
CFLAGS   := -Wall -Wextra -Werror -I.
AR       := ar
ARFLAGS  := rcs
RM       := rm -f

SRCS := \
	ft_printf.c printfhelper.c

OBJS := $(SRCS:.c=.o)

%.o: %.c ft_printf.h
	$(CC) $(CFLAGS) -c $< -o $@

# **************************************************************************** #

all: $(NAME)

$(NAME): $(OBJS)
	$(AR) $(ARFLAGS) $(NAME) $(OBJS)

clean:
	$(RM) $(OBJS) $(BONUS_OBJS)

fclean: clean
	$(RM) $(NAME)

re: fclean all

.PHONY: all bonus clean fclean re
