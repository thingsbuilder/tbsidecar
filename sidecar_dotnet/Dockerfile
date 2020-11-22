FROM mcr.microsoft.com/dotnet/sdk:3.1 AS build-env
WORKDIR /app
COPY . ./
RUN dotnet restore
RUN dotnet publish -c release -o /publish 

FROM mcr.microsoft.com/dotnet/core/aspnet:3.1 AS runtime-env

WORKDIR /publish
COPY --from=build-env  /publish ./

EXPOSE ${SIDECAR_GRPC_PORT}

ENTRYPOINT ["dotnet", "sidecar_dotnet.dll"]