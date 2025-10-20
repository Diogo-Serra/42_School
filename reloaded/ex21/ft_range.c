/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_range.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/14 23:12:12 by diosoare          #+#    #+#             */
/*   Updated: 2025/10/14 23:47:11 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

int	*ft_range(int min, int max)
{
	int			*out;
	size_t		len;
	size_t		i;

	if (min >= max)
		return (NULL);
	len = (size_t)(max - min);
	out = malloc(len * sizeof(int));
	if (!out)
		return (NULL);
	i = 0;
	while (i < len)
	{
		out[i] = min + (int)i;
		i++;
	}
	return (out);
}
