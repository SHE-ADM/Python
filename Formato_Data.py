
from datetime import datetime, timezone
import locale

agora = datetime.now(timezone.utc)

# ISO compacto
print(f"{agora:%Y-%m-%dT%H:%M:%S%z}")  # 2026-01-12T09:56:55+0000

# Customizado
print(f"{agora:%d/%m/%Y %H:%M}")       # 12/01/2026 06:56  (se convertido ao seu fuso)

# Nome do mês e dia da semana
print(f"{agora:%A, %d de %B de %Y}")   # Monday, 12 de January de 2026 (depende de locale)

# Formato Brasileiro
locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
print(f"{agora:%A, %d de %B de %Y}")   # segunda-feira, 12 de janeiro de 2026
# Formato com milissegundos
print(f"{agora:%Y-%m-%d %H:%M:%S.%f}")  # 2026-01-12 09:56:55.123456