/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_operator.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/19 16:52:42 by diosoare          #+#    #+#             */
/*   Updated: 2025/11/19 16:57:11 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

void	ft_putnbr(int n)
{
	char	arr[11];
	long	i[2];

	i[0] = 10;
	i[1] = (long)n;
	if (i[1] < 0)
		i[1] *= -1;
	if (i[1] == 0)
		arr[--i[0]] = '0';
	while (i[1] > 0)
	{
		arr[--i[0]] = (i[1] % 10) + '0';
		i[1] /= 10;
	}
	if (n < 0)
		arr[--i[0]] = '-';
	while (i[0] < 10)
		write(1, &arr[i[0]++], 1);
}

void	ft_putstr(char const *s)
{
	size_t	i;

	if (!s)
		return ;
	i = 0;
	while (s[i])
		i++;
	write(1, s, i);
}

void	ft_putchar(char c)
{
	write(1, &c, 1);
}
