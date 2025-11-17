/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/08 19:26:08 by diosoare          #+#    #+#             */
/*   Updated: 2025/11/17 21:25:21 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

static char	*load_line(char *storage)
{
	char	*ptr_newline;
	size_t	len;

	if (!storage || !storage[0])
		return (NULL);
	ptr_newline = ft_strchr(storage, '\n');
	if (ptr_newline)
		len = (size_t)(ptr_newline - storage) + 1;
	else
		len = ft_strlen(storage);
	return (ft_substr(storage, 0, len));
}

static char	*trim_storage(char *storage)
{
	char	*ptr_newline;
	char	*new_storage;
	size_t	start;
	size_t	total;

	if (!storage)
		return (NULL);
	ptr_newline = ft_strchr(storage, '\n');
	if (!ptr_newline)
	{
		free(storage);
		return (NULL);
	}
	start = (size_t)(ptr_newline - storage) + 1;
	total = ft_strlen(storage);
	if (start >= total)
	{
		free(storage);
		return (NULL);
	}
	new_storage = ft_substr(storage, start, total - start);
	free(storage);
	return (new_storage);
}

static ssize_t	reading(int fd, char **storage, char *buffer)
{
	ssize_t	bytes_read;

	bytes_read = 1;
	while (!ft_strchr(*storage, '\n') && bytes_read > 0)
	{
		bytes_read = read(fd, buffer, BUFFER_SIZE);
		if (bytes_read > 0)
		{
			buffer[bytes_read] = '\0';
			*storage = ft_strjoin_free(*storage, buffer);
			if (!*storage)
				return (-1);
		}
		else if (bytes_read < 0)
		{
			return (-1);
		}
	}
	return (bytes_read);
}

char	*get_next_line(int fd)
{
    static char	*storage;
    char		buffer[BUFFER_SIZE + 1];
    ssize_t		bytes_read;
    char		*line;

    if (fd < 0 || BUFFER_SIZE <= 0)
        return (NULL);
    if (!storage && !(storage = ft_strdup("")))
        return (NULL);
    bytes_read = reading(fd, &storage, buffer);
    if (bytes_read < 0)
    {
        free(storage);
        storage = NULL;
        return (NULL);
    }
    line = load_line(storage);
    storage = trim_storage(storage);
    return (line);
}

int	main(void)
{
	char	*out;
	int		fd;

	fd = open("test.txt", O_RDONLY);
	out = get_next_line(fd);
	printf("Line->%s", out);
	free(out);
	out = get_next_line(fd);
	printf("Line->%s", out);
	free(out);
	out = get_next_line(fd);
	printf("Line->%s", out);
	free(out);
	close(fd);
	return (0);
}
