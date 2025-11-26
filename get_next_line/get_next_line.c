/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/08 19:26:08 by diosoare          #+#    #+#             */
/*   Updated: 2025/11/26 23:22:39 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

static char	*gnl_handler(int fd, char *buffer);
static char	*gnl_extract_line(char *storage, char *buffer);

char	*get_next_line(int fd)
{
	static char	buffer[BUFFER_SIZE + 1];

	if (fd < 0 || BUFFER_SIZE < 1)
		return (NULL);
	return (gnl_handler(fd, buffer));
}

static char	*gnl_handler(int fd, char *buffer)
{
	char	*storage;
	ssize_t	bytes;

	storage = ft_strdup(buffer);
	if (!storage)
		return (NULL);
	buffer[0] = '\0';
	bytes = 1;
	while (bytes > 0 && !ft_strchr(storage, '\n'))
	{
		bytes = read(fd, buffer, BUFFER_SIZE);
		if (bytes < 0)
			return (free(storage), NULL);
		buffer[bytes] = '\0';
		storage = ft_strjoin(storage, buffer);
		if (!storage)
			return (NULL);
	}
	if (!storage[0])
		return (free(storage), NULL);
	if (ft_strchr(storage, '\n'))
		return (gnl_extract_line(storage, buffer));
	return (buffer[0] = '\0', storage);
}

char	*gnl_extract_line(char *storage, char *buffer)
{
	char	*line;
	char	*newline_pos;
	int		line_len;
	int		i;

	newline_pos = ft_strchr(storage, '\n');
	line_len = newline_pos - storage + 1;
	line = malloc(sizeof(char) * (line_len + 1));
	if (!line)
		return (free(storage), NULL);
	i = -1;
	while (++i < line_len)
		line[i] = storage[i];
	line[i] = '\0';
	i = 0;
	while (storage[line_len + i])
	{
		buffer[i] = storage[line_len + i];
		i++;
	}
	buffer[i] = '\0';
	free(storage);
	return (line);
}
