### Steps to run the project.

**Create a virtual environment**
```bash
python3 -m venv venv
```

**Initialize virtual environment**

For linux
```
source venv/bin/activate
```

For Windows
```powershell
venv\Scripts\Activate
```

**Move inside the folder**
```bash
cd entropy_app
```

**Download requirements**
```bash
pip install -r requirements.txt
```

**Move inside the folder**
```bash
cd entropy_app
```

**Make migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

**Open python shell**
```bash
python manage.py shell
```

**Create fake data**
```python
from inventory.models import NomenclatureModel, RecordModel, Department

NomenclatureModel.create_random_data()
RecordModel.create_random_records()
Department.create_random_departments()
quit()
```

**Create Superuser**
```python
python manage.py createsuperuser
```

**Run the project**
```bash
python manage.py runserver
```