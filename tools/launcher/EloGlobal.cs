// EloGlobal.exe - the app's starter: runs main.py with the private Python in runtime\ (no console window).
// Built by tools\build_store.py with the C# compiler that ships with Windows' .NET Framework 4.
using System;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Windows.Forms;

static class Launcher
{
    [STAThread]
    static int Main(string[] args)
    {
        string root = AppDomain.CurrentDomain.BaseDirectory;
        string main = Path.Combine(root, "main.py");
        string pythonw = Path.Combine(root, "runtime", "pythonw.exe");
        if (!File.Exists(main) || !File.Exists(pythonw))
        {
            Error("EloGlobal is incomplete (main.py or runtime\\pythonw.exe is missing). Please reinstall it.");
            return 1;
        }
        // -s: never use packages from the user's own Python installation
        string extra = string.Join(" ", args.Select(a => "\"" + a.Replace("\"", "\\\"") + "\""));
        try
        {
            var psi = new ProcessStartInfo(pythonw, "-s \"" + main + "\" " + extra)
            {
                WorkingDirectory = root,
                UseShellExecute = false,
            };
            psi.EnvironmentVariables["PYTHONNOUSERSITE"] = "1";
            psi.EnvironmentVariables.Remove("PYTHONPATH");
            psi.EnvironmentVariables.Remove("PYTHONHOME");
            var p = Process.Start(psi);
            if (args.Contains("--wait"))
            {
                p.WaitForExit();
                return p.ExitCode;
            }
        }
        catch (Exception e)
        {
            Error("Could not start EloGlobal: " + e.Message);
            return 1;
        }
        return 0;
    }

    static void Error(string text)
    {
        MessageBox.Show(text, "EloGlobal", MessageBoxButtons.OK, MessageBoxIcon.Error);
    }
}
