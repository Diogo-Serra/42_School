/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_swap.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diserra <diserra@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/13 21:32:55 by diserra           #+#    #+#             */
/*   Updated: 2025/10/13 21:50:08 by diserra          ###   ########.fr       */
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
