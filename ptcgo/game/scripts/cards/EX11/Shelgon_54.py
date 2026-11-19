from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import takes_less_passive


card = PokemonCardDef(
    guid="03560889-adad-5025-a646-69a831a5bb74",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shelgon.Name",
    display_name="Shelgon δ",
    searchable_by=["Shelgon \u03b4", "Stage 1", "Shelgon"],
    subtypes=["Stage 1"],
    collector_number=54,
    set_code="EX11",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.COLORLESS,
    resistance_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bagon.Name",
    family_id=372,
    abilities=[
        Ability(
            title="Exoskeleton",
            game_text="Any damage done to Shelgon by attacks is reduced by 10 (after applying Weakness and Resistance).",
            passive=takes_less_passive(10),
        ),
        Attack(
            title="Heat Blast",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)