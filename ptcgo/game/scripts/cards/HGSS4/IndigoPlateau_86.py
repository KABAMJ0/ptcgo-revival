from ptcgo.game.data_utils import StadiumCardDef, unimplemented
from ptcgo.game.card_effects.passives_common import team_hp_bonus
from ptcgo.game.attributes import AttrID, PokemonTypes
from ptcgo.game.card_effects.pokemon import has_pokemon_subtype
from ptcgo.game.data_utils import def_for

def _stage_of(pokemon) -> int:
    definition = def_for(getattr(pokemon, "archetype_id", "") or "")
    stage = getattr(definition, "stage", None)
    return int(getattr(stage, "value", stage)) if stage is not None else -1
from ptcgo.game.attributes import Rarities

card = StadiumCardDef(
    guid="3b2b9d93-19af-5bdc-8b24-cc3e9a9fcff4",
    key="HGSS4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.IndigoPlateau.Name",
    display_name="Indigo Plateau",
    searchable_by=["Indigo Plateau", "Stadium"],
    subtypes=["Stadium"],
    collector_number=86,
    set_code="HGSS4",
    rarity=Rarities.Uncommon,
    passive=team_hp_bonus(30, pred=lambda p, c: has_pokemon_subtype(p, "LEGEND"))
)
