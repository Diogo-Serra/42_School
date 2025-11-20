/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/19 16:49:52 by diosoare          #+#    #+#             */
/*   Updated: 2025/11/20 17:51:00 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdarg.h>
#include <stdio.h>

int ft_printf(const char *src, ...)
{
	va_list	args;

	va_start(args, src);
	printf("%d\n", va_arg(args, int));
	printf("%d\n", va_arg(args, int));
	return (0);
}

int	main(void)
{
	ft_printf("%d", 42, 24);
	return (0);
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