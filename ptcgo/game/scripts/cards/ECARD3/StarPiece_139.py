from ptcgo.game.data_utils import PokemonToolCardDef, Ability, Triggers, Activations
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import evolve_holder_between_turns

card = PokemonToolCardDef(
    guid="2dd3e3fd-7057-5a31-9a5b-db28082522d8",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.StarPiece.Name",
    display_name="Star Piece",
    searchable_by=["Star Piece", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=139,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    granted_abilities=evolve_holder_between_turns('Star Piece', 'bench', 2),
)
