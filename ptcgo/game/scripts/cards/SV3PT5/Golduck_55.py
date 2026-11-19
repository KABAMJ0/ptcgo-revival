from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import discard_defender_tools_then_damage
from ptcgo.game.card_effects.attacks_common import discard_defender_tools_then_damage
card = PokemonCardDef(
    guid="272cd6f6-7156-5a73-9529-172ea92b38c4",
    key="SV3PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Golduck.Name",
    display_name="Golduck",
    searchable_by=["Golduck", "Stage 1", "Golduck"],
    subtypes=["Stage 1"],
    collector_number=55,
    set_code="SV3PT5",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Psyduck.Name",
    family_id=54,
    abilities=[
        Attack(
            title="Aquatic Rescue",
            game_text="Put up to 4 Pok\u00e9mon from your discard pile into your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=discard_defender_tools_then_damage(),
        ),
        Attack(
            title="Super Splash",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
        ),
    ],
)