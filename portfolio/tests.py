from datetime import datetime

from django.test import TestCase

from .models import Solution, Tag


class TagTestCase(TestCase):
    def setUp(self):
        Tag.objects.create(name='Python', category='LANGUAGE')
        Solution.objects.create(title='Solution 1', release_date=datetime.now())
        Solution.objects.create(title='Solution 2', release_date=datetime.now())

    def test_tag_counts_solutions(self):
        python = Tag.objects.get(name='Python')

        solution1 = Solution.objects.get(title='Solution 1')
        solution2 = Solution.objects.get(title='Solution 2')

        python.solution_set.add(solution1)
        python.solution_set.add(solution2)

        self.assertEqual(python.count(), 2)
