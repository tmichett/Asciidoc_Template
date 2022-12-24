$book_arg=$args[0]
Write-Output $book_arg
$container = "quay.io/tmichett/asciidocpdf:latest"
$current_directory = (get-location).path
$pdf_theme="-a pdf-theme=/opt/asciidoc/themes/tm-gls-redhat-theme.yml"
Write-Output $current_directory
Invoke-Expression "docker run -it --name adocpdf --rm -e 'pdf_theme=$pdf_theme' -e 'book_name=$book_arg'-v $current_directory`:/tmp/coursebook $container"
