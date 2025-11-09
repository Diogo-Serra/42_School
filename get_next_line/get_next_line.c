/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/08 19:26:08 by diosoare          #+#    #+#             */
/*   Updated: 2025/11/09 00:26:41 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

static char	*load_storage(char **storage)
{
	char	*line;
	char	*new_storage;
	char	*newline_pos;
	size_t	line_len;

	if (!*storage)
		return (NULL);
	newline_pos = ft_strchr(*storage, '\n');
	if (newline_pos)
	{
		line_len = newline_pos - *storage + 1;
		line = ft_substr(*storage, 0, line_len);
		if (!line)
			return (NULL);
		new_storage = ft_strdup(newline_pos + 1);
		free (*storage);
		*storage = new_storage;
		if (!*storage)
			return (NULL);
	}
	else 
	{
		line = ft_strdup(*storage);
		free(*storage);
		*storage = NULL;
	}
	return (line);
}

static int	save_storage(int fd, char **storage)
{
	char	*buffer;
	char	*temp;
	ssize_t	bytes_read;

	buffer = malloc(BUFFER_SIZE + 1);
	if (!buffer)
		return (0);
	bytes_read = read(fd, buffer, BUFFER_SIZE);
	if (bytes_read <= 0)
	{
		free(buffer);
		return (bytes_read);
	}
	buffer[bytes_read] = '\0';
	if (!*storage)
		*storage = ft_strdup("");
	if (!*storage)
	{
		free(buffer);
		return (-1);
	}
	temp = ft_strjoin(*storage, buffer);
	if (!temp)
		return (-1);
	free(*storage);
	free(buffer);
	*storage = temp;
	return (1);
}

char *get_next_line(int fd)
{
	static char	*storage;
	int			read_status;

	if (fd < 0 || BUFFER_SIZE <= 0)
		return (NULL);
	read_status = 1;
	while (read_status > 0 && storage && !ft_strchr(storage, '\n'))
		read_status = save_storage(fd, &storage);
	if (read_status < 0)
	{
		free(storage);
		storage = NULL;
		return (NULL);
	}
	return (load_storage(&storage));
}

int main(void)
{
    char    *out;
    int     fd;

    fd = open("test.txt", O_RDONLY);
    out = get_next_line(fd);
	printf("%s\n", out);
    free(out);
    return (0);
}
