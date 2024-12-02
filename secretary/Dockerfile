# Stage 1: Build the React application
FROM node:18


WORKDIR /app


EXPOSE 8080


# Command to run the application
ENTRYPOINT [ "./entrypoint.sh" ]
CMD ["npm", "start"]  # Wont run until "docker-compose run "