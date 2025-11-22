/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/08 19:26:08 by diosoare          #+#    #+#             */
/*   Updated: 2025/11/22 20:42:47 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

char	*get_next_line(int fd)
{
	static char	*storage;
	char		*buffer;
	ssize_t		bytes_read;
	char		*line;

	if (fd < 0 || BUFFER_SIZE <= 0)
		return (NULL);
	buffer = (char *)malloc((size_t)BUFFER_SIZE + 1);
	if (!buffer)
		return (NULL);
	bytes_read = reading(fd, &storage, buffer);
	if (bytes_read < 0)
	{
		free(buffer);
		free(storage);
		storage = NULL;
		return (NULL);
	}
	free(buffer);
	line = load_line(storage);
	storage = trim_storage(storage);
	return (line);
}

static ssize_t	reading(int fd, char **storage, char *buffer)
{
	ssize_t	bytes_read;

	bytes_read = 1;
	while ((!*storage || !ft_strchr(*storage, '\n')) && bytes_read > 0)
	{
		bytes_read = read(fd, buffer, BUFFER_SIZE);
		if (bytes_read > 0)
		{
			buffer[bytes_read] = '\0';
			if (*storage)
				*storage = ft_strjoin_free(*storage, buffer);
			else
				*storage = ft_substr(buffer, 0, bytes_read);
			if (!*storage)
				return (-1);
		}
		else if (bytes_read < 0)
			return (-1);
	}
	return (bytes_read);
}

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

static char	*ft_strjoin_free(char *s1, char const *s2)
{
	size_t	len1;
	size_t	len2;
	char	*out;

	if (!s2)
		return (NULL);
	len1 = ft_strlen(s1);
	len2 = ft_strlen(s2);
	out = (char *)ft_calloc(len1 + len2 + 1, sizeof(char));
	if (!out)
		return (NULL);
	ft_memcpy(out, s1, len1);
	ft_memcpy(out + len1, s2, len2);
	free(s1);
	return (out);
}
