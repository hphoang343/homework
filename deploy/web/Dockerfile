############################ Build Stage ##############################
# Use the official Node.js image as a base
FROM node:14 AS builder

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy package.json and package-lock.json to the working directory
COPY package.json /usr/src/app/package.json

# Install dependencies
RUN npm install

############################ Run Stage ################################
FROM node:14
WORKDIR /usr/src/app

COPY --from=builder /usr/src/app/node_modules /usr/src/app/node_modules
# Copy the rest of the application code
COPY . .
RUN groupadd -r myuser && useradd -r -g myuser app
### Change owners code
RUN chown -R app.myuser /usr/src/app/
USER app
# Expose the port the app runs on
EXPOSE 3000

# Command to run the application
CMD ["node", "app.js"]

