# Base Image
FROM node:22-alpine
# Set Working Directory
WORKDIR /app
# copy package.json file
COPY package*.json .
# Install Dependencies
RUN npm install 
# Copy all project files
COPY . .
#Expose Port
EXPOSE 3000

CMD ["node","index.js" ]
