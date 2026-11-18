from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import free_attack_cost_passive

card = PokemonToolCardDef(
    guid="9ee6e547-3b9d-546d-9a1c-42ad33b102e2",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.VictoryPiece.Name",
    display_name="Victory Piece",
    searchable_by=["Victory Piece", "Pok\u00e9mon Tool", "ACE SPEC"],
    subtypes=["Pok\u00e9mon Tool", "ACE SPEC"],
    collector_number=130,
    set_code="BW8",
    rarity=Rarities.Rare,
    passive=free_attack_cost_passive()
)
