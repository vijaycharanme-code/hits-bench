class HITSError(Exception):
    """Base exception for HITS AI Workbench."""
    pass

class HardwareDetectionError(HITSError):
    """Raised when hardware detection fails."""
    pass

class DependencyInstallationError(HITSError):
    """Raised when dependency installation fails."""
    pass

class ModelLoadError(HITSError):
    """Raised when a model fails to load."""
    pass

class LayaRoutingError(HITSError):
    """Raised when Laya router fails to route."""
    pass

class AgentExecutionError(HITSError):
    """Raised when an agent execution fails."""
    pass

class DocumentVerificationError(HITSError):
    """Raised when document verification fails."""
    pass

class SecurityCheckError(HITSError):
    """Raised when a security check fails."""
    pass

class RetryLimitExceededError(HITSError):
    """Raised when self-correction retry limit is exceeded."""
    pass
