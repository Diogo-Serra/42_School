/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_utils.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/25 16:04:36 by diosoare          #+#    #+#             */
/*   Updated: 2025/11/27 22:03:39 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

size_t	ft_strlen(const char *source)
{
	size_t	i;

	i = 0;
	while (source[i])
		i++;
	return (i);
}

char	*ft_strdup(const char *buffer)
{
	char	*dup;
	ssize_t	i;

	if (!buffer)
		return (NULL);
	i = (size_t)ft_strlen(buffer);
	dup = malloc(i + 1);
	if (!dup)
		return (NULL);
	i = -1;
	while (buffer[++i])
		dup[i] = buffer[i];
	dup[i] = '\0';
	return (dup);
}

char	*ft_strjoin(char *storage, char const *buffer)
{
	ssize_t	i;
	ssize_t	j;
	char	*out;

	if (!storage || !buffer)
		return (NULL);
	out = malloc(ft_strlen(storage) + ft_strlen(buffer) + 1);
	if (!out)
		return (free(storage), NULL);
	i = -1;
	while (storage[++i])
		out[i] = storage[i];
	j = -1;
	while (buffer[++j])
		out[i + j] = buffer[j];
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
