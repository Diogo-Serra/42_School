/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/19 16:49:52 by diosoare          #+#    #+#             */
/*   Updated: 2025/11/22 08:40:15 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libftprintf.h"

int			ft_printf(const char *src, ...);
static int	print_nbr(va_list pargs, const char flag);
static int	print_chr(va_list pargs, const char flag);

int	main(void)
{
	ft_printf("%c\n%c\n", 'O', 'K');
	return (0);
}

static int	print_chr(va_list pargs, const char flag)
{
	char	*str;
	char	c;
	int		len;
	int		count;

	count = 0;
	if (flag == 's')
	{
		str = va_arg(pargs, char *);
		if (!str)
			str = "(null)";
		len = ft_strlen(str);
		count = write(1, str, len);
	}
	else if (flag == 'c')
	{
		c = (char)va_arg(pargs, int);
		count = write(1, &c, 1);
	}
	else if (flag == '%')
		count = write(1, "%", 1);
	return (count);
}

static int	print_nbr(va_list pargs, const char flag)
{
	int		count;

	count = 0;
	if (flag == 'd' || flag == 'i')
		count = ft_putnbr_base(va_arg(pargs, int), DECIMAL);
	else if (flag == 'u')
		count = ft_putnbr_base(va_arg(pargs, unsigned int), DECIMAL);
	else if (flag == 'x')
		count = ft_putnbr_base(va_arg(pargs, unsigned int), LOWER_HEX);
	else if (flag == 'X')
		count = ft_putnbr_base(va_arg(pargs, unsigned int), UPPER_HEX);
	return (count);
}

static int	print_handler(va_list pargs, const char flag)
{
	if (flag == 'c' || flag == 's' || flag == '%')
		return (print_chr(pargs, flag));
	else if (flag == 'd' || flag == 'i' || flag == 'u'
		|| flag == 'x' || flag == 'X')
		return (print_nbr(pargs, flag));
	return (0);
}

int	ft_printf(const char *src, ...)
{
	va_list	pargs;
	int		count;
	int		i;

	i = 0;
	count = 0;
	va_start(pargs, src);
	while (src[i])
	{
		if (src[i] == '%' && src[i + 1])
		{
			i++;
			count += print_handler(pargs, src[i]);
		}
		else
			count += write(1, &src[i], 1);
		i++;
	}
	va_end(pargs);
	return (count);
}

/* 
char print:

• %c Prints a single character.
• %s Prints a string (as defined by the common C convention).
• %% Prints a percent sign. 

digit print:
• %d Prints a decimal (base 10) number.
• %i Prints an integer in base 10.
• %u Prints an unsigned decimal (base 10) number.
• %x Prints a number in hexadecimal (base 16) lowercase format.
• %X Prints a number in hexadecimal (base 16) uppercase format.

• %p The void * pointer argument has to be printed in hexadecimal format.

*/