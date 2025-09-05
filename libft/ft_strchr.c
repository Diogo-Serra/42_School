/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strchr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diserra <diserra@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/05 14:55:22 by diserra           #+#    #+#             */
/*   Updated: 2025/09/05 14:55:29 by diserra          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strchr(const char *str, int c)
{
	const char	ch = (char)c;
	size_t		i;

	i = 0;
	while (str[i] != '\0')
	{
		if (str[i] == ch)
			return (char *)&str[i];
		i++;
	}
	if (ch == '\0')
		return (char *)&str[i];
	return (NULL);
}
