/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: diosoare <diosoare@student.42lisboa.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/08 19:26:08 by diosoare          #+#    #+#             */
/*   Updated: 2025/11/09 21:56:21 by diosoare         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

/* static char	*load_storage(char **storage)
{
	
} */

static int	ft_save_storage(int fd, char **storage)
{
	char	buffer[BUFFER_SIZE + 1];
    size_t	readBytes;
    int		reads;

	reads = 0;
    storage = (char **)malloc(BUFFER_SIZE * sizeof(char *));
    if (!storage)
		return (-1);
    while ((readBytes = read(fd, buffer, BUFFER_SIZE)) > 0)
    {
        buffer[readBytes] = '\0';
        storage[reads] = ft_strdup(buffer);
        if (!storage[reads]) 
		{
            ft_free_heap(storage);
            return (-1);
        }
        reads++;
    }
    storage[reads] = NULL; 
    return (reads);
}

char *get_next_line(int fd)
{
	static char	**storage;
	int			reads;
	
	reads = ft_save_storage(fd, storage);
	printf("read %d time(s)\n", reads);
	return (storage[0]);
}

int main(void)
{
    char    *out;
    int     fd;

    fd = open("test.txt", O_RDONLY);
    out = get_next_line(fd);
    free (out);
	return (0);
}
