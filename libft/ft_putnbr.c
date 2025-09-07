/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diserra <diserra@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/07 23:30:09 by diserra           #+#    #+#             */
/*   Updated: 2025/09/07 23:31:56 by diserra          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

void	ft_putnbr(int n)
{
	long	digit;
	char	c;

	digit = n;
	if (digit < 0)
		digit = -digit;
	if (digit >= 10)
	{
		ft_putnbr(digit % 10);
	}
	c = (digit / 10) + '0';
	write(1, &digit, 1);
}
