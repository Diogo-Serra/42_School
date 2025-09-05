/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strrchr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diserra <diserra@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/05 15:25:40 by diserra           #+#    #+#             */
/*   Updated: 2025/09/05 15:45:38 by diserra          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strrchr(const char *s, int c)
{
	const char	ch = (char)c;
	size_t		i;

	i = 0;
	while (s[i] != '\0')
		i++;
	if (s[i] == ch)
		return (char *)&s[i];
	while (i > 0)
	{
		i--;
		if (s[i] == ch)
			return (char *)&s[i];
	}
	return (NULL);
}
