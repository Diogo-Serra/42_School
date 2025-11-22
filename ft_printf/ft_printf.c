/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/19 16:49:52 by diosoare          #+#    #+#             */
/*   Updated: 2025/11/22 06:09:38 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libftprintf.h"

int ft_printf(const char *src, ...);

int	main(void)
{
	ft_printf("%c\n%c\n%s\n", 'O', 'K', "Teste");
	return (0);
}

int ft_printf(const char *src, ...)
{
	va_list	pargs;
	char	*string;
	int		len;
	char	arg;
	int		count;
	int		i;
	
	i = 0;
	count = 0;
 	va_start(pargs, src);
	while (src[i])
	{
		if (src[i] == '%' && src[i + 1] == 'c')
		{
			arg = (char)va_arg(pargs, int);
			write(1, (char)va_arg(pargs, int), 1);
			count++;
			i++;
		}
		else if (src[i] == '%' && src[i + 1] == 's')
		{
			string = va_arg(pargs, char *);
			len = ft_strlen(string);
			count += write(1, string, len);
			i++;
		}
		else
		{
			(write(1, &src[i], 1));
			count++;
		}
		i++;
		
	}
	return (count);
}

/* 
You have to implement the following conversions:

• %c Prints a single character.
• %s Prints a string (as defined by the common C convention).
• %p The void * pointer argument has to be printed in hexadecimal format.
• %d Prints a decimal (base 10) number.
• %i Prints an integer in base 10.
• %u Prints an unsigned decimal (base 10) number.
• %x Prints a number in hexadecimal (base 16) lowercase format.
• %X Prints a number in hexadecimal (base 16) uppercase format.
• %% Prints a percent sign. 
*/