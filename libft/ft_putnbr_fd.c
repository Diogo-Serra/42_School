/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr_fd.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/16 08:34:14 by diosoare          #+#    #+#             */
/*   Updated: 2025/10/27 17:42:21 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_putnbr_fd(int n, int fd)
{
	char	arr[11];
	int		i[2];

	i[0] = sizeof(arr) - 1;
	i[1] = n;
	if (n < 0)
		n *= -1;
	if (n == 0)
		arr[--i[0]] = '0';
	while (n > 0)
	{
		arr[--i[0]] = (n % 10) + '0';
		n /= 10;
	}
	if (i[1] < 0)
		arr[--i[0]] = '-';
	while (i[0] < sizeof(arr) - 1)
		write(fd, &arr[i[0]++], 1);
	write(fd, "\n", 1);
}
