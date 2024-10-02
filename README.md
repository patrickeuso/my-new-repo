# my-new-repo
O objetivo principal deste aplicativo Streamlit é fornecer uma análise interativa dos dados de veículos - através da URL: https://my-new-repo-2u67.onrender.com/. Utilizando uma interface simples e intuitiva, o aplicativo permite que os usuários explorem visualmente as informações contidas no arquivo vehicles.csv. Através de gráficos interativos, os usuários podem compreender melhor os dados sobre os veículos, como a distribuição da quilometragem (odometer) e a relação entre a quilometragem e o preço.

Primeiro, o aplicativo verifica se o arquivo de dados existe no caminho especificado. Caso o arquivo não seja encontrado, uma mensagem de erro é exibida. Se o arquivo estiver presente, os dados são carregados em um DataFrame do Pandas. Isso garante que todos os dados necessários estejam disponíveis para as análises subsequentes.

A interface do Streamlit oferece aos usuários duas opções principais para visualizar os dados: um histograma e um gráfico de dispersão. Os botões "Criar histograma" e "Criar gráfico de dispersão" permitem a criação desses gráficos interativos de forma dinâmica. O histograma mostra a distribuição da quilometragem dos veículos, enquanto o gráfico de dispersão exibe a relação entre a quilometragem e o preço, fornecendo uma visão mais detalhada das tendências nos dados.

Além disso, o aplicativo inclui um desafio extra com caixas de seleção, substituindo os botões tradicionais. Isso oferece uma forma alternativa de interação, onde os usuários podem selecionar as opções de gráfico que desejam visualizar. Essa funcionalidade adicional torna a experiência do usuário mais personalizada e interativa, aumentando a flexibilidade na análise dos dados dos veículos.
