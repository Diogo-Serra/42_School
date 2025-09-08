/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_ft_memalloc.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diserra <diserra@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/08 14:02:05 by diserra           #+#    #+#             */
/*   Updated: 2025/09/08 14:10:22 by diserra          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memalloc(size_t size)
{
	void	*p;
	size_t	i;

	p = malloc(size);
	if (!p)
		return (NULL);
	i = 0;
	while (i < size)
	{
		((unsigned char *)p)[i] = 0;
		i++;
	}
	return (p);
}
