from django.core.management.base import BaseCommand, CommandError
import pandas as pd
import argparse
from myapi.models import County

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('file', type=argparse.FileType('r'))
        parser.add_argument('model', type=str)
    def transform(self, file):
        df = pd.read_csv(file)
        df.columns = df.columns.str.replace('-', '')
        df = df.dropna()
        return df
    def load(self, file, model):
        transformed_df = self.transform(file)
        if model == "County":
            modelInstance = County
        modelInstance.objects.bulk_create(modelInstance(**vals) for vals in transformed_df.to_dict('records'))
    def handle(self, *args, **kwargs):
        self.load(kwargs['file'], kwargs['model'])

    