from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.passives_common import retreat_free_when
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

def _no_energy(pokemon, carrier) -> bool:
    return pokemon is not None and not [e for e in pokemon.children]

card = PokemonCardDef(
    guid="589e8c33-3e2a-5400-bb49-fc866fcd9577",
    key="HGSS4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Yanma.Name",
    display_name="Yanma",
    searchable_by=["Yanma", "Basic", "Yanma"],
    subtypes=["Basic"],
    collector_number=84,
    set_code="HGSS4",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=193,
    abilities=[
        Ability(
            title="Free Flight",
            game_text="If Yanma has no Energy attached to it, Yanma's Retreat Cost is 0.",
            passive=retreat_free_when(_no_energy),
        ),
        Attack(
            title="Dive",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
