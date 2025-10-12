# ¿Qué es Azure DevOps?

Azure DevOps es un conjunto de servicios en la nube de Microsoft para gestionar todo el ciclo de vida del desarrollo de software, desde la planificación hasta la entrega y operación.

En otras palabras:
Es la plataforma de Microsoft para CI/CD, gestión de código, tareas, artefactos y despliegues automáticos.

| Servicio             | Descripción breve                                                                                                       |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| **Azure Repos**      | Repositorios Git privados (como GitHub, pero dentro del entorno de Azure).                                              |
| **Azure Pipelines**  | Automatiza la integración y el despliegue (CI/CD). Puedes compilar, testear y desplegar en Azure, AWS, Kubernetes, etc. |
| **Azure Boards**     | Sistema de gestión ágil: tareas, historias, bugs, sprints, etc. Perfecto para Scrum o Kanban.                           |
| **Azure Artifacts**  | Manejo de paquetes (NuGet, npm, Maven, etc.) dentro del ecosistema de la empresa.                                       |
| **Azure Test Plans** | Gestión de pruebas manuales y automatizadas, con seguimiento de resultados.                                             |

### 💡 En resumen

Azure DevOps = un ecosistema para:

- planificar (Boards),

- codificar (Repos),

- compilar y desplegar (Pipelines),

- almacenar dependencias (Artifacts),

- probar (Test Plans). |

### ✅ gratis

- Los primeros 5 usuarios con plan Basic son gratuitos.
  azure-int.microsoft.com
  +2
  softwaretestinghelp.com
  +2

- Tienes 1 job hospedado por Microsoft (Microsoft-hosted CI/CD) gratis con 1.800 minutos al mes para correr pipelines.
  azure-int.microsoft.com
  +1

- También 1 job self-hosted (cuando tú proves el agente) con minutos ilimitados gratis.
  azure-int.microsoft.com
  +1

- Azure Artifacts (los paquetes) ofrece 2 GB de almacenamiento gratis.
  azure-int.microsoft.com
  +1

- Usuarios “Stakeholder” (con funcionalidades limitadas, como ver qué hay pendiente, dar feedback, etc.) son “gratis” ilimitados.

## 🚀 Qué puedes montar con eso (ejemplo práctico)

Con solo el plan gratuito podrías:

- Tener tu código en Azure Repos (o conectar tu repo de GitHub).

- Crear un pipeline YAML que compile tu microservicio .NET 8 y lo dockerice.

- Desplegarlo automáticamente en AKS (Azure Kubernetes Service) o en una máquina tuya.

- Llevar la gestión de tareas y releases en Boards.

- Todo sin pagar — hasta que necesites escalar el equipo o el número de builds simultáneas.
