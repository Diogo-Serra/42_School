/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr_fd.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/16 08:34:14 by diosoare          #+#    #+#             */
/*   Updated: 2025/10/27 13:14:24 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_putnbr_fd(int n, int fd)
{
	char	arr[12];
	long	nb;
	size_t	i;

	nb = n;
	i = sizeof(arr) - 1;
	if (nb < 0)
		nb = -nb;
	if (nb == 0)
		arr[--i] = '0';
	while (nb > 0)
	{
		ft_putchar_fd((nb % 10) + '0', fd);
		nb /= 10;
	}
	if (n < 0)
		ft_putchar_fd('-', fd);
}
