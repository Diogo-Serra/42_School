/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/08 19:26:08 by diosoare          #+#    #+#             */
/*   Updated: 2025/11/25 16:54:40 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

static char	*read_handler(char *buffer, ssize_t bytes_read);

int	main(void)
{
	char	*str;
	str = get_next_line(open("test.txt", O_RDONLY));
	printf("%s\n", str);
	free(str);
	return (0);
}

char	*get_next_line(int fd)
{
	static char	buffer[BUFFER_SIZE + 1];
	ssize_t		bytes_read;
	char		*line;

	if (fd < 0 || BUFFER_SIZE < 1)
		return (NULL);
	bytes_read = 1;
	line = NULL;
	while (bytes_read)
	{
		if (!*buffer)
			bytes_read = read(fd, buffer, BUFFER_SIZE);
		if (bytes_read < 0)
			return (NULL);
		line = read_handler(buffer, bytes_read);
	}
	return (line);
}

static char	*read_handler(char *buffer, ssize_t bytes_read)
{
	char	*line;

	line = NULL;
	if (ft_strchr(buffer, '\n'))
	{
		line = NULL;;
		if (!line)
			return (NULL);
		line = ft_strjoin_free(line, buffer);
		ft_bzero(buffer, bytes_read);
	}
	return (line);
}
