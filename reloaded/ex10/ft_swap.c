/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_swap.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diserra <diserra@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/13 21:32:55 by diserra           #+#    #+#             */
/*   Updated: 2025/10/13 21:35:57 by diserra          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	ft_putchar(char c)
{
	write(1, &c, 1);
}

void ft_swap(int *a, int *b)
{

}

int	main(void)
{
	int	a;
	int	b;

	ft_putchar(a);
	ft_putchar(b);
	write(1, "\n", 1);
	ft_swap(a, b);
	ft_putchar(a);
	ft_putchar(b);
	write(1, "\n", 1);
}
