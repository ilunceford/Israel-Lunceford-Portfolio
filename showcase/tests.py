from django.test import TestCase
from django.urls import reverse


class PortfolioHomeTests(TestCase):
    def test_home_highlights_cpu_and_all_projects(self):
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "ECEN 240 Final Project: 4-bit CPU")
        self.assertContains(response, "How to open and use the CPU")
        self.assertContains(response, "Program the ROM from the text file")
        self.assertContains(response, "1003 2700 1004 1109")
        self.assertContains(response, "Chess Game")
        self.assertContains(response, "Flash Card Mobile App")

    def test_cpu_download_returns_logisim_file(self):
        response = self.client.get(reverse("cpu_download"))
        content = b"".join(response.streaming_content)

        self.assertEqual(response.status_code, 200)
        self.assertIn("attachment", response.headers["Content-Disposition"])
        self.assertIn("ECEN240_Final_Project_4bit_CPU.circ", response.headers["Content-Disposition"])
        self.assertIn(b"<project source=\"4.0.0\"", content)
        self.assertIn(b"<main name=\"Final_Project\"", content)

    def test_cpu_program_download_returns_rom_listing(self):
        response = self.client.get(reverse("cpu_program_download"))
        content = b"".join(response.streaming_content)

        self.assertEqual(response.status_code, 200)
        self.assertIn("Final_Proj_All_code.txt", response.headers["Content-Disposition"])
        self.assertTrue(content.startswith(b"v3.0 hex words addressed"))
