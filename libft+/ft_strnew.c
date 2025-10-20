/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strnew.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/16 08:43:51 by diosoare          #+#    #+#             */
/*   Updated: 2025/10/16 08:43:53 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strnew(size_t size)
{
	char	*p;
	size_t	i;

	p = (char *)malloc(size + 1);
	if (!p)
		return (NULL);
	i = 0;
	while (i <= size)
		p[i++] = '\0';
	return (p);
}
