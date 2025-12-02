/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/08 19:26:08 by diosoare          #+#    #+#             */
/*   Updated: 2025/12/02 16:03:39 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

#include <stdio.h>
int	main(void)
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
}

char	*get_next_line(int fd)
{
	static char	buffer[BUFFER_SIZE + 1];
	char		*line;
	ssize_t		bytes;

	if (fd < 0 || BUFFER_SIZE < 1)
		return (NULL);
	line = NULL;
	bytes = 1;
	while (bytes > 0 || buffer[0])
	{
		if (!buffer[0])
			bytes = read(fd, buffer, BUFFER_SIZE);
		if (bytes < 0)
			return (clean_buffer(buffer), free(line), NULL);
		if (bytes == 0)
			return (line);
		line = ft_strnjoin(line, buffer);
		if (!line)
			return (clean_buffer(buffer), NULL);
		clean_buffer(buffer);
		if (line && ft_strchr(line, '\n'))
			break ;
	}
	return (line);
}
