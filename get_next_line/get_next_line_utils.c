/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_utils.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/25 16:04:36 by diosoare          #+#    #+#             */
/*   Updated: 2025/11/27 12:50:25 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

size_t	ft_strlen(const char *s)
{
	size_t	i;

	i = 0;
	while (s[i])
		i++;
	return (i);
}

char	*ft_strdup(const char *buffer)
{
	char	*dup;
	size_t	i;

	i = ft_strlen(buffer);
	dup = (char *)malloc(i + 1);
	if (!dup)
		return (NULL);
	i = 0;
	while (buffer[i])
	{
		dup[i] = buffer[i];
		i++;
	}
	dup[i] = '\0';
	return (dup);
}

char	*ft_strjoin(char *storage, char const *buffer)
{
	size_t	i;
	size_t	j;
	char	*out;

	if (!storage || !buffer)
		return (NULL);
	out = (char *)malloc(ft_strlen(storage) + ft_strlen(buffer) + 1);
	if (!out)
		return (NULL);
	i = 0;
	while (storage[i])
	{
		out[i] = storage[i];
		i++;
	}
	j = 0;
	while (buffer[j])
	{
		out[i + j] = buffer[j];
		j++;
	}
	free(storage);
	out[i + j] = '\0';
	return (out);
}

char	*ft_strchr(const char *storage, int newline)
{
	char		ch;

	ch = (unsigned char)newline;
	while (*storage)
	{
		if (*storage == ch)
			return ((char *)storage);
		storage++;
	}
	if (ch == '\0')
		return ((char *)storage);
	return (NULL);
}
