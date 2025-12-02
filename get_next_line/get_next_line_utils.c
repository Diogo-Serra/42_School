/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_utils.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/08 19:26:34 by diosoare          #+#    #+#             */
/*   Updated: 2025/12/02 16:01:20 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

char	*ft_strchr(const char *line, int c)
{
	char		ch;

	ch = (unsigned char)c;
	while (*line)
	{
		if (*line == ch)
			return ((char *)line);
		line++;
	}
	if (ch == '\0')
		return ((char *)line);
	return (NULL);
}

size_t	ft_strllen(const char *source)
{
	size_t	i;

	i = 0;
	if (!source)
		return (0);
	while (source[i])
	{
		if (source[i++] == '\n')
			break ;
	}
	return (i);
}

char	*clean_buffer(char *buffer)
{
	size_t	i;
	size_t	j;

	i = 0;
	while (buffer[i] && buffer[i] != '\n')
		i++;
	if (buffer[i] == '\n')
		i++;
	j = 0;
	while (buffer[i + j])
	{
		buffer[j] = buffer[i + j];
		j++;
	}
	while (j < BUFFER_SIZE + 1)
		buffer[j++] = '\0';
	return (buffer);
}

char	*ft_strnjoin(char *line, char const *buffer)
{
	ssize_t	i;
	ssize_t	j;
	char	*out;

	out = malloc((ft_strllen(line) + ft_strllen(buffer) + 1) * sizeof(char));
	if (!out)
		return (free(line), NULL);
	i = 0;
	while (line && line[i])
	{
		out[i] = line[i];
		i++;
	}
	j = 0;
	while (buffer[j])
	{
		out[i++] = buffer[j];
		if (buffer[j++] == '\n')
			break ;
	}
	out[i] = '\0';
	return (free(line), out);
}
