/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_div_mod.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/13 21:50:44 by diserra           #+#    #+#             */
/*   Updated: 2025/10/14 17:49:46 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

void	ft_div_mod(int a, int b, int *div, int *mod)
{
	*div = a / b;
	*mod = a % b;
}
/*
void	ft_putnbr(int	n)
{
	char	c;

	if (n < 0)
	{
		write(1, "-", 1);
		n = -n;
	}
	if (n >= 10)
		ft_putnbr(n / 10);
	c = (n % 10) + '0';
	write(1, &c, 1);
}

int	main(void)
{
	int	div;
	int	mod;
	int	a = 10;
	int	b = 3;

	ft_div_mod(a, b, &div, &mod);
	write(1, "DIV: ", 5);
	ft_putnbr(div);
	write(1, "\n", 1);
	write(1, "MOD: ", 5);
	ft_putnbr(mod);
	write(1, "\n", 1);
}*/
