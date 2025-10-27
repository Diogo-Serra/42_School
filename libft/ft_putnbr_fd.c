/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr_fd.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/16 08:34:14 by diosoare          #+#    #+#             */
/*   Updated: 2025/10/27 12:53:34 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_putnbr_fd(int n, int fd)
{
	char	arr[12];
	long	nb;
	int		i;

	nb = n;
	i = sizeof(arr);
	if (nb < 0)
		nb = -nb;
	if (nb == 0)
		arr[--i] = '0';
	while (nb > 0)
	{
		arr[--i] = (nb % 10) + '0';
		nb /= 10; 
	}
	if (n < 0)
		arr[--i] = '-';
	ft_putstr_fd(arr + i, fd);
}

int	main(void)
{
	ft_putnbr_fd(25, 1);
	return (0);
}
