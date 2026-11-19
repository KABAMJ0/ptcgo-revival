from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.card_effects.passives_common import no_weakness_passive

GRASS = PokemonTypes.GRASS.value


def _grass_team_no_weakness(target, carrier):
    return (target.owning_player_id == carrier.owning_player_id
            and GRASS in (target.get_attribute(AttrID.POKEMON_TYPES) or []))


card = PokemonCardDef(
    guid="6e0475ee-2185-57f0-bc15-828351a3e175",
    key="HGSS1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Metapod.Name",
    display_name="Metapod",
    searchable_by=["Metapod", "Stage 1", "Metapod"],
    subtypes=["Stage 1"],
    collector_number=46,
    set_code="HGSS1",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Caterpie.Name",
    family_id=10,
    abilities=[
        Ability(
            title="Green Shield",
            game_text="Each of your Grass Pok\u00e9mon has no Weakness.",
            effect=unimplemented,
        ),
        Attack(
            title="Sharpen",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)