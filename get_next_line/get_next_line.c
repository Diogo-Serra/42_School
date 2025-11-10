/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/08 19:26:08 by diosoare          #+#    #+#             */
/*   Updated: 2025/11/10 14:09:34 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

/* static char	*load_line(char **storage)
{
	
} */

/* static size_t	save_storage(int fd, char **storage)
{
	
} */

char	*get_next_line(int fd)
{
	static char	buffer[BUFFER_SIZE + 1];
	size_t		bytes_read;
	char		**storage;
	int			i;

	i = 0;
	bytes_read = 1;
	while (bytes_read > 0)
	{
		bytes_read = read(fd, buffer, BUFFER_SIZE);
		buffer[bytes_read] = '\0';
		storage[i++] = ft_strdup(buffer);
		if (!storage[i])
			return (ft_free_heap(storage));
	}
	printf("Test: %s\n", storage);
	return (storage);
}

int	main(void)
{
	char	*out;
	int		fd;

	fd = open("test.txt", O_RDONLY);
	out = get_next_line(fd);
	free (out);
	return (0);
}
