# Generated by Django 2.1.5 on 2019-10-14 16:55

from django.db import migrations
from perftracker.models.test import TestModel

def recalc_errors(apps, schema_editor):
    JobModel = apps.get_model('perftracker', 'JobModel')
    for job in JobModel.objects.all().order_by('-id'):
        # see JobModel.pt_update, here we imitate the same logic using data from DB
        tests = job.tests.all().only("status", "errors", "warnings", "tag", "category", "group")
        tests_total = 0
        tests_completed = 0
        tests_failed = 0
        tests_errors = 0
        tests_warnings = 0
        testcases = {}
        for t in tests:
            tests_total += 1
            if TestModel.pt_status_is_completed(t):
                tests_completed += 1
            test_ok = True
            if TestModel.pt_status_is_failed(t):
                tests_failed += 1
                test_ok = False
            if t.errors:
                test_ok = False
            if t.warnings:
                tests_warnings += 1

            tests_errors += int(not test_ok)
            testcase = t.tag if t.category else t.group
            if testcase in testcases:
                testcases[testcase] = testcases[testcase] and test_ok
            else:
                testcases[testcase] = test_ok

        testcases_total = len(testcases)
        testcases_errors = len([1 for ok in testcases.values() if not ok])

        changes = ""
        for f in ('tests_total', 'tests_completed', 'tests_failed', 'tests_errors', 'tests_warnings',
                  'testcases_total', 'testcases_errors'):
            x = getattr(job, f)
            y = locals()[f]
            if x != y:
                changes += "   %s(%s -> %s)" % (f, x, y)
                setattr(job, f, y)
        if changes:
            print("fixing job %d: %s" % (job.id, changes))
            job.save()


class Migration(migrations.Migration):

    dependencies = [
        ('perftracker', '0051_jobmodel_add_testcases'),
    ]

    operations = [
        migrations.RunPython(recalc_errors),
    ]