/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/08 19:26:08 by diosoare          #+#    #+#             */
/*   Updated: 2025/11/27 16:03:04 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

static char	*gnl_handler(int fd, char *buffer);
static char	*gnl_extract_line(char *storage, char *buffer);

/* int	main(void)
{
	char *line;
	int fd;
	int i;

	fd = open("test.txt", O_RDONLY);
	if (fd < 0)
	{
		printf("Error opening file\n");
		return (1);
	}
	i = 1;
	while ((line = get_next_line(fd)))
	{
		printf("Line %d: %s", i, line);
		free(line);
		i++;
	}
	printf("Line %d: \n", i);
	free(line);
	close(fd);
	return (0);
} */

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
	}
	if (!storage || !storage[0])
		return (free(storage), NULL);
	if (bytes > 0)
		return (gnl_extract_line(storage, buffer));
	return (buffer[0] = '\0', storage);
}

static char	*gnl_extract_line(char *storage, char *buffer)
{
	char	*line;
	char	*newline_pos;
	ssize_t	line_len;
	ssize_t	i;

	newline_pos = ft_strchr(storage, '\n');
	line_len = newline_pos - storage + 1;
	line = malloc(sizeof(char) * (line_len + 1));
	if (!line)
		return (free(storage), NULL);
	i = -1;
	while (++i < line_len)
		line[i] = storage[i];
	line[i] = '\0';
	i = -1;
	while (storage[line_len + ++i])
		buffer[i] = storage[line_len + i];
	buffer[i] = '\0';
	free(storage);
	return (line);
}
