/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/16 08:28:32 by diosoare          #+#    #+#             */
/*   Updated: 2025/10/22 19:32:29 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_itoa(int n)
{
	char	*s;
	char	num[11]; 
	int		data[3];

	data[0] = 10; 
	data[1] = (n >= 0) - (n < 0);
	while (n)
	{
		num[data[0]--] = (n % 10) + '0';
		n /= 10;
	}
	if (data[1] < 0)
		num[data[0]--] = '-'; 
	data[2] = 10 - data[0];
	s = ft_calloc(data[2] + 1, sizeof(char));
	if (!s)	
		return (NULL);
	data[0] = 10;
	while (data[2]--)
		s[data[2]] = num[data[0]--];
	return(s);
}
int	main(void)
{
	char *p = ft_itoa(42);
	printf("%s", p);
	return (free(p), 0);
}

