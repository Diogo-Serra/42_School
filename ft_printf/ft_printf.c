/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/19 16:49:52 by diosoare          #+#    #+#             */
/*   Updated: 2025/11/27 22:29:42 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

static int	print_nbr(va_list pargs, const char flag);
static int	print_chr(va_list pargs, const char flag);
static int	print_handler(va_list pargs, const char flag);

/* int	main(void)
{
	int				ret1;
	char			*str;
	unsigned int	unum;
	void			*ptr;

	str = "Hello";
	unum = 42000;
	ptr = str;
	ret1 = ft_printf("Char: %c\n", 'A');
	ft_printf("Decimal: %d\n", ret1);
	ret1 = ft_printf("String: %s\n", str);
	ft_printf("Decimal: %d\n", ret1);
	ft_printf("Percent: %%\n");
	ft_printf("Integer: %i\n", -123);
	ft_printf("Unsigned: %u\n", unum);
	ft_printf("Hex lower: %x\n", 255);
	ft_printf("Hex upper: %X\n", 255);
	ft_printf("Pointer: %p\n", ptr);
	ft_printf("Null pointer: %p\n", NULL);
	ft_printf("Null string: %s\n", (char *) NULL);
	return (0);
} */

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
			count += print_handler(pargs, src[++i]);
		else
			count += write(1, &src[i], 1);
		i++;
	}
	va_end(pargs);
	return (count);
}

static int	print_handler(va_list pargs, const char flag)
{
	unsigned long	ptr;
	int				count;

	if (flag == 'c' || flag == 's' || flag == '%')
		return (print_chr(pargs, flag));
	if (flag == 'd' || flag == 'i' || flag == 'u'
		|| flag == 'x' || flag == 'X')
		return (print_nbr(pargs, flag));
	if (flag == 'p')
	{
		ptr = (unsigned long)va_arg(pargs, void *);
		if (ptr == 0)
			return (write(1, "(nil)", 5));
		count = write(1, "0x", 2);
		count += ft_putnbr_base(ptr, LOWER_HEX, 16);
		return (count);
	}
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
		len = 0;
		while (str[len])
			len++;
		count = write(1, str, len);
	}
	else if (flag == 'c')
	{
		c = (char)va_arg(pargs, int);
		count = write(1, &c, 1);
	}
	else if (flag == '%')
		count = write(1, &flag, 1);
	return (count);
}

static int	print_nbr(va_list pargs, const char flag)
{
	int		count;

	count = 0;
	if (flag == 'd' || flag == 'i')
		count = ft_putnbr_base(va_arg(pargs, int), DECIMAL, 10);
	if (flag == 'u')
		count = ft_putnbr_base(va_arg(pargs, unsigned int), DECIMAL, 10);
	if (flag == 'x')
		count = ft_putnbr_base(va_arg(pargs, unsigned int), LOWER_HEX, 16);
	if (flag == 'X')
		count = ft_putnbr_base(va_arg(pargs, unsigned int), UPPER_HEX, 16);
	return (count);
}
