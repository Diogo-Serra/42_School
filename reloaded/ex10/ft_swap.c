/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_swap.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/14 17:43:57 by diosoare          #+#    #+#             */
/*   Updated: 2025/10/14 17:49:15 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

void	ft_swap(int *a, int *b)
{
	*a = *a + *b;
	*b = *a - *b;
	*a = *a - *b;
}
/*
void	ft_putnbr(int n)
{
	char	c;

	c = (n % 10) + '0';
	write(1, &c, 1);
}

int	main(void)
{
	int	a;
	int	b;

	a = 2;
	b = 4;
	ft_putnbr(a);
	ft_putnbr(b);
	write(1, "\n", 1);
	ft_swap(&a, &b);
	ft_putnbr(a);
	ft_putnbr(b);
	write(1, "\n", 1);
}*/